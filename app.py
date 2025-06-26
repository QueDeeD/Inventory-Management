from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_product, get_products, delete_product
from analytics import predict_demand

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    products = get_products()
    prediction = predict_demand()
    return render_template('index.html', products=products, prediction=prediction)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    add_product(name, quantity, price)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    delete_product(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)