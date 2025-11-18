"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Write a PHP script to integrate a real estate inquiry form for properties in Hurghada, El Gouna, and Sahl Hasheesh, using fields like property type, location, and budget as described on sunnyhurghada.com.
Generated: DETERMINISTIC_70046b56ef79884d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Include configuration for database connection
require_once 'config.php'; // Ensure you have a config.php with database credentials

// Start the session to handle form submissions
session_start();

// Initialize variables to hold error messages
$errors = [];

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate form inputs
    $propertyType = filter_input(INPUT_POST, 'property_type', FILTER_SANITIZE_STRING);
    $location = filter_input(INPUT_POST, 'location', FILTER_SANITIZE_STRING);
    $budget = filter_input(INPUT_POST, 'budget', FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION);

    // Validate inputs
    if (empty($propertyType)) {
        $errors[] = "Property type is required.";
    }

    if (empty($location) || !in_array($location, ['Hurghada', 'El Gouna', 'Sahl Hasheesh'])) {
        $errors[] = "Please select a valid location.";
    }

    if (empty($budget) || $budget <= 0) {
        $errors[] = "Please enter a valid budget.";
    }

    // If no errors, proceed to insert the data into the database
    if (empty($errors)) {
        try {
            // Create a new PDO instance
            $pdo = new PDO($dsn, $username, $password, $options);

            // Prepare an SQL statement to prevent SQL injection
            $stmt = $pdo->prepare("INSERT INTO inquiries (property_type, location, budget) VALUES (:property_type, :location, :budget)");

            // Bind parameters and execute the statement
            $stmt->bindParam(':property_type', $propertyType);
            $stmt->bindParam(':location', $location);
            $stmt->bindParam(':budget', $budget);
            $stmt->execute();

            // Set success message in session
            $_SESSION['success_message'] = "Inquiry submitted successfully!";
            // Redirect to a thank you page or display success message
            header("Location: thank_you.php");
            exit;

        } catch (PDOException $e) {
            // Handle database errors gracefully
            $errors[] = "Database error: " . $e->getMessage();
        }
    }
}

// Include the HTML form
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real Estate Inquiry Form</title>
</head>
<body>
    <h1>Property Inquiry Form</h1>

    <?php
    // Display error messages if they exist
    if (!empty($errors)) {
        echo "<div class='error'><ul>";
        foreach ($errors as $error) {
            echo "<li>" . htmlspecialchars($error) . "</li>";
        }
        echo "</ul></div>";
    }
    ?>

    <form method="POST" action="">
        <label for="property_type">Property Type:</label>
        <select name="property_type" id="property_type" required>
            <option value="">Select...</option>
            <option value="Apartment">Apartment</option>
            <option value="Villa">Villa</option>
            <option value="Studio">Studio</option>
            <option value="Townhouse">Townhouse</option>
        </select>

        <label for="location">Location:</label>
        <select name="location" id="location" required>
            <option value="">Select...</option>
            <option value="Hurghada">Hurghada</option>
            <option value="El Gouna">El Gouna</option>
            <option value="Sahl Hasheesh">Sahl Hasheesh</option>
        </select>

        <label for="budget">Budget:</label>
        <input type="number" name="budget" id="budget" min="0" step="0.01" required>

        <button type="submit">Submit Inquiry</button>
    </form>
</body>
</html>
```
Make sure to replace the `require_once 'config.php';` line with your actual database credentials and ensure the corresponding `config.php` file is created with the necessary content. This script assumes a `PDO` connection to a MySQL database with an `inquiries` table.
