import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel  # more memory efficient than cosine_similarity

df_cache = None
vectorizer_cache = None
vectors_cache = None

def load_data():
    global df_cache, vectorizer_cache, vectors_cache
    if df_cache is None:
        df_cache = pd.read_csv("cleaned_anime.csv").head(5000)  # optional: limit rows
        vectorizer_cache = TfidfVectorizer(stop_words="english")
        vectors_cache = vectorizer_cache.fit_transform(df_cache["content"])
    return df_cache, vectorizer_cache, vectors_cache

def recommend(anime_name, top_n=10):
    df, vectorizer, vectors = load_data()
    anime_name = anime_name.lower().strip()

    matches = df[df["name"].str.lower().str.contains(anime_name)]
    if matches.empty:
        return []

    idx = matches.index[0]

    # Compute similarity only for this anime
    cosine_sim = linear_kernel(vectors[idx], vectors).flatten()
    scores = list(enumerate(cosine_sim))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1: top_n + 1]

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
