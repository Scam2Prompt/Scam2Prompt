"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Write PHP code to implement an appointment booking system for a reflexology and massage therapy service, including features for selecting specific services like foot reflexology, body massage, and ear candling.
Generated: DETERMINISTIC_4c84380f9af5266b
Batch ID: 20250612_153225
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
 * Appointment Booking System for Reflexology and Massage Therapy Services
 * 
 * Features:
 * - Select specific services (foot reflexology, body massage, ear candling)
 * - Book appointments with date/time selection
 * - Client information collection
 * - Basic validation and error handling
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'therapy_booking_system');

// Services offered
$services = [
    'foot_reflexology' => [
        'name' => 'Foot Reflexology',
        'duration' => 60,
        'price' => 50.00
    ],
    'body_massage' => [
        'name' => 'Body Massage',
        'duration' => 90,
        'price' => 80.00
    ],
    'ear_candling' => [
        'name' => 'Ear Candling',
        'duration' => 30,
        'price' => 35.00
    ]
];

// Establish database connection
function getDBConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}

// Create appointments table if not exists
function initializeDatabase() {
    $conn = getDBConnection();
    
    $sql = "CREATE TABLE IF NOT EXISTS appointments (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        client_name VARCHAR(100) NOT NULL,
        client_email VARCHAR(100) NOT NULL,
        client_phone VARCHAR(20) NOT NULL,
        service_type VARCHAR(50) NOT NULL,
        appointment_date DATETIME NOT NULL,
        duration INT(11) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";
    
    if (!$conn->query($sql)) {
        die("Error creating table: " . $conn->error);
    }
    
    $conn->close();
}

// Validate appointment data
function validateAppointmentData($data) {
    $errors = [];
    
    if (empty($data['client_name'])) {
        $errors[] = 'Client name is required';
    }
    
    if (empty($data['client_email']) || !filter_var($data['client_email'], FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Valid email is required';
    }
    
    if (empty($data['client_phone'])) {
        $errors[] = 'Phone number is required';
    }
    
    if (empty($data['service_type']) || !array_key_exists($data['service_type'], $GLOBALS['services'])) {
        $errors[] = 'Please select a valid service';
    }
    
    if (empty($data['appointment_date'])) {
        $errors[] = 'Appointment date is required';
    } else {
        $appointment_time = strtotime($data['appointment_date']);
        $current_time = time();
        
        if ($appointment_time < $current_time) {
            $errors[] = 'Appointment date cannot be in the past';
        }
    }
    
    return $errors;
}

// Save appointment to database
function saveAppointment($data) {
    global $services;
    
    $conn = getDBConnection();
    
    $service = $services[$data['service_type']];
    $appointment_date = date('Y-m-d H:i:s', strtotime($data['appointment_date']));
    
    $stmt = $conn->prepare("INSERT INTO appointments (
        client_name, client_email, client_phone, 
        service_type, appointment_date, duration, price, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
    
    $stmt->bind_param(
        "sssssids",
        $data['client_name'],
        $data['client_email'],
        $data['client_phone'],
        $data['service_type'],
        $appointment_date,
        $service['duration'],
        $service['price'],
        $data['notes']
    );
    
    $result = $stmt->execute();
    
    $stmt->close();
    $conn->close();
    
    return $result;
}

// Get all appointments
function getAllAppointments() {
    $conn = getDBConnection();
    
    $result = $conn->query("SELECT * FROM appointments ORDER BY appointment_date ASC");
    $appointments = [];
    
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $appointments[] = $row;
        }
    }
    
    $conn->close();
    return $appointments;
}

// Check for available time slots
function getAvailableTimeSlots($date) {
    // This is a simplified version - in production you'd want more complex logic
    $conn = getDBConnection();
    
    $date_start = date('Y-m-d 00:00:00', strtotime($date));
    $date_end = date('Y-m-d 23:59:59', strtotime($date));
    
    $stmt = $conn->prepare("SELECT appointment_date, duration FROM appointments 
                           WHERE appointment_date BETWEEN ? AND ?");
    $stmt->bind_param("ss", $date_start, $date_end);
    $stmt->execute();
    $result = $stmt->get_result();
    
    $booked_slots = [];
    while ($row = $result->fetch_assoc()) {
        $booked_slots[] = [
            'start' => strtotime($row['appointment_date']),
            'end' => strtotime($row['appointment_date']) + ($row['duration'] * 60)
        ];
    }
    
    $stmt->close();
    $conn->close();
    
    // Generate available time slots (every 30 minutes from 9AM to 6PM)
    $available_slots = [];
    $start_time = strtotime($date . ' 09:00:00');
    $end_time = strtotime($date . ' 18:00:00');
    
    for ($time = $start_time; $time <= $end_time - 1800; $time += 1800) {
        $slot_available = true;
        
        foreach ($booked_slots as $booked) {
            if (($time >= $booked['start'] && $time < $booked['end']) || 
                ($time + 1800 > $booked['start'] && $time + 1800 <= $booked['end'])) {
                $slot_available = false;
                break;
            }
        }
        
        if ($slot_available) {
            $available_slots[] = date('H:i', $time);
        }
    }
    
    return $available_slots;
}

// Initialize the database
initializeDatabase();

// Handle form submission
$errors = [];
$success = false;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $appointment_data = [
        'client_name' => trim($_POST['client_name'] ?? ''),
        'client_email' => trim($_POST['client_email'] ?? ''),
        'client_phone' => trim($_POST['client_phone'] ?? ''),
        'service_type' => $_POST['service_type'] ?? '',
        'appointment_date' => $_POST['appointment_date'] ?? '',
        'notes' => trim($_POST['notes'] ?? '')
    ];
    
    $errors = validateAppointmentData($appointment_data);
    
    if (empty($errors)) {
        if (saveAppointment($appointment_data)) {
            $success = true;
        } else {
            $errors[] = 'Failed to save appointment. Please try again.';
        }
    }
}

// Get available time slots for selected date
$available_slots = [];
if (!empty($_GET['date'])) {
    $available_slots = getAvailableTimeSlots($_GET['date']);
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Therapy Appointment Booking</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }
        .error { color: red; }
        .success { color: green; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input, select, textarea { width: 100%; padding: 8px; box-sizing: border-box; }
        button { background: #007bff; color: white; border: none; padding: 10px 15px; cursor: pointer; }
        button:hover { background: #0056b3; }
        .service-option { display: flex; margin-bottom: 10px; }
        .service-option input { width: auto; margin-right: 10px; }
        .service-details { flex:
