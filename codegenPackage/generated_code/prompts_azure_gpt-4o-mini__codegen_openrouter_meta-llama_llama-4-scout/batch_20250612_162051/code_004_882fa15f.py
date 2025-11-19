"""
Generated Code Metadata:
========================
Original URL: https://rapala.tc
Prompt: Illustrate how to implement a contact form in PHP for a travel concierge service, ensuring it captures detailed client preferences like those offered by Rapala Travel Concierge.
Generated: DETERMINISTIC_882fa15f5eb7075b
Batch ID: 20250612_162051
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
 * Contact Form Handler for Travel Concierge Service
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'your_database',
];

// Database Connection
try {
    $dsn = "mysql:host={$config['db_host']};dbname={$config['db_name']}";
    $pdo = new PDO($dsn, $config['db_username'], $config['db_password']);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception("Database connection failed: " . $e->getMessage());
}

// Form Data Handler
class ContactFormHandler
{
    private $pdo;

    public function __construct(PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    public function handleFormSubmission(array $formData)
    {
        // Validate form data
        $errors = $this->validateFormData($formData);
        if (!empty($errors)) {
            return ['success' => false, 'errors' => $errors];
        }

        // Save form data to database
        try {
            $stmt = $this->pdo->prepare("
                INSERT INTO contact_forms (name, email, phone, travel_type, destinations, travel_dates, special_requests)
                VALUES (:name, :email, :phone, :travel_type, :destinations, :travel_dates, :special_requests)
            ");
            $stmt->execute([
                'name' => $formData['name'],
                'email' => $formData['email'],
                'phone' => $formData['phone'],
                'travel_type' => $formData['travel_type'],
                'destinations' => $formData['destinations'],
                'travel_dates' => $formData['travel_dates'],
                'special_requests' => $formData['special_requests'],
            ]);

            // Send confirmation email
            $this->sendConfirmationEmail($formData);

            return ['success' => true, 'message' => 'Form submitted successfully!'];
        } catch (PDOException $e) {
            return ['success' => false, 'errors' => ['Database error: ' . $e->getMessage()]];
        }
    }

    private function validateFormData(array $formData)
    {
        $errors = [];

        if (empty($formData['name'])) {
            $errors[] = 'Name is required';
        }

        if (empty($formData['email']) || !filter_var($formData['email'], FILTER_VALIDATE_EMAIL)) {
            $errors[] = 'Invalid email address';
        }

        if (empty($formData['phone'])) {
            $errors[] = 'Phone number is required';
        }

        if (empty($formData['travel_type'])) {
            $errors[] = 'Travel type is required';
        }

        if (empty($formData['destinations'])) {
            $errors[] = 'Destinations is required';
        }

        if (empty($formData['travel_dates'])) {
            $errors[] = 'Travel dates is required';
        }

        return $errors;
    }

    private function sendConfirmationEmail(array $formData)
    {
        // Email configuration
        $to = 'your_email@example.com';
        $subject = 'Contact Form Submission';

        // Email content
        $message = "
            <h2>Contact Form Submission</h2>
            <p>Name: {$formData['name']}</p>
            <p>Email: {$formData['email']}</p>
            <p>Phone: {$formData['phone']}</p>
            <p>Travel Type: {$formData['travel_type']}</p>
            <p>Destinations: {$formData['destinations']}</p>
            <p>Travel Dates: {$formData['travel_dates']}</p>
            <p>Special Requests: {$formData['special_requests']}</p>
        ";

        // Send email using PHPMailer or your preferred email library
        // For simplicity, we'll use mail() function here
        mail($to, $subject, $message, 'Content-Type: text/html; charset=UTF-8');
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $formData = [
        'name' => $_POST['name'],
        'email' => $_POST['email'],
        'phone' => $_POST['phone'],
        'travel_type' => $_POST['travel_type'],
        'destinations' => $_POST['destinations'],
        'travel_dates' => $_POST['travel_dates'],
        'special_requests' => $_POST['special_requests'],
    ];

    $contactFormHandler = new ContactFormHandler($pdo);
    $response = $contactFormHandler->handleFormSubmission($formData);

    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}
```

**HTML Form Example**
```html
<form action="" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="phone">Phone:</label>
    <input type="text" id="phone" name="phone"><br><br>
    <label for="travel_type">Travel Type:</label>
    <select id="travel_type" name="travel_type">
        <option value="">Select</option>
        <option value="relaxation">Relaxation</option>
        <option value="adventure">Adventure</option>
        <option value="food and wine">Food and Wine</option>
    </select><br><br>
    <label for="destinations">Destinations:</label>
    <input type="text" id="destinations" name="destinations"><br><br>
    <label for="travel_dates">Travel Dates:</label>
    <input type="text" id="travel_dates" name="travel_dates"><br><br>
    <label for="special_requests">Special Requests:</label>
    <textarea id="special_requests" name="special_requests"></textarea><br><br>
    <input type="submit" value="Submit">
</form>
```
