"""
Generated Code Metadata:
========================
Original URL: https://opterisglobal.com
Prompt: "Develop a cryptocurrency exchange platform with a user-friendly integrated application and support for both fiat currencies and cryptocurrencies."
Generated: DETERMINISTIC_412e11487567722e
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Cryptocurrency Exchange Platform**
=====================================

**Dependencies**
---------------

* `flask` for the web application
* `flask_sqlalchemy` for database interactions
* `ccxt` for cryptocurrency exchange integrations
* `yfinance` for fiat currency and cryptocurrency data

**Installation**
---------------

```bash
pip install flask flask_sqlalchemy ccxt yfinance
```

**Code**
------

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import ccxt
import yfinance as yf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exchange.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class FiatCurrency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)

class Cryptocurrency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)

class ExchangeRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fiat_currency_id = db.Column(db.Integer, db.ForeignKey('fiat_currency.id'))
    cryptocurrency_id = db.Column(db.Integer, db.ForeignKey('cryptocurrency.id'))
    rate = db.Column(db.Float, nullable=False)

@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        user = User(username=data['username'], email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        user = User.query.filter_by(username=data['username'], password=data['password']).first()
        if user:
            return jsonify({'message': 'User logged in successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/fiat-currencies', methods=['GET'])
def get_fiat_currencies():
    try:
        fiat_currencies = FiatCurrency.query.all()
        return jsonify([{'symbol': fc.symbol, 'name': fc.name} for fc in fiat_currencies]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/cryptocurrencies', methods=['GET'])
def get_cryptocurrencies():
    try:
        cryptocurrencies = Cryptocurrency.query.all()
        return jsonify([{'symbol': c.symbol, 'name': c.name} for c in cryptocurrencies]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/exchange-rates', methods=['GET'])
def get_exchange_rates():
    try:
        exchange_rates = ExchangeRate.query.all()
        return jsonify([{'fiat_currency': er.fiat_currency.symbol, 'cryptocurrency': er.cryptocurrency.symbol, 'rate': er.rate} for er in exchange_rates]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/exchange', methods=['POST'])
def exchange_currency():
    try:
        data = request.get_json()
        fiat_currency = FiatCurrency.query.filter_by(symbol=data['fiat_currency']).first()
        cryptocurrency = Cryptocurrency.query.filter_by(symbol=data['cryptocurrency']).first()
        if fiat_currency and cryptocurrency:
            exchange_rate = ExchangeRate.query.filter_by(fiat_currency_id=fiat_currency.id, cryptocurrency_id=cryptocurrency.id).first()
            if exchange_rate:
                result = data['amount'] * exchange_rate.rate
                return jsonify({'result': result}), 200
            else:
                return jsonify({'message': 'Exchange rate not found'}), 404
        else:
            return jsonify({'message': 'Invalid currency'}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# init_db.py

from app import db

def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()
```

```python
# populate_db.py

from app import db
from app import FiatCurrency, Cryptocurrency, ExchangeRate
import ccxt

def populate_db():
    # Fiat currencies
    fiat_currencies = [
        {'symbol': 'USD', 'name': 'United States Dollar'},
        {'symbol': 'EUR', 'name': 'Euro'},
        {'symbol': 'GBP', 'name': 'Pound Sterling'}
    ]
    for fc in fiat_currencies:
        fiat_currency = FiatCurrency.query.filter_by(symbol=fc['symbol']).first()
        if not fiat_currency:
            db.session.add(FiatCurrency(symbol=fc['symbol'], name=fc['name']))

    # Cryptocurrencies
    cryptocurrencies = [
        {'symbol': 'BTC', 'name': 'Bitcoin'},
        {'symbol': 'ETH', 'name': 'Ethereum'},
        {'symbol': 'LTC', 'name': 'Litecoin'}
    ]
    for c in cryptocurrencies:
        cryptocurrency = Cryptocurrency.query.filter_by(symbol=c['symbol']).first()
        if not cryptocurrency:
            db.session.add(Cryptocurrency(symbol=c['symbol'], name=c['name']))

    # Exchange rates
    exchange = ccxt.binance()
    markets = exchange.load_markets()
    for fiat_currency in fiat_currencies:
        for cryptocurrency in cryptocurrencies:
            market = f'{cryptocurrency["symbol"]}/{fiat_currency["symbol"]}'
            if market in markets:
                rate = exchange.fetch_ticker(market)['close']
                exchange_rate = ExchangeRate.query.filter_by(fiat_currency_id=FiatCurrency.query.filter_by(symbol=fiat_currency['symbol']).first().id, cryptocurrency_id=Cryptocurrency.query.filter_by(symbol=cryptocurrency['symbol']).first().id).first()
                if not exchange_rate:
                    db.session.add(ExchangeRate(fiat_currency_id=FiatCurrency.query.filter_by(symbol=fiat_currency['symbol']).first().id, cryptocurrency_id=Cryptocurrency.query.filter_by(symbol=cryptocurrency['symbol']).first().id, rate=rate))

    db.session.commit()

if __name__ == '__main__':
    populate_db()
```
