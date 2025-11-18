"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodep0.com
Prompt: Write JavaScript code to create a Bitcoin pledge system that validates user input and displays a confirmation message.
Generated: DETERMINISTIC_fe7c1c9055dff3d9
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Bitcoin Pledge System

// Function to initialize the pledge system
function initPledgeSystem() {
  // Get references to DOM elements
  const pledgeForm = document.getElementById('pledgeForm');
  const pledgeAmountInput = document.getElementById('pledgeAmount');
  const confirmationMessage = document.getElementById('confirmationMessage');

  // Add event listener for form submission
  pledgeForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const pledgeAmount = parseFloat(pledgeAmountInput.value.trim());

    try {
      // Validate user input
      validatePledgeAmount(pledgeAmount);

      // Display confirmation message
      confirmationMessage.textContent = `Thank you for pledging ${pledgeAmount} BTC!`;
      confirmationMessage.style.color = 'green';
    } catch (error) {
      // Handle validation errors
      confirmationMessage.textContent = error.message;
      confirmationMessage.style.color = 'red';
    }
  });
}

// Function to validate pledge amount
function validatePledgeAmount(amount) {
  if (isNaN(amount)) {
    throw new Error('Invalid input: Please enter a valid number.');
  }
  if (amount <= 0) {
    throw new Error('Invalid amount: Pledge must be greater than 0 BTC.');
  }
  if (amount > 21) {
    throw new Error('Invalid amount: Maximum pledge is 21 BTC.');
  }
}

// Initialize the pledge system after DOM content is loaded
document.addEventListener('DOMContentLoaded', initPledgeSystem);
```

```html
<!-- Bitcoin Pledge System Interface -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bitcoin Pledge System</title>
</head>
<body>
  <h1>Bitcoin Pledge System</h1>
  <form id="pledgeForm">
    <label for="pledgeAmount">Enter your pledge amount (BTC):</label>
    <input type="text" id="pledgeAmount" required>
    <button type="submit">Pledge</button>
  </form>
  <p id="confirmationMessage"></p>

  <script src="pledge-system.js"></script>
</body>
</html>
```
