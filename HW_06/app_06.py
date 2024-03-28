from flask import Flask, request, jsonify
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4

app = Flask(__name__)

# Модели Pydantic для валидации данных
class UserBase(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    name: str
    lastname: str
    email: str
    password: str

class ProductBase(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    name: str
    description: str
    price: float

class OrderBase(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    user_id: UUID
    product_id: UUID
    order_date: str
    status: str

# Имитация базы данных
users_db = []
products_db = []
orders_db = []

# CRUD операции для пользователей
@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.json
    user = UserBase(**user_data)
    users_db.append(user)
    return jsonify(user.dict()), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    for user in users_db:
        if str(user.id) == user_id:
            return jsonify(user.dict()), 200
    return "User not found", 404

# CRUD операции для товаров
@app.route('/product', methods=['POST'])
def create_product():
    product_data = request.json
    product = ProductBase(**product_data)
    products_db.append(product)
    return jsonify(product.dict()), 201


@app.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    for product in products_db:
        if str(product.id) == product_id:
            return jsonify(product.dict()), 200
    return "Product not found", 404

# CRUD операции для заказов
@app.route('/order', methods=['POST'])
def create_order():
    order_data = request.json
    order = OrderBase(**order_data)
    orders_db.append(order)
    return jsonify(order.dict()), 201

@app.route('/order/<order_id>', methods=['GET'])
def get_order(order_id):
    for order in orders_db:
        if str(order.id) == order_id:
            return jsonify(order.dict()), 200
    return "Order not found", 404

if __name__ == '__main__':
    app.run(debug=True)

# Обновление и удаление для пользователей
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    for user in users_db:
        if str(user.id) == user_id:
            user.name = user_data.get('name', user.name)
            user.lastname = user_data.get('lastname', user.lastname)
            user.email = user_data.get('email', user.email)
            user.password = user_data.get('password', user.password)
            return jsonify(user.dict()), 200
    return "User not found", 404

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users_db:
        if str(user.id) == user_id:
            users_db.remove(user)
            return '', 204
    return "User not found", 404

# Обновление и удаление для товаров
@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    product_data = request.json
    for product in products_db:
        if str(product.id) == product_id:
            product.name = product_data.get('name', product.name)
            product.description = product_data.get('description', product.description)
            product.price = product_data.get('price', product.price)
            return jsonify(product.dict()), 200
    return "Product not found", 404

@app.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    for product in products_db:
        if str(product.id) == product_id:
            products_db.remove(product)
            return '', 204
    return "Product not found", 404

# Обновление и удаление для заказов
@app.route('/order/<order_id>', methods=['PUT'])
def update_order(order_id):
    order_data = request.json
    for order in orders_db:
        if str(order.id) == order_id:
            order.user_id = order_data.get('user_id', order.user_id)
            order.product_id = order_data.get('product_id', order.product_id)
            order.order_date = order_data.get('order_date', order.order_date)
            order.status = order_data.get('status', order.status)
            return jsonify(order.dict()), 200
    return "Order not found", 404

@app.route('/order/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    for order in orders_db:
        if str(order.id) == order_id:
            orders_db.remove(order)
            return '', 204
    return "Order not found", 404


