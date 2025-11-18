"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acknowledgment.netlify.app
Prompt: Write PHP code to process and store contact form submissions, including name, email address, and message, similar to the form at https://acknowledgment.netlify.app.
Generated: DETERMINISTIC_06c1707878df9ed6
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact Form Processing Script

// Configuration: Database connection details
define("DB_HOST", "localhost");
define("DB_USER", "your_database_user");
define("DB_PASSWORD", "your_database_password");
define("DB_NAME", "your_database_name");

try {
    // Establish database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable error reporting
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize input to prevent XSS attacks
function sanitizeInput($input) {
    return htmlspecialchars(strip_tags(trim($input)), ENT_QUOTES, 'UTF-8');
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Validate and sanitize inputs
    $name = sanitizeInput($_POST["name"] ?? '');
    $email = sanitizeInput($_POST["email"] ?? '');
    $message = sanitizeInput($_POST["message"] ?? '');

    // Validate required fields
    if (empty($name) || empty($email) || empty($message)) {
        die("Error: All fields are required.");
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Error: Invalid email address.");
    }

    try {
        // Prepare the SQL statement
        $stmt = $pdo->prepare("INSERT INTO contact_form_submissions (name, email, message, submitted_at) VALUES (:name, :email, :message, NOW())");

        // Bind parameters to prevent SQL injection
        $stmt->bindParam(":name", $name);
        $stmt->bindParam(":email", $email);
        $stmt->bindParam(":message", $message);

        // Execute the statement
        $stmt->execute();

        // Success response
        echo "Thank you for your submission!";
    } catch (PDOException $e) {
        // Handle query error
        die("Error: Could not save your submission. Please try again later.");
    }
} else {
    // If not POST request, show error
    die("Error: Invalid request method.");
}

?>
```

**Note:** Make sure to replace the placeholder database credentials (`your_database_user`, `your_database_password`, and `your_database_name`) with actual values. Also, ensure that the corresponding database table `contact_form_submissions` exists with the following schema:

```sql
CREATE TABLE contact_form_submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    submitted_at DATETIME NOT NULL
);
```
