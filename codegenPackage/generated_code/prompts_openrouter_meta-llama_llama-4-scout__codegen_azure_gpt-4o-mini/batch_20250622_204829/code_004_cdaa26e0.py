"""
Generated Code Metadata:
========================
Original URL: https://ethjya.com
Prompt: "Design a simple Bitcoin pledge system interface using HTML, CSS, and JavaScript, inspired by the layout and functionality implied by ethjya.com."
Generated: DETERMINISTIC_cdaa26e0eae0bf9b
Batch ID: 20250622_204829
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
    <title>Bitcoin Pledge System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Bitcoin Pledge System</h1>
        <p>Join the movement and pledge your support!</p>
    </header>
    <main>
        <section id="pledge-form">
            <h2>Pledge Your Support</h2>
            <form id="form">
                <label for="name">Your Name:</label>
                <input type="text" id="name" required>

                <label for="amount">Pledge Amount (BTC):</label>
                <input type="number" id="amount" step="0.0001" required>

                <button type="submit">Pledge</button>
            </form>
            <div id="message"></div>
        </section>
        <section id="pledge-list">
            <h2>Pledges</h2>
            <ul id="pledges"></ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Bitcoin Pledge System</p>
    </footer>
    <script src="script.js"></script>
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
    background-color: #f4f4f4;
    color: #333;
}

header {
    background: #0070f3;
    color: white;
    padding: 20px;
    text-align: center;
}

main {
    padding: 20px;
}

h2 {
    margin-bottom: 10px;
}

form {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="number"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background: #0070f3;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background: #005bb5;
}

#pledge-list {
    margin-top: 20px;
}

#pledges {
    list-style-type: none;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Retrieve input values
    const name = document.getElementById('name').value.trim();
    const amount = parseFloat(document.getElementById('amount').value);

    // Validate input values
    if (!name || isNaN(amount) || amount <= 0) {
        displayMessage('Please enter a valid name and pledge amount.', 'error');
        return;
    }

    // Create a new pledge entry
    const pledge = { name, amount };
    addPledgeToList(pledge);

    // Clear the form fields
    document.getElementById('form').reset();
    displayMessage('Thank you for your pledge!', 'success');
});

// Function to add pledge to the list
function addPledgeToList(pledge) {
    const pledgeList = document.getElementById('pledges');
    const listItem = document.createElement('li');
    listItem.textContent = `${pledge.name} pledged ${pledge.amount} BTC`;
    pledgeList.appendChild(listItem);
}

// Function to display messages to the user
function displayMessage(message, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = message;
    messageDiv.className = type; // Set class for styling based on message type
    setTimeout(() => {
        messageDiv.textContent = ''; // Clear message after 3 seconds
    }, 3000);
}
```

This code provides a simple Bitcoin pledge system interface with HTML, CSS, and JavaScript, following best practices and including error handling.
