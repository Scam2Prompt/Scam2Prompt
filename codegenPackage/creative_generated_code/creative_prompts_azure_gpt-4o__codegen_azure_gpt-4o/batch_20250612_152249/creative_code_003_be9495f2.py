"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Suggest tools or frameworks to create an event calendar for SKI Foundation's "Serial Webinar AgroSociopreneurship" program, ensuring integration with email notifications for participants.
Generated: DETERMINISTIC_be9495f2f376f073
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries and modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure email settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-password'         # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

# Initialize database and email modules
db = SQLAlchemy(app)
mail = Mail(app)

# Define database model for events
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), nullable=False)  # Organizer's email

    def __repr__(self):
        return f"<Event {self.title}>"

# Route to display all events
@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

# Route to add a new event
@app.route('/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        try:
            # Extract event details from form
            title = request.form['title']
            description = request.form['description']
            start_time = datetime.datetime.strptime(request.form['start_time'], '%Y-%m-%d %H:%M:%S')
            end_time = datetime.datetime.strptime(request.form['end_time'], '%Y-%m-%d %H:%M:%S')
            email = request.form['email']

            # Create and save new event to the database
            new_event = Event(title=title, description=description, start_time=start_time, end_time=end_time, email=email)
            db.session.add(new_event)
            db.session.commit()

            # Send email notification to organizer
            send_email_notification(new_event)
            
            flash('Event added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            # Handle errors gracefully
            flash(f'Error adding event: {str(e)}', 'danger')
            return redirect(url_for('add_event'))
    return render_template('add_event.html')

# Function to send email notifications
def send_email_notification(event):
    try:
        message = Message(
            subject=f"Event Created: {event.title}",
            recipients=[event.email],  # Send email to the event organizer
            body=f"Dear Organizer,\n\nYour event '{event.title}' has been successfully created.\n\nDetails:\n"
                 f"Description: {event.description}\n"
                 f"Start Time: {event.start_time}\n"
                 f"End Time: {event.end_time}\n\nThank you for using SKI Foundation Event Calendar!"
        )
        mail.send(message)
    except Exception as e:
        print(f"Error sending email: {str(e)}")  # Log email errors

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Main entry point of the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Note:** This code assumes the existence of HTML templates (`index.html`, `add_event.html`, `404.html`, `500.html`) for rendering pages. Replace `your-email@gmail.com` and `your-password` with actual credentials, or use environment variables for better security.
