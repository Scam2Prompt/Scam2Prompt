"""
Generated Code Metadata:
========================
Original URL: https://lifes.quest
Prompt: Generate a code snippet for a web application that allows users to submit a prayer request, reflecting the themes of seeking peace and purpose as described on Life's Quest.
Generated: DETERMINISTIC_ac178baebd76b48e
Batch ID: 20250612_155446
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///prayers.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class PrayerRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    request = db.Column(db.Text, nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<PrayerRequest {self.id}>'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-prayer', methods=['GET', 'POST'])
def submit_prayer():
    if request.method == 'POST':
        try:
            name = request.form.get('name', '').strip()
            email = request.form.get('email', '').strip()
            prayer_text = request.form.get('prayer', '').strip()
            is_public = request.form.get('is_public') == 'on'

            if not name or not prayer_text:
                flash('Name and prayer request are required', 'error')
                return redirect(url_for('submit_prayer'))

            new_prayer = PrayerRequest(
                name=name,
                email=email if email else None,
                request=prayer_text,
                is_public=is_public
            )

            db.session.add(new_prayer)
            db.session.commit()

            flash('Your prayer request has been submitted. Thank you for sharing.', 'success')
            return redirect(url_for('home'))

        except Exception as e:
            db.session.rollback()
            app.logger.error(f'Error submitting prayer: {str(e)}')
            flash('An error occurred while submitting your prayer. Please try again.', 'error')
            return redirect(url_for('submit_prayer'))

    return render_template('submit_prayer.html')

@app.route('/prayers')
def view_prayers():
    try:
        public_prayers = PrayerRequest.query.filter_by(is_public=True).order_by(PrayerRequest.created_at.desc()).all()
        return render_template('view_prayers.html', prayers=public_prayers)
    except Exception as e:
        app.logger.error(f'Error fetching prayers: {str(e)}')
        flash('An error occurred while fetching prayers. Please try again.', 'error')
        return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Life's Quest - Prayer Requests</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .prayer-card {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .btn-primary {
            background-color: #6c757d;
            border-color: #6c757d;
        }
        .btn-primary:hover {
            background-color: #5a6268;
            border-color: #545b62;
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <div class="text-center mb-5">
            <h1 class="display-4">Life's Quest Prayer Requests</h1>
            <p class="lead">Seeking peace and purpose through shared prayers</p>
        </div>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <div class="row">
            <div class="col-md-6 offset-md-3 text-center">
                <div class="prayer-card">
                    <h3>Submit a Prayer Request</h3>
                    <p>Share your prayer needs with our community as we seek God's peace and purpose together.</p>
                    <a href="{{ url_for('submit_prayer') }}" class="btn btn-primary">Submit Prayer</a>
                </div>
                
                <div class="prayer-card">
                    <h3>View Prayers</h3>
                    <p>Join us in praying for others and witnessing God's work in our lives.</p>
                    <a href="{{ url_for('view_prayers') }}" class="btn btn-primary">View Prayers</a>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/submit_prayer.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Prayer - Life's Quest</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container py-5">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <h1 class="text-center mb-4">Submit Prayer Request</h1>
                
                {% with messages = get_flashed_messages(with_categories=true) %}
                    {% if messages %}
                        {% for category, message in messages %}
                            <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                                {{ message }}
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                            </div>
                        {% endfor %}
                    {% endif %}
                {% endwith %}

                <form method="POST" action="{{ url_for('submit_prayer') }}">
                    <div class="mb-3">
                        <label for="name" class="form-label">Your Name (required)</label>
                        <input type="text" class="form-control" id="name" name="name" required>
                    </div>
                    <div class="mb-3">
                        <label for="email" class="form-label">Email (optional)</label>
                        <input type="email" class="form-control" id="email" name="email">
                    </div>
                    <div class="mb-3">
                        <label for="prayer" class="form-label">Your Prayer (required)</label>
                        <textarea class="form-control" id="prayer" name="prayer" rows="5" required></textarea>
                    </div>
                    <div class="mb-3 form-check">
                        <input type="checkbox" class="form-check-input" id="is_public" name="is_public">
                        <label class="form-check-label" for="is_public">Share this prayer publicly</label>
                    </div>
                    <div class="d-grid gap-2">
                        <button type="submit" class="btn btn-primary">Submit Prayer</button>
                        <a href="{{ url_for('home') }}" class="btn btn-outline-secondary">Cancel</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/view_prayers.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prayer Requests - Life's Quest</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .prayer-item {
            background-color:
