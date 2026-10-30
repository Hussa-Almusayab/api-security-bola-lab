"""Educational BOLA lab (fixed version). Local use only - do not deploy."""
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

ORDERS = {
    1: {"owner": "alice", "item": "Locker A1"},
    2: {"owner": "bob", "item": "Locker B2"},
}


def current_user():
    # Demo only: a real app would read the user from a verified session or token.
    return request.headers.get("X-User", "")


@app.get("/orders/<int:order_id>")
def get_order(order_id):
    order = ORDERS.get(order_id) or abort(404)
    if order["owner"] != current_user():
        abort(403)  # ownership check on the server
    return jsonify(order)


if __name__ == "__main__":
    app.run(port=5000)
