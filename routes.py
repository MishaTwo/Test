import os
from .database import session, User
from . import app
from database.post import *
from flask import render_template, request, redirect, jsonify, json
from dotenv import load_dotenv


@app.route('/posts')
def posts_return():
    posts = session.query(Posts).all()
    posts_list = [{'title': post.title, 'content': post.content} for post in posts]
    return jsonify(posts_list)
    

@app.route('/post/<int:id>')
def posts_return(id):
    post = session.query(Posts).get(id)
    post_list = [{'title': post.title, 'content': post.content}]
    return jsonify(post_list)

@app.route("/delete/<int:id>")
def delete(id):
    post = session.query(Posts).filter_by(id=id).first()
    if post:
        session.delete(post)
        session.commit()
    session.close()
    return jsonify("Post deleted successfully!!!")

@app.route("/update/<int:id>", methods=["GET", 'PUT'])
def update(id):
    post = session.query(Posts).get(id)
    if request.method == 'PUT':
        title = request.form["title"]
        content = request.form["content"]
        if title or content:
                post.title = title
                post.content = content
                session.comit()
    return jsonify("Post updated successfully")