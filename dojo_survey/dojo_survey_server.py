#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def intro_page():
    return render_template("carlos_intropageHTML_0511.html")


@app.route("/submitted", methods=["POST"])
def submitted():
    print(request.form["favorite_language"])
    name = request.form["user_name"]
    dojo_location = request.form["dojo_locaiton"]
    favorite_language = request.form["favorite_language"]
    comment_message = request.form["comment_message"]
    gimme_render = render_template("submitted_page_0512.html", name=name, dojo_location=dojo_location,
                                   favorite_language=favorite_language, comment_message=comment_message)
    return gimme_render


app.run(debug=True)


