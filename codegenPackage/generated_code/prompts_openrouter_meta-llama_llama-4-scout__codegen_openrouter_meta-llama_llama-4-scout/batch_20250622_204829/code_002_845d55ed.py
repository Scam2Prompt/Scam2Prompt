"""
Generated Code Metadata:
========================
Original URL: https://mstoolsnetshop.com
Prompt: Generate a simple PHP script for a courier management system with email notifications, similar to the Courier Management System Php Script.
Generated: DETERMINISTIC_845d55ed24bb4d65
Batch ID: 20250622_204829
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
 * Courier Management System with Email Notifications
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'courier_management',
    'admin_email' => 'admin@example.com',
    'smtp_host' => 'smtp.gmail.com',
    'smtp_port' => 587,
    'smtp_username' => 'your_smtp_username',
    'smtp_password' => 'your_smtp_password',
];

// Database Connection
try {
    $conn = new PDO("mysql:host={$config['db_host']};dbname={$config['db_name']}", $config['db_username'], $config['db_password']);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Error: " . $e->getMessage());
}

// Function to send email notifications
function sendEmail($to, $subject, $message) {
    global $config;
    $headers = "MIME-Version: 1.0\r\n";
    $headers .= "Content-type: text/html; charset=iso-8859-1\r\n";
    $headers .= "From: {$config['admin_email']}\r\n";
    $headers .= "Reply-To: {$config['admin_email']}\r\n";

    $smtp = new PHPMailer(true);
    try {
        $smtp->isSMTP();
        $smtp->Host = $config['smtp_host'];
        $smtp->Port = $config['smtp_port'];
        $smtp->SMTPAuth = true;
        $smtp->Username = $config['smtp_username'];
        $smtp->Password = $config['smtp_password'];
        $smtp->SMTPSecure = 'tls';
        $smtp->setFrom($config['admin_email']);
        $smtp->addAddress($to);
        $smtp->isHTML(true);
        $smtp->Subject = $subject;
        $smtp->Body = $message;
        $smtp->send();
    } catch (Exception $e) {
        echo "Error sending email: " . $e->getMessage();
    }
}

// Function to add new courier
function addCourier($name, $email, $phone) {
    global $conn;
    $query = $conn->prepare("INSERT INTO couriers (name, email, phone) VALUES (:name, :email, :phone)");
    $query->bindParam(':name', $name);
    $query->bindParam(':email', $email);
    $query->bindParam(':phone', $phone);
    try {
        $query->execute();
        sendEmail($email, "Welcome to Courier Management System", "Dear $name, you have been added as a courier.");
    } catch (PDOException $e) {
        echo "Error adding courier: " . $e->getMessage();
    }
}

// Function to view all couriers
function viewCouriers() {
    global $conn;
    $query = $conn->prepare("SELECT * FROM couriers");
    try {
        $query->execute();
        return $query->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        echo "Error viewing couriers: " . $e->getMessage();
    }
}

// Function to update courier status
function updateCourierStatus($id, $status) {
    global $conn;
    $query = $conn->prepare("UPDATE couriers SET status = :status WHERE id = :id");
    $query->bindParam(':status', $status);
    $query->bindParam(':id', $id);
    try {
        $query->execute();
        $query = $conn->prepare("SELECT email, name FROM couriers WHERE id = :id");
        $query->bindParam(':id', $id);
        $query->execute();
        $courier = $query->fetch(PDO::FETCH_ASSOC);
        sendEmail($courier['email'], "Courier Status Update", "Dear {$courier['name']}, your status has been updated to $status.");
    } catch (PDOException $e) {
        echo "Error updating courier status: " . $e->getMessage();
    }
}

// Create table if not exists
$conn->exec("CREATE TABLE IF NOT EXISTS couriers (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active'
)");

// Test the functions
if (isset($_POST['add_courier'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    addCourier($name, $email, $phone);
}

if (isset($_POST['view_couriers'])) {
    $couriers = viewCouriers();
    print_r($couriers);
}

if (isset($_POST['update_status'])) {
    $id = $_POST['id'];
    $status = $_POST['status'];
    updateCourierStatus($id, $status);
}

// Include PHPMailer for email functionality
require 'vendor/autoload.php';
use PHPMailer\PHPMailer\PHPMailer;

?>
```

```html
<!-- Example usage form -->
<form action="" method="post">
    <h2>Add Courier</h2>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="phone">Phone:</label>
    <input type="text" id="phone" name="phone"><br><br>
    <input type="submit" name="add_courier" value="Add Courier">
</form>

<form action="" method="post">
    <h2>View Couriers</h2>
    <input type="submit" name="view_couriers" value="View Couriers">
</form>

<form action="" method="post">
    <h2>Update Courier Status</h2>
    <label for="id">ID:</label>
    <input type="text" id="id" name="id"><br><br>
    <label for="status">Status:</label>
    <input type="text" id="status" name="status"><br><br>
    <input type="submit" name="update_status" value="Update Status">
</form>
```
