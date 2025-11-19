"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Write a Python script to create a website for a Spanish language school that offers classes for foreigners, including features for booking appointments and displaying services.
Generated: DETERMINISTIC_a272eb546ff1f9a3
Batch ID: 20250622_205936
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Database model for services
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Database model for appointments
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the homepage with available services."""
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/book', methods=['GET', 'POST'])
def book():
    """Handle booking appointments."""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        service_id = request.form['service_id']
        
        # Error handling for missing fields
        if not name or not email or not service_id:
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('book'))
        
        # Create a new appointment
        new_appointment = Appointment(name=name, email=email, service_id=service_id)
        db.session.add(new_appointment)
        db.session.commit()
        flash('Appointment booked successfully!', 'success')
        return redirect(url_for('index'))
    
    services = Service.query.all()
    return render_template('book.html', services=services)

@app.route('/services')
def services():
    """Display all services offered by the school."""
    services = Service.query.all()
    return render_template('services.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Escuela de Idiomas</title>
</head>
<body>
    <h1>Bienvenido a nuestra Escuela de Idiomas</h1>
    <h2>Servicios Disponibles</h2>
    <ul>
        {% for service in services %}
            <li>{{ service.name }} - {{ service.description }} - ${{ service.price }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('book') }}">Reservar una Cita</a>
</body>
</html>
```

**book.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reservar Cita</title>
</head>
<body>
    <h1>Reservar una Cita</h1>
    <form method="POST">
        <label for="name">Nombre:</label>
        <input type="text" name="name" required>
        <label for="email">Correo Electrónico:</label>
        <input type="email" name="email" required>
        <label for="service_id">Servicio:</label>
        <select name="service_id" required>
            {% for service in services %}
                <option value="{{ service.id }}">{{ service.name }}</option>
            {% endfor %}
        </select>
        <button type="submit">Reservar</button>
    </form>
    <a href="{{ url_for('index') }}">Volver</a>
</body>
</html>
```

**services.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servicios</title>
</head>
<body>
    <h1>Servicios Ofrecidos</h1>
    <ul>
        {% for service in services %}
            <li>{{ service.name }} - {{ service.description }} - ${{ service.price }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Volver a Inicio</a>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure random key for production.
- The database is set to SQLite for simplicity; consider using a more robust database for production.
