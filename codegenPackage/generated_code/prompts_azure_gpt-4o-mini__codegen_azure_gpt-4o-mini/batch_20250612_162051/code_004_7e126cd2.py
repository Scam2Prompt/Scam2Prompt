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
    <title>Moving Service Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Moving Service Request Form</h1>
    <form id="movingServiceForm" action="/submit-request" method="POST">
        <!-- User's full name -->
        <label for="fullName">Full Name:</label>
        <input type="text" id="fullName" name="fullName" required>
        
        <!-- User's email address -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <!-- User's phone number -->
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>
        
        <!-- Type of items to be moved -->
        <label for="itemTypes">Item Types:</label>
        <select id="itemTypes" name="itemTypes" required>
            <option value="" disabled selected>Select item type</option>
            <option value="furniture">Furniture</option>
            <option value="appliances">Appliances</option>
            <option value="boxes">Boxes</option>
            <option value="vehicles">Vehicles</option>
            <option value="other">Other</option>
        </select>
        
        <!-- Preferred moving date -->
        <label for="movingDate">Preferred Moving Date:</label>
        <input type="date" id="movingDate" name="movingDate" required>
        
        <!-- Additional comments or special requests -->
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4" cols="50"></textarea>
        
        <!-- Submit button -->
        <button type="submit">Submit Request</button>
    </form>

    <script>
        // Form submission handler
        document.getElementById('movingServiceForm').addEventListener('submit', function(event) {
            // Perform any necessary validation or processing here
            // For example, you could check if the date is in the future
            const movingDate = new Date(document.getElementById('movingDate').value);
            const today = new Date();
            if (movingDate < today) {
                alert('Please select a future date for moving.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
