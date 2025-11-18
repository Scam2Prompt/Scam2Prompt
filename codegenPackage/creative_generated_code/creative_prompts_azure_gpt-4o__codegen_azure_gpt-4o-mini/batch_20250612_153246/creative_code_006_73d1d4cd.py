"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gmpinvestments.co.uk
Prompt: Write code to create a contact form for a property investment website, ensuring it collects details for making property offers as described in the "Contact Us" section of Gold Mark Investment Limited.
Generated: DETERMINISTIC_73d1d4cde2271f99
Batch ID: 20250612_153246
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
    <title>Contact Us - Gold Mark Investment Limited</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Contact Us</h1>
    </header>
    
    <main>
        <form id="contact-form" method="post" action="submit_contact.php">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="property">Property of Interest:</label>
            <input type="text" id="property" name="property" required>

            <label for="offer">Offer Amount:</label>
            <input type="number" id="offer" name="offer" required>

            <label for="message">Additional Message:</label>
            <textarea id="message" name="message" rows="4"></textarea>

            <button type="submit">Submit Offer</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Gold Mark Investment Limited</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```php
<?php
// submit_contact.php - Handles the submission of the contact form

// Set content type to JSON for API response
header('Content-Type: application/json');

// Initialize response array
$response = [
    'success' => false,
    'message' => ''
];

// Check if POST request is made
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate required fields
    $requiredFields = ['name', 'email', 'phone', 'property', 'offer'];
    foreach ($requiredFields as $field) {
        if (empty($_POST[$field])) {
            $response['message'] = "Error: '$field' is required.";
            echo json_encode($response);
            exit;
        }
    }

    // Sanitize input data
    $name = filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    $phone = filter_var(trim($_POST['phone']), FILTER_SANITIZE_STRING);
    $property = filter_var(trim($_POST['property']), FILTER_SANITIZE_STRING);
    $offer = filter_var(trim($_POST['offer']), FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION);
    $message = filter_var(trim($_POST['message']), FILTER_SANITIZE_STRING);

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $response['message'] = 'Error: Invalid email format.';
        echo json_encode($response);
        exit;
    }

    // Here, you would typically send the data to a database or an email service
    // For the sake of this example, we'll assume the data is processed successfully.

    // Set success response
    $response['success'] = true;
    $response['message'] = 'Your offer has been submitted successfully!';
} else {
    $response['message'] = 'Error: Invalid request method.';
}

// Return JSON response
echo json_encode($response);
?>
```

```css
/* styles.css - Basic styles for the contact form */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

header {
    background: #35424a;
    color: #ffffff;
    padding: 10px 0;
    text-align: center;
}

form {
    background: #ffffff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background: #35424a;
    color: #ffffff;
    border: none;
    padding: 10px;
    cursor: pointer;
}

button:hover {
    background: #48525e;
}

footer {
    text-align: center;
    margin-top: 20px;
}
```

```javascript
// script.js - Client-side form handling
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Create FormData object
    const formData = new FormData(this);

    // Send data to the server using fetch API
    fetch('submit_contact.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message); // Show success message
            this.reset(); // Reset the form
        } else {
            alert(data.message); // Show error message
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was a problem with your submission. Please try again.');
    });
});
```
