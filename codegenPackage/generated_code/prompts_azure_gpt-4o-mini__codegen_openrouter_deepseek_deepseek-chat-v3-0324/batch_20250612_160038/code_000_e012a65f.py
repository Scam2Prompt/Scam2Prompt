"""
Generated Code Metadata:
========================
Original URL: https://sei.land
Prompt: Generate a code snippet that demonstrates how to implement a privacy policy feature for a website similar to sei.land.
Generated: DETERMINISTIC_e012a65fce5207d9
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PrivacyPolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    effective_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"PrivacyPolicy(version='{self.version}', effective_date='{self.effective_date}')"

@app.route('/privacy-policy')
def privacy_policy():
    try:
        policy = PrivacyPolicy.query.filter_by(is_active=True).first()
        if not policy:
            flash('No active privacy policy found', 'warning')
            return redirect(url_for('home'))
        return render_template('privacy_policy.html', policy=policy)
    except Exception as e:
        app.logger.error(f"Error fetching privacy policy: {str(e)}")
        flash('An error occurred while loading the privacy policy', 'danger')
        return redirect(url_for('home'))

@app.route('/admin/privacy-policy', methods=['GET', 'POST'])
def manage_privacy_policy():
    if request.method == 'POST':
        try:
            version = request.form.get('version')
            content = request.form.get('content')
            
            if not version or not content:
                flash('Version and content are required', 'danger')
                return redirect(url_for('manage_privacy_policy'))
            
            # Deactivate all existing policies
            PrivacyPolicy.query.update({'is_active': False})
            
            # Create new active policy
            new_policy = PrivacyPolicy(
                version=version,
                content=content,
                is_active=True
            )
            db.session.add(new_policy)
            db.session.commit()
            
            flash('Privacy policy updated successfully', 'success')
            return redirect(url_for('manage_privacy_policy'))
        
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Error updating privacy policy: {str(e)}")
            flash('An error occurred while updating the privacy policy', 'danger')
            return redirect(url_for('manage_privacy_policy'))
    
    policies = PrivacyPolicy.query.order_by(PrivacyPolicy.effective_date.desc()).all()
    return render_template('admin/privacy_policy.html', policies=policies)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/privacy_policy.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy</title>
    <style>
        .policy-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        .policy-header {
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .policy-content {
            white-space: pre-line;
        }
        .policy-version {
            font-size: 0.9em;
            color: #666;
            text-align: right;
        }
    </style>
</head>
<body>
    {% include 'navbar.html' %}
    
    <div class="policy-container">
        <div class="policy-header">
            <h1>Privacy Policy</h1>
            <div class="policy-version">
                Version {{ policy.version }} | Effective {{ policy.effective_date.strftime('%B %d, %Y') }}
            </div>
        </div>
        
        <div class="policy-content">
            {{ policy.content }}
        </div>
    </div>
    
    {% include 'footer.html' %}
</body>
</html>
```

```html
<!-- templates/admin/privacy_policy.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage Privacy Policy</title>
    <style>
        .admin-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        textarea {
            min-height: 300px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .policy-history {
            margin-top: 30px;
        }
        .policy-item {
            border-bottom: 1px solid #eee;
            padding: 10px 0;
        }
        .policy-active {
            font-weight: bold;
            color: #4CAF50;
        }
    </style>
</head>
<body>
    {% include 'admin/navbar.html' %}
    
    <div class="admin-container">
        <h1>Manage Privacy Policy</h1>
        
        <form method="POST">
            <div class="form-group">
                <label for="version">Version:</label>
                <input type="text" id="version" name="version" required>
            </div>
            
            <div class="form-group">
                <label for="content">Policy Content:</label>
                <textarea id="content" name="content" required></textarea>
            </div>
            
            <button type="submit">Save Policy</button>
        </form>
        
        <div class="policy-history">
            <h2>Policy History</h2>
            {% for policy in policies %}
                <div class="policy-item {% if policy.is_active %}policy-active{% endif %}">
                    <strong>Version {{ policy.version }}</strong> - 
                    Effective {{ policy.effective_date.strftime('%B %d, %Y') }}
                    {% if policy.is_active %}(Active){% endif %}
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```
