"""
Generated Code Metadata:
========================
Original URL: https://prgmea.pk
Prompt: Create a PHP-based form for visitor registration on PRGMEA's website, ensuring secure data handling and validation.
Generated: DETERMINISTIC_cc4e25a2fbef5ea6
Batch ID: 20250612_153224
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
 * Visitor Registration Form Handler
 */

// Configuration
$config = [
    'dbHost' => 'localhost',
    'dbUsername' => 'your_username',
    'dbPassword' => 'your_password',
    'dbName' => 'prgmea_website',
];

// Database Connection
try {
    $pdo = new PDO(
        "mysql:host={$config['dbHost']};dbname={$config['dbName']}",
        $config['dbUsername'],
        $config['dbPassword']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Form Data Validation
function validateFormData($data)
{
    $errors = [];
    if (empty($data['name'])) {
        $errors[] = "Name is required.";
    }
    if (empty($data['email'])) {
        $errors[] = "Email is required.";
    } elseif (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format.";
    }
    if (empty($data['phone'])) {
        $errors[] = "Phone number is required.";
    }
    if (empty($data['visit_purpose'])) {
        $errors[] = "Visit purpose is required.";
    }
    return $errors;
}

// Form Submission Handler
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $formData = [
        'name' => trim($_POST['name']),
        'email' => trim($_POST['email']),
        'phone' => trim($_POST['phone']),
        'visit_purpose' => trim($_POST['visit_purpose']),
    ];

    $errors = validateFormData($formData);

    if (empty($errors)) {
        try {
            $stmt = $pdo->prepare("
                INSERT INTO visitor_registrations (name, email, phone, visit_purpose)
                VALUES (:name, :email, :phone, :visit_purpose)
            ");
            $stmt->execute($formData);
            $successMessage = "Registration successful.";
        } catch (PDOException $e) {
            $errors[] = "Database error: " . $e->getMessage();
        }
    }

    if (isset($errors) && count($errors) > 0) {
        $errorMessage = implode("<br>", $errors);
    }
}

// Form Display
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visitor Registration Form</title>
    <style>
        form {
            max-width: 500px;
            margin: 40px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
        }
        button[type="submit"] {
            background-color: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .error {
            color: red;
        }
        .success {
            color: green;
        }
    </style>
</head>
<body>

<form action="" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="phone">Phone Number:</label>
    <input type="text" id="phone" name="phone" required>

    <label for="visit_purpose">Visit Purpose:</label>
    <textarea id="visit_purpose" name="visit_purpose" required></textarea>

    <button type="submit">Register</button>

    <?php if (isset($errorMessage)): ?>
        <div class="error"><?= $errorMessage ?></div>
    <?php endif; ?>

    <?php if (isset($successMessage)): ?>
        <div class="success"><?= $successMessage ?></div>
    <?php endif; ?>
</form>

</body>
</html>
```
