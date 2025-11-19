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
// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'faq_database');

// Establish database connection
try {
    $pdo = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Create FAQ table if it doesn't exist
$createTableQuery = "CREATE TABLE IF NOT EXISTS faqs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question VARCHAR(255) NOT NULL,
    answer TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)";
$pdo->exec($createTableQuery);

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['add_faq'])) {
        $question = trim($_POST['question']);
        $answer = trim($_POST['answer']);
        
        if (!empty($question) && !empty($answer)) {
            try {
                $stmt = $pdo->prepare("INSERT INTO faqs (question, answer) VALUES (?, ?)");
                $stmt->execute([$question, $answer]);
                $success = "FAQ added successfully!";
            } catch (PDOException $e) {
                $error = "Error adding FAQ: " . $e->getMessage();
            }
        } else {
            $error = "Both question and answer are required!";
        }
    } elseif (isset($_POST['update_faq'])) {
        $id = (int)$_POST['id'];
        $question = trim($_POST['question']);
        $answer = trim($_POST['answer']);
        
        if (!empty($question) && !empty($answer) && $id > 0) {
            try {
                $stmt = $pdo->prepare("UPDATE faqs SET question = ?, answer = ? WHERE id = ?");
                $stmt->execute([$question, $answer, $id]);
                $success = "FAQ updated successfully!";
            } catch (PDOException $e) {
                $error = "Error updating FAQ: " . $e->getMessage();
            }
        } else {
            $error = "All fields are required!";
        }
    } elseif (isset($_POST['delete_faq'])) {
        $id = (int)$_POST['id'];
        
        if ($id > 0) {
            try {
                $stmt = $pdo->prepare("DELETE FROM faqs WHERE id = ?");
                $stmt->execute([$id]);
                $success = "FAQ deleted successfully!";
            } catch (PDOException $e) {
                $error = "Error deleting FAQ: " . $e->getMessage();
            }
        }
    }
}

// Fetch all FAQs
$faqs = [];
try {
    $stmt = $pdo->query("SELECT * FROM faqs ORDER BY created_at DESC");
    $faqs = $stmt->fetchAll();
} catch (PDOException $e) {
    $error = "Error fetching FAQs: " . $e->getMessage();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQ Management</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .faq-item { margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
        .success { color: green; background: #e6ffe6; padding: 10px; border-radius: 5px; }
        .error { color: red; background: #ffebeb; padding: 10px; border-radius: 5px; }
        form { margin-bottom: 20px; }
        textarea { width: 100%; min-height: 100px; }
    </style>
</head>
<body>
    <h1>FAQ Management</h1>
    
    <?php if (isset($success)): ?>
        <div class="success"><?php echo htmlspecialchars($success); ?></div>
    <?php endif; ?>
    
    <?php if (isset($error)): ?>
        <div class="error"><?php echo htmlspecialchars($error); ?></div>
    <?php endif; ?>
    
    <h2>Add New FAQ</h2>
    <form method="POST">
        <div>
            <label for="question">Question:</label>
            <input type="text" id="question" name="question" required>
        </div>
        <div>
            <label for="answer">Answer:</label>
            <textarea id="answer" name="answer" required></textarea>
        </div>
        <button type="submit" name="add_faq">Add FAQ</button>
    </form>
    
    <h2>Existing FAQs</h2>
    <?php if (empty($faqs)): ?>
        <p>No FAQs found.</p>
    <?php else: ?>
        <?php foreach ($faqs as $faq): ?>
            <div class="faq-item">
                <form method="POST" style="float: right;">
                    <input type="hidden" name="id" value="<?php echo $faq['id']; ?>">
                    <button type="submit" name="delete_faq" onclick="return confirm('Are you sure?')">Delete</button>
                </form>
                <form method="POST">
                    <input type="hidden" name="id" value="<?php echo $faq['id']; ?>">
                    <div>
                        <label>Question:</label>
                        <input type="text" name="question" value="<?php echo htmlspecialchars($faq['question']); ?>" required>
                    </div>
                    <div>
                        <label>Answer:</label>
                        <textarea name="answer" required><?php echo htmlspecialchars($faq['answer']); ?></textarea>
                    </div>
                    <button type="submit" name="update_faq">Update</button>
                </form>
            </div>
        <?php endforeach; ?>
    <?php endif; ?>
</body>
</html>
```
