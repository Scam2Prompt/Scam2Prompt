"""
Generated Code Metadata:
========================
Original URL: https://www.hdadpanaderos.es
Prompt: Write a code snippet in PHP to create a simple form for submitting consultas (inquiries) similar to the one found on the Hermandad de los Panaderos website.
Generated: DETERMINISTIC_d0ac11858feed1c2
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Start the session to handle form submissions
session_start();

// Define a function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Initialize variables for form data and error messages
$name = $email = $inquiry = "";
$nameErr = $emailErr = $inquiryErr = "";

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate name
    if (empty($_POST["name"])) {
        $nameErr = "Name is required";
    } else {
        $name = sanitizeInput($_POST["name"]);
    }

    // Validate email
    if (empty($_POST["email"])) {
        $emailErr = "Email is required";
    } elseif (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
        $emailErr = "Invalid email format";
    } else {
        $email = sanitizeInput($_POST["email"]);
    }

    // Validate inquiry
    if (empty($_POST["inquiry"])) {
        $inquiryErr = "Inquiry is required";
    } else {
        $inquiry = sanitizeInput($_POST["inquiry"]);
    }

    // If no errors, process the inquiry (e.g., save to database or send email)
    if (empty($nameErr) && empty($emailErr) && empty($inquiryErr)) {
        // Here you would typically save the data to a database or send an email
        // For demonstration, we will just store a success message in the session
        $_SESSION['success_message'] = "Inquiry submitted successfully!";
        header("Location: " . $_SERVER['PHP_SELF']);
        exit();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>Consulta Form</h1>

    <?php
    // Display success message if available
    if (isset($_SESSION['success_message'])) {
        echo "<p class='success'>" . $_SESSION['success_message'] . "</p>";
        unset($_SESSION['success_message']);
    }
    ?>

    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="<?php echo $name; ?>">
        <span class="error"><?php echo $nameErr; ?></span><br><br>

        <label for="email">Email:</label>
        <input type="text" id="email" name="email" value="<?php echo $email; ?>">
        <span class="error"><?php echo $emailErr; ?></span><br><br>

        <label for="inquiry">Inquiry:</label>
        <textarea id="inquiry" name="inquiry"><?php echo $inquiry; ?></textarea>
        <span class="error"><?php echo $inquiryErr; ?></span><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
