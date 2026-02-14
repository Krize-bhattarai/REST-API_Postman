from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory database
laptops = [
    {"id": 1, "brand": "Dell", "price": 1500},
    {"id": 2, "brand": "HP", "price": 1300}
]

# ------------------ GET ------------------
@app.route('/laptops', methods=['GET'])
def get_laptops():
    return jsonify(laptops)


# ------------------ POST ------------------
@app.route('/laptops', methods=['POST'])
def add_laptop():
    new_laptop = request.json
    laptops.append(new_laptop)
    return jsonify({"message": "Laptop added successfully"}), 201


# ------------------ PUT ------------------
@app.route('/laptops/<int:id>', methods=['PUT'])
def update_laptop(id):
    for laptop in laptops:
        if laptop["id"] == id:
            laptop["brand"] = request.json.get("brand", laptop["brand"])
            laptop["price"] = request.json.get("price", laptop["price"])
            return jsonify({"message": "Laptop updated"})
    return jsonify({"message": "Laptop not found"}), 404


# ------------------ DELETE ------------------
@app.route('/laptops/<int:id>', methods=['DELETE'])
def delete_laptop(id):
    for laptop in laptops:
        if laptop["id"] == id:
            laptops.remove(laptop)
            return jsonify({"message": "Laptop deleted"})
    return jsonify({"message": "Laptop not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
