"""
Generated Code Metadata:
========================
Original URL: https://mobleman-doostan.com
Prompt: Generate a code snippet for an e-commerce website that lists various salon equipment like "صندلی آرایشگاهی" and "ترولی آرایشگاهی" with options for filtering by category.
Generated: DETERMINISTIC_a7313ca89595f302
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salon_equipment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the SalonEquipment model
class SalonEquipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<SalonEquipment {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Sample data for demonstration purposes
def seed_data():
    if SalonEquipment.query.count() == 0:
        equipment_list = [
            SalonEquipment(name='صندلی آرایشگاهی', category='صندلی'),
            SalonEquipment(name='ترولی آرایشگاهی', category='ترولی'),
            SalonEquipment(name='دستگاه بخور', category='دستگاه'),
            SalonEquipment(name='آینه آرایشگاهی', category='آینه'),
        ]
        db.session.bulk_save_objects(equipment_list)
        db.session.commit()

# Route to list salon equipment with filtering options
@app.route('/equipment', methods=['GET'])
def list_equipment():
    category_filter = request.args.get('category')
    
    # Query the database for salon equipment
    if category_filter:
        equipment = SalonEquipment.query.filter_by(category=category_filter).all()
    else:
        equipment = SalonEquipment.query.all()
    
    return render_template('equipment_list.html', equipment=equipment)

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    seed_data()  # Seed data if the database is empty
    app.run(debug=True)
```

**HTML Template (equipment_list.html)**

```html
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Salon Equipment List</title>
</head>
<body>
    <h1>لیست تجهیزات سالن</h1>
    <form method="GET" action="/equipment">
        <label for="category">فیلتر بر اساس دسته:</label>
        <select name="category" id="category">
            <option value="">همه</option>
            <option value="صندلی">صندلی</option>
            <option value="ترولی">ترولی</option>
            <option value="دستگاه">دستگاه</option>
            <option value="آینه">آینه</option>
        </select>
        <button type="submit">فیلتر</button>
    </form>
    <ul>
        {% for item in equipment %}
            <li>{{ item.name }} - {{ item.category }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**HTML Template (404.html)**

```html
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>صفحه پیدا نشد</title>
</head>
<body>
    <h1>404 - صفحه پیدا نشد</h1>
    <p>متاسفانه صفحه‌ای که به دنبال آن هستید وجود ندارد.</p>
</body>
</html>
```
