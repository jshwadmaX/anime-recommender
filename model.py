import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Lazy load cache variables
df_cache = None
vectorizer_cache = None
vectors_cache = None
similarity_cache = None

def load_data():
    global df_cache, vectorizer_cache, vectors_cache, similarity_cache

    if df_cache is None:
        df_cache = pd.read_csv("cleaned_anime.csv")

        # Create TF-IDF vectors and similarity only once
        vectorizer_cache = TfidfVectorizer(stop_words="english")
        vectors_cache = vectorizer_cache.fit_transform(df_cache["content"])
        similarity_cache = cosine_similarity(vectors_cache)

    return df_cache, similarity_cache

def recommend(anime_name, top_n=10):
    df, similarity = load_data()

    anime_name = anime_name.lower()

    if anime_name not in df["name"].str.lower().values:
        return []

    idx = df[df["name"].str.lower() == anime_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1 : top_n + 1]

    rec = []
    for i, _ in scores:
        rec.append(
            {
                "name": df.iloc[i]["name"],
                "rating": df.iloc[i]["rating"],
                "episodes": int(df.iloc[i]["episodes"]),
                "type": df.iloc[i]["type"],
                "tags": df.iloc[i]["tags"].title(),
                "description": df.iloc[i]["description"][:250] + "...",
            }
        )
    return rec
