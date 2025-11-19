"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Develop a simple HTML form for users to book a spot in the "Patente d'impresa" course, including dropdowns for event selection and user type.
Generated: DETERMINISTIC_7b2a7d29abb8e3df
Batch ID: 20250612_160853
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
    <title>Patente d'impresa Course Booking</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Book Your Spot in the "Patente d'impresa" Course</h1>
        <form id="bookingForm" action="submit_booking.php" method="POST">
            <!-- Dropdown for event selection -->
            <label for="event">Select Event:</label>
            <select id="event" name="event" required>
                <option value="" disabled selected>Select an event</option>
                <option value="event1">Event 1 - Date: 2023-11-01</option>
                <option value="event2">Event 2 - Date: 2023-11-15</option>
                <option value="event3">Event 3 - Date: 2023-12-01</option>
            </select>

            <!-- Dropdown for user type selection -->
            <label for="userType">Select User Type:</label>
            <select id="userType" name="userType" required>
                <option value="" disabled selected>Select your user type</option>
                <option value="student">Student</option>
                <option value="professional">Professional</option>
                <option value="other">Other</option>
            </select>

            <!-- Submit button -->
            <button type="submit">Book Now</button>
        </form>
    </div>

    <script>
        // Form submission event listener
        document.getElementById('bookingForm').addEventListener('submit', function(event) {
            // Perform basic validation
            const eventSelect = document.getElementById('event');
            const userTypeSelect = document.getElementById('userType');

            if (eventSelect.value === "" || userTypeSelect.value === "") {
                alert("Please select both an event and a user type.");
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

select {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```
