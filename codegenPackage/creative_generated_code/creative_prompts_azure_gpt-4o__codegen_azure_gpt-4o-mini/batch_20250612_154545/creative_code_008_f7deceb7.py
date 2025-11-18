"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearmybrand.com
Prompt: Create a PHP script for managing client reviews and testimonials on a website, similar to the client feedback showcased by Bear My Brand, LLC.
Generated: DETERMINISTIC_f7deceb7d3e7e5c0
Batch ID: 20250612_154545
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
$db = 'reviews_db'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password
$charset = 'utf8mb4';

// Set up the PDO connection
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

/**
 * Function to add a review to the database
 *
 * @param string $clientName The name of the client
 * @param string $reviewText The review text
 * @param int $rating The rating given by the client (1-5)
 * @return bool True on success, false on failure
 */
function addReview($clientName, $reviewText, $rating) {
    global $pdo;

    // Prepare the SQL statement
    $sql = "INSERT INTO reviews (client_name, review_text, rating, created_at) VALUES (?, ?, ?, NOW())";
    
    // Validate input data
    if (empty($clientName) || empty($reviewText) || !is_int($rating) || $rating < 1 || $rating > 5) {
        return false; // Simple validation to avoid invalid entries
    }

    try {
        $stmt = $pdo->prepare($sql);
        return $stmt->execute([$clientName, $reviewText, $rating]);
    } catch (PDOException $e) {
        error_log($e->getMessage()); // Log error for debugging
        return false;
    }
}

/**
 * Function to retrieve all reviews from the database
 *
 * @return array An array of reviews
 */
function getReviews() {
    global $pdo;

    $sql = "SELECT * FROM reviews ORDER BY created_at DESC";
    
    try {
        $stmt = $pdo->query($sql);
        return $stmt->fetchAll();
    } catch (PDOException $e) {
        error_log($e->getMessage());
        return [];
    }
}

/**
 * Function to display reviews on the website
 *
 * @param array $reviews An array of reviews to display
 * @return void
 */
function displayReviews($reviews) {
    if (empty($reviews)) {
        echo "<p>No reviews available.</p>";
        return;
    }

    foreach ($reviews as $review) {
        echo "<div class='review'>";
        echo "<h3>" . htmlspecialchars($review['client_name']) . "</h3>";
        echo "<p>" . nl2br(htmlspecialchars($review['review_text'])) . "</p>";
        echo "<p>Rating: " . str_repeat('★', $review['rating']) . str_repeat('☆', 5 - $review['rating']) . "</p>";
        echo "<p><em>Posted on: " . htmlspecialchars($review['created_at']) . "</em></p>";
        echo "</div>";
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $clientName = $_POST['client_name'] ?? '';
    $reviewText = $_POST['review_text'] ?? '';
    $rating = intval($_POST['rating'] ?? 0);

    if (addReview($clientName, $reviewText, $rating)) {
        echo "<p>Review added successfully!</p>";
    } else {
        echo "<p>Error adding review. Please try again.</p>";
    }
}

// Retrieving reviews to display
$reviews = getReviews();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Client Reviews</title>
    <style>
        .review { margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; }
        h3 { margin: 0; }
    </style>
</head>
<body>
    <h1>Client Reviews</h1>
    
    <form method="post">
        <input type="text" name="client_name" placeholder="Your Name" required>
        <textarea name="review_text" placeholder="Your Review" required></textarea>
        <select name="rating" required>
            <option value="">Rate us</option>
            <option value="1">1 Star</option>
            <option value="2">2 Stars</option>
            <option value="3">3 Stars</option>
            <option value="4">4 Stars</option>
            <option value="5">5 Stars</option>
        </select>
        <button type="submit">Submit Review</button>
    </form>

    <h2>All Reviews</h2>
    <?php displayReviews($reviews); ?>
</body>
</html>
```
