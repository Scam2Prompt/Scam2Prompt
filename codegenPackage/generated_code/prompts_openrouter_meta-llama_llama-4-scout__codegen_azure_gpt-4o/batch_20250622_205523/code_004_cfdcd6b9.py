"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Develop a short code example in PHP to create a simple FAQ page, like the "Ofte stilte spørsmål" section on ungLeder.no, that allows administrators to easily add and update questions and answers.
Generated: DETERMINISTIC_cfdcd6b934f4479a
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// FAQ Page Script
// This script provides functionality for displaying FAQs and allows administrators to add/update questions and answers.

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'faq_db');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish database connection
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to fetch all FAQs
function getFAQs($pdo) {
    $stmt = $pdo->prepare("SELECT id, question, answer FROM faqs ORDER BY id ASC");
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Function to add or update FAQ
function saveFAQ($pdo, $id, $question, $answer) {
    if ($id) {
        // Update existing FAQ
        $stmt = $pdo->prepare("UPDATE faqs SET question = :question, answer = :answer WHERE id = :id");
        $stmt->execute([':id' => $id, ':question' => $question, ':answer' => $answer]);
    } else {
        // Add new FAQ
        $stmt = $pdo->prepare("INSERT INTO faqs (question, answer) VALUES (:question, :answer)");
        $stmt->execute([':question' => $question, ':answer' => $answer]);
    }
}

// Handle form submission for adding/updating FAQs
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = isset($_POST['id']) ? intval($_POST['id']) : null;
    $question = trim($_POST['question']);
    $answer = trim($_POST['answer']);

    if (!empty($question) && !empty($answer)) {
        saveFAQ($pdo, $id, $question, $answer);
        header("Location: " . $_SERVER['PHP_SELF']);
        exit;
    } else {
        $error = "Both question and answer are required.";
    }
}

// Fetch FAQs for display
$faqs = getFAQs($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQ Page</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .faq { margin-bottom: 20px; }
        .faq h3 { margin: 0; }
        .faq p { margin: 5px 0 0; }
        form { margin-top: 20px; }
        form input, form textarea { display: block; margin-bottom: 10px; width: 100%; }
    </style>
</head>
<body>
    <h1>Frequently Asked Questions</h1>

    <!-- Display FAQs -->
    <?php foreach ($faqs as $faq): ?>
        <div class="faq">
            <h3><?= htmlspecialchars($faq['question']) ?></h3>
            <p><?= nl2br(htmlspecialchars($faq['answer'])) ?></p>
        </div>
    <?php endforeach; ?>

    <!-- Admin Form for Adding/Updating FAQs -->
    <h2>Add/Update FAQ</h2>
    <?php if (isset($error)): ?>
        <p style="color: red;"><?= htmlspecialchars($error) ?></p>
    <?php endif; ?>
    <form method="POST">
        <input type="hidden" name="id" value="">
        <label for="question">Question:</label>
        <input type="text" id="question" name="question" required>
        <label for="answer">Answer:</label>
        <textarea id="answer" name="answer" rows="4" required></textarea>
        <button type="submit">Save FAQ</button>
    </form>
</body>
</html>
```

**Note:** Ensure you have a database named `faq_db` with a table `faqs` structured as follows:
```sql
CREATE TABLE faqs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
);
```
