from flask import Flask, request, jsonify
app= Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Sherlock",
        "email": "sherlock@gmail.com"
    }
    extra_data = request.args.get("extra_data")
    if extra_data:
        user_data["extra_data"] = extra_data
    return jsonify({"user_id": user_data}),200

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True)