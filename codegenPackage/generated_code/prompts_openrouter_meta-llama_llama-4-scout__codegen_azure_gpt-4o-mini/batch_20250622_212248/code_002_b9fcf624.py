"""
Generated Code Metadata:
========================
Original URL: https://richnaturalfoods.com
Prompt: Write a PHP script snippet that handles a user registration form for a site similar to RJS138 SLOT, including validation for user input.
Generated: DETERMINISTIC_b9fcf624d8a04ebb
Batch ID: 20250622_212248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Start the session to store user data
session_start();

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Function to validate email format
function isValidEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}

// Function to validate password strength
function isValidPassword($password) {
    return preg_match('/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/', $password);
}

// Initialize an array to hold error messages
$errors = [];

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate user inputs
    $username = sanitizeInput($_POST['username']);
    $email = sanitizeInput($_POST['email']);
    $password = sanitizeInput($_POST['password']);
    
    // Validate username
    if (empty($username)) {
        $errors[] = "Username is required.";
    }

    // Validate email
    if (empty($email) || !isValidEmail($email)) {
        $errors[] = "A valid email is required.";
    }

    // Validate password
    if (empty($password) || !isValidPassword($password)) {
        $errors[] = "Password must be at least 8 characters long and include at least one letter and one number.";
    }

    // If there are no errors, proceed with registration
    if (empty($errors)) {
        // Here you would typically hash the password and save the user to the database
        // For demonstration, we will just simulate a successful registration
        $_SESSION['success'] = "Registration successful! Welcome, $username.";
        header("Location: success.php"); // Redirect to a success page
        exit();
    }
}

// Display errors if any
if (!empty($errors)) {
    foreach ($errors as $error) {
        echo "<p style='color:red;'>$error</p>";
    }
}
?>

<!-- HTML form for user registration -->
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    
    <input type="submit" value="Register">
</form>
```
