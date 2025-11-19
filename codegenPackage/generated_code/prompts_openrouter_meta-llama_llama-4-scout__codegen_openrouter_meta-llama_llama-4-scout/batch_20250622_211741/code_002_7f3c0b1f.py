"""
Generated Code Metadata:
========================
Original URL: https://www.tubellaesteticaduepuntozero.it
Prompt: Generate a simple HTML page for displaying the operating hours and contact information of a business, similar to how it's presented on the TuBella Estetica 2.0 website.
Generated: DETERMINISTIC_7f3c0b1f23a0ba2f
Batch ID: 20250622_211741
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
    <title>Business Information</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Business Information</h1>
    </header>
    <main>
        <section id="operating-hours">
            <h2>Operating Hours</h2>
            <table>
                <thead>
                    <tr>
                        <th>Day</th>
                        <th>Hours</th>
                    </tr>
                </thead>
                <tbody id="hours-body">
                    <!-- hours will be populated here -->
                </tbody>
            </table>
        </section>
        <section id="contact-information">
            <h2>Contact Information</h2>
            <address>
                <p id="business-address"></p>
                <p id="business-phone"></p>
                <p id="business-email"></p>
            </address>
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
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
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
    margin-bottom: 2em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
    margin-bottom: 0.5em;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 0.5em;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}
```

```javascript
// script.js

// Business information data
const businessInfo = {
    address: '123 Main St, Anytown, USA 12345',
    phone: '(555) 555-5555',
    email: 'info@example.com',
    hours: [
        { day: 'Monday', hours: '9:00 AM - 5:00 PM' },
        { day: 'Tuesday', hours: '9:00 AM - 5:00 PM' },
        { day: 'Wednesday', hours: '9:00 AM - 5:00 PM' },
        { day: 'Thursday', hours: '9:00 AM - 5:00 PM' },
        { day: 'Friday', hours: '9:00 AM - 5:00 PM' },
        { day: 'Saturday', hours: '10:00 AM - 2:00 PM' },
        { day: 'Sunday', hours: 'Closed' },
    ],
};

// Function to populate hours table
function populateHours() {
    const hoursBody = document.getElementById('hours-body');
    businessInfo.hours.forEach((hour) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${hour.day}</td>
            <td>${hour.hours}</td>
        `;
        hoursBody.appendChild(row);
    });
}

// Function to populate contact information
function populateContactInfo() {
    document.getElementById('business-address').textContent = businessInfo.address;
    document.getElementById('business-phone').textContent = businessInfo.phone;
    document.getElementById('business-email').textContent = businessInfo.email;
}

// Run on page load
document.addEventListener('DOMContentLoaded', () => {
    try {
        populateHours();
        populateContactInfo();
    } catch (error) {
        console.error('Error populating business information:', error);
    }
});
```
