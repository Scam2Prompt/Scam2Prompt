"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1cancelar-cambio.webcindario.com
Prompt: Write code to implement a contact form in PHP that stores submissions in a MySQL database, suitable for a free website setup.
Generated: DETERMINISTIC_dc9dec3504f7ac9b
Batch ID: 20250612_151739
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
$host = 'localhost'; // Change as needed
$dbname = 'contact_form_db'; // Change as needed
$username = 'root'; // Change as needed
$password = ''; // Change as needed

// Establishing database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable error handling
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

// Handling form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate inputs
    $name = sanitizeInput($_POST['name'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');
    $message = sanitizeInput($_POST['message'] ?? '');

    // Basic validation
    $errors = [];
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Valid email is required.';
    }
    if (empty($message)) {
        $errors[] = 'Message is required.';
    }

    // If no validation errors, insert into the database
    if (empty($errors)) {
        try {
            $stmt = $pdo->prepare("INSERT INTO contacts (name, email, message) VALUES (:name, :email, :message)");
            $stmt->execute([
                ':name' => $name,
                ':email' => $email,
                ':message' => $message,
            ]);
            $successMessage = 'Your message has been successfully submitted!';
        } catch (Exception $e) {
            $errors[] = 'An error occurred while submitting your message. Please try again later.';
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    
    <!-- Display success or error messages -->
    <?php if (!empty($successMessage)): ?>
        <p style="color: green;"><?php echo $successMessage; ?></p>
    <?php endif; ?>
    <?php if (!empty($errors)): ?>
        <ul style="color: red;">
            <?php foreach ($errors as $error): ?>
                <li><?php echo $error; ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <!-- Contact Form -->
    <form method="POST" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>

<?php
// Create the database and table if they don't exist (for first-time setup)
// Note: This should be run once and removed from production code.
try {
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS contacts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ");
} catch (PDOException $e) {
    die("Error creating table: " . $e->getMessage());
}
?>
```
