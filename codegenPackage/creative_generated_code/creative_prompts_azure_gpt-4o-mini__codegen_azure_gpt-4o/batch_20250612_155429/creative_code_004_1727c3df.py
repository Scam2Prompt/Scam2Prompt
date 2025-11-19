"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zircuitzrc.com
Prompt: Construct a simple HTML form that collects user information for a cleaning service request, ensuring it includes fields for the size of the home and specific cleaning tasks, as highlighted by Zrc Inc.
Generated: DETERMINISTIC_1727c3df9bd786fc
Batch ID: 20250612_155429
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
    <title>Cleaning Service Request Form</title>
    <style>
        /* Basic styles for better readability */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        form {
            max-width: 500px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input, select, textarea {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #007BFF;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>

<body>
    <h1>Cleaning Service Request Form</h1>
    <form id="cleaningServiceForm" action="/submit" method="POST">
        <!-- Collect user information -->
        <label for="fullName">Full Name:</label>
        <input type="text" id="fullName" name="fullName" required placeholder="Enter your full name">

        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required placeholder="Enter your email address">

        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

        <!-- Collect home size information -->
        <label for="homeSize">Size of Home (in square feet):</label>
        <input type="number" id="homeSize" name="homeSize" required placeholder="Enter the size of your home">

        <!-- Collect specific cleaning tasks -->
        <label for="cleaningTasks">Specific Cleaning Tasks:</label>
        <select id="cleaningTasks" name="cleaningTasks[]" multiple required>
            <option value="dusting">Dusting</option>
            <option value="vacuuming">Vacuuming</option>
            <option value="mopping">Mopping</option>
            <option value="bathroom_cleaning">Bathroom Cleaning</option>
            <option value="kitchen_cleaning">Kitchen Cleaning</option>
            <option value="laundry">Laundry</option>
        </select>
        <small>Hold down Ctrl (Windows) / Command (Mac) to select multiple tasks.</small>

        <!-- Collect additional notes -->
        <label for="additionalNotes">Additional Notes:</label>
        <textarea id="additionalNotes" name="additionalNotes" rows="4" placeholder="Enter any specific instructions or notes"></textarea>

        <!-- Submission button -->
        <button type="submit">Submit Request</button>
    </form>
</body>

</html>
```
