"""
Generated Code Metadata:
========================
Original URL: https://genoverde.com
Prompt: Design a RESTful API for GenoVerde's cultivar library, allowing users to access and optimize their plant portfolios.
Generated: DETERMINISTIC_6fcc736841c14019
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
GenoVerde Cultivar Library RESTful API
This API provides endpoints to manage and optimize plant portfolios.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'genoverde.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class Cultivar(db.Model):
    """Cultivar model representing plant varieties"""
    __tablename__ = 'cultivars'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    species = db.Column(db.String(100), nullable=False)
    growth_rate = db.Column(db.Float, nullable=False)
    yield_potential = db.Column(db.Float, nullable=False)
    disease_resistance = db.Column(db.Float, nullable=False)
    climate_tolerance = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, species, growth_rate, yield_potential, disease_resistance, climate_tolerance):
        self.name = name
        self.species = species
        self.growth_rate = growth_rate
        self.yield_potential = yield_potential
        self.disease_resistance = disease_resistance
        self.climate_tolerance = climate_tolerance

class Portfolio(db.Model):
    """Portfolio model representing user plant portfolios"""
    __tablename__ = 'portfolios'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    
    def __init__(self, user_id, name, description):
        self.user_id = user_id
        self.name = name
        self.description = description

class PortfolioCultivar(db.Model):
    """Junction table for portfolio-cultivar many-to-many relationship"""
    __tablename__ = 'portfolio_cultivars'
    
    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False)
    cultivar_id = db.Column(db.Integer, db.ForeignKey('cultivars.id'), nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    
    def __init__(self, portfolio_id, cultivar_id, percentage):
        self.portfolio_id = portfolio_id
        self.cultivar_id = cultivar_id
        self.percentage = percentage

# Schemas
class CultivarSchema(ma.Schema):
    """Schema for Cultivar model"""
    class Meta:
        fields = ('id', 'name', 'species', 'growth_rate', 'yield_potential', 
                 'disease_resistance', 'climate_tolerance')

class PortfolioSchema(ma.Schema):
    """Schema for Portfolio model"""
    cultivars = fields.Nested(CultivarSchema, many=True)
    
    class Meta:
        fields = ('id', 'user_id', 'name', 'description', 'cultivars')

class PortfolioCultivarSchema(ma.Schema):
    """Schema for PortfolioCultivar model"""
    class Meta:
        fields = ('id', 'portfolio_id', 'cultivar_id', 'percentage')

# Initialize schemas
cultivar_schema = CultivarSchema()
cultivars_schema = CultivarSchema(many=True)
portfolio_schema = PortfolioSchema()
portfolios_schema = PortfolioSchema(many=True)
portfolio_cultivar_schema = PortfolioCultivarSchema()
portfolio_cultivars_schema = PortfolioCultivarSchema(many=True)

# Error Handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Routes
@app.route('/cultivars', methods=['GET'])
def get_cultivars():
    """Get all cultivars"""
    try:
        all_cultivars = Cultivar.query.all()
        return cultivars_schema.jsonify(all_cultivars)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/cultivars/<int:id>', methods=['GET'])
def get_cultivar(id):
    """Get a specific cultivar by ID"""
    try:
        cultivar = Cultivar.query.get(id)
        if not cultivar:
            return jsonify({'error': 'Cultivar not found'}), 404
        return cultivar_schema.jsonify(cultivar)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/cultivars', methods=['POST'])
def add_cultivar():
    """Add a new cultivar"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not all(key in data for key in ['name', 'species', 'growth_rate', 
                                          'yield_potential', 'disease_resistance', 
                                          'climate_tolerance']):
            return jsonify({'error': 'Missing required fields'}), 400
            
        new_cultivar = Cultivar(
            name=data['name'],
            species=data['species'],
            growth_rate=data['growth_rate'],
            yield_potential=data['yield_potential'],
            disease_resistance=data['disease_resistance'],
            climate_tolerance=data['climate_tolerance']
        )
        
        db.session.add(new_cultivar)
        db.session.commit()
        return cultivar_schema.jsonify(new_cultivar), 201
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/cultivars/<int:id>', methods=['PUT'])
def update_cultivar(id):
    """Update an existing cultivar"""
    try:
        cultivar = Cultivar.query.get(id)
        if not cultivar:
            return jsonify({'error': 'Cultivar not found'}), 404
            
        data = request.get_json()
        
        cultivar.name = data.get('name', cultivar.name)
        cultivar.species = data.get('species', cultivar.species)
        cultivar.growth_rate = data.get('growth_rate', cultivar.growth_rate)
        cultivar.yield_potential = data.get('yield_potential', cultivar.yield_potential)
        cultivar.disease_resistance = data.get('disease_resistance', cultivar.disease_resistance)
        cultivar.climate_tolerance = data.get('climate_tolerance', cultivar.climate_tolerance)
        
        db.session.commit()
        return cultivar_schema.jsonify(cultivar)
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/cultivars/<int:id>', methods=['DELETE'])
def delete_cultivar(id):
    """Delete a cultivar"""
    try:
        cultivar = Cultivar.query.get(id)
        if not cultivar:
            return jsonify({'error': 'Cultivar not found'}), 404
            
        db.session.delete(cultivar)
        db.session.commit()
        return jsonify({'message': 'Cultivar deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/portfolios', methods=['GET'])
def get_portfolios():
    """Get all portfolios"""
    try:
        all_portfolios = Portfolio.query.all()
        return portfolios_schema.jsonify(all_portfolios)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/portfolios/<int:id>', methods=['GET'])
def get_portfolio(id):
    """Get a specific portfolio by ID"""
    try:
        portfolio = Portfolio.query.get(id)
        if not portfolio:
            return jsonify({'error': 'Portfolio not found'}), 404
            
        # Get associated cultivars
        portfolio_cultivars = PortfolioCultivar.query.filter_by(portfolio_id=id).all()
        cultivars = []
        for pc in portfolio_cultivars:
            cultivar = Cultivar.query.get(pc.cultivar_id)
            if cultivar:
                cultivars.append(cultivar)
                
        portfolio.cultivars = cultivars
        return portfolio_schema.jsonify(portfolio)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/portfolios', methods=['POST'])
def add_portfolio():
    """Add a new portfolio"""
    try:
