"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labvidadourados.com.br
Prompt: Develop a PHP application that lists available health plans for laboratory tests, incorporating features like user authentication and appointment booking.
Generated: DETERMINISTIC_977552c151265968
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a session for user authentication
session_start();

// Database configuration settings
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'health_plans_db');

// Function to connect to the database
function dbConnect() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check connection
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    
    return $connection;
}

// User authentication function
function authenticateUser($username, $password) {
    $connection = dbConnect();
    
    // Prepare the SQL statement to prevent SQL injection
    $stmt = $connection->prepare("SELECT * FROM users WHERE username = ? AND password = ? LIMIT 1");
    $hashedPassword = hash('sha256', $password); // Hashing password for security
    $stmt->bind_param("ss", $username, $hashedPassword);
    $stmt->execute();
    
    $result = $stmt->get_result();
    
    if ($result->num_rows === 1) {
        $_SESSION['user'] = $username; // Set session variable
        return true;
    }
    
    return false; // Authentication failed
}

// Function to fetch available health plans
function getHealthPlans() {
    $connection = dbConnect();
    
    $result = $connection->query("SELECT * FROM health_plans");
    
    // Check for query execution errors
    if (!$result) {
        die("Query failed: " . $connection->error);
    }

    $plans = $result->fetch_all(MYSQLI_ASSOC);
    $connection->close();
    
    return $plans;
}

// Function to book an appointment
function bookAppointment($userId, $planId, $appointmentDate) {
    $connection = dbConnect();
    
    // Prepare the SQL statement
    $stmt = $connection->prepare("INSERT INTO appointments (user_id, health_plan_id, appointment_date) VALUES (?, ?, ?)");
    $stmt->bind_param("iis", $userId, $planId, $appointmentDate);
    
    if ($stmt->execute()) {
        return true; // Appointment booked successfully
    }

    return false; // Appointment booking failed
}

// Login handler
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if (authenticateUser($username, $password)) {
        header("Location: dashboard.php"); // Redirect to the dashboard upon successful login
        exit;
    } else {
        $error = "Invalid username or password.";
    }
}

// Fetch health plans for display
$healthPlans = getHealthPlans();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Plans</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Available Health Plans for Laboratory Tests</h1>

    <!-- User Login Form -->
    <form method="POST" action="">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
        <?php if (isset($error)) echo "<p style='color: red;'>$error</p>"; ?>
    </form>

    <!-- Display health plans -->
    <h2>Health Plans</h2>
    <ul>
        <?php foreach ($healthPlans as $plan): ?>
            <li>
                <h3><?php echo htmlspecialchars($plan['name']); ?></h3>
                <p><?php echo htmlspecialchars($plan['description']); ?></p>
                <p>Price: $<?php echo htmlspecialchars($plan['price']); ?></p>
                <form method="POST" action="book_appointment.php">
                    <input type="hidden" name="plan_id" value="<?php echo $plan['id']; ?>">
                    <input type="date" name="appointment_date" required>
                    <button type="submit">Book Appointment</button>
                </form>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```
