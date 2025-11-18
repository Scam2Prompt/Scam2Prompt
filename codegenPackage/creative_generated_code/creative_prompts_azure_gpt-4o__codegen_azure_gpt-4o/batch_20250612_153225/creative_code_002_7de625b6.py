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
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'reflexology_reviews');

try {
    // Establish database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Create reviews table if it doesn't exist
try {
    $createTableQuery = "
        CREATE TABLE IF NOT EXISTS reviews (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_name VARCHAR(255) NOT NULL,
            review_text TEXT NOT NULL,
            rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ";
    $pdo->exec($createTableQuery);
} catch (PDOException $e) {
    die("Error creating table: " . $e->getMessage());
}

// Function to store a new review
function storeReview($pdo, $customerName, $reviewText, $rating) {
    try {
        $query = "INSERT INTO reviews (customer_name, review_text, rating) VALUES (:customer_name, :review_text, :rating)";
        $stmt = $pdo->prepare($query);
        $stmt->bindParam(':customer_name', $customerName);
        $stmt->bindParam(':review_text', $reviewText);
        $stmt->bindParam(':rating', $rating);
        $stmt->execute();
        echo "Review successfully stored!\n";
    } catch (PDOException $e) {
        echo "Error storing review: " . $e->getMessage();
    }
}

// Function to retrieve all reviews
function getReviews($pdo) {
    try {
        $query = "SELECT customer_name, review_text, rating, created_at FROM reviews ORDER BY created_at DESC";
        $stmt = $pdo->query($query);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        echo "Error retrieving reviews: " . $e->getMessage();
        return [];
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Handle new review submission
    if (isset($_POST['customer_name'], $_POST['review_text'], $_POST['rating'])) {
        $customerName = htmlspecialchars($_POST['customer_name']);
        $reviewText = htmlspecialchars($_POST['review_text']);
        $rating = (int) $_POST['rating'];

        // Validate inputs
        if (!empty($customerName) && !empty($reviewText) && $rating >= 1 && $rating <= 5) {
            storeReview($pdo, $customerName, $reviewText, $rating);
        } else {
            echo "Invalid input data. Please ensure all fields are filled correctly.\n";
        }
    }
}

// Display all reviews (example output)
$reviews = getReviews($pdo);
foreach ($reviews as $review) {
    echo "Customer: " . $review['customer_name'] . "\n";
    echo "Review: " . $review['review_text'] . "\n";
    echo "Rating: " . $review['rating'] . "/5\n";
    echo "Date: " . $review['created_at'] . "\n";
    echo "--------------------\n";
}
?>
```
