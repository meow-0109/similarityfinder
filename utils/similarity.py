from sklearn.metrics.pairwise import cosine_similarity

def get_top_k_similar(user_vector, message_vectors, messages, k=3):
    similarities = cosine_similarity(user_vector, message_vectors)[0]

    ranked = sorted(
        enumerate(similarities),
        key=lambda x: x[1],
        reverse=True
    )

    top_results = []
    for idx, score in ranked[:k]:
        top_results.append((messages[idx], score))

    return top_results
