import sqlite3
from flask import Flask, g, render_template, request
from flask_paginate import Pagination, get_page_parameter

app = app = Flask(__name__)

app.config.from_object(__name__)

db_name = 'Maven_Pizza_Orders.db'

def connect_db():
    conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/orders')
def orders():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 8
    offset = (page - 1) * per_page

    db = get_db()
    cur = db.execute("SELECT COUNT(*) FROM orders")
    rows = cur.fetchone()[0]

    cur = db.execute("SELECT * FROM orders ORDER BY id LIMIT ? OFFSET ?", (per_page, offset))
    data = cur.fetchall()

    pagination = Pagination(page=page, per_page=per_page, total=rows, css_framework='bootstrap4')

    return render_template('orders.html', rows=data, pagination=pagination)





@app.route('/order_details/<id>')
def order_details(id):
    db = get_db()
    cur = db.execute("select * from orders WHERE id=?", (id,))
    order = cur.fetchall()
    cur = db.execute("select * from order_details WHERE OrderID=?", (id,))
    #逗号代表有多个数据，见老师发的邮件
    rows = cur.fetchall()
    return render_template('order_details.html', order=order, rows = rows)

@app.route('/pizzas/<id>')
def pizzas(id):
    db = get_db()
    cur = db.execute("select * from pizzas WHERE PizzaID=?", (id,))
    rows = cur.fetchall()
    return render_template('pizzas.html', rows=rows)