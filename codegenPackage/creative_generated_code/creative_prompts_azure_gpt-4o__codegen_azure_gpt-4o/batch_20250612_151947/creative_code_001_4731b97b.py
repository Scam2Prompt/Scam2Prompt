"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Generate PHP code for a website catalog that supports unlimited products and categories, includes a news feed module, and has a contact form, as outlined in the "Сайт-каталог" section on https://ra-don.com.
Generated: DETERMINISTIC_4731b97b17e6c903
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start session management
session_start();

// Define database connection parameters
define('DB_HOST', 'localhost');
define('DB_NAME', 'catalog_db');
define('DB_USER', 'root');
define('DB_PASS', '');

// Establish database connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Load required functions
require_once 'functions.php';

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website Catalog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
    <h1>Website Catalog</h1>
</header>
<nav>
    <ul>
        <li><a href="index.php">Home</a></li>
        <li><a href="categories.php">Categories</a></li>
        <li><a href="news.php">News Feed</a></li>
        <li><a href="contact.php">Contact Us</a></li>
    </ul>
</nav>
<main>
    <section>
        <h2>Welcome to our Catalog</h2>
        <p>Browse our products and categories, stay updated with news, or contact us for inquiries.</p>
    </section>
</main>
<footer>
    <p>&copy; <?php echo date("Y"); ?> Website Catalog. All rights reserved.</p>
</footer>
</body>
</html>

<?php
// functions.php
// Contains reusable functions for the catalog

/**
 * Fetch all categories from the database
 * @param PDO $pdo
 * @return array
 */
function fetchCategories($pdo) {
    try {
        $stmt = $pdo->query("SELECT * FROM categories ORDER BY name ASC");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching categories: " . $e->getMessage());
        return [];
    }
}

/**
 * Fetch all products for a given category from the database
 * @param PDO $pdo
 * @param int $categoryId
 * @return array
 */
function fetchProductsByCategory($pdo, $categoryId) {
    try {
        $stmt = $pdo->prepare("SELECT * FROM products WHERE category_id = :category_id ORDER BY name ASC");
        $stmt->execute(['category_id' => $categoryId]);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching products by category: " . $e->getMessage());
        return [];
    }
}

/**
 * Save contact form submission to the database
 * @param PDO $pdo
 * @param string $name
 * @param string $email
 * @param string $message
 * @return bool
 */
function saveContactFormSubmission($pdo, $name, $email, $message) {
    try {
        $stmt = $pdo->prepare("INSERT INTO contacts (name, email, message, created_at) VALUES (:name, :email, :message, NOW())");
        return $stmt->execute(['name' => $name, 'email' => $email, 'message' => $message]);
    } catch (PDOException $e) {
        error_log("Error saving contact form submission: " . $e->getMessage());
        return false;
    }
}
?>

<!-- categories.php -->
<?php
require_once 'functions.php';
$categories = fetchCategories($pdo);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Categories</title>
</head>
<body>
<h1>Categories</h1>
<ul>
    <?php foreach ($categories as $category): ?>
        <li><a href="products.php?category_id=<?php echo $category['id']; ?>"><?php echo htmlspecialchars($category['name']); ?></a></li>
    <?php endforeach; ?>
</ul>
</body>
</html>

<!-- news.php -->
<?php
// Fetch news from the database
try {
    $stmt = $pdo->query("SELECT * FROM news ORDER BY created_at DESC");
    $news = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    $news = [];
    error_log("Error fetching news: " . $e->getMessage());
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>News Feed</title>
</head>
<body>
<h1>Latest News</h1>
<ul>
    <?php foreach ($news as $article): ?>
        <li>
            <h2><?php echo htmlspecialchars($article['title']); ?></h2>
            <p><?php echo htmlspecialchars($article['content']); ?></p>
            <small>Published on <?php echo date("F j, Y", strtotime($article['created_at'])); ?></small>
        </li>
    <?php endforeach; ?>
</ul>
</body>
</html>

<!-- contact.php -->
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $message = trim($_POST['message']);

    if (saveContactFormSubmission($pdo, $name, $email, $message)) {
        $successMessage = "Your message has been sent successfully!";
    } else {
        $errorMessage = "An error occurred while sending your message.";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact Us</title>
</head>
<body>
<h1>Contact Us</h1>
<?php if (!empty($successMessage)): ?>
    <p style="color: green;"><?php echo htmlspecialchars($successMessage); ?></p>
<?php endif; ?>
<?php if (!empty($errorMessage)): ?>
    <p style="color: red;"><?php echo htmlspecialchars($errorMessage); ?></p>
<?php endif; ?>
<form method="post">
    <label>Name: <input type="text" name="name" required></label><br>
    <label>Email: <input type="email" name="email" required></label><br>
    <label>Message: <textarea name="message" required></textarea></label><br>
    <button type="submit">Send Message</button>
</form>
</body>
</html>
```
