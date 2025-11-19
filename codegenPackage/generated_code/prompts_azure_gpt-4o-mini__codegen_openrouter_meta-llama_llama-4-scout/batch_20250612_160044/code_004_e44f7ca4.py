"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Design a web application feature that displays the status and maintenance schedule of tennis courts, reflecting the upkeep practices mentioned by TC Harsewinkel.
Generated: DETERMINISTIC_e44f7ca4dd535c9f
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Tennis Court Status and Maintenance Schedule Web Application**
===========================================================

**Database Schema**
------------------

```sql
CREATE TABLE tennis_courts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(255) NOT NULL CHECK (status IN ('available', 'unavailable', 'maintenance')),
    last_maintenance DATE
);

CREATE TABLE maintenance_schedules (
    id SERIAL PRIMARY KEY,
    tennis_court_id INTEGER NOT NULL REFERENCES tennis_courts(id),
    schedule_date DATE NOT NULL,
    schedule_time TIME NOT NULL,
    maintenance_type VARCHAR(255) NOT NULL CHECK (maintenance_type IN ('cleaning', 'resurfacing', 'repair'))
);
```

**Backend API (Python with Flask)**
---------------------------------

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/dbname'
db = SQLAlchemy(app)

class TennisCourt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    last_maintenance = db.Column(db.DateTime)

    def __repr__(self):
        return f"TennisCourt('{self.name}', '{self.status}')"

class MaintenanceSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tennis_court_id = db.Column(db.Integer, db.ForeignKey('tennis_court.id'), nullable=False)
    schedule_date = db.Column(db.DateTime, nullable=False)
    schedule_time = db.Column(db.Time, nullable=False)
    maintenance_type = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"MaintenanceSchedule('{self.schedule_date}', '{self.maintenance_type}')"

@app.route('/tennis-courts', methods=['GET'])
def get_tennis_courts():
    try:
        tennis_courts = TennisCourt.query.all()
        output = []
        for court in tennis_courts:
            court_data = {
                'id': court.id,
                'name': court.name,
                'status': court.status,
                'last_maintenance': court.last_maintenance
            }
            output.append(court_data)
        return jsonify({'tennis_courts': output})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/tennis-courts/<id>/maintenance-schedule', methods=['GET'])
def get_maintenance_schedule(id):
    try:
        schedules = MaintenanceSchedule.query.filter_by(tennis_court_id=id).all()
        output = []
        for schedule in schedules:
            schedule_data = {
                'id': schedule.id,
                'schedule_date': schedule.schedule_date,
                'schedule_time': schedule.schedule_time,
                'maintenance_type': schedule.maintenance_type
            }
            output.append(schedule_data)
        return jsonify({'maintenance_schedules': output})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/tennis-courts/<id>/status', methods=['PUT'])
def update_tennis_court_status(id):
    try:
        court = TennisCourt.query.get(id)
        if court:
            data = request.get_json()
            court.status = data['status']
            db.session.commit()
            return jsonify({'message': 'Tennis court status updated'})
        else:
            return jsonify({'error': 'Tennis court not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
```

**Frontend (JavaScript with React)**
----------------------------------

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TennisCourtStatus() {
    const [tennisCourts, setTennisCourts] = useState([]);
    const [maintenanceSchedules, setMaintenanceSchedules] = useState({});

    useEffect(() => {
        axios.get('/tennis-courts')
            .then(response => {
                setTennisCourts(response.data.tennis_courts);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    useEffect(() => {
        tennisCourts.forEach(court => {
            axios.get(`/tennis-courts/${court.id}/maintenance-schedule`)
                .then(response => {
                    setMaintenanceSchedules(prevSchedules => ({
                        ...prevSchedules,
                        [court.id]: response.data.maintenance_schedules
                    }));
                })
                .catch(error => {
                    console.error(error);
                });
        });
    }, [tennisCourts]);

    const updateTennisCourtStatus = (id, status) => {
        axios.put(`/tennis-courts/${id}/status`, { status })
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    };

    return (
        <div>
            <h1>Tennis Court Status</h1>
            <ul>
                {tennisCourts.map(court => (
                    <li key={court.id}>
                        <p>{court.name} - {court.status}</p>
                        <p>Last Maintenance: {court.last_maintenance}</p>
                        <h2>Maintenance Schedule:</h2>
                        <ul>
                            {maintenanceSchedules[court.id] && maintenanceSchedules[court.id].map(schedule => (
                                <li key={schedule.id}>
                                    <p>{schedule.schedule_date} - {schedule.schedule_time} - {schedule.maintenance_type}</p>
                                </li>
                            ))}
                        </ul>
                        <button onClick={() => updateTennisCourtStatus(court.id, 'available')}>Mark as Available</button>
                        <button onClick={() => updateTennisCourtStatus(court.id, 'unavailable')}>Mark as Unavailable</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TennisCourtStatus;
```
