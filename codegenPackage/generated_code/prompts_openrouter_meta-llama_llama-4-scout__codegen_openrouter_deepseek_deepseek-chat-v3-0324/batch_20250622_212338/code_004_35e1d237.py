"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Develop a simple web application for creating and managing slo-pitch softball tournament brackets, including single and double elimination formats.
Generated: DETERMINISTIC_35e1d23719308e31
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# slo-pitch-tournament-brackets/app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import json
from datetime import datetime
from typing import List, Dict, Optional

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tournaments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    tournaments = db.relationship('Tournament', backref='organizer', lazy=True)

class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    max_teams = db.Column(db.Integer, nullable=False)
    bracket_type = db.Column(db.String(20), nullable=False)  # 'single' or 'double'
    organizer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    teams = db.relationship('Team', backref='tournament', lazy=True)
    matches = db.relationship('Match', backref='tournament', lazy=True)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_number = db.Column(db.Integer, nullable=False)
    match_number = db.Column(db.Integer, nullable=False)
    team1_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team2_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    winner_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)
    team1 = db.relationship('Team', foreign_keys=[team1_id])
    team2 = db.relationship('Team', foreign_keys=[team2_id])
    winner = db.relationship('Team', foreign_keys=[winner_id])

# Initialize database
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper Functions
def generate_bracket(tournament: Tournament) -> List[Dict]:
    """Generate bracket structure based on tournament type and teams."""
    teams = Team.query.filter_by(tournament_id=tournament.id).all()
    bracket = []
    
    if tournament.bracket_type == 'single':
        rounds = single_elimination_rounds(len(teams))
    else:
        rounds = double_elimination_rounds(len(teams))
    
    for round_num, matches in enumerate(rounds, 1):
        round_matches = []
        for match_num, (team1_idx, team2_idx) in enumerate(matches, 1):
            team1 = teams[team1_idx] if team1_idx is not None else None
            team2 = teams[team2_idx] if team2_idx is not None else None
            
            # Check if match already exists
            existing_match = Match.query.filter_by(
                tournament_id=tournament.id,
                round_number=round_num,
                match_number=match_num
            ).first()
            
            if existing_match:
                round_matches.append(existing_match)
            else:
                new_match = Match(
                    round_number=round_num,
                    match_number=match_num,
                    team1_id=team1.id if team1 else None,
                    team2_id=team2.id if team2 else None,
                    tournament_id=tournament.id
                )
                db.session.add(new_match)
                round_matches.append(new_match)
        
        bracket.append({
            'round': round_num,
            'matches': round_matches
        })
    
    db.session.commit()
    return bracket

def single_elimination_rounds(num_teams: int) -> List[List[tuple]]:
    """Generate single elimination bracket structure."""
    rounds = []
    teams = list(range(num_teams))
    
    while len(teams) > 1:
        round_matches = []
        next_round_teams = []
        
        for i in range(0, len(teams), 2):
            if i+1 < len(teams):
                round_matches.append((teams[i], teams[i+1]))
                next_round_teams.append(None)  # Placeholder for winner
            else:
                round_matches.append((teams[i], None))
                next_round_teams.append(teams[i])
        
        rounds.append(round_matches)
        teams = next_round_teams
    
    return rounds

def double_elimination_rounds(num_teams: int) -> List[List[tuple]]:
    """Generate double elimination bracket structure."""
    # Simplified implementation - would need more complex logic for full double elimination
    winners_rounds = single_elimination_rounds(num_teams)
    losers_rounds = single_elimination_rounds(num_teams - 1)
    
    # Combine winners and losers brackets
    all_rounds = winners_rounds + losers_rounds
    return all_rounds

# Routes
@app.route('/')
def home():
    tournaments = Tournament.query.all()
    return render_template('home.html', tournaments=tournaments)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Please fill out all fields')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password_hash, password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user)
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    tournaments = Tournament.query.filter_by(organizer_id=current_user.id).all()
    return render_template('dashboard.html', tournaments=tournaments)

@app.route('/tournament/new', methods=['GET', 'POST'])
@login_required
def new_tournament():
    if request.method == 'POST':
        name = request.form.get('name')
        start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d')
        end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')
        max_teams = int(request.form.get('max_teams'))
        bracket_type = request.form.get('bracket_type')
        
        if not all([name, start_date, end_date, max_teams, bracket_type]):
            flash('Please fill out all fields')
            return redirect(url_for('new_tournament'))
        
        tournament = Tournament(
            name=name,
            start_date=start_date,
            end_date=end_date,
            max_teams=max_teams,
            bracket_type=bracket_type,
            organizer_id=current_user.id
        )
        
        db.session.add(tournament)
        db.session.commit()
        
        flash('Tournament created successfully')
        return redirect(url_for('dashboard'))
    
    return render_template('new_tournament.html')

@app.route('/tournament/<int:tournament_id>')
def view_tournament(tournament_id):
    tournament = Tournament.query.get_or_404(tournament_id)
    teams = Team.query.filter_by(tournament_id=tournament_id).all()
    matches = Match.query.filter_by(tournament_id=tournament_id).order_by(Match.round_number, Match.match_number).all()
    
    # Organize matches by
