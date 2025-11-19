"""
Generated Code Metadata:
========================
Original URL: https://amici.nz
Prompt: Create a PHP code snippet that allows users to reserve a table at Amici Italian Cafe, including form validation for contact details.
Generated: DETERMINISTIC_f6fd9589fdcf565d
Batch ID: 20250612_155233
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
define('DB_NAME', 'amici_cafe');

// Establish database connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Initialize variables
$errors = [];
$success = false;
$name = $email = $phone = $date = $time = $guests = $specialRequests = '';

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize inputs
    $name = trim(filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING));
    $email = trim(filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL));
    $phone = trim(filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING));
    $date = trim(filter_input(INPUT_POST, 'date', FILTER_SANITIZE_STRING));
    $time = trim(filter_input(INPUT_POST, 'time', FILTER_SANITIZE_STRING));
    $guests = trim(filter_input(INPUT_POST, 'guests', FILTER_SANITIZE_NUMBER_INT));
    $specialRequests = trim(filter_input(INPUT_POST, 'special_requests', FILTER_SANITIZE_STRING));

    // Validate inputs
    if (empty($name)) {
        $errors['name'] = 'Please enter your name';
    }

    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = 'Please enter a valid email address';
    }

    if (empty($phone) || !preg_match('/^[\d\s\-\(\)]{10,15}$/', $phone)) {
        $errors['phone'] = 'Please enter a valid phone number';
    }

    if (empty($date) || !strtotime($date)) {
        $errors['date'] = 'Please select a valid date';
    }

    if (empty($time) || !preg_match('/^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/', $time)) {
        $errors['time'] = 'Please select a valid time';
    }

    if (empty($guests) || $guests < 1 || $guests > 20) {
        $errors['guests'] = 'Please enter a number between 1 and 20';
    }

    // If no errors, proceed with reservation
    if (empty($errors)) {
        try {
            $stmt = $pdo->prepare("INSERT INTO reservations 
                (name, email, phone, date, time, guests, special_requests, created_at) 
                VALUES (?, ?, ?, ?, ?, ?, ?, NOW())");
            
            $stmt->execute([$name, $email, $phone, $date, $time, $guests, $specialRequests]);
            
            $success = true;
            // Clear form fields after successful submission
            $name = $email = $phone = $date = $time = $guests = $specialRequests = '';
        } catch (PDOException $e) {
            $errors['database'] = 'Error saving reservation: ' . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amici Italian Cafe - Table Reservation</title>
    <style>
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <h1>Reserve a Table at Amici Italian Cafe</h1>
    
    <?php if ($success): ?>
        <p class="success">Thank you! Your reservation has been confirmed. We look forward to serving you.</p>
    <?php endif; ?>
    
    <?php if (isset($errors['database'])): ?>
        <p class="error"><?php echo htmlspecialchars($errors['database']); ?></p>
    <?php endif; ?>
    
    <form method="post" action="">
        <div>
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($name); ?>" required>
            <?php if (isset($errors['name'])): ?>
                <span class="error"><?php echo htmlspecialchars($errors['name']); ?></span>
            <?php endif; ?>
        </div>
        
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="<?php echo htmlspecialchars($email); ?>" required>
            <?php if (isset($errors['email'])): ?>
                <span class="error"><?php echo htmlspecialchars($errors['email']); ?></span>
            <?php endif; ?>
        </div>
        
        <div>
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" value="<?php echo htmlspecialchars($phone); ?>" required>
            <?php if (isset($errors['phone'])): ?>
                <span class="error"><?php echo htmlspecialchars($errors['phone']); ?></span>
            <?php endif; ?>
        </div>
        
        <div>
            <label for="date">Date:</label>
            <input type="date" id="date" name="date" value="<?php echo htmlspecialchars($date); ?>" required>
            <?php if (isset($errors['date'])): ?>
                <span class="error"><?php echo htmlspecialchars($errors['date']); ?></span>
            <?php endif; ?>
        </div>
        
        <div>
            <label for="time">Time:</label>
            <input type="time" id="time" name="time" min="11:00" max="22:00" value="<?php echo htmlspecialchars($time); ?>" required>
            <?php if (isset($errors['time'])): ?>
                <span class="error"><?php echo htmlspecialchars($errors['time']); ?></span>
            <?php endif; ?>
        </div>
        
        <div>
            <label for="guests">Number of Guests (1-20):</label>
            <input type="number" id="guests" name="guests" min="1" max="20" value="<?php echo htmlspecialchars($guests); ?>" required>
            <?php if (isset($errors['guests'])): ?>
                <span class="error"><?php echo htmlspecialchars($errors['guests']); ?></span>
            <?php endif; ?>
        </div>
        
        <div>
            <label for="special_requests">Special Requests:</label>
            <textarea id="special_requests" name="special_requests"><?php echo htmlspecialchars($specialRequests); ?></textarea>
        </div>
        
        <button type="submit">Reserve Table</button>
    </form>
</body>
</html>
```
