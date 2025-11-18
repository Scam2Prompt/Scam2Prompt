"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rb.itsmeplabon.xyz
Prompt: Write a Bootstrap-based web application interface that displays user information, including username, balance, total earnings, and task completion statistics, similar to the layout described on the webpage. Include functionality for withdrawal methods like Mobile Recharge, Bkash, Rocket, and Nogod.
Generated: DETERMINISTIC_0ceac19327ae93ed
Batch ID: 20250612_150246
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js": {
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
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Information Dashboard</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        /* Custom styles for better UI */
        .card-header {
            background-color: #007bff;
            color: white;
        }
        .withdraw-method {
            cursor: pointer;
        }
    </style>
</head>
<body>

<div class="container mt-5">
    <h1 class="text-center">User Information Dashboard</h1>

    <!-- User Information Card -->
    <div class="card mt-4">
        <div class="card-header">
            User Details
        </div>
        <div class="card-body">
            <h5 id="username">Username: JohnDoe</h5>
            <p id="balance">Balance: $500.00</p>
            <p id="earnings">Total Earnings: $1500.00</p>
            <p id="completed-tasks">Tasks Completed: 20</p>
        </div>
    </div>

    <!-- Withdrawal Methods Card -->
    <div class="card mt-4">
        <div class="card-header">
            Withdrawal Methods
        </div>
        <div class="card-body">
            <h5>Select a method to withdraw:</h5>
            <div class="row">
                <div class="col-md-3">
                    <div class="card withdraw-method" onclick="initiateWithdrawal('Mobile Recharge')">
                        <div class="card-body text-center">
                            <h5 class="card-title">Mobile Recharge</h5>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card withdraw-method" onclick="initiateWithdrawal('Bkash')">
                        <div class="card-body text-center">
                            <h5 class="card-title">Bkash</h5>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card withdraw-method" onclick="initiateWithdrawal('Rocket')">
                        <div class="card-body text-center">
                            <h5 class="card-title">Rocket</h5>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card withdraw-method" onclick="initiateWithdrawal('Nogod')">
                        <div class="card-body text-center">
                            <h5 class="card-title">Nogod</h5>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Bootstrap JS and dependencies -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

<script>
    /**
     * Initiates the withdrawal process for the selected method.
     * @param {string} method - The withdrawal method selected by the user.
     */
    function initiateWithdrawal(method) {
        // Confirm withdrawal action
        const userConfirmed = confirm(`Are you sure you want to withdraw using ${method}?`);

        if (userConfirmed) {
            // Here you would typically handle the withdrawal logic, e.g. API call
            console.log(`Withdrawal initiated through ${method}.`);
            alert(`Withdrawal through ${method} has been initiated.`);
        } else {
            console.log(`Withdrawal canceled.`);
        }
    }
</script>
</body>
</html>
```
