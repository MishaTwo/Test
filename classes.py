from flask import Flask, jsonify, json, request, get_json
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
from .database.post import *
from .database.base import *
from dotenv import load_dotenv
import os

class NewPost(Resource):
    def get(self):
        posts = Posts.query.all()
        post_list = [{"id": post.id, "title": post.title, "content": post.content} for post in posts]
        return jsonify(post_list)

    def post(self):
        data = request.get_json()
        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            return jsonify({"message": "Title and Email are reqired!"}), 400
        
        new_post = Posts(
            title = title,
            content = content,
        )

        session.add(new_post)
        session.commit()

        message = {
            "message": "Post created successfully!",
            'post': {
                "id": new_post.id,
                "title": new_post.title,
                "content": new_post.content
            }
        }

        return jsonify(message), 201