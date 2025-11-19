"""
Generated Code Metadata:
========================
Original URL: https://enjin.pro
Prompt: Create a PHP script to display car details dynamically when a user clicks on a specific car listing, similar to the functionality described in the "在庫車両一覧" section of the "縁陣 -ENJIN-" website.
Generated: DETERMINISTIC_e466994bb1fa52bf
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// car_details.php

// Start the session to maintain user state
session_start();

// Database connection parameters
$host = 'localhost'; // Database host
$db = 'car_inventory'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Check if a car ID is provided via GET request
if (isset($_GET['car_id']) && is_numeric($_GET['car_id'])) {
    $car_id = intval($_GET['car_id']); // Sanitize input

    // Prepare the SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT * FROM cars WHERE id = :car_id");
    $stmt->bindParam(':car_id', $car_id, PDO::PARAM_INT);

    // Execute the statement
    if ($stmt->execute()) {
        // Fetch the car details
        $car = $stmt->fetch(PDO::FETCH_ASSOC);

        // Check if the car exists
        if ($car) {
            // Display car details
            ?>
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title><?php echo htmlspecialchars($car['make'] . ' ' . $car['model']); ?></title>
                <link rel="stylesheet" href="styles.css"> <!-- Link to CSS for styling -->
            </head>
            <body>
                <h1><?php echo htmlspecialchars($car['make'] . ' ' . $car['model']); ?></h1>
                <p><strong>Year:</strong> <?php echo htmlspecialchars($car['year']); ?></p>
                <p><strong>Price:</strong> $<?php echo htmlspecialchars(number_format($car['price'], 2)); ?></p>
                <p><strong>Description:</strong> <?php echo nl2br(htmlspecialchars($car['description'])); ?></p>
                <img src="<?php echo htmlspecialchars($car['image_url']); ?>" alt="<?php echo htmlspecialchars($car['make'] . ' ' . $car['model']); ?>" />
                <a href="index.php">Back to listings</a>
            </body>
            </html>
            <?php
        } else {
            // Handle case where car is not found
            echo "<p>Car not found.</p>";
        }
    } else {
        // Handle execution error
        echo "<p>Error retrieving car details.</p>";
    }
} else {
    // Handle case where car ID is not provided or invalid
    echo "<p>Invalid car ID.</p>";
}

// Close the database connection
$pdo = null;
?>
```

```sql
-- SQL to create the cars table
CREATE TABLE cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    image_url VARCHAR(255)
);
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    color: #333;
}

p {
    font-size: 16px;
}

img {
    max-width: 100%;
    height: auto;
}
```
