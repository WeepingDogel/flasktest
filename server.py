'''
简单的 Flask 项目练习
'''
import os  # 导入 os 库，因为可能会有一些系统的操作
from flask import Flask  # 导入 Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route("/")
def Index():
    style = url_for('static', filename='style.css')
    return render_template("example.html", style=style)
