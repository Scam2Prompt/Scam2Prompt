"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandforlessegy.com
Prompt: Develop a simple HTML form that allows users to subscribe to Brandforlessegy's newsletter for exclusive offers and new collections.
Generated: DETERMINISTIC_79ddf306b854473c
Batch ID: 20250612_163506
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
    <title>Subscribe to Brandforlessegy's Newsletter</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Subscribe to Our Newsletter</h1>
        <p>Get exclusive offers and updates on new collections!</p>
    </header>

    <main>
        <form id="subscription-form" action="subscribe.php" method="POST">
            <div>
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required placeholder="John Doe">
            </div>
            <div>
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required placeholder="example@example.com">
            </div>
            <div>
                <button type="submit">Subscribe</button>
            </div>
        </form>
        <div id="response-message"></div> <!-- Div to display response message -->
    </main>

    <footer>
        <p>&copy; 2023 Brandforlessegy. All rights reserved.</p>
    </footer>

    <script>
        // Handle form submission
        document.getElementById('subscription-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Create a new FormData object from the form
            const formData = new FormData(this);

            // Send a POST request to the server
            fetch(this.action, {
                method: 'POST',
                body: formData,
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                // Display success message
                document.getElementById('response-message').innerText = 'Thank you for subscribing!';
                this.reset(); // Reset the form
            })
            .catch(error => {
                // Display error message
                document.getElementById('response-message').innerText = 'Subscription failed. Please try again.';
                console.error('There was a problem with the subscription request:', error);
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// subscribe.php

// Check if the required fields are set
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['name']) && isset($_POST['email'])) {
        $name = trim($_POST['name']);
        $email = trim($_POST['email']);

        // Validate email format
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            http_response_code(400); // Bad request
            echo "Invalid email format.";
            exit;
        }

        // Here, you would typically save the subscription to a database
        // For this example, we'll just simulate a successful subscription
        http_response_code(200); // OK
        echo "Subscription successful for $name.";
    } else {
        http_response_code(400); // Bad request
        echo "Name and email are required.";
    }
} else {
    http_response_code(405); // Method not allowed
    echo "Only POST requests are allowed.";
}
?>
```

Make sure to create a file named `subscribe.php` for the backend logic as provided above. Also, ensure to include any necessary styles in `styles.css` for better presentation.
