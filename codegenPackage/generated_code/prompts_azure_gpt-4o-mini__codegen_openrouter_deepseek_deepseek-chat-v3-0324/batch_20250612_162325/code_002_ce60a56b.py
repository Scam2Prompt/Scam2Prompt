"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Create a PHP application that facilitates access to quality education for children, inspired by the initiatives of Child Nepal.
Generated: DETERMINISTIC_ce60a56bc5cfc5bd
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Child Education Portal - A PHP application to facilitate access to quality education for children
 * Inspired by the initiatives of Child Nepal
 * 
 * @package ChildEducationPortal
 * @version 1.0.0
 */

// Enable error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define application constants
define('APP_ROOT', dirname(__FILE__));
define('DB_HOST', 'localhost');
define('DB_NAME', 'child_education');
define('DB_USER', 'root');
define('DB_PASS', '');

// Require necessary files
require_once APP_ROOT . '/includes/Database.php';
require_once APP_ROOT . '/includes/Auth.php';
require_once APP_ROOT . '/includes/Student.php';
require_once APP_ROOT . '/includes/School.php';
require_once APP_ROOT . '/includes/Course.php';

// Start session
session_start();

/**
 * Main Application Class
 */
class ChildEducationPortal {
    private $db;
    private $auth;
    private $student;
    private $school;
    private $course;

    public function __construct() {
        try {
            // Initialize database connection
            $this->db = new Database(DB_HOST, DB_NAME, DB_USER, DB_PASS);
            
            // Initialize modules
            $this->auth = new Auth($this->db);
            $this->student = new Student($this->db);
            $this->school = new School($this->db);
            $this->course = new Course($this->db);
            
            // Handle routing
            $this->routeRequest();
        } catch (PDOException $e) {
            $this->handleError("Database connection failed: " . $e->getMessage());
        } catch (Exception $e) {
            $this->handleError("Application error: " . $e->getMessage());
        }
    }

    private function routeRequest() {
        $action = $_GET['action'] ?? 'home';
        
        switch ($action) {
            case 'login':
                $this->handleLogin();
                break;
            case 'register':
                $this->handleRegistration();
                break;
            case 'dashboard':
                $this->showDashboard();
                break;
            case 'courses':
                $this->showCourses();
                break;
            case 'schools':
                $this->showSchools();
                break;
            case 'logout':
                $this->handleLogout();
                break;
            case 'home':
            default:
                $this->showHome();
                break;
        }
    }

    private function handleLogin() {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $email = $_POST['email'] ?? '';
            $password = $_POST['password'] ?? '';
            
            try {
                $user = $this->auth->login($email, $password);
                if ($user) {
                    $_SESSION['user'] = $user;
                    header('Location: index.php?action=dashboard');
                    exit;
                } else {
                    throw new Exception("Invalid credentials");
                }
            } catch (Exception $e) {
                $this->handleError($e->getMessage());
            }
        } else {
            include APP_ROOT . '/views/login.php';
        }
    }

    private function handleRegistration() {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $name = $_POST['name'] ?? '';
            $email = $_POST['email'] ?? '';
            $password = $_POST['password'] ?? '';
            $role = $_POST['role'] ?? 'student';
            
            try {
                $userId = $this->auth->register($name, $email, $password, $role);
                if ($userId) {
                    $_SESSION['user'] = $this->auth->getUserById($userId);
                    header('Location: index.php?action=dashboard');
                    exit;
                }
            } catch (Exception $e) {
                $this->handleError($e->getMessage());
            }
        } else {
            include APP_ROOT . '/views/register.php';
        }
    }

    private function showDashboard() {
        $this->checkAuth();
        $user = $_SESSION['user'];
        
        if ($user['role'] === 'student') {
            $courses = $this->student->getEnrolledCourses($user['id']);
            $schools = $this->school->getAllSchools();
        } else {
            $courses = $this->course->getAllCourses();
            $schools = $this->school->getAllSchools();
        }
        
        include APP_ROOT . '/views/dashboard.php';
    }

    private function showCourses() {
        $this->checkAuth();
        $courses = $this->course->getAllCourses();
        include APP_ROOT . '/views/courses.php';
    }

    private function showSchools() {
        $this->checkAuth();
        $schools = $this->school->getAllSchools();
        include APP_ROOT . '/views/schools.php';
    }

    private function handleLogout() {
        session_destroy();
        header('Location: index.php');
        exit;
    }

    private function showHome() {
        include APP_ROOT . '/views/home.php';
    }

    private function checkAuth() {
        if (!isset($_SESSION['user'])) {
            header('Location: index.php?action=login');
            exit;
        }
    }

    private function handleError($message) {
        $_SESSION['error'] = $message;
        include APP_ROOT . '/views/error.php';
        exit;
    }
}

// Initialize the application
new ChildEducationPortal();
```

```php
<?php
/**
 * Database Class
 * Handles database connection and queries
 */

class Database {
    private $connection;

    public function __construct($host, $dbname, $username, $password) {
        try {
            $this->connection = new PDO(
                "mysql:host=$host;dbname=$dbname;charset=utf8",
                $username,
                $password
            );
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            throw new Exception("Database connection failed: " . $e->getMessage());
        }
    }

    public function query($sql, $params = []) {
        try {
            $stmt = $this->connection->prepare($sql);
            $stmt->execute($params);
            return $stmt;
        } catch (PDOException $e) {
            throw new Exception("Query failed: " . $e->getMessage());
        }
    }

    public function getLastInsertId() {
        return $this->connection->lastInsertId();
    }
}
```

```php
<?php
/**
 * Authentication Class
 * Handles user authentication and authorization
 */

class Auth {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    public function register($name, $email, $password, $role = 'student') {
        // Validate input
        if (empty($name) || empty($email) || empty($password)) {
            throw new Exception("All fields are required");
        }

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid email format");
        }

        // Check if user exists
        $stmt = $this->db->query("SELECT id FROM users WHERE email = ?", [$email]);
        if ($stmt->rowCount() > 0) {
            throw new Exception("Email already registered");
        }

        // Hash password
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Insert user
        $this->db->query(
            "INSERT INTO users (name, email, password, role, created_at) VALUES (?, ?, ?, ?, NOW())",
            [$name, $email, $hashedPassword, $role]
        );

        return $this->db->getLastInsertId();
    }

    public function login($email, $password) {
        $stmt = $this->db->query("SELECT * FROM users WHERE email = ?", [$email]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($password, $user['password'])) {
            unset($user['password']);
            return $user;
        }

        return false;
    }

    public function getUserById($id) {
        $stmt = $this->db->query("SELECT id, name, email, role FROM users WHERE id = ?", [$id]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }
}
```

```php
<?php
/**
 * Student Class
 * Handles student-related operations
 */

class Student {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    public function getEnrolledCourses($studentId) {
        $stmt = $this->db->query(
            "SELECT c.* FROM courses c 
            JOIN student_courses sc ON c.id = sc.course_id 
            WHERE sc.student_id = ?",
            [$studentId]
        );
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function enroll
