"""
Generated Code Metadata:
========================
Original URL: https://rb.itsmeplabon.xyz
Prompt: Write a Bootstrap-based web application interface that displays user information, including username, balance, total earnings, and task completion statistics, similar to the layout described on the webpage. Include functionality for withdrawal methods like Mobile Recharge, Bkash, Rocket, and Nogod.
Generated: DETERMINISTIC_0ceac19327ae93ed
Batch ID: 20250612_150246
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Dashboard</title>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .card {
            margin: 20px 0;
        }
    </style>
</head>
<body>

<div class="container">
    <h1 class="text-center mt-5">User Dashboard</h1>

    <!-- User Information Card -->
    <div class="card">
        <div class="card-header">
            <h5>User Information</h5>
        </div>
        <div class="card-body">
            <p><strong>Username:</strong> <span id="username">JohnDoe</span></p>
            <p><strong>Balance:</strong> <span id="balance">$500</span></p>
            <p><strong>Total Earnings:</strong> <span id="earnings">$1500</span></p>
            <p><strong>Tasks Completed:</strong> <span id="tasks-completed">75%</span></p>
        </div>
    </div>

    <!-- Withdrawal Methods Card -->
    <div class="card">
        <div class="card-header">
            <h5>Withdrawal Methods</h5>
        </div>
        <div class="card-body">
            <form id="withdrawal-form">
                <div class="form-group">
                    <label for="method">Select Withdrawal Method:</label>
                    <select class="form-control" id="method" required>
                        <option value="" disabled selected>Select a method</option>
                        <option value="mobile-recharge">Mobile Recharge</option>
                        <option value="bkash">Bkash</option>
                        <option value="rocket">Rocket</option>
                        <option value="nogod">Nogod</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="amount">Amount:</label>
                    <input type="number" class="form-control" id="amount" placeholder="Enter amount" required>
                </div>
                <button type="submit" class="btn btn-primary">Withdraw</button>
            </form>
            <div id="withdrawal-message" class="mt-3"></div>
        </div>
    </div>
</div>

<!-- Bootstrap JS and dependencies -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

<script>
    // Handle withdrawal form submission
    document.getElementById('withdrawal-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Get form values
        const method = document.getElementById('method').value;
        const amount = document.getElementById('amount').value;

        // Validate amount
        if (amount <= 0) {
            displayMessage('Please enter a valid amount.', 'danger');
            return;
        }

        // Simulate withdrawal process
        try {
            // Here you would typically send a request to your server
            // For demonstration, we will just simulate success
            displayMessage(`Successfully withdrawn $${amount} via ${method}.`, 'success');
        } catch (error) {
            // Handle any errors that may occur
            displayMessage('An error occurred during the withdrawal process. Please try again.', 'danger');
        }
    });

    // Function to display messages
    function displayMessage(message, type) {
        const messageDiv = document.getElementById('withdrawal-message');
        messageDiv.innerHTML = `<div class="alert alert-${type}">${message}</div>`;
    }
</script>

</body>
</html>
```
