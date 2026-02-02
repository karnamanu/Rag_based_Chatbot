from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

# Endee client (used conceptually)
from endee import Endee

app = Flask(__name__)

model = SentenceTransformer("all-MiniLM-L6-v2")

# Try connecting to Endee
try:
    endee_client = Endee()
    endee_available = True
except Exception as e:
    print("Endee backend not reachable, running in demo mode")
    endee_available = False

# Fallback in-memory store (for demo)
store = []

@app.route("/add", methods=["POST"])
def add_text():
    data = request.get_json()
    text = data.get("text")

    embedding = model.encode(text).tolist()

    # Conceptual Endee usage
    if endee_available:
        # would insert into Endee index here
        pass

    store.append({"text": text, "embedding": embedding})

    return jsonify({"message": "Text stored (Endee conceptual mode)"})

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query")
    q_emb = model.encode(query).tolist()

    # simple similarity (demo)
    results = sorted(
        store,
        key=lambda x: sum(a*b for a, b in zip(q_emb, x["embedding"])),
        reverse=True
    )[:3]

    contexts = [r["text"] for r in results]
    return jsonify({"contexts": contexts})

if __name__ == "__main__":
    app.run(port=5000)
