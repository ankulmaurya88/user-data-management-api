# controllers/v1/user_controller.py
from flask import Blueprint, request, jsonify
from models import db, User

user_blueprint_v1 = Blueprint('user_v1', __name__)

@user_blueprint_v1.route('/users', methods=['GET'])
def get_users_v1():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age} for user in users])

@user_blueprint_v1.route('/users', methods=['POST'])
def add_user_v1():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added'}), 201


@user_blueprint_v1.route('/users/<int:id>', methods=['DELETE'])
def delete_user_v1(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'User with id {id} has been deleted'}), 200
    return jsonify({'message': 'User not found'}), 404



@user_blueprint_v1.route('/users/<int:id>', methods=['PUT'])
def update_user_v1(id):
    user = User.query.get(id)
    if user:
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        user.age = data['age']
        db.session.commit()
        return jsonify({'message': f'User with id {id} has been updated'}), 200
    return jsonify({'message': 'User not found'}), 404
