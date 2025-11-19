"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rahelesadeghi.ir
Prompt: Develop a simple mobile app interface that allows users to book individual or child counseling sessions, reflecting the offerings of Dr. Raheleh Sadeghi.
Generated: DETERMINISTIC_523be75affbcfe17
Batch ID: 20250612_163350
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample data to simulate counseling offerings
counseling_offerings = {
    "individual": {
        "title": "Individual Counseling",
        "duration": "60 minutes",
        "price": 100.0
    },
    "child": {
        "title": "Child Counseling",
        "duration": "45 minutes",
        "price": 80.0
    }
}

@app.route("/")
def home():
    """Render the home page with counseling offerings."""
    return render_template("index.html", offerings=counseling_offerings)

@app.route("/book", methods=["POST"])
def book_session():
    """Handle booking of counseling sessions."""
    try:
        session_type = request.form.get("session_type")
        date_time = request.form.get("date_time")

        # Validate input
        if session_type not in counseling_offerings:
            return jsonify({"error": "Invalid session type."}), 400
        
        # Parse the date and time
        booking_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
        
        # Logic to save the booking would go here
        # For now, we simply return a success message
        return jsonify({
            "message": "Booking successful!",
            "session_type": counseling_offerings[session_type]["title"],
            "date_time": booking_time.strftime("%Y-%m-%d %H:%M"),
            "price": counseling_offerings[session_type]["price"]
        }), 200

    except ValueError as ve:
        return jsonify({"error": f"Invalid date format: {str(ve)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Counseling Booking</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Book a Counseling Session with Dr. Raheleh Sadeghi</h1>
        <form id="bookingForm">
            <div class="form-group">
                <label for="session_type">Select Session Type:</label>
                <select id="session_type" name="session_type" class="form-control" required>
                    <option value="" disabled selected>Select a session</option>
                    <option value="individual">Individual Counseling</option>
                    <option value="child">Child Counseling</option>
                </select>
            </div>
            <div class="form-group">
                <label for="date_time">Select Date and Time:</label>
                <input type="datetime-local" id="date_time" name="date_time" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Book Session</button>
        </form>
        <div id="response" class="mt-3"></div>
    </div>
    
    <script>
        document.getElementById("bookingForm").addEventListener("submit", function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            fetch("/book", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("response").innerText = data.message || data.error;
            })
            .catch(error => {
                document.getElementById("response").innerText = "An error occurred while booking.";
            });
        });
    </script>
</body>
</html>
```
### Requirements
- To run this application, you will need to have Flask installed. You can install it using pip:
```bash
pip install Flask
```
- Save the Python code in a file (e.g., `app.py`) and the HTML code in a folder named `templates` as `index.html`.
- Run the application with the command:
```bash
python app.py
```
