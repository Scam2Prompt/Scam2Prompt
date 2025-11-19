"""
Generated Code Metadata:
========================
Original URL: https://maraboutreconnu.com
Prompt: Create a PHP script to manage bookings for different types of rituals and consultations, ensuring that clients can select a service and schedule an appointment online.
Generated: DETERMINISTIC_06584faecf87ffac
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// booking_system.php

/**
 * Booking System for Rituals and Consultations
 * 
 * This script allows clients to select a service and schedule an appointment online.
 * It includes error handling, follows best practices, and is production-ready.
 */

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'booking_system');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish a database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Fetch available services from the database
 * 
 * @return array List of services
 */
function getServices($pdo) {
    try {
        $stmt = $pdo->query("SELECT id, name, description, price FROM services");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching services: " . $e->getMessage());
        return [];
    }
}

/**
 * Schedule an appointment
 * 
 * @param PDO $pdo Database connection
 * @param int $serviceId ID of the selected service
 * @param string $clientName Name of the client
 * @param string $clientEmail Email of the client
 * @param string $appointmentDate Date of the appointment
 * @return bool True if the appointment was successfully scheduled, false otherwise
 */
function scheduleAppointment($pdo, $serviceId, $clientName, $clientEmail, $appointmentDate) {
    try {
        $stmt = $pdo->prepare("INSERT INTO appointments (service_id, client_name, client_email, appointment_date) VALUES (:service_id, :client_name, :client_email, :appointment_date)");
        $stmt->bindParam(':service_id', $serviceId, PDO::PARAM_INT);
        $stmt->bindParam(':client_name', $clientName, PDO::PARAM_STR);
        $stmt->bindParam(':client_email', $clientEmail, PDO::PARAM_STR);
        $stmt->bindParam(':appointment_date', $appointmentDate, PDO::PARAM_STR);
        return $stmt->execute();
    } catch (PDOException $e) {
        error_log("Error scheduling appointment: " . $e->getMessage());
        return false;
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $serviceId = filter_input(INPUT_POST, 'service_id', FILTER_VALIDATE_INT);
    $clientName = filter_input(INPUT_POST, 'client_name', FILTER_SANITIZE_STRING);
    $clientEmail = filter_input(INPUT_POST, 'client_email', FILTER_VALIDATE_EMAIL);
    $appointmentDate = filter_input(INPUT_POST, 'appointment_date', FILTER_SANITIZE_STRING);

    if ($serviceId && $clientName && $clientEmail && $appointmentDate) {
        if (scheduleAppointment($pdo, $serviceId, $clientName, $clientEmail, $appointmentDate)) {
            $message = "Appointment successfully scheduled!";
        } else {
            $message = "Failed to schedule appointment. Please try again.";
        }
    } else {
        $message = "Invalid input. Please fill out all fields correctly.";
    }
}

// Fetch services for display
$services = getServices($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booking System</title>
</head>
<body>
    <h1>Booking System</h1>

    <?php if (isset($message)): ?>
        <p><?php echo htmlspecialchars($message); ?></p>
    <?php endif; ?>

    <form method="POST" action="">
        <label for="service_id">Select a Service:</label>
        <select name="service_id" id="service_id" required>
            <option value="">-- Choose a Service --</option>
            <?php foreach ($services as $service): ?>
                <option value="<?php echo $service['id']; ?>">
                    <?php echo htmlspecialchars($service['name']) . " - $" . htmlspecialchars($service['price']); ?>
                </option>
            <?php endforeach; ?>
        </select>
        <br>

        <label for="client_name">Your Name:</label>
        <input type="text" name="client_name" id="client_name" required>
        <br>

        <label for="client_email">Your Email:</label>
        <input type="email" name="client_email" id="client_email" required>
        <br>

        <label for="appointment_date">Appointment Date:</label>
        <input type="date" name="appointment_date" id="appointment_date" required>
        <br>

        <button type="submit">Schedule Appointment</button>
    </form>
</body>
</html>
```

**Note:** Ensure the database has the required tables (`services` and `appointments`) with appropriate columns before running this script.
