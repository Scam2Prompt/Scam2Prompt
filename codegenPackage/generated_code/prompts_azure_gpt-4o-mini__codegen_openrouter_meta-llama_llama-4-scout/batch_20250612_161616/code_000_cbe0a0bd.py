"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: How can I implement a cashless payment system for school meals similar to the NO CASH initiative described on the It's Cool website?
Generated: DETERMINISTIC_cbe0a0bd470358aa
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Cashless Payment System for School Meals**
=============================================

### **Database Schema**
```sql
-- schema.sql

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  balance DECIMAL(10, 2) DEFAULT 0.00
);

CREATE TABLE meals (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  student_id INTEGER NOT NULL,
  meal_id INTEGER NOT NULL,
  timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (meal_id) REFERENCES meals(id)
);
```

### **Backend API (Python with Flask)**
```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@host:port/dbname"
db = SQLAlchemy(app)

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), unique=True, nullable=False)
  balance = db.Column(db.DECIMAL(10, 2), default=0.00)
  password_hash = db.Column(db.String(128))

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

class Meal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  price = db.Column(db.DECIMAL(10, 2), nullable=False)

class Transaction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
  meal_id = db.Column(db.Integer, db.ForeignKey("meal.id"), nullable=False)
  timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
  amount = db.Column(db.DECIMAL(10, 2), nullable=False)

@app.route("/students", methods=["POST"])
def create_student():
  data = request.get_json()
  student = Student(name=data["name"], email=data["email"])
  student.set_password(data["password"])
  db.session.add(student)
  db.session.commit()
  return jsonify({"message": "Student created successfully"}), 201

@app.route("/meals", methods=["POST"])
def create_meal():
  data = request.get_json()
  meal = Meal(name=data["name"], price=data["price"])
  db.session.add(meal)
  db.session.commit()
  return jsonify({"message": "Meal created successfully"}), 201

@app.route("/students/<int:student_id>/balance", methods=["GET"])
def get_balance(student_id):
  student = Student.query.get(student_id)
  if student is None:
    return jsonify({"error": "Student not found"}), 404
  return jsonify({"balance": student.balance})

@app.route("/students/<int:student_id>/balance", methods=["PATCH"])
def update_balance(student_id):
  student = Student.query.get(student_id)
  if student is None:
    return jsonify({"error": "Student not found"}), 404
  data = request.get_json()
  student.balance = data["balance"]
  db.session.commit()
  return jsonify({"message": "Balance updated successfully"})

@app.route("/meals/<int:meal_id>/purchase", methods=["POST"])
def purchase_meal(meal_id):
  meal = Meal.query.get(meal_id)
  if meal is None:
    return jsonify({"error": "Meal not found"}), 404
  student_id = request.json["student_id"]
  student = Student.query.get(student_id)
  if student is None:
    return jsonify({"error": "Student not found"}), 404
  if student.balance < meal.price:
    return jsonify({"error": "Insufficient balance"}), 400
  transaction = Transaction(student_id=student_id, meal_id=meal_id, amount=meal.price)
  student.balance -= meal.price
  db.session.add(transaction)
  db.session.commit()
  return jsonify({"message": "Meal purchased successfully"})

if __name__ == "__main__":
  app.run(debug=True)
```

### **Frontend (JavaScript with React)**
```javascript
// App.js

import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [students, setStudents] = useState([]);
  const [meals, setMeals] = useState([]);
  const [balance, setBalance] = useState(0.00);
  const [selectedMeal, setSelectedMeal] = useState(null);

  useEffect(() => {
    axios.get("/students")
      .then(response => {
        setStudents(response.data);
      })
      .catch(error => {
        console.error(error);
      });
    axios.get("/meals")
      .then(response => {
        setMeals(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handlePurchaseMeal = () => {
    if (selectedMeal) {
      axios.post(`/meals/${selectedMeal.id}/purchase`, { student_id: 1 })
        .then(response => {
          setBalance(response.data.balance);
        })
        .catch(error => {
          console.error(error);
        });
    }
  };

  return (
    <div>
      <h1>Cashless Payment System</h1>
      <h2>Students</h2>
      <ul>
        {students.map(student => (
          <li key={student.id}>{student.name}</li>
        ))}
      </ul>
      <h2>Meals</h2>
      <ul>
        {meals.map(meal => (
          <li key={meal.id}>
            {meal.name} - ${meal.price}
            <button onClick={() => setSelectedMeal(meal)}>Select</button>
          </li>
        ))}
      </ul>
      {selectedMeal && (
        <div>
          <p>You have selected: {selectedMeal.name}</p>
          <p>Balance: ${balance}</p>
          <button onClick={handlePurchaseMeal}>Purchase</button>
        </div>
      )}
    </div>
  );
}

export default App;
```
