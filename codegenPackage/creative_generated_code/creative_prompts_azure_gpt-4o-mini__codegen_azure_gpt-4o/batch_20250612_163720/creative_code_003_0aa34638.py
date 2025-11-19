"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Develop a PHP script that retrieves available times for ecoendoscopia appointments from a database and displays them to the user.
Generated: DETERMINISTIC_0aa3463824e29b87
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// ecoendoscopy-appointments.php

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'medical_appointments');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');

// Function to connect to the database
function connectToDatabase() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8";
        $pdo = new PDO($dsn, DB_USER, DB_PASSWORD, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
        ]);
        return $pdo;
    } catch (PDOException $e) {
        // Log error in production (replace 'error_log' with actual logging mechanism if necessary)
        error_log("Database connection failed: " . $e->getMessage());
        die("Database connection error. Please try again later.");
    }
}

// Function to fetch available appointment times from the database
function getAvailableAppointments() {
    try {
        $pdo = connectToDatabase();
        $query = "SELECT appointment_date, appointment_time FROM appointments WHERE appointment_type = 'ecoendoscopia' AND is_available = 1 ORDER BY appointment_date, appointment_time";
        $stmt = $pdo->prepare($query);
        $stmt->execute();
        return $stmt->fetchAll(); // Return all available appointments
    } catch (Exception $e) {
        // Log error in production
        error_log("Failed to retrieve appointments: " . $e->getMessage());
        return [];
    }
}

// Fetch available appointments
$appointments = getAvailableAppointments();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Available Ecoendoscopia Appointments</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 50%;
            margin: auto;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: center;
            border: 1px solid #ddd;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center;">Available Ecoendoscopia Appointments</h1>
    <?php if (!empty($appointments)): ?>
        <table>
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Time</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($appointments as $appointment): ?>
                    <tr>
                        <td><?= htmlspecialchars($appointment['appointment_date']) ?></td>
                        <td><?= htmlspecialchars($appointment['appointment_time']) ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php else: ?>
        <p style="text-align: center;">No available appointments at the moment.</p>
    <?php endif; ?>
</body>
</html>
```
