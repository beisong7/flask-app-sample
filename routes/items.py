from flask import Blueprint, request, jsonify

items_bp = Blueprint('items', __name__)

# Sample data
data = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]


@items_bp.route('/')
def home():
    response = jsonify({"app": "Flask Api Running", "Version": "0"})
    response.status_code = 200
    return response

# Get all items
@items_bp.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Get a single item by ID
@items_bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Add a new item
@items_bp.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item["id"] = data[-1]["id"] + 1 if data else 1
    data.append(new_item)
    return jsonify(new_item), 201

# Update an existing item
@items_bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        updated_data = request.get_json()
        item.update(updated_data)
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Delete an item
@items_bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200
