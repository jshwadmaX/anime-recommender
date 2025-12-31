import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("cleaned_anime.csv")

vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(df["content"])
similarity = cosine_similarity(vectors)


def recommend(anime_name, top_n=10):
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
