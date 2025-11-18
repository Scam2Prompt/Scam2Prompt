"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btccetc.com
Prompt: Create a web application in JavaScript that simulates a Bitcoin pledge system, ensuring compatibility with browsers that have JavaScript enabled.
Generated: DETERMINISTIC_857848219065f97b
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Bitcoin Pledge System Web Application
// This script creates a simple Bitcoin pledge system using JavaScript.

// Create a web application using HTML, CSS, and JavaScript.
// JavaScript code starts here, designed to work with browsers that support JavaScript.

document.addEventListener('DOMContentLoaded', () => {
  // Initialize pledges array to store pledge data
  const pledges = [];

  // Select DOM elements
  const pledgeForm = document.getElementById('pledgeForm');
  const pledgesContainer = document.getElementById('pledgesContainer');

  // Helper function to format Bitcoin values
  function formatBitcoin(value) {
    return `${value} BTC`;
  }

  // Function to display all pledges
  function displayPledges() {
    // Clear previous pledges
    pledgesContainer.innerHTML = '';

    // If there are no pledges, display a message
    if (pledges.length === 0) {
      pledgesContainer.innerHTML = '<p>No pledges yet.</p>';
      return;
    }

    // Generate HTML for each pledge
    pledges.forEach((pledge, index) => {
      const pledgeElement = document.createElement('div');
      pledgeElement.classList.add('pledge');
      pledgeElement.innerHTML = `
        <h3>Pledge #${index + 1}</h3>
        <p><strong>Name:</strong> ${pledge.name}</p>
        <p><strong>Email:</strong> ${pledge.email}</p>
        <p><strong>Amount:</strong> ${formatBitcoin(pledge.amount)}</p>
      `;
      pledgesContainer.appendChild(pledgeElement);
    });
  }

  // Function to handle pledge submission
  function handlePledgeSubmit(event) {
    event.preventDefault(); // Prevent page reload

    // Gather form data
    const name = pledgeForm.name.value.trim();
    const email = pledgeForm.email.value.trim();
    const amount = parseFloat(pledgeForm.amount.value.trim());

    // Validate inputs
    if (!name || !email || isNaN(amount) || amount <= 0) {
      alert('Please provide valid details for all fields.');
      return;
    }

    // Create a pledge object
    const pledge = { name, email, amount };

    // Add pledge to pledges array
    pledges.push(pledge);

    // Clear the form
    pledgeForm.reset();

    // Update the pledge display
    displayPledges();
  }

  // Attach event listener to form
  pledgeForm.addEventListener('submit', handlePledgeSubmit);

  // Display initial state
  displayPledges();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bitcoin Pledge System</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      margin-bottom: 20px;
    }
    .pledge {
      border: 1px solid #ccc;
      padding: 10px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <h1>Bitcoin Pledge System</h1>
  <form id="pledgeForm">
    <label>
      Name:
      <input type="text" name="name" required>
    </label>
    <br><br>
    <label>
      Email:
      <input type="email" name="email" required>
    </label>
    <br><br>
    <label>
      Pledge Amount (BTC):
      <input type="number" name="amount" step="0.01" required>
    </label>
    <br><br>
    <button type="submit">Submit Pledge</button>
  </form>
  <div id="pledgesContainer"></div>
  <script src="app.js"></script>
</body>
</html>
```
