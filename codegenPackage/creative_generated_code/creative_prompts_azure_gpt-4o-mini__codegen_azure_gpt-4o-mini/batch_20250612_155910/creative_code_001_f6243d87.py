"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ct.ws
Prompt: Write a PHP script that can be hosted on a ct.ws domain using InfinityFree's free hosting service.
Generated: DETERMINISTIC_f6243d87036602a4
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// index.php

// Set the content type to HTML
header('Content-Type: text/html; charset=utf-8');

// Start output buffering
ob_start();

/**
 * Function to sanitize user input
 * 
 * @param string $data The input data to sanitize
 * @return string The sanitized data
 */
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize the user input
    $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
    $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : '';
    
    // Validate name and email
    $errors = [];
    if (empty($name)) {
        $errors[] = "Name is required.";
    }

    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Valid email is required.";
    }
    
    // Process the form if there are no errors
    if (empty($errors)) {
        // Here you would typically send an email or store the data in a database
        echo "<h2>Thank you, $name! Your email ($email) has been submitted successfully!</h2>";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<h1>Contact Us</h1>

<!-- Display errors if there are any -->
<?php if (!empty($errors)): ?>
    <div class="error">
        <ul>
            <?php foreach ($errors as $error): ?>
                <li><?php echo $error; ?></li>
            <?php endforeach; ?>
        </ul>
    </div>
<?php endif; ?>

<!-- Contact form -->
<form action="" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <button type="submit">Submit</button>
</form>

</body>
</html>

<?php
// End output buffering and flush output
ob_end_flush();
?>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"],
input[type="email"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #5cb85c;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

.error {
    background-color: #f8d7da;
    color: #721c24;
    padding: 10px;
    margin-bottom: 20px;
}
```
