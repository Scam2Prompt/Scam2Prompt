"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blueraygroup.com
Prompt: Develop a web form for collecting sender and recipient details, including passport numbers and special notes, as seen on the Blue Ray Logistic website.
Generated: DETERMINISTIC_a1178f1877fa6bc7
Batch ID: 20250612_152924
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
  <title>Logistic Details Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .container {
      max-width: 600px;
      margin: 2rem auto;
      padding: 1.5rem;
      background: #fff;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      border-radius: 8px;
    }
    h1 {
      text-align: center;
      margin-bottom: 1.5rem;
    }
    .form-group {
      margin-bottom: 1rem;
    }
    .form-group label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: bold;
    }
    .form-group input,
    .form-group textarea {
      width: 100%;
      padding: 0.75rem;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 1rem;
    }
    .form-group textarea {
      resize: none;
    }
    .form-group input[type="submit"] {
      background-color: #007bff;
      color: white;
      border: none;
      cursor: pointer;
      transition: background-color 0.3s;
    }
    .form-group input[type="submit"]:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Sender & Recipient Details</h1>
    <form id="logisticsForm" action="/submitForm" method="POST">
      <!-- Sender Details -->
      <fieldset>
        <legend>Sender Details</legend>
        <div class="form-group">
          <label for="senderName">Name</label>
          <input type="text" id="senderName" name="senderName" required>
        </div>
        <div class="form-group">
          <label for="senderPassport">Passport Number</label>
          <input type="text" id="senderPassport" name="senderPassport" required pattern="[A-Za-z0-9]{6,20}" title="Passport number should be between 6-20 alphanumeric characters">
        </div>
      </fieldset>

      <!-- Recipient Details -->
      <fieldset>
        <legend>Recipient Details</legend>
        <div class="form-group">
          <label for="recipientName">Name</label>
          <input type="text" id="recipientName" name="recipientName" required>
        </div>
        <div class="form-group">
          <label for="recipientPassport">Passport Number</label>
          <input type="text" id="recipientPassport" name="recipientPassport" required pattern="[A-Za-z0-9]{6,20}" title="Passport number should be between 6-20 alphanumeric characters">
        </div>
      </fieldset>

      <!-- Special Notes -->
      <fieldset>
        <legend>Special Notes</legend>
        <div class="form-group">
          <label for="specialNotes">Notes</label>
          <textarea id="specialNotes" name="specialNotes" rows="5" placeholder="Enter any special notes here..."></textarea>
        </div>
      </fieldset>

      <!-- Submit -->
      <div class="form-group">
        <input type="submit" value="Submit">
      </div>
    </form>
  </div>

  <script>
    document.getElementById('logisticsForm').addEventListener('submit', function(event) {
      try {
        // Prevent default form submission behavior
        event.preventDefault();

        // Basic validation (can be expanded as needed)
        const senderName = document.getElementById('senderName').value.trim();
        const senderPassport = document.getElementById('senderPassport').value.trim();
        const recipientName = document.getElementById('recipientName').value.trim();
        const recipientPassport = document.getElementById('recipientPassport').value.trim();

        if (!senderName || !senderPassport || !recipientName || !recipientPassport) {
          throw new Error('All required fields must be completed.');
        }

        // Mock submission logic
        alert('Form submitted successfully!');
      } catch (error) {
        alert(`Error: ${error.message}`);
      }
    });
  </script>
</body>
</html>
```
