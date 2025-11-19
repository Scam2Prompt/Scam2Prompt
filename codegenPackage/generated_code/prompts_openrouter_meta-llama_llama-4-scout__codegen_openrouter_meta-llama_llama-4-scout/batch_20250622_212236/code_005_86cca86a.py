"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Design a system to handle student testimonials and reviews for Sakura Dance Studio, including data storage, moderation, and display on the website.
Generated: DETERMINISTIC_86cca86a54db4b65
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Sakura Dance Studio Testimonial System**
==========================================

### Database Schema

```sql
CREATE TABLE testimonials (
  id INT PRIMARY KEY AUTO_INCREMENT,
  student_name VARCHAR(255) NOT NULL,
  review TEXT NOT NULL,
  rating TINYINT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  is_approved BOOLEAN DEFAULT FALSE
);

CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('admin', 'moderator') NOT NULL
);
```

### Backend API (Python, Flask)

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(255), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    is_approved = db.Column(db.Boolean, nullable=False, default=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('admin', 'moderator'), nullable=False)

@app.route('/testimonials', methods=['POST'])
def create_testimonial():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    
    testimonial = Testimonial(
        student_name=data['student_name'],
        review=data['review'],
        rating=data['rating']
    )
    db.session.add(testimonial)
    db.session.commit()
    return jsonify({'message': 'Testimonial created successfully'}), 201

@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    testimonials = Testimonial.query.filter_by(is_approved=True).all()
    output = []
    for testimonial in testimonials:
        testimonial_data = {
            'id': testimonial.id,
            'student_name': testimonial.student_name,
            'review': testimonial.review,
            'rating': testimonial.rating,
            'created_at': testimonial.created_at
        }
        output.append(testimonial_data)
    return jsonify({'testimonials': output})

@app.route('/testimonials/<id>', methods=['GET'])
def get_testimonial(id):
    testimonial = Testimonial.query.get(id)
    if not testimonial:
        return jsonify({'error': 'Testimonial not found'}), 404
    if not testimonial.is_approved:
        return jsonify({'error': 'Testimonial not approved'}), 403
    testimonial_data = {
        'id': testimonial.id,
        'student_name': testimonial.student_name,
        'review': testimonial.review,
        'rating': testimonial.rating,
        'created_at': testimonial.created_at
    }
    return jsonify({'testimonial': testimonial_data})

@app.route('/testimonials/<id>/approve', methods=['PATCH'])
def approve_testimonial(id):
    user = User.query.get(request.json['user_id'])
    if not user or user.role not in ['admin', 'moderator']:
        return jsonify({'error': 'Unauthorized'}), 401
    testimonial = Testimonial.query.get(id)
    if not testimonial:
        return jsonify({'error': 'Testimonial not found'}), 404
    testimonial.is_approved = True
    db.session.commit()
    return jsonify({'message': 'Testimonial approved successfully'})

if __name__ == '__main__':
    app.run(debug=True)
```

### Frontend (JavaScript, React)

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TestimonialForm() {
    const [studentName, setStudentName] = useState('');
    const [review, setReview] = useState('');
    const [rating, setRating] = useState(0);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/testimonials', {
                student_name: studentName,
                review,
                rating
            });
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Student Name:
                <input type="text" value={studentName} onChange={(e) => setStudentName(e.target.value)} />
            </label>
            <br />
            <label>
                Review:
                <textarea value={review} onChange={(e) => setReview(e.target.value)} />
            </label>
            <br />
            <label>
                Rating:
                <input type="number" value={rating} onChange={(e) => setRating(e.target.value)} />
            </label>
            <br />
            <button type="submit">Submit</button>
        </form>
    );
}

function TestimonialList() {
    const [testimonials, setTestimonials] = useState([]);

    useEffect(() => {
        axios.get('/testimonials')
            .then(response => {
                setTestimonials(response.data.testimonials);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    return (
        <ul>
            {testimonials.map(testimonial => (
                <li key={testimonial.id}>
                    <p>{testimonial.student_name}</p>
                    <p>{testimonial.review}</p>
                    <p>Rating: {testimonial.rating}</p>
                </li>
            ))}
        </ul>
    );
}

export { TestimonialForm, TestimonialList };
```

### Moderation Panel (JavaScript, React)

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ModerationPanel() {
    const [testimonials, setTestimonials] = useState([]);
    const [userId, setUserId] = useState('');

    useEffect(() => {
        axios.get('/testimonials')
            .then(response => {
                setTestimonials(response.data.testimonials);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    const handleApprove = async (id) => {
        try {
            const response = await axios.patch(`/testimonials/${id}/approve`, {
                user_id: userId
            });
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h1>Moderation Panel</h1>
            <ul>
                {testimonials.map(testimonial => (
                    <li key={testimonial.id}>
                        <p>{testimonial.student_name}</p>
                        <p>{testimonial.review}</p>
                        <p>Rating: {testimonial.rating}</p>
                        <button onClick={() => handleApprove(testimonial.id)}>Approve</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ModerationPanel;
```
