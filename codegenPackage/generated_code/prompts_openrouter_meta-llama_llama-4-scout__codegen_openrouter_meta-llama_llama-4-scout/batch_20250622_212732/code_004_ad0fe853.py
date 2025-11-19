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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Salty Daze Charters</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Salty Daze Charters</h1>
    </header>
    <main>
        <section id="schedule">
            <h2>Daily Schedule</h2>
            <table id="schedule-table">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Trip Type</th>
                        <th>Availability</th>
                    </tr>
                </thead>
                <tbody id="schedule-body">
                    <!-- Schedule data will be populated here -->
                </tbody>
            </table>
        </section>
        <section id="book-inquire">
            <h2>Book or Inquire about Custom Trips</h2>
            <form id="book-form">
                <label for="trip-type">Trip Type:</label>
                <select id="trip-type" name="trip-type">
                    <option value="">Select a trip type</option>
                    <option value="half-day">Half Day</option>
                    <option value="full-day">Full Day</option>
                    <option value="custom">Custom</option>
                </select>
                <label for="date">Date:</label>
                <input type="date" id="date" name="date">
                <label for="num-guests">Number of Guests:</label>
                <input type="number" id="num-guests" name="num-guests">
                <button id="book-btn">Book</button>
                <button id="inquire-btn">Inquire</button>
            </form>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

#schedule {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 2em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#schedule-table {
    width: 100%;
    border-collapse: collapse;
}

#schedule-table th, #schedule-table td {
    border: 1px solid #ddd;
    padding: 0.5em;
    text-align: left;
}

#book-inquire {
    background-color: #f7f7f7;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#book-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

label {
    margin-bottom: 0.5em;
}

input, select {
    padding: 0.5em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 0.5em 1em;
    cursor: pointer;
}

button:hover {
    background-color: #444;
}
```

**script.js**
```javascript
// Sample schedule data
const scheduleData = [
    { time: '9:00 AM', tripType: 'Half Day', availability: 'Available' },
    { time: '1:00 PM', tripType: 'Full Day', availability: 'Booked' },
    { time: '5:00 PM', tripType: 'Custom', availability: 'Available' },
];

// Populate schedule table
const scheduleBody = document.getElementById('schedule-body');
scheduleData.forEach((schedule) => {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${schedule.time}</td>
        <td>${schedule.tripType}</td>
        <td>${schedule.availability}</td>
    `;
    scheduleBody.appendChild(row);
});

// Get book and inquire buttons
const bookBtn = document.getElementById('book-btn');
const inquireBtn = document.getElementById('inquire-btn');

// Add event listeners to buttons
bookBtn.addEventListener('click', handleBook);
inquireBtn.addEventListener('click', handleInquire);

// Handle book button click
function handleBook() {
    const tripType = document.getElementById('trip-type').value;
    const date = document.getElementById('date').value;
    const numGuests = document.getElementById('num-guests').value;

    if (!tripType || !date || !numGuests) {
        alert('Please fill out all fields');
        return;
    }

    // Call booking API or send booking request
    console.log(`Booking ${tripType} trip on ${date} for ${numGuests} guests`);
    alert('Booking successful!');
}

// Handle inquire button click
function handleInquire() {
    const tripType = document.getElementById('trip-type').value;
    const date = document.getElementById('date').value;
    const numGuests = document.getElementById('num-guests').value;

    if (!tripType || !date || !numGuests) {
        alert('Please fill out all fields');
        return;
    }

    // Call inquiry API or send inquiry request
    console.log(`Inquiring about ${tripType} trip on ${date} for ${numGuests} guests`);
    alert('Inquiry sent successfully!');
}
```
