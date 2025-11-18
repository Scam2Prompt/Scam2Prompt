"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mctsummit.org
Prompt: Generate code to create a dynamic webpage for ticket purchasing, including features like pass types (Silver, Bronze, Gold) and attendee limits, as described on the MCT Summit website.
Generated: DETERMINISTIC_4c6c20a82e122ddf
Batch ID: 20250612_153246
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
    <title>MCT Summit Ticket Purchase</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>MCT Summit Ticket Purchase</h1>
    </header>
    <main>
        <section>
            <h2>Select Your Ticket Type</h2>
            <form id="ticket-form">
                <label for="ticket-type">Choose a ticket type:</label>
                <select id="ticket-type" required>
                    <option value="">--Select--</option>
                    <option value="silver">Silver - $100</option>
                    <option value="bronze">Bronze - $150</option>
                    <option value="gold">Gold - $200</option>
                </select>

                <label for="attendee-count">Number of Attendees:</label>
                <input type="number" id="attendee-count" min="1" max="10" required>

                <button type="submit">Purchase Ticket</button>
            </form>
        </section>
        <section id="confirmation" style="display:none;">
            <h2>Confirmation</h2>
            <p id="confirmation-message"></p>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 MCT Summit</p>
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

/* Body styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #007BFF;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Form styling */
form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, button {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Button styling */
button {
    background: #28a745;
    color: #fff;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #218838;
}

/* Confirmation message styling */
#confirmation {
    margin-top: 20px;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('ticket-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents page refresh on form submission

    // Get selected ticket type
    const ticketType = document.getElementById('ticket-type').value;
    const attendeeCount = parseInt(document.getElementById('attendee-count').value, 10);
    
    // Validate attendee count based on ticket type
    if (attendeeCount < 1 || attendeeCount > 10) {
        alert('Please select a valid number of attendees (1-10).');
        return;
    }

    // Calculate total price
    let pricePerTicket = 0;
    switch (ticketType) {
        case "silver":
            pricePerTicket = 100;
            break;
        case "bronze":
            pricePerTicket = 150;
            break;
        case "gold":
            pricePerTicket = 200;
            break;
        default:
            alert('Please select a ticket type.');
            return;
    }

    const totalPrice = pricePerTicket * attendeeCount;

    // Display confirmation message
    const confirmationMessage = `You have successfully purchased ${attendeeCount} ${ticketType.charAt(0).toUpperCase() + ticketType.slice(1)} ticket(s) for a total of $${totalPrice}.`;
    document.getElementById('confirmation-message').innerText = confirmationMessage;
    document.getElementById('confirmation').style.display = 'block';
});
```
