"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enjin.pro
Prompt: Create a PHP script to display car details dynamically when a user clicks on a specific car listing, similar to the functionality described in the "在庫車両一覧" section of the "縁陣 -ENJIN-" website.
Generated: DETERMINISTIC_e466994bb1fa52bf
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// database.php: Contains database connection logic
// Ensure this file contains proper credentials and is secured.
require_once 'database.php';

// Helper function to fetch car details by ID
function getCarDetails($carId, $pdo) {
    try {
        $sql = "SELECT id, name, model, year, price, description, image_url FROM cars WHERE id = :carId";
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':carId', $carId, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetch(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Database error: " . $e->getMessage());
        return null; // Return null if there's any issue
    }
}

// Check if a car ID is provided via GET request
if (isset($_GET['car_id']) && is_numeric($_GET['car_id'])) {
    $carId = intval($_GET['car_id']);

    // Fetch car details from database
    $carDetails = getCarDetails($carId, $pdo);

    if ($carDetails) {
        // Display car details dynamically
        ?>
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title><?php echo htmlspecialchars($carDetails['name']); ?> Details</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; padding: 0; }
                .car-details { max-width: 600px; margin: auto; }
                .car-details img { max-width: 100%; height: auto; }
                .car-details h1 { font-size: 24px; }
                .car-details p { font-size: 18px; margin: 10px 0; }
            </style>
        </head>
        <body>
            <div class="car-details">
                <h1><?php echo htmlspecialchars($carDetails['name']); ?> (<?php echo htmlspecialchars($carDetails['year']); ?>)</h1>
                <img src="<?php echo htmlspecialchars($carDetails['image_url']); ?>" alt="<?php echo htmlspecialchars($carDetails['name']); ?>">
                <p><strong>Model:</strong> <?php echo htmlspecialchars($carDetails['model']); ?></p>
                <p><strong>Price:</strong> $<?php echo number_format($carDetails['price'], 2); ?></p>
                <p><strong>Description:</strong> <?php echo htmlspecialchars($carDetails['description']); ?></p>
                <a href="car_list.php">Back to Listings</a>
            </div>
        </body>
        </html>
        <?php
    } else {
        // Handle case where car details are not found
        http_response_code(404);
        echo "<h1>Car Not Found</h1>";
        echo "<p>The car you are looking for does not exist.</p>";
        echo '<a href="car_list.php">Back to Listings</a>';
    }
} else {
    // Redirect to car listing page if no valid car ID is provided
    header("Location: car_list.php");
    exit;
}
?>
```
