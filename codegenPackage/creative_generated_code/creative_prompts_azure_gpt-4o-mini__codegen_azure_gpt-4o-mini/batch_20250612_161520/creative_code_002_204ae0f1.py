"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Create a PHP code snippet that handles user registration for new members of the Grad košarke association, ensuring it captures essential details like name, email, and membership type.
Generated: DETERMINISTIC_204ae0f108de7856
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "grad_kosarke";

// Create connection to MySQL database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to register a new user
function registerUser($name, $email, $membershipType) {
    global $conn;

    // Validate input data
    if (empty($name) || empty($email) || empty($membershipType)) {
        return ["status" => "error", "message" => "All fields are required."];
    }

    // Check if the email is already registered
    $stmt = $conn->prepare("SELECT id FROM members WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        return ["status" => "error", "message" => "Email is already registered."];
    }
    $stmt->close();

    // Insert new user into the database
    $stmt = $conn->prepare("INSERT INTO members (name, email, membership_type) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $name, $email, $membershipType);

    // Execute the statement
    if ($stmt->execute()) {
        return ["status" => "success", "message" => "Registration successful."];
    } else {
        return ["status" => "error", "message" => "Registration failed: " . $stmt->error];
    }

    // Close the prepared statement
    $stmt->close();
}

// Example of handling a registration request
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $membershipType = $_POST['membership_type'] ?? '';

    // Call the registration function and capture the response
    $response = registerUser($name, $email, $membershipType);

    // Return response as JSON
    header('Content-Type: application/json');
    echo json_encode($response);
}

// Close the database connection
$conn->close();
?>
```

Make sure to create a database named `grad_kosarke` and a table `members` with appropriate columns (`id`, `name`, `email`, `membership_type`) for this code to function correctly.
