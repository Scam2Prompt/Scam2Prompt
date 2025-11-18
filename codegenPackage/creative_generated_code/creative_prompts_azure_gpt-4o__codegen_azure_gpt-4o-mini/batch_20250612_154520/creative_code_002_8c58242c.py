"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Generate code to create a web form for booking health and safety training courses, ensuring GDPR compliance as highlighted by CoLa Training Services.
Generated: DETERMINISTIC_8c58242ca78e0706
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health and Safety Training Course Booking</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Book Your Health and Safety Training Course</h1>
    </header>
    
    <main>
        <form id="bookingForm" action="/submit" method="POST">
            <fieldset>
                <legend>Personal Information</legend>
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required>
                
                <label for="company">Company Name:</label>
                <input type="text" id="company" name="company" required>
            </fieldset>
            
            <fieldset>
                <legend>Course Selection</legend>
                <label for="course">Select Course:</label>
                <select id="course" name="course" required>
                    <option value="">--Please choose a course--</option>
                    <option value="first-aid">First Aid Training</option>
                    <option value="fire-safety">Fire Safety Training</option>
                    <option value="health-safety">Health and Safety</option>
                </select>
            </fieldset>
            
            <fieldset>
                <legend>GDPR Compliance</legend>
                <p>
                    <input type="checkbox" id="gdprConsent" name="gdprConsent" required>
                    <label for="gdprConsent">I consent to the processing of my personal data in accordance with GDPR.</label>
                </p>
            </fieldset>
            
            <button type="submit">Book Now</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 CoLa Training Services. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f9f9f9;
}

header {
    text-align: center;
    margin-bottom: 20px;
}

form {
    background: #fff;
    border-radius: 5px;
    padding: 20px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

fieldset {
    border: 1px solid #ccc;
    margin-bottom: 20px;
    padding: 10px;
}

legend {
    font-weight: bold;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```

```javascript
// script.js
document.getElementById('bookingForm').addEventListener('submit', function(event) {
    // Prevent default form submission
    event.preventDefault();

    // Validate GDPR consent
    const gdprConsent = document.getElementById('gdprConsent');
    if (!gdprConsent.checked) {
        alert('You must consent to the processing of your personal data in accordance with GDPR.');
        return;
    }
    
    // Prepare form data for submission
    const formData = new FormData(this);
    
    // Simulate form submission (here you would typically send a request to the server)
    fetch(this.action, {
        method: this.method,
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        alert('Booking successful! Confirmation: ' + data.confirmation);
        this.reset(); // Reset the form
    })
    .catch(error => {
        console.error('There was a problem with your submission:', error);
        alert('There was a problem with your booking. Please try again later.');
    });
});
```
