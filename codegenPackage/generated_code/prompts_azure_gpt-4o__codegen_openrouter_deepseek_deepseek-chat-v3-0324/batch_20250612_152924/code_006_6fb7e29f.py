"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Provide a code example for creating a bot panel system in PHP, referencing the "Hamsafar bot panel" project from Hadi Dadkhah's portfolio.
Generated: DETERMINISTIC_6fb7e29f612c8905
Batch ID: 20250612_152924
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
 * Hamsafar Bot Panel System
 * 
 * A PHP-based bot management panel inspired by Hadi Dadkhah's portfolio project.
 * This system allows administrators to manage bots, view statistics, and configure settings.
 */

// Ensure strict types for better type safety
declare(strict_types=1);

// Namespace for better organization
namespace Hamsafar\BotPanel;

// Import required dependencies
use PDO;
use PDOException;

/**
 * Database Configuration Class
 */
class DatabaseConfig {
    private string $host;
    private string $username;
    private string $password;
    private string $database;

    public function __construct(string $host, string $username, string $password, string $database) {
        $this->host = $host;
        $this->username = $username;
        $this->password = $password;
        $this->database = $database;
    }

    public function getDSN(): string {
        return "mysql:host={$this->host};dbname={$this->database};charset=utf8mb4";
    }

    public function getUsername(): string {
        return $this->username;
    }

    public function getPassword(): string {
        return $this->password;
    }
}

/**
 * Database Connection Handler
 */
class Database {
    private PDO $connection;

    public function __construct(DatabaseConfig $config) {
        try {
            $this->connection = new PDO(
                $config->getDSN(),
                $config->getUsername(),
                $config->getPassword(),
                [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                    PDO::ATTR_EMULATE_PREPARES => false,
                ]
            );
        } catch (PDOException $e) {
            throw new \RuntimeException("Database connection failed: " . $e->getMessage());
        }
    }

    public function getConnection(): PDO {
        return $this->connection;
    }
}

/**
 * Bot Manager Class
 */
class BotManager {
    private Database $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Get all bots from database
     */
    public function getAllBots(): array {
        try {
            $stmt = $this->db->getConnection()->query("SELECT * FROM bots WHERE is_active = 1");
            return $stmt->fetchAll();
        } catch (PDOException $e) {
            error_log("Failed to fetch bots: " . $e->getMessage());
            return [];
        }
    }

    /**
     * Get bot by ID
     */
    public function getBotById(int $id): ?array {
        try {
            $stmt = $this->db->getConnection()->prepare("SELECT * FROM bots WHERE id = ?");
            $stmt->execute([$id]);
            $result = $stmt->fetch();
            return $result ?: null;
        } catch (PDOException $e) {
            error_log("Failed to fetch bot with ID {$id}: " . $e->getMessage());
            return null;
        }
    }

    /**
     * Create a new bot
     */
    public function createBot(array $botData): bool {
        try {
            $stmt = $this->db->getConnection()->prepare(
                "INSERT INTO bots (name, token, description, created_at) VALUES (?, ?, ?, NOW())"
            );
            return $stmt->execute([
                $botData['name'],
                $botData['token'],
                $botData['description']
            ]);
        } catch (PDOException $e) {
            error_log("Failed to create bot: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Update bot information
     */
    public function updateBot(int $id, array $botData): bool {
        try {
            $stmt = $this->db->getConnection()->prepare(
                "UPDATE bots SET name = ?, token = ?, description = ?, updated_at = NOW() WHERE id = ?"
            );
            return $stmt->execute([
                $botData['name'],
                $botData['token'],
                $botData['description'],
                $id
            ]);
        } catch (PDOException $e) {
            error_log("Failed to update bot with ID {$id}: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Delete a bot (soft delete)
     */
    public function deleteBot(int $id): bool {
        try {
            $stmt = $this->db->getConnection()->prepare(
                "UPDATE bots SET is_active = 0, deleted_at = NOW() WHERE id = ?"
            );
            return $stmt->execute([$id]);
        } catch (PDOException $e) {
            error_log("Failed to delete bot with ID {$id}: " . $e->getMessage());
            return false;
        }
    }
}

/**
 * Authentication Class
 */
class Auth {
    private Database $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Login user
     */
    public function login(string $username, string $password): bool {
        try {
            $stmt = $this->db->getConnection()->prepare(
                "SELECT id, password FROM users WHERE username = ? AND is_active = 1"
            );
            $stmt->execute([$username]);
            $user = $stmt->fetch();

            if ($user && password_verify($password, $user['password'])) {
                $_SESSION['user_id'] = $user['id'];
                return true;
            }
            return false;
        } catch (PDOException $e) {
            error_log("Login failed for user {$username}: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Check if user is logged in
     */
    public function isLoggedIn(): bool {
        return isset($_SESSION['user_id']);
    }

    /**
     * Logout user
     */
    public function logout(): void {
        session_unset();
        session_destroy();
    }
}

/**
 * Bot Panel Controller
 */
class BotPanelController {
    private BotManager $botManager;
    private Auth $auth;

    public function __construct(BotManager $botManager, Auth $auth) {
        $this->botManager = $botManager;
        $this->auth = $auth;
    }

    /**
     * Handle dashboard request
     */
    public function dashboard(): void {
        if (!$this->auth->isLoggedIn()) {
            header("Location: login.php");
            exit;
        }

        $bots = $this->botManager->getAllBots();
        include 'views/dashboard.php';
    }

    /**
     * Handle bot creation request
     */
    public function createBot(array $data): void {
        if (!$this->auth->isLoggedIn()) {
            header("Location: login.php");
            exit;
        }

        if ($this->botManager->createBot($data)) {
            $_SESSION['success'] = "Bot created successfully!";
        } else {
            $_SESSION['error'] = "Failed to create bot.";
        }
        header("Location: dashboard.php");
        exit;
    }

    /**
     * Handle bot update request
     */
    public function updateBot(int $id, array $data): void {
        if (!$this->auth->isLoggedIn()) {
            header("Location: login.php");
            exit;
        }

        if ($this->botManager->updateBot($id, $data)) {
            $_SESSION['success'] = "Bot updated successfully!";
        } else {
            $_SESSION['error'] = "Failed to update bot.";
        }
        header("Location: dashboard.php");
        exit;
    }

    /**
     * Handle bot deletion request
     */
    public function deleteBot(int $id): void {
        if (!$this->auth->isLoggedIn()) {
            header("Location: login.php");
            exit;
        }

        if ($this->botManager->deleteBot($id)) {
            $_SESSION['success'] = "Bot deleted successfully!";
        } else {
            $_SESSION['error'] = "Failed to delete bot.";
        }
        header("Location: dashboard.php");
        exit;
    }
}

// Initialize session
session_start();

// Configuration
$config = new DatabaseConfig(
    'localhost',
    'hamsafar_user',
    'secure_password',
    'hamsafar_bot_panel'
);

// Initialize components
try {
    $db = new Database($config);
    $botManager = new BotManager($db);
    $auth = new Auth($db);
    $controller = new BotPanelController($botManager, $auth);
} catch (\RuntimeException $e) {
    die("System initialization failed: " . $e->getMessage());
}

// Handle requests
$action = $_GET['action'] ?? 'dashboard';

switch ($action) {
    case 'create':
        $controller->createBot($_POST);
        break;
    case 'update':
        $controller->updateBot((int)$_POST['id'], $_POST);
        break;
    case 'delete':
        $controller->deleteBot((int)$_GET['id']);
