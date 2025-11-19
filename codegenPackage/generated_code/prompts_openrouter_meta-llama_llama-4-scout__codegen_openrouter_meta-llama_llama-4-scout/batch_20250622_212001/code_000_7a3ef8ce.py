"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Design a simple ticket booking form with fields for number of tickets, ticket type, and preferred communication method using HTML and CSS.
Generated: DETERMINISTIC_7a3ef8cef76e4936
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### HTML (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ticket Booking Form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Ticket Booking Form</h2>
        <form id="ticketBookingForm">
            <div class="form-group">
                <label for="numTickets">Number of Tickets:</label>
                <input type="number" id="numTickets" name="numTickets" required min="1">
            </div>
            <div class="form-group">
                <label for="ticketType">Ticket Type:</label>
                <select id="ticketType" name="ticketType" required>
                    <option value="" selected disabled>Choose a ticket type</option>
                    <option value="adult">Adult</option>
                    <option value="child">Child</option>
                    <option value="senior">Senior</option>
                </select>
            </div>
            <div class="form-group">
                <label for="communicationMethod">Preferred Communication Method:</label>
                <select id="communicationMethod" name="communicationMethod" required>
                    <option value="" selected disabled>Choose a communication method</option>
                    <option value="email">Email</option>
                    <option value="phone">Phone</option>
                    <option value="mail">Mail</option>
                </select>
            </div>
            <button type="submit">Book Tickets</button>
            <div id="formResponse"></div>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS (style.css)

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.container {
    width: 50%;
    margin: 40px auto;
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

h2 {
    text-align: center;
}

.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #007bff;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #0056b3;
}

#formResponse {
    margin-top: 20px;
}
```

### JavaScript (script.js)

```javascript
document.getElementById('ticketBookingForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    try {
        const numTickets = document.getElementById('numTickets').value;
        const ticketType = document.getElementById('ticketType').value;
        const communicationMethod = document.getElementById('communicationMethod').value;

        if (numTickets && ticketType && communicationMethod) {
            const formData = {
                numTickets: numTickets,
                ticketType: ticketType,
                communicationMethod: communicationMethod
            };

            // Here you would send formData to your server using fetch or XMLHttpRequest
            // For demonstration purposes, we'll just log it and display a success message
            console.log(formData);

            document.getElementById('formResponse').innerHTML = `
                <p>Tickets booked successfully!</p>
                <p>Number of Tickets: ${numTickets}</p>
                <p>Ticket Type: ${ticketType}</p>
                <p>Communication Method: ${communicationMethod}</p>
            `;
        } else {
            throw new Error('Please fill in all fields.');
        }
    } catch (error) {
        document.getElementById('formResponse').innerHTML = `
            <p style="color: red;">Error: ${error.message}</p>
        `;
    }
});
```
