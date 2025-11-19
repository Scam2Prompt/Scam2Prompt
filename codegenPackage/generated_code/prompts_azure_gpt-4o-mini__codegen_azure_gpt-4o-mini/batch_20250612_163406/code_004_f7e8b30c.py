"""
Generated Code Metadata:
========================
Original URL: https://autocarescosme.com
Prompt: Construct a sample HTML form for users to inquire about renting classic vehicles from Autocares Cosme, ensuring it captures all necessary information for the booking process.
Generated: DETERMINISTIC_f7e8b30c74729fb1
Batch ID: 20250612_163406
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
    <title>Classic Vehicle Rental Inquiry - Autocares Cosme</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Inquire About Renting Classic Vehicles</h1>
        <p>Fill out the form below to get started with your booking.</p>
    </header>

    <form id="rentalInquiryForm" action="/submit-inquiry" method="POST">
        <!-- User's Full Name -->
        <label for="fullName">Full Name:</label>
        <input type="text" id="fullName" name="fullName" required placeholder="John Doe">

        <!-- User's Email Address -->
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required placeholder="example@example.com">

        <!-- User's Phone Number -->
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required placeholder="+1 (555) 555-5555">

        <!-- Vehicle Selection -->
        <label for="vehicle">Select Vehicle:</label>
        <select id="vehicle" name="vehicle" required>
            <option value="" disabled selected>Select a vehicle</option>
            <option value="classic-car-1">Classic Car 1</option>
            <option value="classic-car-2">Classic Car 2</option>
            <option value="classic-car-3">Classic Car 3</option>
        </select>

        <!-- Rental Start Date -->
        <label for="startDate">Rental Start Date:</label>
        <input type="date" id="startDate" name="startDate" required>

        <!-- Rental End Date -->
        <label for="endDate">Rental End Date:</label>
        <input type="date" id="endDate" name="endDate" required>

        <!-- Additional Comments -->
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4" placeholder="Any special requests or questions?"></textarea>

        <!-- Submit Button -->
        <button type="submit">Submit Inquiry</button>
    </form>

    <footer>
        <p>&copy; 2023 Autocares Cosme. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('rentalInquiryForm').addEventListener('submit', function(event) {
            // Perform any necessary validation or processing here
            // For example, check if the end date is after the start date
            const startDate = new Date(document.getElementById('startDate').value);
            const endDate = new Date(document.getElementById('endDate').value);
            if (endDate <= startDate) {
                alert('End date must be after the start date.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
