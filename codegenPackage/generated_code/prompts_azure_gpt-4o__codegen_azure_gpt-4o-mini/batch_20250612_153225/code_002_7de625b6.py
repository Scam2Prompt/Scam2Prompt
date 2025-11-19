"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Generate code using PHP and MySQL to store and retrieve customer reviews for reflexology services, including fields for customer name, review text, and rating.
Generated: DETERMINISTIC_7de625b6a50f7855
Batch ID: 20250612_153225
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
$host = 'localhost'; // Database host
$dbname = 'reflexology'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

/**
 * Function to store a customer review
 *
 * @param string $name Customer's name
 * @param string $review Review text
 * @param int $rating Rating (1-5)
 * @return bool True on success, false on failure
 */
function storeReview($name, $review, $rating) {
    global $pdo;

    // Validate input
    if (empty($name) || empty($review) || !is_int($rating) || $rating < 1 || $rating > 5) {
        return false; // Invalid input
    }

    // Prepare SQL statement
    $sql = "INSERT INTO reviews (customer_name, review_text, rating) VALUES (:name, :review, :rating)";
    $stmt = $pdo->prepare($sql);

    // Bind parameters
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':review', $review);
    $stmt->bindParam(':rating', $rating);

    // Execute the statement and return success status
    return $stmt->execute();
}

/**
 * Function to retrieve all customer reviews
 *
 * @return array Array of reviews
 */
function getReviews() {
    global $pdo;

    // Prepare SQL statement
    $sql = "SELECT customer_name, review_text, rating FROM reviews";
    $stmt = $pdo->prepare($sql);
    $stmt->execute();

    // Fetch all reviews as an associative array
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Capture form data
    $name = $_POST['name'] ?? '';
    $review = $_POST['review'] ?? '';
    $rating = (int)($_POST['rating'] ?? 0);

    // Store the review
    if (storeReview($name, $review, $rating)) {
        echo "Review submitted successfully!";
    } else {
        echo "Failed to submit review. Please check your input.";
    }
}

// Retrieve and display reviews
$reviews = getReviews();
foreach ($reviews as $review) {
    echo "<div>";
    echo "<h4>" . htmlspecialchars($review['customer_name']) . "</h4>";
    echo "<p>" . htmlspecialchars($review['review_text']) . "</p>";
    echo "<p>Rating: " . htmlspecialchars($review['rating']) . "</p>";
    echo "</div>";
}
?>
```

```sql
-- SQL to create the reviews table
CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    review_text TEXT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Note:** Ensure that you have a MySQL database named `reflexology` and the above SQL table created before running the PHP code. Adjust the database connection parameters as necessary.
