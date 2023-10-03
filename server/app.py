#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Game/Review/User API"

@app.route('/games')
def games():
    games = []
    for game in Game.query.all():
        game_dict = {
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        games.append(game_dict)
    return jsonify(games), 200

@app.route('/games/<int:id>')
def game_by_id(id):
    game = Game.query.filter(Game.id == id).first()
    if game:
        game_dict = {
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        return jsonify(game_dict), 200
    else:
        return "Game not found", 404

@app.route('/reviews')
def reviews():
    reviews = []
    for review in Review.query.all():
        review_dict = {
            "score": review.score,
            "comment": review.comment,
            "game_id": review.game_id,
            "user_id": review.user_id,
        }
        reviews.append(review_dict)
    return jsonify(reviews), 200

@app.route('/users')
def users():
    users = []
    for user in User.query.all():
        user_dict = {
            "name": user.name,
            "user_id": user.id,
        }
        users.append(user_dict)
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
