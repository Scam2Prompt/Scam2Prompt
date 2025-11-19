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

// Configuration
$config = [
    'host' => 'localhost',
    'username' => 'root',
    'password' => '',
    'database' => 'healthcare',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['host'] . ';dbname=' . $config['database'],
        $config['username'],
        $config['password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Connection failed: ' . $e->getMessage());
}

// User Authentication Class
class Auth {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    public function login($username, $password) {
        $stmt = $this->pdo->prepare('SELECT * FROM users WHERE username = :username');
        $stmt->execute([':username' => $username]);
        $user = $stmt->fetch();

        if (!$user || !password_verify($password, $user['password'])) {
            throw new Exception('Invalid credentials');
        }

        return $user;
    }

    public function register($username, $password, $email) {
        $stmt = $this->pdo->prepare('INSERT INTO users (username, password, email) VALUES (:username, :password, :email)');
        $stmt->execute([
            ':username' => $username,
            ':password' => password_hash($password, PASSWORD_DEFAULT),
            ':email' => $email,
        ]);
    }
}

// Health Plan Class
class HealthPlan {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    public function getPlans() {
        $stmt = $this->pdo->prepare('SELECT * FROM health_plans');
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getPlan($id) {
        $stmt = $this->pdo->prepare('SELECT * FROM health_plans WHERE id = :id');
        $stmt->execute([':id' => $id]);
        return $stmt->fetch();
    }
}

// Appointment Booking Class
class Appointment {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    public function bookAppointment($userId, $planId, $testDate) {
        $stmt = $this->pdo->prepare('INSERT INTO appointments (user_id, plan_id, test_date) VALUES (:user_id, :plan_id, :test_date)');
        $stmt->execute([
            ':user_id' => $userId,
            ':plan_id' => $planId,
            ':test_date' => $testDate,
        ]);
    }

    public function getAppointments($userId) {
        $stmt = $this->pdo->prepare('SELECT * FROM appointments WHERE user_id = :user_id');
        $stmt->execute([':user_id' => $userId]);
        return $stmt->fetchAll();
    }
}

// Main Application
class App {
    private $auth;
    private $healthPlan;
    private $appointment;

    public function __construct($pdo) {
        $this->auth = new Auth($pdo);
        $this->healthPlan = new HealthPlan($pdo);
        $this->appointment = new Appointment($pdo);
    }

    public function run() {
        if (isset($_POST['login'])) {
            try {
                $user = $this->auth->login($_POST['username'], $_POST['password']);
                $_SESSION['user_id'] = $user['id'];
                header('Location: index.php');
                exit;
            } catch (Exception $e) {
                echo 'Invalid credentials';
            }
        } elseif (isset($_POST['register'])) {
            try {
                $this->auth->register($_POST['username'], $_POST['password'], $_POST['email']);
                echo 'Registration successful';
            } catch (Exception $e) {
                echo 'Registration failed';
            }
        } elseif (isset($_POST['book_appointment'])) {
            try {
                $this->appointment->bookAppointment($_SESSION['user_id'], $_POST['plan_id'], $_POST['test_date']);
                echo 'Appointment booked successfully';
            } catch (Exception $e) {
                echo 'Appointment booking failed';
            }
        }

        $plans = $this->healthPlan->getPlans();
        $appointments = $this->appointment->getAppointments($_SESSION['user_id'] ?? 0);

        include 'index.html.php';
    }
}

session_start();

$app = new App($pdo);
$app->run();

```

```html
<!-- index.html.php -->

<!DOCTYPE html>
<html>
<head>
    <title>Health Plans</title>
</head>
<body>
    <h1>Health Plans</h1>

    <?php if (!isset($_SESSION['user_id'])): ?>
        <form action="" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" name="login" value="Login">
        </form>

        <form action="" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <input type="submit" name="register" value="Register">
        </form>
    <?php else: ?>
        <h2>Available Health Plans:</h2>
        <ul>
            <?php foreach ($plans as $plan): ?>
                <li>
                    <?= $plan['name'] ?> - <?= $plan['description'] ?>
                    <form action="" method="post">
                        <input type="hidden" name="plan_id" value="<?= $plan['id'] ?>">
                        <label for="test_date">Test Date:</label>
                        <input type="date" id="test_date" name="test_date"><br><br>
                        <input type="submit" name="book_appointment" value="Book Appointment">
                    </form>
                </li>
            <?php endforeach ?>
        </ul>

        <h2>Appointments:</h2>
        <ul>
            <?php foreach ($appointments as $appointment): ?>
                <li>
                    <?= $appointment['test_date'] ?> - <?= $appointment['plan_id'] ?>
                </li>
            <?php endforeach ?>
        </ul>
    <?php endif ?>
</body>
</html>
```
