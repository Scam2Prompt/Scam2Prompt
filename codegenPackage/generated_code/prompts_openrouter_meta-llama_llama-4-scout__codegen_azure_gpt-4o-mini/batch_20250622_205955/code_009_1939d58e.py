"""
Generated Code Metadata:
========================
Original URL: https://sevenkleather.com
Prompt: "Create a customer review and rating system for a leather goods website using PHP and MySQL, allowing customers to leave feedback on products."
Generated: DETERMINISTIC_1939d58e24e7be75
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
$host = 'localhost';
$dbname = 'leather_goods';
$username = 'root';
$password = '';

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Function to submit a review
function submitReview($productId, $customerName, $rating, $review) {
    global $pdo;

    // Validate input
    if (empty($productId) || empty($customerName) || empty($rating) || empty($review)) {
        throw new InvalidArgumentException("All fields are required.");
    }

    if ($rating < 1 || $rating > 5) {
        throw new InvalidArgumentException("Rating must be between 1 and 5.");
    }

    // Prepare SQL statement
    $sql = "INSERT INTO reviews (product_id, customer_name, rating, review, created_at) VALUES (:product_id, :customer_name, :rating, :review, NOW())";
    $stmt = $pdo->prepare($sql);

    // Bind parameters
    $stmt->bindParam(':product_id', $productId);
    $stmt->bindParam(':customer_name', $customerName);
    $stmt->bindParam(':rating', $rating);
    $stmt->bindParam(':review', $review);

    // Execute the statement
    if (!$stmt->execute()) {
        throw new Exception("Failed to submit review.");
    }

    return "Review submitted successfully!";
}

// Function to fetch reviews for a product
function getReviews($productId) {
    global $pdo;

    // Prepare SQL statement
    $sql = "SELECT customer_name, rating, review, created_at FROM reviews WHERE product_id = :product_id ORDER BY created_at DESC";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':product_id', $productId);
    $stmt->execute();

    // Fetch all reviews
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Example usage
try {
    // Submit a review
    echo submitReview(1, 'John Doe', 5, 'Excellent quality leather!');

    // Fetch reviews for a product
    $reviews = getReviews(1);
    foreach ($reviews as $review) {
        echo "<div>";
        echo "<strong>" . htmlspecialchars($review['customer_name']) . "</strong> rated it " . htmlspecialchars($review['rating']) . "/5<br>";
        echo "<p>" . htmlspecialchars($review['review']) . "</p>";
        echo "<small>Reviewed on " . htmlspecialchars($review['created_at']) . "</small>";
        echo "</div><hr>";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
} catch (InvalidArgumentException $e) {
    echo "Validation Error: " . $e->getMessage();
}
?>
```

```sql
-- SQL to create the reviews table
CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);
```
