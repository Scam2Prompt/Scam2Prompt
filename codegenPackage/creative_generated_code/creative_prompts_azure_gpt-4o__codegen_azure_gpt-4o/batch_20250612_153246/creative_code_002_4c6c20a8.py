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
  <title>MCT Summit Ticket Purchasing</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .form-group label {
      display: block;
      margin-bottom: 5px;
    }
    .form-group select, .form-group input {
      width: 100%;
      padding: 8px;
      box-sizing: border-box;
    }
    .error {
      color: red;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <h1>MCT Summit Ticket Purchasing</h1>
  <form id="ticketForm">
    <div class="form-group">
      <label for="passType">Select Pass Type:</label>
      <select id="passType" name="passType" required>
        <option value="">--Choose Pass Type--</option>
        <option value="Silver">Silver Pass</option>
        <option value="Bronze">Bronze Pass</option>
        <option value="Gold">Gold Pass</option>
      </select>
      <span class="error" id="passTypeError"></span>
    </div>
    <div class="form-group">
      <label for="attendees">Number of Attendees:</label>
      <input type="number" id="attendees" name="attendees" min="1" max="10" required>
      <span class="error" id="attendeesError"></span>
    </div>
    <button type="submit">Purchase Tickets</button>
  </form>
  <div id="confirmationMessage" style="margin-top: 20px;"></div>

  <script>
    // Event listener for form submission
    document.getElementById('ticketForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission
      // Clear previous error messages
      document.getElementById('passTypeError').textContent = '';
      document.getElementById('attendeesError').textContent = '';

      // Validate inputs
      const passType = document.getElementById('passType').value;
      const attendees = document.getElementById('attendees').value;

      let valid = true;

      // Validate pass type
      if (!passType) {
        document.getElementById('passTypeError').textContent = 'Please select a pass type.';
        valid = false;
      }

      // Validate number of attendees
      if (!attendees || attendees < 1 || attendees > 10) {
        document.getElementById('attendeesError').textContent = 'Please enter a number between 1 and 10.';
        valid = false;
      }

      if (valid) {
        // Generate confirmation message
        const message = `You have successfully purchased ${attendees} ${passType} Pass${attendees > 1 ? 'es' : ''}.`;
        document.getElementById('confirmationMessage').textContent = message;
        document.getElementById('confirmationMessage').style.color = 'green';
      }
    });
  </script>
</body>
</html>
```
