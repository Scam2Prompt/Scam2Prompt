"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstbaptistnj.org
Prompt: Develop a web form for planning a visit to a church, incorporating elements from the First Baptist Church's visitor engagement strategies.
Generated: DETERMINISTIC_03a989c713eb66bd
Batch ID: 20250612_163912
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
    <title>Plan Your Visit - First Baptist Church</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Welcome to First Baptist Church</h1>
        <p>We're excited to plan your visit!</p>
    </header>
    
    <main>
        <form id="visitForm" method="POST" action="submit_visit.php">
            <fieldset>
                <legend>Visitor Information</legend>
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required placeholder="John Doe">

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="you@example.com">
                
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" placeholder="(123) 456-7890">
                
                <label for="visitDate">Preferred Visit Date:</label>
                <input type="date" id="visitDate" name="visitDate" required>
                
                <label for="serviceType">Service Type:</label>
                <select id="serviceType" name="serviceType" required>
                    <option value="">Select a Service</option>
                    <option value="sunday_service">Sunday Service</option>
                    <option value="youth_service">Youth Service</option>
                    <option value="special_event">Special Event</option>
                </select>
                
                <label for="comments">Additional Comments:</label>
                <textarea id="comments" name="comments" rows="4" placeholder="Any specific requests or questions?"></textarea>
                
                <button type="submit">Submit</button>
            </fieldset>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 First Baptist Church. All Rights Reserved.</p>
    </footer>

    <script>
        // Form validation before submission
        document.getElementById('visitForm').onsubmit = function(event) {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const visitDate = document.getElementById('visitDate').value.trim();

            // Simple validation for empty fields
            if (!name || !email || !visitDate) {
                alert("Please fill in all required fields.");
                event.preventDefault(); // Prevent form submission
                return false;
            }
            return true; // Proceed with form submission
        };
    </script>
</body>
</html>
```

```php
<?php
// submit_visit.php

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $visitDate = filter_input(INPUT_POST, 'visitDate', FILTER_SANITIZE_STRING);
    $serviceType = filter_input(INPUT_POST, 'serviceType', FILTER_SANITIZE_STRING);
    $comments = filter_input(INPUT_POST, 'comments', FILTER_SANITIZE_STRING);

    // Validate required fields
    if (!$name || !$email || !$visitDate || !$serviceType) {
        die('Please fill in all required fields.');
    }

    // Prepare data for database or email
    $to = 'info@firstbaptistchurch.org'; // Change to the church's actual email
    $subject = 'New Visit Request from ' . $name;
    $message = "Name: $name\nEmail: $email\nPhone: $phone\nVisit Date: $visitDate\nService Type: $serviceType\nComments: $comments";
    $headers = 'From: ' . $email;

    // Send email
    if (mail($to, $subject, $message, $headers)) {
        echo "Thank you for planning your visit! We look forward to seeing you soon.";
    } else {
        echo "There was an error sending your request. Please try again later.";
    }
} else {
    // Redirect if accessed directly
    header('Location: index.html');
    exit();
}
?>
```

```css
/* styles.css */

/* Basic styles for the visit form */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 1rem;
    text-align: center;
}

main {
    margin: 20px;
}

fieldset {
    border: 1px solid #ccc;
    padding: 20px;
    margin-bottom: 20px;
}

legend {
    font-weight: bold;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, textarea {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

footer {
    text-align: center;
    padding: 10px;
    background-color: #f1f1f1;
}
```
