"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Develop a sample HTML form for clients to submit their event details, including venue, date, and preferred DJ package, based on the services offered by Central Oregon DJs.
Generated: DETERMINISTIC_e6bb5fd548154f1f
Batch ID: 20250612_155332
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
    <title>Event Submission Form - Central Oregon DJs</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        .form-container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input, select, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: #0056b3;
        }

        .error-message {
            color: red;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Event Submission Form</h1>
        <form id="eventForm" action="/submit-event" method="POST">
            <!-- Venue Name -->
            <label for="venue">Venue Name:</label>
            <input type="text" id="venue" name="venue" placeholder="Enter venue name" required>
            
            <!-- Event Date -->
            <label for="date">Event Date:</label>
            <input type="date" id="date" name="date" required>
            
            <!-- DJ Package -->
            <label for="djPackage">Preferred DJ Package:</label>
            <select id="djPackage" name="djPackage" required>
                <option value="">Select a package</option>
                <option value="basic">Basic Package</option>
                <option value="premium">Premium Package</option>
                <option value="vip">VIP Package</option>
            </select>
            
            <!-- Additional Notes -->
            <label for="notes">Additional Notes:</label>
            <textarea id="notes" name="notes" rows="4" placeholder="Enter any additional details"></textarea>
            
            <!-- Submit Button -->
            <button type="submit">Submit Event Details</button>
        </form>
    </div>

    <script>
        // Basic client-side validation
        document.getElementById('eventForm').addEventListener('submit', function(event) {
            const venue = document.getElementById('venue').value.trim();
            const date = document.getElementById('date').value.trim();
            const djPackage = document.getElementById('djPackage').value.trim();

            if (!venue || !date || !djPackage) {
                event.preventDefault(); // Prevent form submission
                alert('Please fill out all required fields.');
            }
        });
    </script>
</body>
</html>
```
