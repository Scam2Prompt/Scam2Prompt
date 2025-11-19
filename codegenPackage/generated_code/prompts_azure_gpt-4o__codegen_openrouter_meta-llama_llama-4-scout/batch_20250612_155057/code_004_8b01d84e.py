"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Create a REST API design for Stellar Crop that supports player data storage, including crop growth statistics, planetary exploration logs, and interactions with "Koloni sakinleri."
Generated: DETERMINISTIC_8b01d84ed7aa2046
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Stellar Crop REST API**
=========================

### Dependencies

* `flask`: For building the REST API
* `flask_sqlalchemy`: For database operations
* `marshmallow`: For serialization and deserialization

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stellar_crop.db"
db = SQLAlchemy(app)


# Models
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    crop_growth_stats = db.relationship("CropGrowthStat", backref="player", lazy=True)
    planetary_exploration_logs = db.relationship("PlanetaryExplorationLog", backref="player", lazy=True)
    koloni_sakinleri_interactions = db.relationship("KoloniSakinleriInteraction", backref="player", lazy=True)

    def __init__(self, name):
        self.name = name


class CropGrowthStat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    crop_name = db.Column(db.String(100), nullable=False)
    growth_stage = db.Column(db.String(100), nullable=False)

    def __init__(self, player_id, crop_name, growth_stage):
        self.player_id = player_id
        self.crop_name = crop_name
        self.growth_stage = growth_stage


class PlanetaryExplorationLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    planet_name = db.Column(db.String(100), nullable=False)
    exploration_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, player_id, planet_name, exploration_date):
        self.player_id = player_id
        self.planet_name = planet_name
        self.exploration_date = exploration_date


class KoloniSakinleriInteraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    interaction_type = db.Column(db.String(100), nullable=False)
    interaction_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, player_id, interaction_type, interaction_date):
        self.player_id = player_id
        self.interaction_type = interaction_type
        self.interaction_date = interaction_date


# Schemas
class PlayerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))


class CropGrowthStatSchema(Schema):
    id = fields.Int(dump_only=True)
    player_id = fields.Int(required=True)
    crop_name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    growth_stage = fields.Str(required=True, validate=validate.Length(min=1, max=100))


class PlanetaryExplorationLogSchema(Schema):
    id = fields.Int(dump_only=True)
    player_id = fields.Int(required=True)
    planet_name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    exploration_date = fields.DateTime(required=True)


class KoloniSakinleriInteractionSchema(Schema):
    id = fields.Int(dump_only=True)
    player_id = fields.Int(required=True)
    interaction_type = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    interaction_date = fields.DateTime(required=True)


# API Endpoints
@app.route("/players", methods=["GET", "POST"])
def players():
    if request.method == "GET":
        players = Player.query.all()
        schema = PlayerSchema(many=True)
        return jsonify(schema.dump(players))
    elif request.method == "POST":
        try:
            schema = PlayerSchema()
            data = schema.load(request.json)
            player = Player(data["name"])
            db.session.add(player)
            db.session.commit()
            return jsonify(schema.dump(player)), 201
        except ValidationError as err:
            return jsonify({"error": err.messages}), 400


@app.route("/players/<int:player_id>/crop-growth-stats", methods=["GET", "POST"])
def crop_growth_stats(player_id):
    if request.method == "GET":
        stats = CropGrowthStat.query.filter_by(player_id=player_id).all()
        schema = CropGrowthStatSchema(many=True)
        return jsonify(schema.dump(stats))
    elif request.method == "POST":
        try:
            schema = CropGrowthStatSchema()
            data = schema.load(request.json)
            stat = CropGrowthStat(data["player_id"], data["crop_name"], data["growth_stage"])
            db.session.add(stat)
            db.session.commit()
            return jsonify(schema.dump(stat)), 201
        except ValidationError as err:
            return jsonify({"error": err.messages}), 400


@app.route("/players/<int:player_id>/planetary-exploration-logs", methods=["GET", "POST"])
def planetary_exploration_logs(player_id):
    if request.method == "GET":
        logs = PlanetaryExplorationLog.query.filter_by(player_id=player_id).all()
        schema = PlanetaryExplorationLogSchema(many=True)
        return jsonify(schema.dump(logs))
    elif request.method == "POST":
        try:
            schema = PlanetaryExplorationLogSchema()
            data = schema.load(request.json)
            log = PlanetaryExplorationLog(data["player_id"], data["planet_name"], data["exploration_date"])
            db.session.add(log)
            db.session.commit()
            return jsonify(schema.dump(log)), 201
        except ValidationError as err:
            return jsonify({"error": err.messages}), 400


@app.route("/players/<int:player_id>/koloni-sakinleri-interactions", methods=["GET", "POST"])
def koloni_sakinleri_interactions(player_id):
    if request.method == "GET":
        interactions = KoloniSakinleriInteraction.query.filter_by(player_id=player_id).all()
        schema = KoloniSakinleriInteractionSchema(many=True)
        return jsonify(schema.dump(interactions))
    elif request.method == "POST":
        try:
            schema = KoloniSakinleriInteractionSchema()
            data = schema.load(request.json)
            interaction = KoloniSakinleriInteraction(data["player_id"], data["interaction_type"], data["interaction_date"])
            db.session.add(interaction)
            db.session.commit()
            return jsonify(schema.dump(interaction)), 201
        except ValidationError as err:
            return jsonify({"error": err.messages}), 400


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
