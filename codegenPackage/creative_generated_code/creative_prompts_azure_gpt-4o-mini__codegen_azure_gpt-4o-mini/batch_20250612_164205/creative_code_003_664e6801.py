"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Develop a PHP application that allows users to sign up and choose an investment package from MET LIFE INVESTS, including form validation for user input.
Generated: DETERMINISTIC_664e68014056f68a
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a session to manage user data across pages
session_start();

// Database connection parameters
$host = 'localhost';
$db = 'investment_db';
$user = 'root';
$pass = '';

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Could not connect to the database: " . $e->getMessage());
}

// Function to validate user input
function validateInput($data) {
    $errors = [];
    // Name validation
    if (empty($data['name'])) {
        $errors['name'] = 'Name is required.';
    } elseif (!preg_match("/^[a-zA-Z ]*$/", $data['name'])) {
        $errors['name'] = 'Only letters and white space allowed.';
    }

    // Email validation
    if (empty($data['email'])) {
        $errors['email'] = 'Email is required.';
    } elseif (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = 'Invalid email format.';
    }

    // Package selection validation
    if (empty($data['package'])) {
        $errors['package'] = 'Investment package is required.';
    }

    return $errors;
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $package = $_POST['package'];

    $inputData = [
        'name' => $name,
        'email' => $email,
        'package' => $package
    ];

    // Validate the input data
    $errors = validateInput($inputData);

    // If no errors, proceed to store user data
    if (empty($errors)) {
        try {
            // Prepare the SQL statement
            $stmt = $pdo->prepare("INSERT INTO users (name, email, package) VALUES (:name, :email, :package)");
            $stmt->execute([
                ':name' => $name,
                ':email' => $email,
                ':package' => $package
            ]);
            $_SESSION['success'] = "Registration successful!";
            header("Location: success.php");
            exit();
        } catch (PDOException $e) {
            $errors['database'] = "Database error: " . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Sign Up</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Sign Up for MET LIFE INVESTS</h1>
    <form method="POST" action="">
        <div>
            <label for="name">Name:</label>
            <input type="text" name="name" id="name" value="<?= htmlspecialchars($name ?? '') ?>">
            <span class="error"><?= $errors['name'] ?? '' ?></span>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" value="<?= htmlspecialchars($email ?? '') ?>">
            <span class="error"><?= $errors['email'] ?? '' ?></span>
        </div>
        <div>
            <label for="package">Investment Package:</label>
            <select name="package" id="package">
                <option value="">Select a package</option>
                <option value="basic" <?= (isset($package) && $package === 'basic') ? 'selected' : '' ?>>Basic</option>
                <option value="premium" <?= (isset($package) && $package === 'premium') ? 'selected' : '' ?>>Premium</option>
                <option value="deluxe" <?= (isset($package) && $package === 'deluxe') ? 'selected' : '' ?>>Deluxe</option>
            </select>
            <span class="error"><?= $errors['package'] ?? '' ?></span>
        </div>
        <div>
            <button type="submit">Sign Up</button>
        </div>
        <?php if (!empty($errors['database'])): ?>
            <div class="error"><?= $errors['database'] ?></div>
        <?php endif; ?>
    </form>
</body>
</html>
```

**Note:** This code assumes a pre-existing database named `investment_db` with a table `users` that contains columns `name`, `email`, and `package`. Adjust the database connection parameters as needed.
