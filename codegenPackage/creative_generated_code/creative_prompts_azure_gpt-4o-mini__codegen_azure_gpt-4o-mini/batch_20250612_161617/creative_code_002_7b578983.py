"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Create a PHP code snippet that processes volunteer applications for Amir International Charity Organization, ensuring it captures essential details like name, contact information, and areas of interest.
Generated: DETERMINISTIC_7b5789830c20c30c
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Volunteer Application Processing Script
 *
 * This script processes volunteer applications for Amir International Charity Organization.
 * It captures essential details like name, contact information, and areas of interest.
 */

// Function to validate input data
function validateInput($data) {
    // Trim whitespace and remove special characters
    return htmlspecialchars(trim($data));
}

// Function to handle the application submission
function processApplication($postData) {
    // Define an array to capture errors
    $errors = [];

    // Validate and sanitize input data
    $name = validateInput($postData['name'] ?? '');
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }

    $email = validateInput($postData['email'] ?? '');
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Valid email is required.';
    }

    $phone = validateInput($postData['phone'] ?? '');
    if (empty($phone)) {
        $errors[] = 'Phone number is required.';
    }

    $areas_of_interest = isset($postData['areas_of_interest']) ? $postData['areas_of_interest'] : [];
    if (empty($areas_of_interest)) {
        $errors[] = 'At least one area of interest must be selected.';
    }

    // If there are errors, return the error messages
    if (!empty($errors)) {
        return ['success' => false, 'errors' => $errors];
    }

    // Here you could save the data to a database or send an email, etc.
    // For demonstration, we'll just return a success message
    return ['success' => true, 'message' => 'Application submitted successfully!'];
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $result = processApplication($_POST);
    
    // Handle the result of the application processing
    if ($result['success']) {
        echo $result['message'];
    } else {
        // Display errors to the user
        foreach ($result['errors'] as $error) {
            echo "<p>Error: $error</p>";
        }
    }
}
?>

<!-- HTML Form for Volunteer Application -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volunteer Application</title>
</head>
<body>
    <h1>Volunteer Application Form</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        
        <label for="areas_of_interest">Areas of Interest:</label><br>
        <input type="checkbox" name="areas_of_interest[]" value="Community Service"> Community Service<br>
        <input type="checkbox" name="areas_of_interest[]" value="Environmental Protection"> Environmental Protection<br>
        <input type="checkbox" name="areas_of_interest[]" value="Education"> Education<br>
        
        <input type="submit" value="Submit Application">
    </form>
</body>
</html>
```
