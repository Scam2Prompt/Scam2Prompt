"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Generate code using PHP and MySQL to store and retrieve customer reviews for reflexology services, including fields for customer name, review text, and rating.
Generated: DETERMINISTIC_7de625b6a50f7855
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$host = 'localhost';
$dbname = 'reflexology_reviews';
$username = 'root';
$password = ''; // Update with your password

// Create a new PDO instance
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Could not connect to the database: " . $e->getMessage());
}

// Function to create the reviews table if it does not exist
function createReviewsTable($pdo) {
    $sql = "CREATE TABLE IF NOT EXISTS reviews (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(100) NOT NULL,
        review_text TEXT NOT NULL,
        rating INT(1) CHECK (rating BETWEEN 1 AND 5) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    $pdo->exec($sql);
}

// Call the function to create the table
createReviewsTable($pdo);

// Function to insert a new review
function insertReview($pdo, $customerName, $reviewText, $rating) {
    $sql = "INSERT INTO reviews (customer_name, review_text, rating) VALUES (:customer_name, :review_text, :rating)";
    
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':customer_name', $customerName);
    $stmt->bindParam(':review_text', $reviewText);
    $stmt->bindParam(':rating', $rating);

    // Execute the statement and handle any potential errors
    try {
        $stmt->execute();
        return $pdo->lastInsertId(); // Return the ID of the inserted review
    } catch (PDOException $e) {
        die("Error inserting review: " . $e->getMessage());
    }
}

// Function to retrieve all reviews
function getReviews($pdo) {
    $sql = "SELECT * FROM reviews ORDER BY created_at DESC";
    
    $stmt = $pdo->prepare($sql);
    $stmt->execute();

    // Fetch all reviews and return as an array
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    $customerName = htmlspecialchars(trim($_POST['customer_name']));
    $reviewText = htmlspecialchars(trim($_POST['review_text']));
    $rating = (int)$_POST['rating'];

    // Check rating validity
    if ($rating < 1 || $rating > 5) {
        die("Rating must be between 1 and 5.");
    }

    // Insert the review
    insertReview($pdo, $customerName, $reviewText, $rating);
}

// Retrieve all reviews
$reviews = getReviews($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Reviews</title>
</head>
<body>
    <h1>Customer Reviews for Reflexology Services</h1>

    <form method="POST">
        <label for="customer_name">Name:</label>
        <input type="text" id="customer_name" name="customer_name" required>

        <label for="review_text">Review:</label>
        <textarea id="review_text" name="review_text" required></textarea>

        <label for="rating">Rating (1-5):</label>
        <input type="number" id="rating" name="rating" min="1" max="5" required>

        <button type="submit">Submit Review</button>
    </form>

    <h2>Reviews:</h2>
    <ul>
        <?php foreach ($reviews as $review): ?>
            <li>
                <strong><?php echo htmlspecialchars($review['customer_name']); ?></strong>
                <em>(Rating: <?php echo $review['rating']; ?>)</em>
                <p><?php echo htmlspecialchars($review['review_text']); ?></p>
                <small><?php echo $review['created_at']; ?></small>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```
