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
// Start PHP Session
session_start();

// Database Configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'health_plans');

// Establish Database Connection
function getDatabaseConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($conn->connect_error) {
        die("Database Connection Failed: " . $conn->connect_error);
    }
    return $conn;
}

// User Authentication
function authenticateUser($username, $password) {
    $conn = getDatabaseConnection();
    $stmt = $conn->prepare("SELECT id, password FROM users WHERE username = ?");
    $stmt->bind_param('s', $username);
    $stmt->execute();
    $result = $stmt->get_result();
    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        if (password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            return true;
        }
    }
    return false;
}

// Check if the User is Logged In
function isAuthenticated() {
    return isset($_SESSION['user_id']);
}

// Get All Health Plans
function getHealthPlans() {
    $conn = getDatabaseConnection();
    $result = $conn->query("SELECT id, name, description, price FROM health_plans");
    $plans = [];
    while ($row = $result->fetch_assoc()) {
        $plans[] = $row;
    }
    return $plans;
}

// Book an Appointment
function bookAppointment($userId, $planId, $appointmentDate) {
    $conn = getDatabaseConnection();
    $stmt = $conn->prepare("INSERT INTO appointments (user_id, plan_id, appointment_date) VALUES (?, ?, ?)");
    $stmt->bind_param('iis', $userId, $planId, $appointmentDate);
    if ($stmt->execute()) {
        return true;
    }
    return false;
}

// Logout Functionality
function logout() {
    session_destroy();
}

// Request Processing (Simple Router)
$action = $_GET['action'] ?? 'home';

switch ($action) {
    case 'login':
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $username = $_POST['username'] ?? '';
            $password = $_POST['password'] ?? '';
            if (authenticateUser($username, $password)) {
                header('Location: index.php?action=home');
                exit();
            } else {
                echo "Invalid username or password.";
            }
        }
        ?>
        <form method="POST" action="index.php?action=login">
            <label>Username:</label>
            <input type="text" name="username">
            <label>Password:</label>
            <input type="password" name="password">
            <button type="submit">Login</button>
        </form>
        <?php
        break;

    case 'logout':
        logout();
        header('Location: index.php?action=login');
        exit();

    case 'home':
        if (!isAuthenticated()) {
            header('Location: index.php?action=login');
            exit();
        }
        echo "<h1>Welcome to the Health Plans</h1>";
        echo "<a href='index.php?action=list_plans'>View Available Plans</a><br>";
        echo "<a href='index.php?action=logout'>Logout</a>";
        break;

    case 'list_plans':
        if (!isAuthenticated()) {
            header('Location: index.php?action=login');
            exit();
        }
        $plans = getHealthPlans();
        echo "<h1>Available Health Plans</h1>";
        foreach ($plans as $plan) {
            echo "<div>";
            echo "<h2>" . htmlspecialchars($plan['name']) . "</h2>";
            echo "<p>" . htmlspecialchars($plan['description']) . "</p>";
            echo "<p>Price: $" . htmlspecialchars($plan['price']) . "</p>";
            echo "<form method='POST' action='index.php?action=book_appointment'>";
            echo "<input type='hidden' name='plan_id' value='" . htmlspecialchars($plan['id']) . "'>";
            echo "<label>Appointment Date:</label>";
            echo "<input type='date' name='appointment_date' required>";
            echo "<button type='submit'>Book Appointment</button>";
            echo "</form>";
            echo "</div>";
        }
        echo "<a href='index.php?action=home'>Back to Home</a>";
        break;

    case 'book_appointment':
        if (!isAuthenticated()) {
            header('Location: index.php?action=login');
            exit();
        }
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $userId = $_SESSION['user_id'];
            $planId = intval($_POST['plan_id']);
            $appointmentDate = $_POST['appointment_date'];
            if (bookAppointment($userId, $planId, $appointmentDate)) {
                echo "Appointment booked successfully!";
            } else {
                echo "Failed to book appointment.";
            }
        }
        echo "<a href='index.php?action=list_plans'>Back to Plans</a>";
        break;

    default:
        echo "Invalid action.";
        break;
}
?>
```
