"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Write a code snippet in PHP to implement a contact form for a coaching center website like Retina, allowing students to submit inquiries about courses and batch schedules.
Generated: DETERMINISTIC_9addce32767f8af2
Batch ID: 20250612_154452
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.google.com/recaptcha/api.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.google.com/recaptcha/api/siteverify": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Contact Form Handler for Coaching Center Website
 * 
 * This script processes the contact form submissions, validates the input,
 * and sends an email notification to the coaching center admin.
 */

// Enable error reporting for debugging (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 0); // Hide errors from users in production

// Configuration
define('ADMIN_EMAIL', 'admin@coachingcenter.com');
define('EMAIL_SUBJECT', 'New Course Inquiry from Website');
define('MIN_MESSAGE_LENGTH', 10);
define('MAX_MESSAGE_LENGTH', 1000);
define('RECAPTCHA_SECRET', 'your_recaptcha_secret_key'); // Replace with actual key

// Validate and sanitize input
function sanitizeInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Validate email format
function isValidEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}

// Verify reCAPTCHA response
function verifyRecaptcha($response) {
    if (empty($response)) return false;
    
    $url = 'https://www.google.com/recaptcha/api/siteverify';
    $data = [
        'secret' => RECAPTCHA_SECRET,
        'response' => $response,
        'remoteip' => $_SERVER['REMOTE_ADDR']
    ];
    
    $options = [
        'http' => [
            'header' => "Content-type: application/x-www-form-urlencoded\r\n",
            'method' => 'POST',
            'content' => http_build_query($data)
        ]
    ];
    
    $context = stream_context_create($options);
    $result = file_get_contents($url, false, $context);
    $responseData = json_decode($result);
    
    return $responseData->success;
}

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate required fields
        $requiredFields = ['name', 'email', 'phone', 'message', 'course', 'g-recaptcha-response'];
        foreach ($requiredFields as $field) {
            if (empty($_POST[$field])) {
                throw new Exception("Please fill in all required fields.");
            }
        }
        
        // Sanitize inputs
        $name = sanitizeInput($_POST['name']);
        $email = sanitizeInput($_POST['email']);
        $phone = sanitizeInput($_POST['phone']);
        $course = sanitizeInput($_POST['course']);
        $message = sanitizeInput($_POST['message']);
        $recaptchaResponse = $_POST['g-recaptcha-response'];
        
        // Additional validation
        if (!isValidEmail($email)) {
            throw new Exception("Please enter a valid email address.");
        }
        
        if (strlen($message) < MIN_MESSAGE_LENGTH || strlen($message) > MAX_MESSAGE_LENGTH) {
            throw new Exception("Message must be between " . MIN_MESSAGE_LENGTH . " and " . MAX_MESSAGE_LENGTH . " characters.");
        }
        
        if (!verifyRecaptcha($recaptchaResponse)) {
            throw new Exception("reCAPTCHA verification failed. Please try again.");
        }
        
        // Prepare email content
        $emailBody = "New Course Inquiry Received:\n\n";
        $emailBody .= "Name: $name\n";
        $emailBody .= "Email: $email\n";
        $emailBody .= "Phone: $phone\n";
        $emailBody .= "Course Interested In: $course\n\n";
        $emailBody .= "Message:\n$message\n";
        
        $headers = "From: $email\r\n";
        $headers .= "Reply-To: $email\r\n";
        $headers .= "X-Mailer: PHP/" . phpversion();
        
        // Send email
        if (mail(ADMIN_EMAIL, EMAIL_SUBJECT, $emailBody, $headers)) {
            $response = [
                'success' => true,
                'message' => 'Thank you for your inquiry! We will contact you shortly.'
            ];
        } else {
            throw new Exception("Failed to send email. Please try again later.");
        }
        
    } catch (Exception $e) {
        $response = [
            'success' => false,
            'message' => $e->getMessage()
        ];
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
    <title>Contact Us - Coaching Center</title>
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
    <style>
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <h1>Course Inquiry Form</h1>
    <div id="response-message" class="hidden"></div>
    
    <form id="contact-form" method="post">
        <div>
            <label for="name">Full Name:*</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div>
            <label for="email">Email:*</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div>
            <label for="phone">Phone Number:*</label>
            <input type="tel" id="phone" name="phone" required>
        </div>
        
        <div>
            <label for="course">Course Interested In:*</label>
            <select id="course" name="course" required>
                <option value="">Select a course</option>
                <option value="JEE Main">JEE Main</option>
                <option value="JEE Advanced">JEE Advanced</option>
                <option value="NEET">NEET</option>
                <option value="Foundation (Class 9-10)">Foundation (Class 9-10)</option>
            </select>
        </div>
        
        <div>
            <label for="message">Your Inquiry:*</label>
            <textarea id="message" name="message" rows="5" required></textarea>
        </div>
        
        <div class="g-recaptcha" data-sitekey="your_recaptcha_site_key"></div>
        
        <button type="submit">Submit Inquiry</button>
    </form>
    
    <script>
        document.getElementById('contact-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const form = e.target;
            const formData = new FormData(form);
            const responseElement = document.getElementById('response-message');
            
            fetch('', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                responseElement.textContent = data.message;
                responseElement.className = data.success ? 'success' : 'error';
                
                if (data.success) {
                    form.reset();
                    grecaptcha.reset();
                }
            })
            .catch(error => {
                responseElement.textContent = 'An error occurred. Please try again.';
                responseElement.className = 'error';
            });
        });
    </script>
</body>
</html>
```
