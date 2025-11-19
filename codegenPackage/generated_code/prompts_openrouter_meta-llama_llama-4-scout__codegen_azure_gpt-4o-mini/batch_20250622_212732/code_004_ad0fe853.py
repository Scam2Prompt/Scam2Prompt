"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Create a simple web page using HTML and JavaScript to display the daily schedule and availability of boat charters for Salty Daze Charters, including options to book or inquire about custom trips."
Generated: DETERMINISTIC_ad0fe853004fb45c
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Salty Daze Charters - Daily Schedule</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Salty Daze Charters</h1>
        <p>Your adventure awaits!</p>
    </header>
    
    <main>
        <section id="schedule">
            <h2>Daily Schedule</h2>
            <table>
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Availability</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody id="schedule-body">
                    <!-- Schedule will be populated here by JavaScript -->
                </tbody>
            </table>
        </section>

        <section id="booking">
            <h2>Book a Trip</h2>
            <form id="booking-form">
                <label for="name">Your Name:</label>
                <input type="text" id="name" required>
                
                <label for="email">Your Email:</label>
                <input type="email" id="email" required>
                
                <label for="trip-time">Select Time:</label>
                <select id="trip-time" required>
                    <!-- Options will be populated here by JavaScript -->
                </select>
                
                <button type="submit">Book Now</button>
            </form>
        </section>

        <section id="inquiry">
            <h2>Inquire About Custom Trips</h2>
            <form id="inquiry-form">
                <label for="inquiry-name">Your Name:</label>
                <input type="text" id="inquiry-name" required>
                
                <label for="inquiry-email">Your Email:</label>
                <input type="email" id="inquiry-email" required>
                
                <label for="inquiry-message">Message:</label>
                <textarea id="inquiry-message" required></textarea>
                
                <button type="submit">Send Inquiry</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Salty Daze Charters. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f0f8ff;
    color: #333;
}

header {
    background: #0077be;
    color: white;
    padding: 20px;
    text-align: center;
}

h1, h2 {
    margin-bottom: 10px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

th, td {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
}

th {
    background: #0077be;
    color: white;
}

form {
    margin: 20px 0;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
}

button {
    background: #0077be;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
}

button:hover {
    background: #005f8a;
}
```

```javascript
// script.js

// Sample schedule data
const scheduleData = [
    { time: "8:00 AM", available: true },
    { time: "10:00 AM", available: false },
    { time: "12:00 PM", available: true },
    { time: "2:00 PM", available: true },
    { time: "4:00 PM", available: false },
];

// Function to populate the schedule table
function populateSchedule() {
    const scheduleBody = document.getElementById('schedule-body');
    const tripTimeSelect = document.getElementById('trip-time');

    scheduleData.forEach((slot) => {
        // Create a new row for the schedule
        const row = document.createElement('tr');
        const availabilityText = slot.available ? "Available" : "Not Available";

        row.innerHTML = `
            <td>${slot.time}</td>
            <td>${availabilityText}</td>
            <td>
                ${slot.available ? '<button class="book-btn">Book</button>' : ''}
            </td>
        `;

        scheduleBody.appendChild(row);

        // Populate the trip time select dropdown
        if (slot.available) {
            const option = document.createElement('option');
            option.value = slot.time;
            option.textContent = slot.time;
            tripTimeSelect.appendChild(option);
        }
    });
}

// Function to handle booking form submission
function handleBooking(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const tripTime = document.getElementById('trip-time').value;

    // Simple validation
    if (!name || !email || !tripTime) {
        alert("Please fill in all fields.");
        return;
    }

    // Simulate booking process
    alert(`Booking confirmed for ${name} at ${tripTime}. Confirmation sent to ${email}.`);
    document.getElementById('booking-form').reset();
}

// Function to handle inquiry form submission
function handleInquiry(event) {
    event.preventDefault();
    const name = document.getElementById('inquiry-name').value;
    const email = document.getElementById('inquiry-email').value;
    const message = document.getElementById('inquiry-message').value;

    // Simple validation
    if (!name || !email || !message) {
        alert("Please fill in all fields.");
        return;
    }

    // Simulate inquiry process
    alert(`Inquiry sent from ${name}. We will respond to ${email} shortly.`);
    document.getElementById('inquiry-form').reset();
}

// Event listeners for form submissions
document.getElementById('booking-form').addEventListener('submit', handleBooking);
document.getElementById('inquiry-form').addEventListener('submit', handleInquiry);

// Populate the schedule on page load
document.addEventListener('DOMContentLoaded', populateSchedule);
```
