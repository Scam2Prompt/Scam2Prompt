"""
Generated Code Metadata:
========================
Original URL: https://antalyasehiricinakliye.com
Prompt: Construct a sample HTML form that collects user information for a moving service request in Antalya, including fields for item types and preferred moving dates.
Generated: DETERMINISTIC_7e126cd20f7a7c34
Batch ID: 20250612_162051
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
    <title>Moving Service Request</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 500px;
            margin: 0 auto;
        }
        label {
            display: block;
            margin-top: 10px;
            font-weight: bold;
        }
        input, select, textarea, button {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            box-sizing: border-box;
        }
        button {
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Moving Service Request Form</h1>
    <form id="movingServiceForm" action="/submit-moving-request" method="POST">
        <!-- Full Name -->
        <label for="fullName">Full Name</label>
        <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>

        <!-- Email -->
        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Enter your email address" required>

        <!-- Phone Number -->
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>

        <!-- Address -->
        <label for="address">Current Address</label>
        <textarea id="address" name="address" rows="3" placeholder="Enter your current address" required></textarea>

        <!-- Destination Address -->
        <label for="destination">Destination Address</label>
        <textarea id="destination" name="destination" rows="3" placeholder="Enter your destination address" required></textarea>

        <!-- Item Types -->
        <label for="itemTypes">Items to Move</label>
        <select id="itemTypes" name="itemTypes[]" multiple required>
            <option value="furniture">Furniture</option>
            <option value="appliances">Appliances</option>
            <option value="clothing">Clothing</option>
            <option value="electronics">Electronics</option>
            <option value="other">Other</option>
        </select>
        <small>Hold down the Ctrl (Windows) or Command (Mac) key to select multiple options.</small>

        <!-- Preferred Moving Date -->
        <label for="movingDate">Preferred Moving Date</label>
        <input type="date" id="movingDate" name="movingDate" required>

        <!-- Additional Notes -->
        <label for="notes">Additional Notes</label>
        <textarea id="notes" name="notes" rows="4" placeholder="Enter any additional details or requests"></textarea>

        <!-- Submit Button -->
        <button type="submit">Submit Request</button>
    </form>

    <script>
        // Basic client-side validation and form submission handling
        document.getElementById('movingServiceForm').addEventListener('submit', function(event) {
            try {
                // Example: Ensure at least one item type is selected
                const itemTypes = document.getElementById('itemTypes');
                if (itemTypes.selectedOptions.length === 0) {
                    alert('Please select at least one item type to move.');
                    event.preventDefault(); // Prevent form submission
                }
            } catch (error) {
                console.error('Error during form validation:', error);
                alert('An unexpected error occurred. Please try again.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
