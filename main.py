import sys
import time
from data.messages import MESSAGES
from embeddings.embedding_service import EmbeddingService
from utils.similarity import get_top_k_similar


def color_text(text, score):
    """
    Color-code message based on similarity score
    """
    if score >= 0.75:
        return f"\033[92m{text}\033[0m"   # Green
    elif score >= 0.40:
        return f"\033[93m{text}\033[0m"   # Yellow
    else:
        return f"\033[91m{text}\033[0m"   # Red


def main():
    start_time = time.time()

    # Default top-K value
    k = 3

    # Handle command-line input
    if len(sys.argv) > 1:
        try:
            k = int(sys.argv[-1])
            user_input = " ".join(sys.argv[1:-1])
            if not user_input:
                raise ValueError
        except ValueError:
            user_input = " ".join(sys.argv[1:])
            k = 3
    else:
        user_input = input("Enter your message: ").strip()

    if not user_input:
        print("❌ Please enter a valid message.")
        return

    # Create embeddings 
    embedding_service = EmbeddingService(MESSAGES)
    user_vector = embedding_service.embed(user_input)

    # Get similar messages
    results = get_top_k_similar(
        user_vector,
        embedding_service.message_vectors,
        MESSAGES,
        k=k
    )

    print(f"\nTop {k} Similar Messages:")
    for i, (msg, score) in enumerate(results, start=1):
        colored_msg = color_text(msg, score)
        print(f"{i}. [Similarity: {score * 100:.2f}%] {colored_msg}")

    end_time = time.time()
    print(f"\nExecution Time: {(end_time - start_time) * 1000:.2f} ms")


if __name__ == "__main__":
    main()
