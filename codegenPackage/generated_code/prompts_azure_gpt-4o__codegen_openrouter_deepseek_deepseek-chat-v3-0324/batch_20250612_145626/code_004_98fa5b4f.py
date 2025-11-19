"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Suggest an API or library for managing player profiles and performance metrics, tailored for basketball training programs like those offered by L-Zero, including skill refinement and game IQ tracking.
Generated: DETERMINISTIC_98fa5b4f7a5c90c9
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# basketball_profile_manager.py
"""
A module for managing basketball player profiles and performance metrics.
Uses SQLAlchemy for database operations and Marshmallow for data serialization.
"""

from datetime import datetime
from typing import Dict, List, Optional
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import exc
from marshmallow import fields, validate, ValidationError

# Initialize database and marshmallow
db = SQLAlchemy()
ma = Marshmallow()

class PlayerProfile(db.Model):
    """Database model for player profiles."""
    __tablename__ = 'player_profiles'

    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    height = db.Column(db.Float)  # in meters
    weight = db.Column(db.Float)  # in kg
    position = db.Column(db.String(50))
    team = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to performance metrics
    metrics = db.relationship('PerformanceMetric', backref='player', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<PlayerProfile {self.player_name}>'

class PerformanceMetric(db.Model):
    """Database model for performance metrics."""
    __tablename__ = 'performance_metrics'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player_profiles.id'), nullable=False)
    date_recorded = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Skill metrics
    shooting_percentage = db.Column(db.Float)
    free_throw_percentage = db.Column(db.Float)
    three_point_percentage = db.Column(db.Float)
    dribbling_rating = db.Column(db.Integer, validate=validate.Range(min=1, max=10))
    passing_rating = db.Column(db.Integer, validate=validate.Range(min=1, max=10))
    defense_rating = db.Column(db.Integer, validate=validate.Range(min=1, max=10))
    
    # Game IQ metrics
    decision_making = db.Column(db.Integer, validate=validate.Range(min=1, max=10))
    basketball_iq = db.Column(db.Integer, validate=validate.Range(min=1, max=10))
    leadership = db.Column(db.Integer, validate=validate.Range(min=1, max=10))

    def __repr__(self):
        return f'<PerformanceMetric for Player {self.player_id}>'

class PlayerProfileSchema(ma.SQLAlchemyAutoSchema):
    """Schema for player profile serialization."""
    class Meta:
        model = PlayerProfile
        load_instance = True
        include_fk = True
    
    metrics = fields.Nested('PerformanceMetricSchema', many=True, exclude=('player',))

class PerformanceMetricSchema(ma.SQLAlchemyAutoSchema):
    """Schema for performance metric serialization."""
    class Meta:
        model = PerformanceMetric
        load_instance = True
        include_fk = True
    
    player = fields.Nested(PlayerProfileSchema, exclude=('metrics',))

# Initialize schemas
player_profile_schema = PlayerProfileSchema()
performance_metric_schema = PerformanceMetricSchema()
player_profiles_schema = PlayerProfileSchema(many=True)
performance_metrics_schema = PerformanceMetricSchema(many=True)

class BasketballProfileManager:
    """Manager class for handling player profiles and metrics."""
    
    @staticmethod
    def create_player_profile(profile_data: Dict) -> Dict:
        """Create a new player profile."""
        try:
            profile = player_profile_schema.load(profile_data)
            db.session.add(profile)
            db.session.commit()
            return player_profile_schema.dump(profile), 201
        except ValidationError as err:
            db.session.rollback()
            return {'error': err.messages}, 400
        except exc.SQLAlchemyError as err:
            db.session.rollback()
            return {'error': str(err)}, 500

    @staticmethod
    def get_player_profile(player_id: int) -> Dict:
        """Retrieve a player profile by ID."""
        profile = PlayerProfile.query.get(player_id)
        if not profile:
            return {'error': 'Player not found'}, 404
        return player_profile_schema.dump(profile), 200

    @staticmethod
    def update_player_profile(player_id: int, update_data: Dict) -> Dict:
        """Update an existing player profile."""
        try:
            profile = PlayerProfile.query.get(player_id)
            if not profile:
                return {'error': 'Player not found'}, 404
            
            for key, value in update_data.items():
                setattr(profile, key, value)
            
            db.session.commit()
            return player_profile_schema.dump(profile), 200
        except exc.SQLAlchemyError as err:
            db.session.rollback()
            return {'error': str(err)}, 500

    @staticmethod
    def delete_player_profile(player_id: int) -> Dict:
        """Delete a player profile."""
        try:
            profile = PlayerProfile.query.get(player_id)
            if not profile:
                return {'error': 'Player not found'}, 404
            
            db.session.delete(profile)
            db.session.commit()
            return {'message': 'Player deleted successfully'}, 200
        except exc.SQLAlchemyError as err:
            db.session.rollback()
            return {'error': str(err)}, 500

    @staticmethod
    def add_performance_metric(player_id: int, metric_data: Dict) -> Dict:
        """Add performance metrics for a player."""
        try:
            metric_data['player_id'] = player_id
            metric = performance_metric_schema.load(metric_data)
            db.session.add(metric)
            db.session.commit()
            return performance_metric_schema.dump(metric), 201
        except ValidationError as err:
            db.session.rollback()
            return {'error': err.messages}, 400
        except exc.SQLAlchemyError as err:
            db.session.rollback()
            return {'error': str(err)}, 500

    @staticmethod
    def get_player_metrics(player_id: int) -> Dict:
        """Get all performance metrics for a player."""
        metrics = PerformanceMetric.query.filter_by(player_id=player_id).all()
        if not metrics:
            return {'error': 'No metrics found for player'}, 404
        return performance_metrics_schema.dump(metrics), 200

    @staticmethod
    def get_metric_trends(player_id: int, metric_name: str) -> Dict:
        """Get historical trends for a specific metric."""
        if not hasattr(PerformanceMetric, metric_name):
            return {'error': 'Invalid metric name'}, 400
            
        metrics = PerformanceMetric.query.filter_by(player_id=player_id).order_by(PerformanceMetric.date_recorded).all()
        if not metrics:
            return {'error': 'No metrics found for player'}, 404
            
        trend_data = [{
            'date': m.date_recorded.isoformat(),
            'value': getattr(m, metric_name)
        } for m in metrics if getattr(m, metric_name) is not None]
        
        return {'trend_data': trend_data}, 200
```
