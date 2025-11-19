"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: Write a PHP script to integrate a contact form for inquiries about aluminum windows, PVC termopanels, and security blinds, ensuring data validation for required fields like name, email, and phone number.
Generated: DETERMINISTIC_88a891ec44564f49
Batch ID: 20250612_145200
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
define('DB_NAME', 'database_name');

// Contact form configuration
define('REQUIRED_FIELDS', ['name', 'email', 'phone', 'product_type', 'message']);
define('VALID_PRODUCT_TYPES', ['aluminum_windows', 'pvc_termopanels', 'security_blinds']);

// Error and success messages
$errors = [];
$success = false;

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $product_type = filter_input(INPUT_POST, 'product_type', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate required fields
    foreach (REQUIRED_FIELDS as $field) {
        if (empty($_POST[$field])) {
            $errors[$field] = "This field is required.";
        }
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Please enter a valid email address.";
    }

    // Validate phone number (basic validation)
    if (!preg_match('/^[0-9\s\+\-\(\)]{10,20}$/', $phone)) {
        $errors['phone'] = "Please enter a valid phone number.";
    }

    // Validate product type
    if (!in_array($product_type, VALID_PRODUCT_TYPES)) {
        $errors['product_type'] = "Please select a valid product type.";
    }

    // If no errors, proceed with database insertion
    if (empty($errors)) {
        try {
            $conn = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            $stmt = $conn->prepare("INSERT INTO inquiries (name, email, phone, product_type, message, created_at) 
                                   VALUES (:name, :email, :phone, :product_type, :message, NOW())");
            
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':phone', $phone);
            $stmt->bindParam(':product_type', $product_type);
            $stmt->bindParam(':message', $message);
            
            $stmt->execute();
            $success = true;
        } catch(PDOException $e) {
            $errors['database'] = "There was an error submitting your inquiry. Please try again later.";
            error_log("Database error: " . $e->getMessage());
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Window Products Inquiry</title>
    <style>
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <h1>Product Inquiry Form</h1>
    
    <?php if ($success): ?>
        <p class="success">Thank you for your inquiry! We'll contact you shortly.</p>
    <?php else: ?>
        <?php if (!empty($errors['database'])): ?>
            <p class="error"><?php echo htmlspecialchars($errors['database']); ?></p>
        <?php endif; ?>

        <form method="post" action="">
            <div>
                <label for="name">Name*:</label>
                <input type="text" id="name" name="name" value="<?php echo isset($name) ? htmlspecialchars($name) : ''; ?>">
                <?php if (!empty($errors['name'])): ?>
                    <span class="error"><?php echo htmlspecialchars($errors['name']); ?></span>
                <?php endif; ?>
            </div>

            <div>
                <label for="email">Email*:</label>
                <input type="email" id="email" name="email" value="<?php echo isset($email) ? htmlspecialchars($email) : ''; ?>">
                <?php if (!empty($errors['email'])): ?>
                    <span class="error"><?php echo htmlspecialchars($errors['email']); ?></span>
                <?php endif; ?>
            </div>

            <div>
                <label for="phone">Phone*:</label>
                <input type="tel" id="phone" name="phone" value="<?php echo isset($phone) ? htmlspecialchars($phone) : ''; ?>">
                <?php if (!empty($errors['phone'])): ?>
                    <span class="error"><?php echo htmlspecialchars($errors['phone']); ?></span>
                <?php endif; ?>
            </div>

            <div>
                <label for="product_type">Product Type*:</label>
                <select id="product_type" name="product_type">
                    <option value="">Select a product</option>
                    <option value="aluminum_windows" <?php echo (isset($product_type) && $product_type === 'aluminum_windows') ? 'selected' : ''; ?>>Aluminum Windows</option>
                    <option value="pvc_termopanels" <?php echo (isset($product_type) && $product_type === 'pvc_termopanels') ? 'selected' : ''; ?>>PVC Termopanels</option>
                    <option value="security_blinds" <?php echo (isset($product_type) && $product_type === 'security_blinds') ? 'selected' : ''; ?>>Security Blinds</option>
                </select>
                <?php if (!empty($errors['product_type'])): ?>
                    <span class="error"><?php echo htmlspecialchars($errors['product_type']); ?></span>
                <?php endif; ?>
            </div>

            <div>
                <label for="message">Message*:</label>
                <textarea id="message" name="message"><?php echo isset($message) ? htmlspecialchars($message) : ''; ?></textarea>
                <?php if (!empty($errors['message'])): ?>
                    <span class="error"><?php echo htmlspecialchars($errors['message']); ?></span>
                <?php endif; ?>
            </div>

            <button type="submit">Submit Inquiry</button>
        </form>
    <?php endif; ?>
</body>
</html>
```
