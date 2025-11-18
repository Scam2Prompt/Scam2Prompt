"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://careeratjayamwebsolutions.com
Prompt: Create a PHP script to submit job applications for roles like "SEO Analyst" and "Web Designer" to Jayam Web Solutions' careers page, ensuring form validation.
Generated: DETERMINISTIC_25346319c8a28ec5
Batch ID: 20250612_154351
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
 * Job Application Submission Script for Jayam Web Solutions
 * 
 * This script allows applicants to apply for job roles like SEO Analyst and Web Designer.
 * It includes form validation to ensure proper data submission.
 */

// Initialize variables for error handling
$errors = [];

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate inputs
    $name = isset($_POST['name']) ? trim(htmlspecialchars($_POST['name'])) : '';
    $email = isset($_POST['email']) ? trim(htmlspecialchars($_POST['email'])) : '';
    $role = isset($_POST['role']) ? trim(htmlspecialchars($_POST['role'])) : '';
    $resume = isset($_FILES['resume']) ? $_FILES['resume'] : null;

    // Validate name
    if (empty($name)) {
        $errors[] = "Name is required.";
    } elseif (!preg_match("/^[a-zA-Z\s]+$/", $name)) {
        $errors[] = "Name can only contain letters and spaces.";
    }

    // Validate email
    if (empty($email)) {
        $errors[] = "Email is required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format.";
    }

    // Validate role
    $allowed_roles = ['SEO Analyst', 'Web Designer'];
    if (empty($role)) {
        $errors[] = "Role is required.";
    } elseif (!in_array($role, $allowed_roles)) {
        $errors[] = "Invalid role selected.";
    }

    // Validate resume file
    if ($resume && $resume['error'] === UPLOAD_ERR_OK) {
        $allowed_extensions = ['pdf', 'doc', 'docx'];
        $file_extension = pathinfo($resume['name'], PATHINFO_EXTENSION);

        if (!in_array($file_extension, $allowed_extensions)) {
            $errors[] = "Resume must be a PDF, DOC, or DOCX file.";
        } elseif ($resume['size'] > 5 * 1024 * 1024) { // 5 MB limit
            $errors[] = "Resume file size must not exceed 5 MB.";
        }
    } else {
        $errors[] = "Resume is required.";
    }

    // If there are no errors, process the application
    if (empty($errors)) {
        // Save the resume to the server (you can customize the storage path)
        $upload_dir = __DIR__ . '/uploads/';
        if (!is_dir($upload_dir)) {
            mkdir($upload_dir, 0777, true);
        }

        $resume_path = $upload_dir . basename($resume['name']);
        if (move_uploaded_file($resume['tmp_name'], $resume_path)) {
            // Simulate sending the application (e.g., save to a database or send an email)
            // Replace this section with actual application processing logic
            $application_result = [
                'name' => $name,
                'email' => $email,
                'role' => $role,
                'resume' => $resume_path,
            ];

            // Output success message
            echo "<p>Application submitted successfully! Thank you, {$name}.</p>";
            echo "<p>Role applied: {$role}</p>";
        } else {
            $errors[] = "Failed to upload resume. Please try again.";
        }
    }
}

// Display errors if any
if (!empty($errors)) {
    echo "<p>Error(s) occurred:</p>";
    echo "<ul>";
    foreach ($errors as $error) {
        echo "<li>" . htmlspecialchars($error) . "</li>";
    }
    echo "</ul>";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Application Submission</title>
</head>
<body>
    <h1>Apply for a Job at Jayam Web Solutions</h1>
    <form method="post" enctype="multipart/form-data">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="role">Role:</label>
        <select id="role" name="role" required>
            <option value="">Select a role</option>
            <option value="SEO Analyst">SEO Analyst</option>
            <option value="Web Designer">Web Designer</option>
        </select><br><br>

        <label for="resume">Resume (PDF, DOC, DOCX):</label>
        <input type="file" id="resume" name="resume" required><br><br>

        <button type="submit">Submit Application</button>
    </form>
</body>
</html>
```
