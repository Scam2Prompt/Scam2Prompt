"""
Generated Code Metadata:
========================
Original URL: https://mesogia.com
Prompt: Write Python code to create a directory listing application that categorizes services like "Κοπτικά Εργαλεία," "Οδοντίατροι," and "Φυσικοθεραπευτές," and allows users to search by category and location.
Generated: DETERMINISTIC_5e328c5e49dedd2d
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'json'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Sample data structure
categories = ["Κοπτικά Εργαλεία", "Οδοντίατροι", "Φυσικοθεραπευτές"]
locations = ["Αθήνα", "Θεσσαλονίκη", "Πάτρα", "Ηράκλειο"]

# Database file path
DB_FILE = os.path.join(app.config['UPLOAD_FOLDER'], 'services_db.json')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_services():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_services(services):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(services, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    services = load_services()
    return render_template('index.html', 
                         categories=categories, 
                         locations=locations,
                         services=services)

@app.route('/search', methods=['GET'])
def search():
    category = request.args.get('category', '')
    location = request.args.get('location', '')
    
    services = load_services()
    filtered_services = []
    
    for service in services:
        if (not category or service['category'] == category) and \
           (not location or service['location'] == location):
            filtered_services.append(service)
    
    return render_template('index.html', 
                         categories=categories, 
                         locations=locations,
                         services=filtered_services,
                         selected_category=category,
                         selected_location=location)

@app.route('/add', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        location = request.form.get('location')
        address = request.form.get('address')
        phone = request.form.get('phone')
        
        if not all([name, category, location]):
            return render_template('add.html', 
                                 categories=categories, 
                                 locations=locations,
                                 error="Name, category, and location are required")
        
        services = load_services()
        services.append({
            'name': name,
            'category': category,
            'location': location,
            'address': address,
            'phone': phone
        })
        save_services(services)
        
        return redirect(url_for('index'))
    
    return render_template('add.html', 
                         categories=categories, 
                         locations=locations)

@app.route('/import', methods=['GET', 'POST'])
def import_services():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('import.html', error="No file selected")
        
        file = request.files['file']
        if file.filename == '':
            return render_template('import.html', error="No file selected")
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    imported_services = json.load(f)
                
                if not isinstance(imported_services, list):
                    return render_template('import.html', error="Invalid data format")
                
                services = load_services()
                services.extend(imported_services)
                save_services(services)
                
                os.remove(filepath)
                return redirect(url_for('index'))
            
            except json.JSONDecodeError:
                return render_template('import.html', error="Invalid JSON file")
            except Exception as e:
                return render_template('import.html', error=f"Error processing file: {str(e)}")
        
        return render_template('import.html', error="Invalid file type")
    
    return render_template('import.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="el">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .search-form { margin-bottom: 20px; padding: 15px; background: #f5f5f5; border-radius: 5px; }
        .service-card { border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 5px; }
        .service-name { font-weight: bold; font-size: 1.2em; }
        .service-category { color: #666; }
        .service-location { color: #444; }
        .nav { margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="nav">
        <a href="{{ url_for('index') }}">Home</a> |
        <a href="{{ url_for('add_service') }}">Add Service</a> |
        <a href="{{ url_for('import_services') }}">Import Services</a>
    </div>

    <form class="search-form" action="{{ url_for('search') }}" method="get">
        <select name="category">
            <option value="">All Categories</option>
            {% for category in categories %}
                <option value="{{ category }}" {% if selected_category == category %}selected{% endif %}>{{ category }}</option>
            {% endfor %}
        </select>
        
        <select name="location">
            <option value="">All Locations</option>
            {% for location in locations %}
                <option value="{{ location }}" {% if selected_location == location %}selected{% endif %}>{{ location }}</option>
            {% endfor %}
        </select>
        
        <button type="submit">Search</button>
        <a href="{{ url_for('index') }}">Clear</a>
    </form>

    {% if services %}
        <h2>Found {{ services|length }} services</h2>
        {% for service in services %}
            <div class="service-card">
                <div class="service-name">{{ service.name }}</div>
                <div class="service-category">{{ service.category }}</div>
                <div class="service-location">{{ service.location }}</div>
                {% if service.address %}<div>{{ service.address }}</div>{% endif %}
                {% if service.phone %}<div>Phone: {{ service.phone }}</div>{% endif %}
            </div>
        {% endfor %}
    {% else %}
        <p>No services found. Try different search criteria.</p>
    {% endif %}
</body>
</html>
```

```html
<!-- templates/add.html -->
<!DOCTYPE html>
<html lang="el">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Service</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input, select { padding: 8px; width: 300px; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>Add New Service</h1>
    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}
    <form method="post">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div class="form-group">
            <label for="category">Category:</label>
            <select id="category" name="category" required>
                <option value="">Select a category</option>
                {% for category in categories %}
                    <option value="{{ category }}">{{ category }}</option>
                {% endfor %}
            </select>
        </div>
        
        <div class="form-group">
            <label for="location">Location:</label>
            <select id="location" name="location" required>
                <option value="">Select a location</option>
                {% for location in locations %}
                    <option value="{{ location }}">{{ location }}</option>
                {% endfor %}
            </select>
        </div>
        
        <div class="form-group">
            <label for="address">Address (optional):</label>
            <input type="text
