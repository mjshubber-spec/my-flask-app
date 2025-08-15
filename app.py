from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from MJ"

# New API endpoint
@app.route("/add", methods=["GET"])
def add_numbers():
    try:
        # Get numbers from query parameters
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        result = a + b
        return jsonify({"sum": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Use numbers only."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
