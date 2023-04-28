from financialprogramm.db import insert_category, get_categories
from flask import Flask, request, render_template, url_for, redirect


app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return render_template('base.html')


@app.route('/categories', methods=['GET'])
def categories():
    categories = get_categories()
    return render_template('categories.html', categories=categories)


@app.route('/add_new_category', methods=["POST"])
def add_new_category():
    value = request.form.get('category')
    insert_category(value)
    return redirect(url_for('categories'))


if __name__ == '__main__':
    app()
