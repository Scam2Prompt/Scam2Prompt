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

/**
 * CarListing.php
 *
 * Displays car details dynamically when a user clicks on a specific car listing.
 */

// Configuration
$config = [
    'dbHost' => 'localhost',
    'dbUsername' => 'your_username',
    'dbPassword' => 'your_password',
    'dbName' => 'your_database',
];

// Establish database connection
try {
    $pdo = new PDO(
        "mysql:host={$config['dbHost']};dbname={$config['dbName']}",
        $config['dbUsername'],
        $config['dbPassword']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception("Database connection failed: " . $e->getMessage());
}

/**
 * Retrieves car listing details from the database.
 *
 * @param int $carId
 * @return array|false
 */
function getCarDetails($carId) {
    global $pdo;

    $query = "
        SELECT 
            cl.id,
            cl.make,
            cl.model,
            cl.year,
            cl.price,
            cl.description
        FROM 
            car_listings cl
        WHERE 
            cl.id = :carId
    ";

    try {
        $stmt = $pdo->prepare($query);
        $stmt->bindParam(':carId', $carId, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetch();
    } catch (PDOException $e) {
        error_log("Error retrieving car details: " . $e->getMessage());
        return false;
    }
}

/**
 * Displays car details dynamically.
 *
 * @param int $carId
 */
function displayCarDetails($carId) {
    $carDetails = getCarDetails($carId);

    if (!$carDetails) {
        http_response_code(404);
        echo "Car not found.";
        return;
    }

    $output = "
        <div class='car-details'>
            <h2>{$carDetails['make']} {$carDetails['model']} ({$carDetails['year']})</h2>
            <p>Price: \${$carDetails['price']}</p>
            <p>Description: {$carDetails['description']}</p>
        </div>
    ";

    echo $output;
}

// Handle AJAX request
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['carId'])) {
    $carId = filter_var($_POST['carId'], FILTER_VALIDATE_INT);
    if ($carId === false) {
        http_response_code(400);
        echo "Invalid car ID.";
        return;
    }

    displayCarDetails($carId);
} else {
    http_response_code(405);
    echo "Method not allowed.";
}

// Close database connection
$pdo = null;

```

```javascript
// For dynamic display using JavaScript and AJAX

// Get all car listings
const carListings = document.querySelectorAll('.car-listing');

// Add event listener to each car listing
carListings.forEach((listing) => {
    listing.addEventListener('click', (e) => {
        const carId = listing.dataset.carId;

        // Create AJAX request
        const xhr = new XMLHttpRequest();
        xhr.open('POST', 'CarListing.php', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send(`carId=${carId}`);

        // Handle response
        xhr.onload = function() {
            if (xhr.status === 200) {
                const carDetails = xhr.responseText;
                const carDetailsContainer = document.getElementById('car-details');
                carDetailsContainer.innerHTML = carDetails;
            } else {
                console.error('Error:', xhr.statusText);
            }
        };

        xhr.onerror = function() {
            console.error('Error:', xhr.statusText);
        };
    });
});
```

```html
<!-- Example usage in HTML -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Listings</title>
</head>
<body>
    <h1>Car Listings</h1>
    <div class="car-listings">
        <!-- Assume car listings are generated dynamically -->
        <div class="car-listing" data-car-id="1">Listing 1</div>
        <div class="car-listing" data-car-id="2">Listing 2</div>
    </div>
    <div id="car-details"></div>

    <script src="script.js"></script>
</body>
</html>
```
