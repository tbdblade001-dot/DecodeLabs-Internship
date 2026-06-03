import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "JobRole": [
        "Data Scientist",
        "DevOps Engineer",
        "Backend Developer",
        "Cloud Architect",
        "System Administrator"
    ],
    "Skills": [
        "Python SQL Machine Learning Data Analysis",
        "AWS Docker Kubernetes CI/CD",
        "Java Python SQL APIs",
        "Cloud Computing Automation Security",
        "Linux Networking Security Automation"
    ]
}

df = pd.DataFrame(data)
user_input = ["Python", "Cloud", "Automation"]
user_profile = " ".join(user_input)
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Skills"].tolist() + [user_profile])
cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

df["SimilarityScore"] = cosine_sim.flatten()
recommendations = df.sort_values(by="SimilarityScore", ascending=False).head(3)
print("User Input Skills:", user_input)
print("\nTop 3 Recommended Career Paths:\n")
for idx, row in recommendations.iterrows():
    print(f"{row['JobRole']} (Score: {row['SimilarityScore']:.2f})")