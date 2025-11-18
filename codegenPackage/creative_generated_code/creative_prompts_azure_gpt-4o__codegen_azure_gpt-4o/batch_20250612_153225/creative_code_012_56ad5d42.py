"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maraboutreconnu.com
Prompt: Write a PHP script to implement a "Contact Us" form that sends messages to "contact@maraboutreconnu.com" and logs inquiries in a MySQL database.
Generated: DETERMINISTIC_56ad5d4264d826c1
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
define('DB_HOST', 'localhost'); // Change as needed
define('DB_USER', 'your_db_user'); // Change as needed
define('DB_PASS', 'your_db_password'); // Change as needed
define('DB_NAME', 'your_database_name'); // Change as needed

// Recipient email configuration
define('RECIPIENT_EMAIL', 'contact@maraboutreconnu.com');

// Error reporting (disable in production if needed)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Helper function to sanitize user input
function sanitize_input($input) {
    return htmlspecialchars(strip_tags(trim($input)));
}

// Main script
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user inputs
    $name = sanitize_input($_POST['name'] ?? '');
    $email = sanitize_input($_POST['email'] ?? '');
    $message = sanitize_input($_POST['message'] ?? '');

    // Validate required fields
    if (empty($name) || empty($email) || empty($message)) {
        die(json_encode(['status' => 'error', 'message' => 'All fields are required.']));
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die(json_encode(['status' => 'error', 'message' => 'Invalid email format.']));
    }

    // Establish database connection
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($conn->connect_error) {
        die(json_encode(['status' => 'error', 'message' => 'Database connection failed: ' . $conn->connect_error]));
    }

    // SQL query to insert inquiry into database
    $query = $conn->prepare("INSERT INTO inquiries (name, email, message, submitted_at) VALUES (?, ?, ?, NOW())");
    $query->bind_param("sss", $name, $email, $message);

    if ($query->execute()) {
        // Send email to recipient
        $subject = "New Inquiry from $name";
        $emailMessage = "Name: $name\nEmail: $email\nMessage:\n$message";

        if (mail(RECIPIENT_EMAIL, $subject, $emailMessage)) {
            // Successful response
            echo json_encode(['status' => 'success', 'message' => 'Your inquiry has been sent successfully.']);
        } else {
            // Email sending failed
            echo json_encode(['status' => 'error', 'message' => 'Failed to send the email.']);
        }
    } else {
        // Database insertion failed
        echo json_encode(['status' => 'error', 'message' => 'Failed to log inquiry in the database.']);
    }

    // Close database connection
    $query->close();
    $conn->close();
} else {
    // Invalid request method
    echo json_encode(['status' => 'error', 'message' => 'Invalid request method.']);
}
?>
```

### Notes:
- Replace database credentials `DB_HOST`, `DB_USER`, `DB_PASS`, and `DB_NAME` with your actual MySQL database configuration.
- Ensure the `inquiries` table is created with the appropriate schema in your MySQL database:
    ```sql
    CREATE TABLE inquiries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        message TEXT NOT NULL,
        submitted_at DATETIME NOT NULL
    );
    ```
- This script assumes the form is submitting `POST` data with `name`, `email`, and `message` fields.
