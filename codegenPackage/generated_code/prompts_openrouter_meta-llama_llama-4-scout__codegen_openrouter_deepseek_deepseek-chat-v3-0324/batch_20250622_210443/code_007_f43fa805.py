"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: How can I implement a digital signage solution for my business in Palermo using Azeta Toner's Web & Media Project services?
Generated: DETERMINISTIC_f43fa8059437d60a
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Digital Signage Solution Implementation for Azeta Toner's Web & Media Project Services

import os
import json
import requests
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm'}
app.config['SCHEDULE_FILE'] = 'schedule.json'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def load_schedule():
    try:
        with open(app.config['SCHEDULE_FILE'], 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"slides": []}

def save_schedule(schedule):
    with open(app.config['SCHEDULE_FILE'], 'w') as f:
        json.dump(schedule, f, indent=2)

@app.route('/')
def display():
    schedule = load_schedule()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('display.html', slides=schedule['slides'], current_time=now)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Handle file upload
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Add to schedule
            schedule = load_schedule()
            slide = {
                'file': filename,
                'duration': int(request.form.get('duration', 10)),
                'start_time': request.form.get('start_time', '00:00'),
                'end_time': request.form.get('end_time', '23:59'),
                'days': request.form.getlist('days')
            }
            schedule['slides'].append(slide)
            save_schedule(schedule)
            
            return redirect(url_for('admin'))
    
    schedule = load_schedule()
    return render_template('admin.html', slides=schedule['slides'])

@app.route('/delete/<int:slide_id>')
def delete_slide(slide_id):
    schedule = load_schedule()
    try:
        # Remove file from filesystem
        slide = schedule['slides'].pop(slide_id)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], slide['file'])
        if os.path.exists(filepath):
            os.remove(filepath)
        save_schedule(schedule)
    except IndexError:
        pass
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

```html
<!-- templates/display.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Digital Signage Display</title>
    <style>
        body { margin: 0; padding: 0; overflow: hidden; }
        #slideshow { width: 100vw; height: 100vh; }
        #slideshow img, #slideshow video { 
            width: 100%; height: 100%; object-fit: contain; 
        }
        #clock {
            position: absolute;
            top: 10px;
            right: 10px;
            color: white;
            background: rgba(0,0,0,0.5);
            padding: 5px 10px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <div id="clock">{{ current_time }}</div>
    <div id="slideshow"></div>

    <script>
        const slides = {{ slides|tojson }};
        let currentSlide = 0;
        
        function updateClock() {
            const now = new Date();
            document.getElementById('clock').textContent = 
                now.toLocaleString('it-IT', { 
                    weekday: 'long', 
                    year: 'numeric', 
                    month: 'long', 
                    day: 'numeric',
                    hour: '2-digit',
                    minute: '2-digit',
                    second: '2-digit'
                });
        }
        
        function showSlide() {
            const now = new Date();
            const currentDay = now.getDay(); // 0=Sunday, 1=Monday, etc.
            const currentTime = now.getHours() * 100 + now.getMinutes();
            
            // Filter slides based on current day and time
            const activeSlides = slides.filter(slide => {
                const days = slide.days || ['0','1','2','3','4','5','6'];
                const start = parseInt(slide.start_time.replace(':', ''));
                const end = parseInt(slide.end_time.replace(':', ''));
                
                return days.includes(currentDay.toString()) && 
                       currentTime >= start && 
                       currentTime <= end;
            });
            
            if (activeSlides.length === 0) return;
            
            currentSlide = (currentSlide + 1) % activeSlides.length;
            const slide = activeSlides[currentSlide];
            const slideshow = document.getElementById('slideshow');
            
            if (slide.file.endsWith('.mp4') || slide.file.endsWith('.webm')) {
                slideshow.innerHTML = `
                    <video autoplay muted loop>
                        <source src="/static/uploads/${slide.file}" type="video/mp4">
                    </video>
                `;
            } else {
                slideshow.innerHTML = `<img src="/static/uploads/${slide.file}" />`;
            }
            
            setTimeout(showSlide, slide.duration * 1000);
        }
        
        // Initialize
        updateClock();
        setInterval(updateClock, 1000);
        showSlide();
    </script>
</body>
</html>
```

```html
<!-- templates/admin.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Digital Signage Admin</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        .slides-list { display: flex; flex-wrap: wrap; gap: 20px; }
        .slide-card { 
            border: 1px solid #ddd; padding: 10px; 
            width: 200px; position: relative;
        }
        .slide-card img, .slide-card video { 
            width: 100%; height: 150px; object-fit: cover; 
        }
        .delete-btn { 
            position: absolute; top: 5px; right: 5px; 
            background: red; color: white; border: none; 
            border-radius: 50%; width: 20px; height: 20px;
            cursor: pointer;
        }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input, select { padding: 8px; width: 100%; }
        .checkbox-group { display: flex; flex-wrap: wrap; gap: 10px; }
        .checkbox-group label { display: flex; align-items: center; }
        button { padding: 10px 15px; background: #4CAF50; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Digital Signage Admin</h1>
        
        <h2>Add New Slide</h2>
        <form method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="file">Media File:</label>
                <input type="file" name="file" id="file" required>
            </div>
            
            <div class="form-group">
                <label for="duration">Duration (seconds):</label>
                <input type="number" name="duration" id="duration" value="10" min="1" required>
            </div>
            
            <div class="form-group">
                <label for="start_time">Start Time:</label>
                <input type="time" name="start_time" id="start_time" value="00:00" required>
            </div>
            
            <div class="form-group">
                <label for="end_time">End Time:</label>
                <input type="time" name="end_time" id="end_time" value="23:59" required>
            </div>
            
            <div class
