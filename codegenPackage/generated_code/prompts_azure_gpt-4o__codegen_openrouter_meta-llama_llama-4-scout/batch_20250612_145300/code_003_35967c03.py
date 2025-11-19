"""
Generated Code Metadata:
========================
Original URL: https://enjin.pro
Prompt: Generate PHP code to create a contact form for car inquiries, including fields for name, email, phone number, and specific car details, similar to the "お問い合わせ" section on the "縁陣 -ENJIN-" website.
Generated: DETERMINISTIC_35967c030d20d03e
Batch ID: 20250612_145300
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
try {
    $dsn = "mysql:host={$config['db_host']};dbname={$config['db_name']}";
    $pdo = new PDO($dsn, $config['db_username'], $config['db_password']);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception("Database connection failed: " . $e->getMessage());
}

// Contact form class
class ContactForm
{
    private $pdo;

    public function __construct(PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    public function handleSubmit(array $data)
    {
        // Validate input data
        $errors = $this->validateData($data);
        if (!empty($errors)) {
            return ['success' => false, 'errors' => $errors];
        }

        // Save inquiry to database
        try {
            $stmt = $this->pdo->prepare("INSERT INTO car_inquiries (name, email, phone_number, car_details) VALUES (:name, :email, :phone_number, :car_details)");
            $stmt->execute([
                'name' => $data['name'],
                'email' => $data['email'],
                'phone_number' => $data['phone_number'],
                'car_details' => $data['car_details'],
            ]);

            return ['success' => true, 'message' => 'Inquiry submitted successfully'];
        } catch (PDOException $e) {
            return ['success' => false, 'errors' => ['Database error: ' . $e->getMessage()]];
        }
    }

    private function validateData(array $data)
    {
        $errors = [];

        if (empty($data['name'])) {
            $errors[] = 'Name is required';
        }

        if (empty($data['email']) || !filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
            $errors[] = 'Invalid email address';
        }

        if (empty($data['phone_number'])) {
            $errors[] = 'Phone number is required';
        }

        if (empty($data['car_details'])) {
            $errors[] = 'Car details are required';
        }

        return $errors;
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $contactForm = new ContactForm($pdo);

    $data = [
        'name' => trim($_POST['name']),
        'email' => trim($_POST['email']),
        'phone_number' => trim($_POST['phone_number']),
        'car_details' => trim($_POST['car_details']),
    ];

    $result = $contactForm->handleSubmit($data);

    header('Content-Type: application/json');
    echo json_encode($result);
    exit;
}

// HTML form
?>

<form id="contact-form" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="phone_number">Phone Number:</label>
    <input type="tel" id="phone_number" name="phone_number" required>

    <label for="car_details">Car Details:</label>
    <textarea id="car_details" name="car_details" required></textarea>

    <button type="submit">Submit Inquiry</button>

    <div id="form-errors"></div>
    <div id="form-success"></div>
</form>

<script>
    const form = document.getElementById('contact-form');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);

        try {
            const response = await fetch('', {
                method: 'POST',
                body: formData,
            });

            const result = await response.json();

            if (result.success) {
                document.getElementById('form-success').innerText = result.message;
                form.reset();
            } else {
                const errorsElement = document.getElementById('form-errors');
                errorsElement.innerHTML = '';
                result.errors.forEach((error) => {
                    const errorElement = document.createElement('div');
                    errorElement.innerText = error;
                    errorsElement.appendChild(errorElement);
                });
            }
        } catch (error) {
            console.error(error);
        }
    });
</script>
```
