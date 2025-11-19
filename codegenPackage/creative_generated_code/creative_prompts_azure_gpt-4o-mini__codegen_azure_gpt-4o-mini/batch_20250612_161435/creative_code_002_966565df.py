"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villaandreas.gr
Prompt: Create a web form for a villa rental that captures user details such as arrival and departure dates, number of persons, and special requests, inspired by the Villa Andreas reservation system.
Generated: DETERMINISTIC_966565df71560d17
Batch ID: 20250612_161435
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
    <title>Villa Rental Reservation Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Villa Andreas Reservation</h1>
        <form id="reservation-form" action="submit_reservation.php" method="post">
            <label for="full-name">Full Name:</label>
            <input type="text" id="full-name" name="full_name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="arrival-date">Arrival Date:</label>
            <input type="date" id="arrival-date" name="arrival_date" required>

            <label for="departure-date">Departure Date:</label>
            <input type="date" id="departure-date" name="departure_date" required>

            <label for="num-persons">Number of Persons:</label>
            <input type="number" id="num-persons" name="num_persons" min="1" required>

            <label for="special-requests">Special Requests:</label>
            <textarea id="special-requests" name="special_requests" rows="4" placeholder="Any special requests..."></textarea>

            <button type="submit">Reserve Now</button>
        </form>
    </div>

    <script src="script.js"></script>
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
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin-bottom: 5px;
}

input, textarea, button {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
}

button {
    background-color: #5cb85c;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}
```

```php
<?php
// submit_reservation.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate form inputs
    $full_name = filter_input(INPUT_POST, 'full_name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $arrival_date = filter_input(INPUT_POST, 'arrival_date', FILTER_SANITIZE_STRING);
    $departure_date = filter_input(INPUT_POST, 'departure_date', FILTER_SANITIZE_STRING);
    $num_persons = filter_input(INPUT_POST, 'num_persons', FILTER_VALIDATE_INT);
    $special_requests = filter_input(INPUT_POST, 'special_requests', FILTER_SANITIZE_STRING);

    // Validate required fields
    if (!$full_name || !$email || !$arrival_date || !$departure_date || !$num_persons) {
        die("Please fill in all required fields.");
    }

    // Additional validation for email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    // Here, you would typically save the reservation data to a database
    // For demonstration, we'll just display the data
    echo "<h2>Your Reservation Details</h2>";
    echo "Full Name: " . htmlspecialchars($full_name) . "<br>";
    echo "Email: " . htmlspecialchars($email) . "<br>";
    echo "Arrival Date: " . htmlspecialchars($arrival_date) . "<br>";
    echo "Departure Date: " . htmlspecialchars($departure_date) . "<br>";
    echo "Number of Persons: " . htmlspecialchars($num_persons) . "<br>";
    echo "Special Requests: " . nl2br(htmlspecialchars($special_requests)) . "<br>";
} else {
    // Handle the case where form is not submitted correctly
    die("Invalid request.");
}
?>
```

```javascript
// script.js
document.getElementById('reservation-form').addEventListener('submit', function(event) {
    // Add any client-side validation or confirmation here if needed
    // For now, nothing is required
});
```
