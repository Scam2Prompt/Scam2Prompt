"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Write PHP code to implement an appointment booking system for a reflexology and massage therapy service, including features for selecting specific services like foot reflexology, body massage, and ear candling.
Generated: DETERMINISTIC_4c84380f9af5266b
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
// Appointment Booking System for Reflexology and Massage Therapy Service

// Initialize database connection (Replace with your DB credentials)
$host = 'localhost';
$db_name = 'appointment_booking';
$db_user = 'root';
$db_password = '';
$dsn = "mysql:host=$host;dbname=$db_name;charset=utf8";

try {
    $pdo = new PDO($dsn, $db_user, $db_password, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to sanitize user input
 * @param string $data User input to sanitize
 * @return string Sanitized input
 */
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

// Handle booking submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize user inputs
    $name = sanitizeInput($_POST['name']);
    $email = sanitizeInput($_POST['email']);
    $phone = sanitizeInput($_POST['phone']);
    $service = sanitizeInput($_POST['service']);
    $appointment_date = sanitizeInput($_POST['appointment_date']);
    $appointment_time = sanitizeInput($_POST['appointment_time']);

    // Validate input fields
    if (empty($name) || empty($email) || empty($phone) || empty($service) || empty($appointment_date) || empty($appointment_time)) {
        $error_message = "All fields are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error_message = "Invalid email format.";
    } else {
        // Insert booking into the database
        try {
            $sql = "INSERT INTO bookings (name, email, phone, service, appointment_date, appointment_time) 
                    VALUES (:name, :email, :phone, :service, :appointment_date, :appointment_time)";
            $stmt = $pdo->prepare($sql);
            $stmt->execute([
                ':name' => $name,
                ':email' => $email,
                ':phone' => $phone,
                ':service' => $service,
                ':appointment_date' => $appointment_date,
                ':appointment_time' => $appointment_time,
            ]);
            $success_message = "Appointment booked successfully!";
        } catch (PDOException $e) {
            $error_message = "Failed to book appointment: " . $e->getMessage();
        }
    }
}

// Fetch available services from the database
try {
    $services = $pdo->query("SELECT id, name FROM services")->fetchAll();
} catch (PDOException $e) {
    die("Failed to fetch services: " . $e->getMessage());
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Appointment Booking</title>
</head>
<body>
    <h1>Book an Appointment</h1>
    
    <!-- Display messages -->
    <?php if (!empty($success_message)): ?>
        <p style="color: green;"><?php echo $success_message; ?></p>
    <?php elseif (!empty($error_message)): ?>
        <p style="color: red;"><?php echo $error_message; ?></p>
    <?php endif; ?>

    <!-- Booking Form -->
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required><br><br>

        <label for="service">Select Service:</label>
        <select id="service" name="service" required>
            <option value="">--Select Service--</option>
            <?php foreach ($services as $service): ?>
                <option value="<?php echo $service['id']; ?>"><?php echo $service['name']; ?></option>
            <?php endforeach; ?>
        </select><br><br>

        <label for="appointment_date">Appointment Date:</label>
        <input type="date" id="appointment_date" name="appointment_date" required><br><br>

        <label for="appointment_time">Appointment Time:</label>
        <input type="time" id="appointment_time" name="appointment_time" required><br><br>

        <button type="submit">Book Appointment</button>
    </form>
</body>
</html>
```
