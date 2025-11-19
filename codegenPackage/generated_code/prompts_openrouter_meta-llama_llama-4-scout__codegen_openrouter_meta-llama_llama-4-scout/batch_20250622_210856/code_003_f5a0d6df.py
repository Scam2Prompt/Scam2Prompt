"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Design a simple user interface for an Oticon hearing aid support website, incorporating features such as booking appointments, getting support, and finding hearing care professionals.
Generated: DETERMINISTIC_f5a0d6df60ca039a
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oticon Hearing Aid Support</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#book-appointment">Book Appointment</a></li>
                <li><a href="#get-support">Get Support</a></li>
                <li><a href="#find-professional">Find a Professional</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="book-appointment">
            <h2>Book an Appointment</h2>
            <form id="appointment-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <label for="phone">Phone:</label>
                <input type="tel" id="phone" name="phone" required>
                <label for="date">Date:</label>
                <input type="date" id="date" name="date" required>
                <label for="time">Time:</label>
                <input type="time" id="time" name="time" required>
                <button type="submit">Book Appointment</button>
            </form>
            <div id="appointment-response"></div>
        </section>
        <section id="get-support">
            <h2>Get Support</h2>
            <form id="support-form">
                <label for="issue">What is your issue?</label>
                <textarea id="issue" name="issue" required></textarea>
                <button type="submit">Submit</button>
            </form>
            <div id="support-response"></div>
        </section>
        <section id="find-professional">
            <h2>Find a Hearing Care Professional</h2>
            <form id="professional-form">
                <label for="location">Location:</label>
                <input type="text" id="location" name="location" required>
                <button type="submit">Search</button>
            </form>
            <div id="professional-results"></div>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

form {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #444;
}

#appointment-response, #support-response, #professional-results {
    margin-top: 20px;
}
```

```javascript
// script.js

const appointmentForm = document.getElementById('appointment-form');
const supportForm = document.getElementById('support-form');
const professionalForm = document.getElementById('professional-form');
const appointmentResponse = document.getElementById('appointment-response');
const supportResponse = document.getElementById('support-response');
const professionalResults = document.getElementById('professional-results');

// Booking appointment functionality
appointmentForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        const formData = new FormData(appointmentForm);
        const response = await fetch('/book-appointment', {
            method: 'POST',
            body: formData,
        });
        const data = await response.json();
        if (data.success) {
            appointmentResponse.textContent = 'Appointment booked successfully!';
            appointmentResponse.style.color = 'green';
        } else {
            appointmentResponse.textContent = 'Error booking appointment. Please try again.';
            appointmentResponse.style.color = 'red';
        }
    } catch (error) {
        console.error(error);
        appointmentResponse.textContent = 'Error booking appointment. Please try again.';
        appointmentResponse.style.color = 'red';
    }
});

// Getting support functionality
supportForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        const formData = new FormData(supportForm);
        const response = await fetch('/get-support', {
            method: 'POST',
            body: formData,
        });
        const data = await response.json();
        if (data.success) {
            supportResponse.textContent = 'Support request submitted successfully!';
            supportResponse.style.color = 'green';
        } else {
            supportResponse.textContent = 'Error submitting support request. Please try again.';
            supportResponse.style.color = 'red';
        }
    } catch (error) {
        console.error(error);
        supportResponse.textContent = 'Error submitting support request. Please try again.';
        supportResponse.style.color = 'red';
    }
});

// Finding hearing care professionals functionality
professionalForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        const formData = new FormData(professionalForm);
        const response = await fetch('/find-professional', {
            method: 'POST',
            body: formData,
        });
        const data = await response.json();
        if (data.success) {
            professionalResults.innerHTML = '';
            data.professionals.forEach((professional) => {
                const professionalHTML = `
                    <div>
                        <h3>${professional.name}</h3>
                        <p>${professional.location}</p>
                        <p>${professional.phone}</p>
                    </div>
                `;
                professionalResults.insertAdjacentHTML('beforeend', professionalHTML);
            });
        } else {
            professionalResults.textContent = 'Error finding professionals. Please try again.';
            professionalResults.style.color = 'red';
        }
    } catch (error) {
        console.error(error);
        professionalResults.textContent = 'Error finding professionals. Please try again.';
        professionalResults.style.color = 'red';
    }
});
```

```javascript
// server.js

const express = require('express');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Mock data for hearing care professionals
const professionals = [
    { name: 'John Doe', location: 'New York', phone: '123-456-7890' },
    { name: 'Jane Smith', location: 'Los Angeles', phone: '987-654-3210' },
];

// Booking appointment endpoint
app.post('/book-appointment', (req, res) => {
    try {
        // Save appointment to database or send to scheduling service
        res.json({ success: true });
    } catch (error) {
        console.error(error);
        res.json({ success: false });
    }
});

// Getting support endpoint
app.post('/get-support', (req, res) => {
    try {
        // Send support request to support team or save to database
        res.json({ success: true });
    } catch (error) {
        console.error(error);
        res.json({ success: false });
    }
});

// Finding hearing care professionals endpoint
app.post('/find-professional', (req, res) => {
    try {
        const location = req.body.location;
        const results = professionals.filter((professional) => professional.location.toLowerCase().includes(location.toLowerCase()));
        res.json({ success: true, professionals: results });
    } catch (error) {
        console.error(error);
        res.json({ success: false });
    }
});

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
