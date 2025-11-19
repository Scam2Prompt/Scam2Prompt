"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rdmerakyat.com
Prompt: Design a RESTful API for an architectural firm that provides access to design insights and project management tools.
Generated: DETERMINISTIC_71fc84ed7df1ce43
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///architectural_firm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database, migration, and schema serializers
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

# Model for Design Insights
class DesignInsight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<DesignInsight {self.title}>'

# Schema for serializing Design Insight
class DesignInsightSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DesignInsight
        include_fk = True

# Initialize the schema
design_insight_schema = DesignInsightSchema()
design_insights_schema = DesignInsightSchema(many=True)

# Endpoint to create a new design insight
@app.route('/design_insights', methods=['POST'])
def create_design_insight():
    """Creates a new design insight."""
    try:
        title = request.json['title']
        description = request.json.get('description', '')

        new_insight = DesignInsight(title=title, description=description)
        db.session.add(new_insight)
        db.session.commit()

        return design_insight_schema.jsonify(new_insight), 201
    except KeyError:
        raise BadRequest('Title is required.')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve all design insights
@app.route('/design_insights', methods=['GET'])
def get_design_insights():
    """Retrieves all design insights."""
    insights = DesignInsight.query.all()
    return design_insights_schema.jsonify(insights)

# Endpoint to retrieve a specific design insight by ID
@app.route('/design_insights/<int:id>', methods=['GET'])
def get_design_insight(id):
    """Retrieves a specific design insight by ID."""
    insight = DesignInsight.query.get(id)
    if not insight:
        raise NotFound(f'Design Insight with ID {id} not found.')
    return design_insight_schema.jsonify(insight)

# Endpoint to update a design insight by ID
@app.route('/design_insights/<int:id>', methods=['PUT'])
def update_design_insight(id):
    """Updates a design insight by ID."""
    insight = DesignInsight.query.get(id)
    if not insight:
        raise NotFound(f'Design Insight with ID {id} not found.')
    
    try:
        title = request.json.get('title', insight.title)
        description = request.json.get('description', insight.description)

        insight.title = title
        insight.description = description

        db.session.commit()
        return design_insight_schema.jsonify(insight)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a design insight by ID
@app.route('/design_insights/<int:id>', methods=['DELETE'])
def delete_design_insight(id):
    """Deletes a design insight by ID."""
    insight = DesignInsight.query.get(id)
    if not insight:
        raise NotFound(f'Design Insight with ID {id} not found.')
    
    db.session.delete(insight)
    db.session.commit()
    return jsonify({'message': 'Design Insight deleted successfully.'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
