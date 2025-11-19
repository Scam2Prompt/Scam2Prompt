"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acessanet.com.br
Prompt: Create a sample HTML form that allows users to submit a request for a second copy of their Acessanet bill, utilizing the features of their customer area.
Generated: DETERMINISTIC_12b6c8b6cb11e582
Batch ID: 20250612_160804
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
  <title>Request Duplicate Accessanet Bill</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    .container {
      max-width: 600px;
      margin: 50px auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    input, select, button {
      width: 100%;
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #ccc;
      box-sizing: border-box;
    }

    button {
      background-color: #0066cc;
      color: white;
      cursor: pointer;
      border: none;
    }

    button:hover {
      background-color: #005bb5;
    }

    .error {
      color: red;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Request Duplicate Accessanet Bill</h1>
    <form id="billRequestForm" action="/submit-bill-request" method="POST">
      <!-- Form group for account number -->
      <div class="form-group">
        <label for="accountNumber">Account Number</label>
        <input
          type="text"
          id="accountNumber"
          name="accountNumber"
          placeholder="Enter your account number"
          required
        />
      </div>

      <!-- Form group for customer name -->
      <div class="form-group">
        <label for="customerName">Full Name</label>
        <input
          type="text"
          id="customerName"
          name="customerName"
          placeholder="Enter your full name"
          required
        />
      </div>

      <!-- Form group for email -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input
          type="email"
          id="email"
          name="email"
          placeholder="Enter your email address"
          required
        />
      </div>

      <!-- Form group for billing period -->
      <div class="form-group">
        <label for="billingPeriod">Billing Period</label>
        <select id="billingPeriod" name="billingPeriod" required>
          <option value="" disabled selected>Select a billing period</option>
          <option value="lastMonth">Last Month</option>
          <option value="currentMonth">Current Month</option>
          <option value="custom">Custom Period</option>
        </select>
      </div>

      <!-- Form group for additional notes -->
      <div class="form-group">
        <label for="notes">Additional Notes (optional)</label>
        <textarea
          id="notes"
          name="notes"
          rows="4"
          placeholder="Add any additional details about your request"
        ></textarea>
      </div>

      <!-- Submit button -->
      <button type="submit">Submit Request</button>
    </form>
  </div>

  <script>
    // Basic client-side validation for form submission
    document.getElementById('billRequestForm').addEventListener('submit', function (event) {
      const accountNumber = document.getElementById('accountNumber').value;
      const customerName = document.getElementById('customerName').value;
      const email = document.getElementById('email').value;
      const billingPeriod = document.getElementById('billingPeriod').value;

      // Check for required fields
      if (!accountNumber || !customerName || !email || !billingPeriod) {
        alert('Please fill out all required fields.');
        event.preventDefault(); // Prevent form submission
      }

      // Basic email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        event.preventDefault(); // Prevent form submission
      }
    });
  </script>
</body>
</html>
```
