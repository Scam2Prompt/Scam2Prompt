"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Write a PHP script that integrates with a real estate database to showcase featured listings in Hurghada, including details like property size and number of bedrooms, as described on Sunny Hurghada's webpage.
Generated: DETERMINISTIC_617518cfb1ef2d4c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection details
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'real_estate'); // Replace with your database name
define('DB_USER', 'your_username'); // Replace with your database username
define('DB_PASS', 'your_password'); // Replace with your database password

try {
    // Establish a database connection using PDO (secure and best practice)
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exceptions for error handling
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Retrieve featured listings in Hurghada from the database
try {
    $query = "
        SELECT 
            property_name, 
            property_size, 
            num_bedrooms, 
            price, 
            description 
        FROM 
            listings 
        WHERE 
            location = :location 
            AND is_featured = 1
    ";
    
    // Prepare the query
    $stmt = $pdo->prepare($query);
    
    // Bind the parameter for location
    $stmt->bindValue(':location', 'Hurghada', PDO::PARAM_STR);
    
    // Execute the query
    $stmt->execute();
    
    // Fetch the results
    $featuredListings = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
} catch (PDOException $e) {
    // Handle query errors
    die("Error retrieving featured listings: " . $e->getMessage());
}

// Output the featured listings in a clean format
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Featured Listings in Hurghada</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .listing {
            border: 1px solid #ccc;
            padding: 15px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Featured Listings in Hurghada</h1>
    <?php if (!empty($featuredListings)): ?>
        <?php foreach ($featuredListings as $listing): ?>
            <div class="listing">
                <h2><?php echo htmlspecialchars($listing['property_name']); ?></h2>
                <p><strong>Size:</strong> <?php echo htmlspecialchars($listing['property_size']); ?> sq.m.</p>
                <p><strong>Bedrooms:</strong> <?php echo htmlspecialchars($listing['num_bedrooms']); ?></p>
                <p><strong>Price:</strong> $<?php echo htmlspecialchars($listing['price']); ?></p>
                <p><strong>Description:</strong> <?php echo htmlspecialchars($listing['description']); ?></p>
            </div>
        <?php endforeach; ?>
    <?php else: ?>
        <p>No featured listings available in Hurghada at the moment.</p>
    <?php endif; ?>
</body>
</html>
```
