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

// Configuration
$dbHost = 'localhost';
$dbUsername = 'your_username';
$dbPassword = 'your_password';
$dbName = 'ritual_bookings';

// Establish database connection
try {
    $pdo = new PDO("mysql:host=$dbHost;dbname=$dbName", $dbUsername, $dbPassword);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}

// Define services
$services = [
    1 => "Ritual Consultation",
    2 => "Spiritual Healing",
    3 => "Astrology Reading",
];

// Function to display services
function displayServices($services) {
    echo "Available Services:\n";
    foreach ($services as $id => $service) {
        echo "$id. $service\n";
    }
}

// Function to book appointment
function bookAppointment($pdo, $services) {
    displayServices($services);
    
    // Get client input
    echo "Enter service ID: ";
    $serviceId = (int) trim(fgets(STDIN));
    
    if (!isset($services[$serviceId])) {
        echo "Invalid service ID.\n";
        return;
    }
    
    echo "Enter client name: ";
    $clientName = trim(fgets(STDIN));
    
    echo "Enter appointment date (YYYY-MM-DD): ";
    $appointmentDate = trim(fgets(STDIN));
    
    echo "Enter appointment time (HH:MM): ";
    $appointmentTime = trim(fgets(STDIN));
    
    try {
        $stmt = $pdo->prepare("INSERT INTO bookings (service_id, client_name, appointment_date, appointment_time) VALUES (:serviceId, :clientName, :appointmentDate, :appointmentTime)");
        $stmt->execute([
            'serviceId' => $serviceId,
            'clientName' => $clientName,
            'appointmentDate' => $appointmentDate,
            'appointmentTime' => $appointmentTime,
        ]);
        
        echo "Booking successful!\n";
    } catch (PDOException $e) {
        echo "Booking failed: " . $e->getMessage() . "\n";
    }
}

// Function to view bookings
function viewBookings($pdo) {
    try {
        $stmt = $pdo->prepare("SELECT * FROM bookings");
        $stmt->execute();
        $bookings = $stmt->fetchAll(PDO::FETCH_ASSOC);
        
        if (empty($bookings)) {
            echo "No bookings found.\n";
            return;
        }
        
        echo "Bookings:\n";
        foreach ($bookings as $booking) {
            echo "{$booking['id']}. Service ID: {$booking['service_id']}, Client: {$booking['client_name']}, Date: {$booking['appointment_date']}, Time: {$booking['appointment_time']}\n";
        }
    } catch (PDOException $e) {
        echo "Failed to retrieve bookings: " . $e->getMessage() . "\n";
    }
}

// Main program
function main($pdo, $services) {
    while (true) {
        echo "Ritual Booking System\n";
        echo "1. Book Appointment\n";
        echo "2. View Bookings\n";
        echo "3. Exit\n";
        echo "Choose an option: ";
        
        $option = (int) trim(fgets(STDIN));
        
        switch ($option) {
            case 1:
                bookAppointment($pdo, $services);
                break;
            case 2:
                viewBookings($pdo);
                break;
            case 3:
                echo "Exiting...\n";
                return;
            default:
                echo "Invalid option. Please choose a valid option.\n";
        }
    }
}

// Create bookings table if it doesn't exist
try {
    $pdo->exec("CREATE TABLE IF NOT EXISTS bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        service_id INT,
        client_name VARCHAR(255),
        appointment_date DATE,
        appointment_time TIME
    )");
} catch (PDOException $e) {
    echo "Failed to create bookings table: " . $e->getMessage() . "\n";
}

main($pdo, $services);

$pdo = null;
```
