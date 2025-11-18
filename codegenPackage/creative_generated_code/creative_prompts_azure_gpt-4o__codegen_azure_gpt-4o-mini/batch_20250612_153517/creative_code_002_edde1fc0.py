"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://videtisconsultores.es
Prompt: Generate code to create a web-based form for collecting candidate information, ensuring it meets the requirements of Videtis Consultores' recruitment process.
Generated: DETERMINISTIC_edde1fc013c8db2d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Candidate Information Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Candidate Information Form</h1>
    <form id="candidateForm" action="submitCandidate.php" method="POST" onsubmit="return validateForm()">
        <!-- Full Name -->
        <label for="fullName">Full Name:</label>
        <input type="text" id="fullName" name="fullName" required>
        
        <!-- Email -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <!-- Phone Number -->
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required pattern="[0-9]{10}">
        
        <!-- Resume Upload -->
        <label for="resume">Upload Resume (PDF only):</label>
        <input type="file" id="resume" name="resume" accept=".pdf" required>
        
        <!-- Position Applying For -->
        <label for="position">Position Applying For:</label>
        <select id="position" name="position" required>
            <option value="" disabled selected>Select a position</option>
            <option value="developer">Developer</option>
            <option value="designer">Designer</option>
            <option value="manager">Manager</option>
        </select>
        
        <!-- Comments -->
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments"></textarea>
        
        <!-- Submit Button -->
        <button type="submit">Submit</button>
    </form>

    <script>
        // Function to validate form inputs before submission
        function validateForm() {
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;

            // Basic email format validation
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                alert("Please enter a valid email address.");
                return false;
            }

            // Basic phone number format validation
            if (phone.length !== 10) {
                alert("Phone number must be 10 digits.");
                return false;
            }

            return true; // Form is valid
        }
    </script>
</body>
</html>
```

```php
<?php
// submitCandidate.php

// Start the session
session_start();

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Initialize an array for errors
    $errors = [];

    // Sanitize and validate inputs
    $fullName = sanitizeInput($_POST['fullName']);
    if (empty($fullName)) {
        $errors[] = "Full name is required.";
    }

    $email = sanitizeInput($_POST['email']);
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format.";
    }

    $phone = sanitizeInput($_POST['phone']);
    if (!preg_match('/^[0-9]{10}$/', $phone)) {
        $errors[] = "Phone number must be 10 digits.";
    }

    // Handle file upload
    if (isset($_FILES['resume'])) {
        $fileType = $_FILES['resume']['type'];
        $fileTmpName = $_FILES['resume']['tmp_name'];
        $fileError = $_FILES['resume']['error'];

        // Check for errors in file upload
        if ($fileError === UPLOAD_ERR_OK) {
            if ($fileType !== 'application/pdf') {
                $errors[] = "Only PDF files are allowed.";
            } else {
                // Move uploaded file to desired directory
                move_uploaded_file($fileTmpName, "uploads/" . basename($_FILES['resume']['name']));
            }
        } else {
            $errors[] = "Error uploading file.";
        }
    }

    // Check if there are no validation errors
    if (empty($errors)) {
        // Here, you would typically insert the data into the database
        // For example:
        // $stmt = $db->prepare("INSERT INTO candidates (name, email, phone) VALUES (?, ?, ?)");
        // $stmt->execute([$fullName, $email, $phone]);

        // Redirect to a success page
        header("Location: success.php");
        exit();
    } else {
        // Store errors in session and redirect back to the form
        $_SESSION['errors'] = $errors;
        header("Location: form.php");
        exit();
    }
} else {
    // Redirect to form if accessed directly
    header("Location: form.php");
    exit();
}
?>
```
