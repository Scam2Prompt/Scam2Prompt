"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Construct a sample HTML form for users to submit requests for RV inspections, including fields for service type and contact information.
Generated: DETERMINISTIC_9e3b7aa97b97fbb5
Batch ID: 20250612_163350
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
    <title>RV Inspection Request Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            max-width: 600px;
            margin: auto;
            background-color: #f9f9f9;
        }

        h1 {
            text-align: center;
        }

        form {
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 5px;
            background: #fff;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input, select, textarea {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .error {
            color: red;
        }
    </style>
</head>
<body>

    <h1>RV Inspection Request Form</h1>
    <form id="inspectionForm" action="/submit-inspection-request" method="POST">
        <!-- Input for Full Name -->
        <div class="form-group">
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required>
        </div>

        <!-- Input for Email -->
        <div class="form-group">
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>
        </div>

        <!-- Input for Phone Number -->
        <div class="form-group">
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" required>
            <small>Format: 1234567890</small>
        </div>

        <!-- Dropdown for Service Type -->
        <div class="form-group">
            <label for="serviceType">Service Type:</label>
            <select id="serviceType" name="serviceType" required>
                <option value="">-- Select a Service Type --</option>
                <option value="Pre-purchase Inspection">Pre-purchase Inspection</option>
                <option value="Routine Maintenance">Routine Maintenance</option>
                <option value="Safety Inspection">Safety Inspection</option>
                <option value="Other">Other</option>
            </select>
        </div>

        <!-- Textarea for Additional Details -->
        <div class="form-group">
            <label for="details">Additional Details (optional):</label>
            <textarea id="details" name="details" rows="5"></textarea>
        </div>

        <!-- Submit Button -->
        <div class="form-group">
            <button type="submit">Submit Request</button>
        </div>
    </form>

    <script>
        // Basic client-side validation (optional enhancement)
        document.getElementById('inspectionForm').addEventListener('submit', function(event) {
            const email = document.getElementById('email').value;
            if (!email.includes('@')) {
                event.preventDefault();
                alert('Please enter a valid email address.');
            }
        });
    </script>

</body>
</html>
```
