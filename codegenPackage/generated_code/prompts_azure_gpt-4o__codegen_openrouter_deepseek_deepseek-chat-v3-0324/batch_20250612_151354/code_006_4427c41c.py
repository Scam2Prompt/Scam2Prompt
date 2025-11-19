"""
Generated Code Metadata:
========================
Original URL: https://1minutedog.com
Prompt: Write code in PHP to implement a contact form for dog owners to reach out for personalized advice, similar to the contact options available on the "1 Minute Dog Training" website.
Generated: DETERMINISTIC_4427c41c4e6a61dd
Batch ID: 20250612_151354
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
 * Contact Form for Dog Owners
 * 
 * This script handles a contact form submission for dog owners seeking personalized advice.
 * It validates input, sanitizes data, sends an email, and returns a response.
 */

// Enable error reporting for debugging (remove in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define response array
$response = [
    'success' => false,
    'message' => '',
    'errors' => []
];

// Check if form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $dog_name = filter_input(INPUT_POST, 'dog_name', FILTER_SANITIZE_STRING);
    $dog_breed = filter_input(INPUT_POST, 'dog_breed', FILTER_SANITIZE_STRING);
    $dog_age = filter_input(INPUT_POST, 'dog_age', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);
    $training_goal = filter_input(INPUT_POST, 'training_goal', FILTER_SANITIZE_STRING);

    // Validate required fields
    if (empty($name)) {
        $response['errors']['name'] = 'Please enter your name';
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $response['errors']['email'] = 'Please enter a valid email address';
    }
    if (empty($message)) {
        $response['errors']['message'] = 'Please enter your message';
    }

    // If no errors, proceed with sending email
    if (empty($response['errors'])) {
        // Email configuration
        $to = 'contact@dogtrainingexample.com';
        $subject = 'Dog Training Advice Request: ' . $dog_name;
        
        // Email headers
        $headers = "From: $email\r\n";
        $headers .= "Reply-To: $email\r\n";
        $headers .= "MIME-Version: 1.0\r\n";
        $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
        
        // Email body
        $email_body = "
            <html>
            <head>
                <title>Dog Training Advice Request</title>
            </head>
            <body>
                <h2>Dog Training Advice Request</h2>
                <p><strong>From:</strong> $name</p>
                <p><strong>Email:</strong> $email</p>
                <p><strong>Phone:</strong> $phone</p>
                <p><strong>Dog's Name:</strong> $dog_name</p>
                <p><strong>Dog's Breed:</strong> $dog_breed</p>
                <p><strong>Dog's Age:</strong> $dog_age</p>
                <p><strong>Training Goal:</strong> $training_goal</p>
                <h3>Message:</h3>
                <p>$message</p>
            </body>
            </html>
        ";

        // Send email
        if (mail($to, $subject, $email_body, $headers)) {
            $response['success'] = true;
            $response['message'] = 'Thank you! Your message has been sent. We will get back to you soon.';
        } else {
            $response['message'] = 'Sorry, there was an error sending your message. Please try again later.';
        }
    } else {
        $response['message'] = 'Please correct the errors below.';
    }
    
    // Return JSON response
    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us for Dog Training Advice</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        textarea,
        select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 120px;
        }
        button {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            color: #27ae60;
            padding: 10px;
            background-color: #e8f8f0;
            border-radius: 4px;
            margin-bottom: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <h1>Get Personalized Dog Training Advice</h1>
    <p>Fill out the form below and we'll get back to you with expert advice tailored to your dog's needs.</p>
    
    <div id="success-message" class="success-message"></div>
    
    <form id="contact-form" method="post">
        <div class="form-group">
            <label for="name">Your Name*</label>
            <input type="text" id="name" name="name" required>
            <div id="error-name" class="error"></div>
        </div>
        
        <div class="form-group">
            <label for="email">Email Address*</label>
            <input type="email" id="email" name="email" required>
            <div id="error-email" class="error"></div>
        </div>
        
        <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone">
        </div>
        
        <div class="form-group">
            <label for="dog_name">Your Dog's Name</label>
            <input type="text" id="dog_name" name="dog_name">
        </div>
        
        <div class="form-group">
            <label for="dog_breed">Dog Breed</label>
            <input type="text" id="dog_breed" name="dog_breed">
        </div>
        
        <div class="form-group">
            <label for="dog_age">Dog's Age</label>
            <input type="text" id="dog_age" name="dog_age">
        </div>
        
        <div class="form-group">
            <label for="training_goal">Training Goal</label>
            <select id="training_goal" name="training_goal">
                <option value="">Select a goal</option>
                <option value="Basic Obedience">Basic Obedience</option>
                <option value="Behavior Issues">Behavior Issues</option>
                <option value="Puppy Training">Puppy Training</option>
                <option value="Advanced Training">Advanced Training</option>
                <option value="Other">Other</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="message">Your Message*</label>
            <textarea id="message" name="message" required></textarea>
            <div id="error-message" class="error"></div>
        </div>
        
        <button type="submit">Send Message</button>
    </form>
    
    <script>
        document.getElementById('contact-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Clear previous errors
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            document.getElementById('success-message').style.display = 'none';
            
            // Submit form via AJAX
            fetch('', {
                method: 'POST',
                body: new FormData(this),
                headers: {
                    'Accept': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Show success message
                    document.getElementById('success-message').text
