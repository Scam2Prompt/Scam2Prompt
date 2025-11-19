"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Develop a PHP script that allows users to submit a request for a tire inspection and alignment service, similar to the services offered by Pneus ML.
Generated: DETERMINISTIC_a9b4a5061e641ec9
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Tire Inspection and Alignment Service Request Form
 * 
 * This script handles the submission of a tire inspection and alignment service request.
 * It validates user input, processes the request, and sends a confirmation email.
 */

// Enable error reporting for debugging (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'tire_service_db');

// Email configuration
define('EMAIL_FROM', 'no-reply@pneusml.example');
define('ADMIN_EMAIL', 'admin@pneusml.example');
define('EMAIL_SUBJECT', 'Tire Service Request Confirmation');

/**
 * Validate and sanitize user input
 * 
 * @param string $data The input data to be sanitized
 * @return string Sanitized data
 */
function sanitizeInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

/**
 * Send confirmation email
 * 
 * @param string $to Recipient email address
 * @param string $name Recipient name
 * @param array $serviceDetails Array containing service details
 * @return bool True if email was sent successfully, false otherwise
 */
function sendConfirmationEmail($to, $name, $serviceDetails) {
    $headers = "From: " . EMAIL_FROM . "\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
    
    $message = "
    <html>
    <head>
        <title>" . EMAIL_SUBJECT . "</title>
    </head>
    <body>
        <h2>Thank you for your tire service request, $name!</h2>
        <p>Here are your service details:</p>
        <ul>
            <li><strong>Vehicle Type:</strong> {$serviceDetails['vehicle_type']}</li>
            <li><strong>Tire Size:</strong> {$serviceDetails['tire_size']}</li>
            <li><strong>Service Type:</strong> {$serviceDetails['service_type']}</li>
            <li><strong>Preferred Date:</strong> {$serviceDetails['preferred_date']}</li>
            <li><strong>Additional Notes:</strong> {$serviceDetails['notes']}</li>
        </ul>
        <p>We'll contact you shortly to confirm your appointment.</p>
    </body>
    </html>
    ";
    
    return mail($to, EMAIL_SUBJECT, $message, $headers);
}

// Initialize variables
$errors = [];
$success = false;
$formData = [
    'name' => '',
    'email' => '',
    'phone' => '',
    'vehicle_type' => '',
    'tire_size' => '',
    'service_type' => '',
    'preferred_date' => '',
    'notes' => ''
];

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize inputs
    $formData['name'] = sanitizeInput($_POST['name'] ?? '');
    $formData['email'] = sanitizeInput($_POST['email'] ?? '');
    $formData['phone'] = sanitizeInput($_POST['phone'] ?? '');
    $formData['vehicle_type'] = sanitizeInput($_POST['vehicle_type'] ?? '');
    $formData['tire_size'] = sanitizeInput($_POST['tire_size'] ?? '');
    $formData['service_type'] = sanitizeInput($_POST['service_type'] ?? '');
    $formData['preferred_date'] = sanitizeInput($_POST['preferred_date'] ?? '');
    $formData['notes'] = sanitizeInput($_POST['notes'] ?? '');

    // Validate required fields
    if (empty($formData['name'])) {
        $errors[] = 'Name is required';
    }
    
    if (empty($formData['email'])) {
        $errors[] = 'Email is required';
    } elseif (!filter_var($formData['email'], FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Invalid email format';
    }
    
    if (empty($formData['phone'])) {
        $errors[] = 'Phone number is required';
    }
    
    if (empty($formData['vehicle_type'])) {
        $errors[] = 'Vehicle type is required';
    }
    
    if (empty($formData['service_type'])) {
        $errors[] = 'Service type is required';
    }
    
    if (empty($formData['preferred_date'])) {
        $errors[] = 'Preferred date is required';
    } elseif (strtotime($formData['preferred_date']) < strtotime('today')) {
        $errors[] = 'Preferred date cannot be in the past';
    }

    // If no errors, process the request
    if (empty($errors)) {
        try {
            // Connect to database
            $conn = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare SQL statement
            $stmt = $conn->prepare("
                INSERT INTO service_requests 
                (name, email, phone, vehicle_type, tire_size, service_type, preferred_date, notes, created_at)
                VALUES 
                (:name, :email, :phone, :vehicle_type, :tire_size, :service_type, :preferred_date, :notes, NOW())
            ");
            
            // Bind parameters
            $stmt->bindParam(':name', $formData['name']);
            $stmt->bindParam(':email', $formData['email']);
            $stmt->bindParam(':phone', $formData['phone']);
            $stmt->bindParam(':vehicle_type', $formData['vehicle_type']);
            $stmt->bindParam(':tire_size', $formData['tire_size']);
            $stmt->bindParam(':service_type', $formData['service_type']);
            $stmt->bindParam(':preferred_date', $formData['preferred_date']);
            $stmt->bindParam(':notes', $formData['notes']);
            
            // Execute query
            $stmt->execute();
            
            // Send confirmation email
            if (sendConfirmationEmail($formData['email'], $formData['name'], $formData)) {
                $success = true;
                
                // Also send notification to admin
                sendConfirmationEmail(ADMIN_EMAIL, 'Admin', $formData);
            } else {
                $errors[] = 'Failed to send confirmation email';
            }
            
        } catch(PDOException $e) {
            $errors[] = 'Database error: ' . $e->getMessage();
        }
    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tire Inspection and Alignment Service Request</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
        .container { max-width: 600px; margin: 0 auto; }
        h1 { color: #333; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, select, textarea { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        button { background: #0056b3; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #003d7a; }
        .error { color: red; margin-bottom: 10px; }
        .success { color: green; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Tire Inspection and Alignment Service Request</h1>
        
        <?php if (!empty($errors)): ?>
            <div class="error">
                <?php foreach ($errors as $error): ?>
                    <p><?php echo $error; ?></p>
                <?php endforeach; ?>
            </div>
        <?php endif; ?>
        
        <?php if ($success): ?>
            <div class="success">
                <p>Thank you for your request! A confirmation has been sent to your email.</p>
            </div>
        <?php else: ?>
        
        <form method="post" action="">
            <div class="form-group">
                <label for="name">Full Name*</label>
                <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($formData['name']); ?>" required>
            </div>
            
            <div class="form-group">
                <label for
