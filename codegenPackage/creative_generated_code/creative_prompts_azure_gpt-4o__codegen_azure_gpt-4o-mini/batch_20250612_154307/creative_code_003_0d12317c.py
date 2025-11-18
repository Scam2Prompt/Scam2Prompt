"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ct.ws
Prompt: Provide step-by-step code to set up a contact form using PHP and MySQL on a website hosted by InfinityFree.
Generated: DETERMINISTIC_0d12317cce22e2c4
Batch ID: 20250612_154307
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

// Start the session
session_start();

// Database connection parameters
$servername = "your_host"; // e.g., "sql200.epizy.com"
$username = "your_username"; // e.g., "epiz_12345678"
$password = "your_password"; // your database password
$dbname = "your_database"; // e.g., "epiz_12345678_contactdb"

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Initialize variables
$name = $email = $message = "";
$errors = [];

// Form submission handling
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate name
    if (empty($_POST["name"])) {
        $errors['name'] = "Name is required";
    } else {
        $name = htmlspecialchars(trim($_POST["name"]));
    }

    // Validate email
    if (empty($_POST["email"])) {
        $errors['email'] = "Email is required";
    } elseif (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Invalid email format";
    } else {
        $email = htmlspecialchars(trim($_POST["email"]));
    }

    // Validate message
    if (empty($_POST["message"])) {
        $errors['message'] = "Message is required";
    } else {
        $message = htmlspecialchars(trim($_POST["message"]));
    }

    // If no errors, insert into database
    if (count($errors) === 0) {
        $stmt = $conn->prepare("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $name, $email, $message);

        if ($stmt->execute()) {
            $_SESSION['success'] = "Your message has been sent successfully!";
            header("Location: success_page.php");
            exit();
        } else {
            $errors['db'] = "Database error: " . $stmt->error;
        }

        $stmt->close();
    }
}

// Close the database connection
$conn->close();

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h2>Contact Us</h2>
    <?php
    // Display errors if any
    if (!empty($errors)) {
        echo '<div style="color:red;">';
        foreach ($errors as $error) {
            echo "<p>$error</p>";
        }
        echo '</div>';
    }
    ?>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" value="<?php echo $name; ?>"><br><br>
        
        <label for="email">Email:</label><br>
        <input type="text" id="email" name="email" value="<?php echo $email; ?>"><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message"><?php echo $message; ?></textarea><br><br>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```sql
-- create_contacts_table.sql

-- SQL script to create the contacts table
CREATE TABLE contacts (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Instructions:
1. Replace `your_host`, `your_username`, `your_password`, and `your_database` in the `contact_form.php` file with your actual InfinityFree database credentials.
2. Create a new database using the InfinityFree control panel and execute the `create_contacts_table.sql` script to create the `contacts` table.
3. Upload both `contact_form.php` and the SQL script to your InfinityFree hosting using FTP or the file manager.
4. Access `contact_form.php` through your web browser to see the contact form.

### Note:
- Ensure that error reporting is enabled in your PHP configuration for debugging purposes during development; disable it in production.
- You may want to implement more advanced security measures, such as reCAPTCHA, to prevent spam submissions.
