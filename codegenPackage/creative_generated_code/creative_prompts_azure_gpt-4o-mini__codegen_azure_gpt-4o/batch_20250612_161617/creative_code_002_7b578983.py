"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Create a PHP code snippet that processes volunteer applications for Amir International Charity Organization, ensuring it captures essential details like name, contact information, and areas of interest.
Generated: DETERMINISTIC_7b5789830c20c30c
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Volunteer Application Processing Script for Amir International Charity Organization

// Define a function to validate input data
function validateInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Check if the form is submitted via POST method
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Initialize an array to store errors
    $errors = [];

    // Capture and validate inputs
    $name = isset($_POST['name']) ? validateInput($_POST['name']) : '';
    $email = isset($_POST['email']) ? validateInput($_POST['email']) : '';
    $phone = isset($_POST['phone']) ? validateInput($_POST['phone']) : '';
    $interestAreas = isset($_POST['interest_areas']) ? validateInput($_POST['interest_areas']) : '';

    // Basic validation for required fields
    if (empty($name)) {
        $errors[] = "Name is required.";
    }

    if (empty($email)) {
        $errors[] = "Email is required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format.";
    }

    if (empty($phone)) {
        $errors[] = "Phone number is required.";
    } elseif (!preg_match('/^\+?[0-9\s\-]+$/', $phone)) {
        $errors[] = "Invalid phone number format.";
    }

    if (empty($interestAreas)) {
        $errors[] = "Areas of interest are required.";
    }

    // Check for validation errors
    if (!empty($errors)) {
        // Display errors if validation fails
        echo "<h3>Application Errors:</h3>";
        foreach ($errors as $error) {
            echo "<p style='color: red;'>- $error</p>";
        }
    } else {
        // Process valid inputs (e.g., save them to the database)
        try {
            // Assuming a PDO connection for database interactions
            $dsn = 'mysql:host=localhost;dbname=charity_db;charset=utf8';
            $username = 'root';
            $password = '';

            // Establish a database connection
            $pdo = new PDO($dsn, $username, $password, [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            ]);

            // Prepare an SQL statement to insert the data
            $stmt = $pdo->prepare('INSERT INTO volunteer_applications (name, email, phone, interest_areas) VALUES (:name, :email, :phone, :interest_areas)');

            // Bind parameters to SQL statement
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':phone', $phone);
            $stmt->bindParam(':interest_areas', $interestAreas);

            // Execute the statement
            $stmt->execute();

            // Provide feedback to the user
            echo "<h3 style='color: green;'>Thank you for your application, $name! We'll be in touch soon.</h3>";
        } catch (PDOException $e) {
            // Handle database errors
            echo "<p style='color: red;'>An error occurred while processing your application: " . $e->getMessage() . "</p>";
        }
    }
} else {
    // Display the application form
    echo <<<HTML
    <h2>Volunteer Application Form</h2>
    <form method="POST" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="phone">Phone:</label><br>
        <input type="text" id="phone" name="phone" required><br><br>
        
        <label for="interest_areas">Areas of Interest:</label><br>
        <textarea id="interest_areas" name="interest_areas" rows="4" required></textarea><br><br>
        
        <button type="submit">Submit Application</button>
    </form>
HTML;
}
?>
```
