"""
Generated Code Metadata:
========================
Original URL: https://energiakert.com
Prompt: Provide an example of how to integrate customer satisfaction tracking in a web application, drawing on the principles highlighted by EnergiaKert's commitment to quality and service.
Generated: DETERMINISTIC_51092f6e1f3e5920
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# customer_satisfaction_tracker.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///customer_satisfaction.db"
db = SQLAlchemy(app)


class CustomerSatisfaction(db.Model):
    """Represents a customer's satisfaction feedback."""

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    satisfaction_level = db.Column(db.String(10), nullable=False)  # e.g., "Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"
    feedback = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"CustomerSatisfaction('{self.customer_name}', '{self.satisfaction_level}')"


@app.route("/feedback", methods=["POST"])
def submit_feedback():
    """
    Handles customer satisfaction feedback submission.

    Expects a JSON payload with the following structure:
    {
        "customer_name": string,
        "satisfaction_level": string,
        "feedback": string (optional)
    }

    Returns:
        A JSON response with a success message or an error message.
    """

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request payload"}), 400

        customer_name = data.get("customer_name")
        satisfaction_level = data.get("satisfaction_level")
        feedback = data.get("feedback")

        if not customer_name or not satisfaction_level:
            return jsonify({"error": "Customer name and satisfaction level are required"}), 400

        # Validate satisfaction level
        valid_satisfaction_levels = ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]
        if satisfaction_level not in valid_satisfaction_levels:
            return jsonify({"error": f"Invalid satisfaction level. Must be one of: {', '.join(valid_satisfaction_levels)}"}), 400

        # Create a new CustomerSatisfaction instance
        feedback_entry = CustomerSatisfaction(
            customer_name=customer_name,
            satisfaction_level=satisfaction_level,
            feedback=feedback,
        )

        # Add to database
        db.session.add(feedback_entry)
        db.session.commit()

        return jsonify({"message": "Feedback submitted successfully"}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Failed to submit feedback"}), 500


@app.route("/feedback", methods=["GET"])
def get_feedback():
    """
    Retrieves all customer satisfaction feedback.

    Returns:
        A JSON response with a list of feedback entries.
    """

    try:
        feedback_entries = CustomerSatisfaction.query.all()
        output = []

        for entry in feedback_entries:
            output.append(
                {
                    "id": entry.id,
                    "customer_name": entry.customer_name,
                    "satisfaction_level": entry.satisfaction_level,
                    "feedback": entry.feedback,
                }
            )

        return jsonify(output), 200

    except SQLAlchemyError as e:
        return jsonify({"error": "Failed to retrieve feedback"}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
