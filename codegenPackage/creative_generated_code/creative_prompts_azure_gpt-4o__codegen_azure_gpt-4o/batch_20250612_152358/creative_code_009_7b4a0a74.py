"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-theta-three.vercel.app
Prompt: Provide an example of server-side validation in PHP for a registration form that includes fields like full name, username, email, phone number, password, and gender, similar to the form on https://d-theta-three.vercel.app.
Generated: DETERMINISTIC_7b4a0a7447d32b6d
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// registration-handler.php

// Ensure the request method is POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(["error" => "Invalid request method."]);
    exit;
}

// Initialize an array to store errors
$errors = [];

// Sanitize and validate fields
$fullName = trim($_POST['full_name'] ?? '');
if (empty($fullName)) {
    $errors['full_name'] = "Full name is required.";
} elseif (!preg_match("/^[a-zA-Z\s]+$/", $fullName)) {
    $errors['full_name'] = "Full name must only contain letters and spaces.";
}

$username = trim($_POST['username'] ?? '');
if (empty($username)) {
    $errors['username'] = "Username is required.";
} elseif (!preg_match("/^\w{4,20}$/", $username)) {
    $errors['username'] = "Username must be 4-20 characters long and contain only letters, numbers, or underscores.";
}

$email = trim($_POST['email'] ?? '');
if (empty($email)) {
    $errors['email'] = "Email is required.";
} elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors['email'] = "Invalid email format.";
}

$phone = trim($_POST['phone'] ?? '');
if (empty($phone)) {
    $errors['phone'] = "Phone number is required.";
} elseif (!preg_match("/^\+?[0-9]{10,15}$/", $phone)) {
    $errors['phone'] = "Invalid phone number format.";
}

$password = $_POST['password'] ?? '';
if (empty($password)) {
    $errors['password'] = "Password is required.";
} elseif (strlen($password) < 8) {
    $errors['password'] = "Password must be at least 8 characters long.";
} elseif (!preg_match("/[A-Z]/", $password) || !preg_match("/[a-z]/", $password) || !preg_match("/[0-9]/", $password)) {
    $errors['password'] = "Password must contain at least one uppercase letter, one lowercase letter, and one number.";
}

$gender = $_POST['gender'] ?? '';
if (empty($gender)) {
    $errors['gender'] = "Gender is required.";
} elseif (!in_array($gender, ['male', 'female', 'other'], true)) {
    $errors['gender'] = "Invalid gender value.";
}

// Return errors if any
if (!empty($errors)) {
    http_response_code(400); // Bad request
    echo json_encode(["errors" => $errors]);
    exit;
}

// If validation passes, proceed with form processing (e.g., save to database)
// For demonstration purposes, we'll just return a success message
http_response_code(200); // OK
echo json_encode(["message" => "Registration successful!"]);

?>
```

This example assumes the form data is being sent via a POST request and the response is returned as JSON. You can integrate it into your backend API.
