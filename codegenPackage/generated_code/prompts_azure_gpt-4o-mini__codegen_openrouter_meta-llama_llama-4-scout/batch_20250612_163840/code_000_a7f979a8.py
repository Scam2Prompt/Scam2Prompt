"""
Generated Code Metadata:
========================
Original URL: https://mstoolsnetshop.com
Prompt: Generate a PHP script for a simple logistic/courier system, incorporating features like email notifications and billing code as described on mstoolsnetshop.com.
Generated: DETERMINISTIC_a7f979a8388b78ca
Batch ID: 20250612_163840
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
 * Logistic/Courier System
 *
 * This script provides a basic implementation of a logistic/courier system.
 * It includes features like email notifications and billing code.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'logistic_system',
    'admin_email' => 'admin@example.com',
    'smtp_host' => 'your_smtp_host',
    'smtp_username' => 'your_smtp_username',
    'smtp_password' => 'your_smtp_password',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
    exit();
}

// Email Notification Function
function sendEmail($to, $subject, $message) {
    $headers = 'From: ' . $config['admin_email'] . "\r\n";
    $headers .= 'Reply-To: ' . $config['admin_email'] . "\r\n";
    $headers .= 'X-Mailer: PHP/' . phpversion() . "\r\n";
    $headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";

    try {
        $smtp = new PHPMailer\PHPMailer\SMTP();
        $mail = new PHPMailer\PHPMailer\PHPMailer(true);

        $mail->isSMTP();
        $mail->Host = $config['smtp_host'];
        $mail->SMTPAuth = true;
        $mail->Username = $config['smtp_username'];
        $mail->Password = $config['smtp_password'];
        $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = 587;

        $mail->setFrom($config['admin_email'], 'Logistic System');
        $mail->addAddress($to);
        $mail->isHTML(true);

        $mail->Subject = $subject;
        $mail->Body = $message;

        $mail->send();
    } catch (Exception $e) {
        echo 'Email sending failed: ' . $e->getMessage();
    }
}

// Create Tables
$createTables = [
    'couriers' => '
        CREATE TABLE IF NOT EXISTS couriers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            address TEXT NOT NULL
        )
    ',
    'packages' => '
        CREATE TABLE IF NOT EXISTS packages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            courier_id INT NOT NULL,
            package_name VARCHAR(255) NOT NULL,
            package_description TEXT NOT NULL,
            package_status VARCHAR(50) NOT NULL DEFAULT "pending",
            FOREIGN KEY (courier_id) REFERENCES couriers(id)
        )
    ',
    'billings' => '
        CREATE TABLE IF NOT EXISTS billings (
            id INT AUTO_INCREMENT PRIMARY KEY,
            package_id INT NOT NULL,
            billing_code VARCHAR(255) NOT NULL,
            billing_status VARCHAR(50) NOT NULL DEFAULT "pending",
            FOREIGN KEY (package_id) REFERENCES packages(id)
        )
    ',
];

foreach ($createTables as $table => $query) {
    try {
        $pdo->exec($query);
    } catch (PDOException $e) {
        echo "Table $table creation failed: " . $e->getMessage();
    }
}

// Add Courier
if (isset($_POST['add_courier'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $address = $_POST['address'];

    try {
        $stmt = $pdo->prepare('INSERT INTO couriers (name, email, phone, address) VALUES (:name, :email, :phone, :address)');
        $stmt->execute([':name' => $name, ':email' => $email, ':phone' => $phone, ':address' => $address]);
        sendEmail($email, 'Courier Account Created', 'Your courier account has been created successfully.');
        echo 'Courier added successfully!';
    } catch (PDOException $e) {
        echo 'Courier addition failed: ' . $e->getMessage();
    }
}

// Add Package
if (isset($_POST['add_package'])) {
    $courierId = $_POST['courier_id'];
    $packageName = $_POST['package_name'];
    $packageDescription = $_POST['package_description'];

    try {
        $stmt = $pdo->prepare('INSERT INTO packages (courier_id, package_name, package_description) VALUES (:courier_id, :package_name, :package_description)');
        $stmt->execute([':courier_id' => $courierId, ':package_name' => $packageName, ':package_description' => $packageDescription]);
        sendEmail($_POST['courier_email'], 'Package Added', 'A new package has been added to your account.');
        echo 'Package added successfully!';
    } catch (PDOException $e) {
        echo 'Package addition failed: ' . $e->getMessage();
    }
}

// Generate Billing Code
if (isset($_POST['generate_billing_code'])) {
    $packageId = $_POST['package_id'];

    try {
        $stmt = $pdo->prepare('SELECT * FROM packages WHERE id = :package_id');
        $stmt->execute([':package_id' => $packageId]);
        $package = $stmt->fetch();

        if ($package) {
            $billingCode = uniqid();
            $stmt = $pdo->prepare('INSERT INTO billings (package_id, billing_code) VALUES (:package_id, :billing_code)');
            $stmt->execute([':package_id' => $packageId, ':billing_code' => $billingCode]);
            sendEmail($_POST['courier_email'], 'Billing Code Generated', "Your billing code is: $billingCode");
            echo 'Billing code generated successfully!';
        } else {
            echo 'Package not found!';
        }
    } catch (PDOException $e) {
        echo 'Billing code generation failed: ' . $e->getMessage();
    }
}

// HTML Form
?>

<form action="" method="post">
    <h2>Add Courier</h2>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="phone">Phone:</label>
    <input type="text" id="phone" name="phone"><br><br>
    <label for="address">Address:</label>
    <textarea id="address" name="address"></textarea><br><br>
    <input type="submit" name="add_courier" value="Add Courier">
</form>

<form action="" method="post">
    <h2>Add Package</h2>
    <label for="courier_id">Courier ID:</label>
    <input type="text" id="courier_id" name="courier_id"><br><br>
    <label for="courier_email">Courier Email:</label>
    <input type="email" id="courier_email" name="courier_email"><br><br>
    <label for="package_name">Package Name:</label>
    <input type="text" id="package_name" name="package_name"><br><br>
    <label for="package_description">Package Description:</label>
    <textarea id="package_description" name="package_description"></textarea><br><br>
    <input type="submit" name="add_package" value="Add Package">
</form>

<form action="" method="post">
    <h2>Generate Billing Code</h2>
    <label for="package_id">Package ID:</label>
    <input type="text" id="package_id" name="package_id"><br><br>
    <label for="courier_email">Courier Email:</label>
    <input type="email" id="courier_email" name="courier_email"><br><br>
    <input type="submit" name="generate_billing_code" value="Generate Billing Code">
</form>
```
