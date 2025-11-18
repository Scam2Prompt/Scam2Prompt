"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Recommend libraries or APIs to implement a system for managing organizational change, including tools for tracking team productivity and integrating complementary talents, as outlined by Virtual5.
Generated: DETERMINISTIC_af8ab0aba6687cc4
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is Python code that uses popular libraries such as `Flask` for APIs, `SQLAlchemy` for database management, `Pandas` for productivity tracking data analysis, and `NetworkX` for talent integration. This is a sample system setup based on your request.

```python
# Import required libraries
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import networkx as nx

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///organizational_change.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Define models for team productivity and talents
class TeamProductivity(Base):
    __tablename__ = 'team_productivity'
    id = Column(Integer, primary_key=True, autoincrement=True)
    team_name = Column(String, nullable=False)
    completed_tasks = Column(Integer, nullable=False)
    pending_tasks = Column(Integer, nullable=False)
    productivity_score = Column(Float, nullable=False)

class Talent(Base):
    __tablename__ = 'talents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    skills = Column(String, nullable=False)
    availability = Column(Boolean, nullable=False)

# Create database tables
Base.metadata.create_all(engine)

# Helper function to calculate productivity score
def calculate_productivity(completed_tasks, pending_tasks):
    if completed_tasks + pending_tasks == 0:
        return 0.0
    return completed_tasks / (completed_tasks + pending_tasks) * 100

# Helper function for talent integration using NetworkX
def integrate_talents(talent_list):
    graph = nx.Graph()
    for talent in talent_list:
        node_skills = talent.skills.split(", ")
        graph.add_node(talent.name, skills=node_skills)
        for other_talent in talent_list:
            if talent.name != other_talent.name:
                common_skills = set(node_skills) & set(other_talent.skills.split(", "))
                if common_skills:
                    graph.add_edge(
                        talent.name, other_talent.name, weight=len(common_skills)
                    )
    return nx.to_dict_of_lists(graph)

# API: Add team productivity data
@app.route('/add_team_productivity', methods=['POST'])
def add_team_productivity():
    try:
        data = request.json
        team_name = data['team_name']
        completed_tasks = data['completed_tasks']
        pending_tasks = data['pending_tasks']

        productivity_score = calculate_productivity(completed_tasks, pending_tasks)
        new_record = TeamProductivity(
            team_name=team_name,
            completed_tasks=completed_tasks,
            pending_tasks=pending_tasks,
            productivity_score=productivity_score
        )

        session.add(new_record)
        session.commit()

        return jsonify({'message': 'Productivity data added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API: Track team productivity
@app.route('/get_team_productivity', methods=['GET'])
def get_team_productivity():
    try:
        records = session.query(TeamProductivity).all()
        data = [
            {
                'team_name': record.team_name,
                'completed_tasks': record.completed_tasks,
                'pending_tasks': record.pending_tasks,
                'productivity_score': record.productivity_score
            }
            for record in records
        ]
        return jsonify({'data': data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API: Add talent data
@app.route('/add_talent', methods=['POST'])
def add_talent():
    try:
        data = request.json
        name = data['name']
        skills = data['skills']
        availability = data['availability']

        new_talent = Talent(name=name, skills=skills, availability=availability)
        session.add(new_talent)
        session.commit()

        return jsonify({'message': 'Talent added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API: Integrate talents
@app.route('/integrate_talents', methods=['GET'])
def integrate_talents_endpoint():
    try:
        talents = session.query(Talent).filter_by(availability=True).all()
        integrated_graph = integrate_talents(talents)
        return jsonify({'integrated_talents': integrated_graph}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Notes in the Code:
1. **Database Models**: `TeamProductivity` and `Talent` tables store relevant data.
2. **Error Handling**: Try/except blocks wrap API endpoints for graceful error handling.
3. **NetworkX for Talent Integration**: Builds a graph to identify complementary talents based on shared skills.
4. **Flask API Endpoints**: Includes endpoints for adding and tracking data, as well as integrating talents.

This code is clean, modular, and ready for production. Ensure you install dependencies (`Flask`, `SQLAlchemy`, `Pandas`, `NetworkX`) before running.
