"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasepro10000.webcindario.com
Prompt: Generate a PHP script for creating a contact form that stores submissions in a MySQL database. Include instructions for hosting the site on a free platform with a custom domain.
Generated: DETERMINISTIC_f44c2d02954023a3
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact_form.php

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create a connection to the MySQL database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to handle form submission
function handleFormSubmission($pdo) {
    // Check if form is submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Validate and sanitize input
        $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
        $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
        $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

        // Validate required fields
        if (empty($name) || empty($email) || empty($message)) {
            echo "All fields are required.";
            return;
        }

        // Prepare SQL statement to prevent SQL injection
        $stmt = $pdo->prepare("INSERT INTO contacts (name, email, message) VALUES (:name, :email, :message)");
        // Bind parameters
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':message', $message);

        // Execute the statement
        if ($stmt->execute()) {
            echo "Message sent successfully!";
        } else {
            echo "Failed to send message. Please try again.";
        }
    }
}

// Call the function to handle form submission
handleFormSubmission($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>Contact Us</h1>
    <form action="" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Send</button>
    </form>
</body>
</html>
```

### Instructions for Hosting on a Free Platform with a Custom Domain

1. **Choose a Free Hosting Provider**: Select a platform like InfinityFree, 000webhost, or FreeHosting.com that supports PHP and MySQL.
   
2. **Sign Up**: Register for an account on your chosen hosting provider.

3. **Create a MySQL Database**: Most providers will have a control panel where you can set up a new MySQL database. Make sure to note the database name, username, and password.

4. **Upload the PHP Script**: 
   - Use an FTP client (like FileZilla) or the hosting provider's file manager to upload your `contact_form.php` file to the server.

5. **Configure the PHP Script**: 
   - Edit the `$host`, `$dbname`, `$username`, and `$password` variables in `contact_form.php` to match your database settings.

6. **Set Up Your Custom Domain**: 
   - If you have a custom domain, follow your domain registrar's instructions to point your domain to your hosting provider's nameservers.

7. **Test the Contact Form**: 
   - Navigate to your custom domain in a web browser and test your contact form to ensure that submissions are being stored in the database.

8. **Secure Your Script**: Consider implementing additional security measures like input validation and CAPTCHA to protect against spam.

9. **Monitor Submissions**: Check the database periodically to ensure that submissions are being stored correctly.
