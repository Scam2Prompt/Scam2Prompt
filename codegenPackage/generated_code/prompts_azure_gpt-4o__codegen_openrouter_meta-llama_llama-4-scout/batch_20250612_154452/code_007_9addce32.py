"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Write a code snippet in PHP to implement a contact form for a coaching center website like Retina, allowing students to submit inquiries about courses and batch schedules.
Generated: DETERMINISTIC_9addce32767f8af2
Batch ID: 20250612_154452
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
$config = [
    'db_host' => 'your_host',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'your_database',
];

// Database connection
function connectToDatabase($config) {
    try {
        $pdo = new PDO(
            "mysql:host={$config['db_host']};dbname={$config['db_name']}",
            $config['db_username'],
            $config['db_password']
        );
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        throw new Exception("Database connection failed: " . $e->getMessage());
    }
}

// Contact form submission handler
function handleContactFormSubmission($pdo, $data) {
    try {
        $stmt = $pdo->prepare("
            INSERT INTO contact_inquiries (name, email, phone, course_interest, message, created_at)
            VALUES (:name, :email, :phone, :course_interest, :message, NOW())
        ");

        $stmt->execute([
            'name' => $data['name'],
            'email' => $data['email'],
            'phone' => $data['phone'],
            'course_interest' => $data['course_interest'],
            'message' => $data['message'],
        ]);

        return ['success' => true, 'message' => 'Inquiry submitted successfully.'];
    } catch (PDOException $e) {
        return ['success' => false, 'message' => 'Error submitting inquiry: ' . $e->getMessage()];
    }
}

// Validate form data
function validateFormData($data) {
    $errors = [];

    if (empty($data['name'])) {
        $errors[] = 'Name is required.';
    }

    if (empty($data['email']) || !filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Valid email is required.';
    }

    if (empty($data['phone'])) {
        $errors[] = 'Phone number is required.';
    }

    if (empty($data['course_interest'])) {
        $errors[] = 'Course interest is required.';
    }

    if (empty($data['message'])) {
        $errors[] = 'Message is required.';
    }

    return $errors;
}

// Main script
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $pdo = connectToDatabase($config);

    $formData = [
        'name' => trim($_POST['name']),
        'email' => trim($_POST['email']),
        'phone' => trim($_POST['phone']),
        'course_interest' => trim($_POST['course_interest']),
        'message' => trim($_POST['message']),
    ];

    $errors = validateFormData($formData);

    if (!empty($errors)) {
        $response = ['success' => false, 'errors' => $errors];
    } else {
        $response = handleContactFormSubmission($pdo, $formData);
    }

    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}

?>
```

**contact_form.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form id="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone"><br><br>
        <label for="course_interest">Course Interest:</label>
        <select id="course_interest" name="course_interest">
            <option value="">Select a course</option>
            <option value="course1">Course 1</option>
            <option value="course2">Course 2</option>
        </select><br><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>

    <div id="response"></div>

    <script>
        const form = document.getElementById('contact-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = new FormData(form);
            const response = await fetch('', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();

            const responseDiv = document.getElementById('response');
            if (data.success) {
                responseDiv.innerText = data.message;
                form.reset();
            } else {
                responseDiv.innerHTML = '';
                data.errors.forEach((error) => {
                    const p = document.createElement('p');
                    p.style.color = 'red';
                    p.innerText = error;
                    responseDiv.appendChild(p);
                });
            }
        });
    </script>
</body>
</html>
```
