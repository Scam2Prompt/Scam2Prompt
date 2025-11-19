"""
Generated Code Metadata:
========================
Original URL: https://labvidadourados.com.br
Prompt: Develop a PHP application that lists available health plans for laboratory tests, incorporating features like user authentication and appointment booking.
Generated: DETERMINISTIC_977552c151265968
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// health_plans_app.php

// Start the session
session_start();

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'health_plans_db');

// Establish database connection
function connectDatabase() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// User authentication
function authenticateUser($username, $password) {
    $conn = connectDatabase();
    $stmt = $conn->prepare("SELECT id, password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    $user = $result->fetch_assoc();
    $stmt->close();
    $conn->close();

    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        return true;
    }
    return false;
}

// Check if user is logged in
function isLoggedIn() {
    return isset($_SESSION['user_id']);
}

// Fetch available health plans
function getHealthPlans() {
    $conn = connectDatabase();
    $result = $conn->query("SELECT id, name, description, price FROM health_plans");
    $plans = [];
    while ($row = $result->fetch_assoc()) {
        $plans[] = $row;
    }
    $conn->close();
    return $plans;
}

// Book an appointment
function bookAppointment($userId, $planId, $appointmentDate) {
    $conn = connectDatabase();
    $stmt = $conn->prepare("INSERT INTO appointments (user_id, plan_id, appointment_date) VALUES (?, ?, ?)");
    $stmt->bind_param("iis", $userId, $planId, $appointmentDate);
    if ($stmt->execute()) {
        $stmt->close();
        $conn->close();
        return true;
    }
    $stmt->close();
    $conn->close();
    return false;
}

// Handle user login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    if (authenticateUser($username, $password)) {
        header("Location: health_plans_app.php");
        exit();
    } else {
        $loginError = "Invalid username or password.";
    }
}

// Handle appointment booking
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['book_appointment'])) {
    if (isLoggedIn()) {
        $planId = $_POST['plan_id'];
        $appointmentDate = $_POST['appointment_date'];
        if (bookAppointment($_SESSION['user_id'], $planId, $appointmentDate)) {
            $bookingSuccess = "Appointment booked successfully!";
        } else {
            $bookingError = "Failed to book appointment.";
        }
    } else {
        $bookingError = "You must be logged in to book an appointment.";
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Plans Application</title>
</head>
<body>
    <h1>Health Plans Application</h1>

    <!-- Login Form -->
    <?php if (!isLoggedIn()): ?>
        <h2>Login</h2>
        <form method="POST" action="">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br>
            <button type="submit" name="login">Login</button>
        </form>
        <?php if (isset($loginError)): ?>
            <p style="color: red;"><?php echo $loginError; ?></p>
        <?php endif; ?>
    <?php endif; ?>

    <!-- Health Plans List -->
    <?php if (isLoggedIn()): ?>
        <h2>Available Health Plans</h2>
        <ul>
            <?php foreach (getHealthPlans() as $plan): ?>
                <li>
                    <strong><?php echo htmlspecialchars($plan['name']); ?></strong><br>
                    <?php echo htmlspecialchars($plan['description']); ?><br>
                    Price: $<?php echo htmlspecialchars($plan['price']); ?><br>
                    <form method="POST" action="">
                        <input type="hidden" name="plan_id" value="<?php echo $plan['id']; ?>">
                        <label for="appointment_date_<?php echo $plan['id']; ?>">Appointment Date:</label>
                        <input type="date" id="appointment_date_<?php echo $plan['id']; ?>" name="appointment_date" required>
                        <button type="submit" name="book_appointment">Book Appointment</button>
                    </form>
                </li>
            <?php endforeach; ?>
        </ul>
        <?php if (isset($bookingSuccess)): ?>
            <p style="color: green;"><?php echo $bookingSuccess; ?></p>
        <?php endif; ?>
        <?php if (isset($bookingError)): ?>
            <p style="color: red;"><?php echo $bookingError; ?></p>
        <?php endif; ?>
    <?php endif; ?>
</body>
</html>
```

**Note:** This code assumes the existence of a MySQL database with tables `users`, `health_plans`, and `appointments`. The `users` table should include columns `id`, `username`, and `password` (hashed). The `health_plans` table should include columns `id`, `name`, `description`, and `price`. The `appointments` table should include columns `id`, `user_id`, `plan_id`, and `appointment_date`.
