"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://co-djs.com
Prompt: Develop a sample HTML form for clients to submit their event details, including venue, date, and preferred DJ package, based on the services offered by Central Oregon DJs.
Generated: DETERMINISTIC_e6bb5fd548154f1f
Batch ID: 20250612_155332
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
    <title>Event Submission Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        form {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input, select, textarea {
            width: 100%;
            margin-bottom: 15px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }

        button {
            background-color: #007BFF;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Submit Your Event Details</h1>
    <form id="eventForm" action="/submit-event" method="POST">
        <!-- Field for event venue -->
        <label for="venue">Event Venue:</label>
        <input type="text" id="venue" name="venue" placeholder="Enter venue name" required>

        <!-- Field for event date -->
        <label for="date">Event Date:</label>
        <input type="date" id="date" name="date" required>

        <!-- Dropdown for selecting DJ packages -->
        <label for="djPackage">Preferred DJ Package:</label>
        <select id="djPackage" name="djPackage" required>
            <option value="">-- Select a Package --</option>
            <option value="basic">Basic Package</option>
            <option value="premium">Premium Package</option>
            <option value="vip">VIP Package</option>
        </select>

        <!-- Field for additional comments -->
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4" placeholder="Any specific requirements or details?"></textarea>

        <!-- Submit button -->
        <button type="submit">Submit</button>
    </form>

    <script>
        // Add basic form validation
        const form = document.getElementById('eventForm');
        form.addEventListener('submit', (event) => {
            // Prevent default form submission behavior
            event.preventDefault();

            // Basic validation (e.g., ensure no empty fields)
            const venue = document.getElementById('venue').value.trim();
            const date = document.getElementById('date').value.trim();
            const djPackage = document.getElementById('djPackage').value.trim();

            if (!venue || !date || !djPackage) {
                alert('Please fill out all required fields.');
                return;
            }

            // Submit the form if validation passes
            alert('Form submitted successfully!');
            form.submit();
        });
    </script>
</body>
</html>
```
