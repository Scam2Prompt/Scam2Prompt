"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ptei.edu.bd
Prompt: Develop a PHP script that submits an online application for the Mechanical Technology program at PTEI, including necessary form fields.
Generated: DETERMINISTIC_8597e9324734b436
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Mechanical Technology Program Application Submission Script
// Author: [Your Name]
// Date: [Insert Date]
// Description: This script submits an online application for the Mechanical Technology program at PTEI.

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input fields
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $address = filter_input(INPUT_POST, 'address', FILTER_SANITIZE_STRING);
    $dob = filter_input(INPUT_POST, 'dob', FILTER_SANITIZE_STRING); // Date of Birth
    $highschool = filter_input(INPUT_POST, 'highschool', FILTER_SANITIZE_STRING);
    $comments = filter_input(INPUT_POST, 'comments', FILTER_SANITIZE_STRING);

    // Check for required fields
    if (!$name || !$email || !$phone || !$address || !$dob || !$highschool) {
        // Return an error if required fields are missing
        die('Error: All required fields must be filled out.');
    }

    // Database connection
    try {
        $dsn = 'mysql:host=localhost;dbname=ptei'; // Update with your database host and name
        $username = 'root'; // Update with your database username
        $password = ''; // Update with your database password

        $pdo = new PDO($dsn, $username, $password, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]);

        // Prepare SQL query to insert application data
        $sql = "INSERT INTO applications (name, email, phone, address, dob, highschool, comments, program) 
                VALUES (:name, :email, :phone, :address, :dob, :highschool, :comments, :program)";

        $stmt = $pdo->prepare($sql);

        // Bind parameters
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':phone', $phone);
        $stmt->bindParam(':address', $address);
        $stmt->bindParam(':dob', $dob);
        $stmt->bindParam(':highschool', $highschool);
        $stmt->bindParam(':comments', $comments);
        $stmt->bindValue(':program', 'Mechanical Technology');

        // Execute the query
        $stmt->execute();

        // Application successfully submitted
        echo 'Application submitted successfully. Thank you for applying!';
    } catch (PDOException $e) {
        // Handle database connection errors
        die('Database error: ' . $e->getMessage());
    }
} else {
    // Display the application form
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mechanical Technology Application</title>
    </head>
    <body>
        <h1>Apply for the Mechanical Technology Program</h1>
        <form method="POST" action="">
            <label for="name">Full Name:</label><br>
            <input type="text" id="name" name="name" required><br><br>

            <label for="email">Email Address:</label><br>
            <input type="email" id="email" name="email" required><br><br>

            <label for="phone">Phone Number:</label><br>
            <input type="text" id="phone" name="phone" required><br><br>

            <label for="address">Home Address:</label><br>
            <input type="text" id="address" name="address" required><br><br>

            <label for="dob">Date of Birth:</label><br>
            <input type="date" id="dob" name="dob" required><br><br>

            <label for="highschool">High School Attended:</label><br>
            <input type="text" id="highschool" name="highschool" required><br><br>

            <label for="comments">Additional Comments:</label><br>
            <textarea id="comments" name="comments"></textarea><br><br>

            <button type="submit">Submit Application</button>
        </form>
    </body>
    </html>
    <?php
}
?>
```
