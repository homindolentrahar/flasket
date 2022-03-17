from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': "Laptop", 'price': 20.4},
        {'id': 2, 'name': "Mobile Phone", 'price': 32.9},
        {'id': 3, 'name': "PC", 'price': 28.45},
    ]

    return render_template('market.html', title="Market Page", items=items)


if __name__ == '__main__':
    app.run()
