"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inkawasiollague.cl
Prompt: Develop a simple web form for users to submit their contact information and comments when reserving a room at a hostel in Ollagüe.
Generated: DETERMINISTIC_a583d1c59d28c7ba
Batch ID: 20250612_162051
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
    <title>Room Reservation Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>

<body>
    <div class="container">
        <h1>Hostel Room Reservation</h1>
        <form id="reservation-form">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="comments">Comments:</label>
            <textarea id="comments" name="comments" rows="4" cols="50"></textarea>

            <button type="submit">Reserve Room</button>
        </form>
        <div id="response-message"></div>
    </div>

    <script>
        // Add event listener to handle form submission
        document.getElementById('reservation-form').addEventListener('submit', async function (event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            try {
                const response = await fetch('submit_reservation.php', {
                    method: 'POST',
                    body: formData,
                });

                // Check if the response is ok (status in the range 200-299)
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }

                const result = await response.json(); // Parse JSON response
                document.getElementById('response-message').innerText = result.message; // Display success message
            } catch (error) {
                document.getElementById('response-message').innerText = 'Error: ' + error.message; // Display error message
            }
        });
    </script>
</body>

</html>
```

```php
<?php
// submit_reservation.php

header('Content-Type: application/json'); // Set content type to JSON

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input data
    $name = filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    $phone = filter_var(trim($_POST['phone']), FILTER_SANITIZE_STRING);
    $comments = filter_var(trim($_POST['comments']), FILTER_SANITIZE_STRING);

    // Simple validation
    if (empty($name) || empty($email) || empty($phone)) {
        echo json_encode(['message' => 'Please fill in all required fields.']);
        http_response_code(400); // Bad Request
        exit;
    }

    // Here you would typically save the data to a database
    // For demonstration, we'll just simulate saving with a success response

    echo json_encode(['message' => 'Reservation successfully submitted!']);
    http_response_code(200); // OK
} else {
    echo json_encode(['message' => 'Invalid request method.']);
    http_response_code(405); // Method Not Allowed
}
?>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin-top: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    margin-top: 20px;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

#response-message {
    margin-top: 20px;
    text-align: center;
}
```
