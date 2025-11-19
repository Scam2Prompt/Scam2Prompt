"""
Generated Code Metadata:
========================
Original URL: https://www.izikard.com
Prompt: Generate PHP code for handling NFC tag data on a server, enabling dynamic updates to links and actions, similar to Izikard's platform for managing NFC products.
Generated: DETERMINISTIC_434da8845199f667
Batch ID: 20250612_153224
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
 * NFC Tag Data Handler
 * 
 * This script provides an API for managing NFC tag data, allowing dynamic updates
 * to links and actions associated with NFC products.
 */

// Enable strict typing and error reporting
declare(strict_types=1);
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'nfc_tags_db');
define('DB_USER', 'nfc_user');
define('DB_PASS', 'secure_password');

// API response constants
define('STATUS_SUCCESS', 'success');
define('STATUS_ERROR', 'error');

/**
 * Database connection class
 */
class Database {
    private static $instance = null;
    private $connection;

    private function __construct() {
        try {
            $this->connection = new PDO(
                "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME,
                DB_USER,
                DB_PASS,
                [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                    PDO::ATTR_EMULATE_PREPARES => false,
                ]
            );
        } catch (PDOException $e) {
            $this->handleError("Database connection failed: " . $e->getMessage());
        }
    }

    public static function getInstance(): Database {
        if (!self::$instance) {
            self::$instance = new Database();
        }
        return self::$instance;
    }

    public function getConnection(): PDO {
        return $this->connection;
    }

    private function handleError(string $message): void {
        error_log($message);
        header('Content-Type: application/json');
        die(json_encode([
            'status' => STATUS_ERROR,
            'message' => 'Database error occurred'
        ]));
    }
}

/**
 * NFC Tag Manager
 */
class NFCTagManager {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    /**
     * Get tag data by tag ID
     */
    public function getTagData(string $tagId): array {
        try {
            $stmt = $this->db->prepare("SELECT * FROM nfc_tags WHERE tag_id = :tag_id");
            $stmt->execute([':tag_id' => $tagId]);
            $tagData = $stmt->fetch();

            if (!$tagData) {
                return [
                    'status' => STATUS_ERROR,
                    'message' => 'Tag not found'
                ];
            }

            return [
                'status' => STATUS_SUCCESS,
                'data' => $tagData
            ];
        } catch (PDOException $e) {
            error_log("Error fetching tag data: " . $e->getMessage());
            return [
                'status' => STATUS_ERROR,
                'message' => 'Failed to fetch tag data'
            ];
        }
    }

    /**
     * Update tag action
     */
    public function updateTagAction(string $tagId, string $actionType, string $actionValue): array {
        try {
            // Validate action type
            $validActions = ['url', 'text', 'email', 'phone'];
            if (!in_array($actionType, $validActions)) {
                return [
                    'status' => STATUS_ERROR,
                    'message' => 'Invalid action type'
                ];
            }

            $stmt = $this->db->prepare(
                "UPDATE nfc_tags 
                SET action_type = :action_type, action_value = :action_value, updated_at = NOW() 
                WHERE tag_id = :tag_id"
            );

            $stmt->execute([
                ':action_type' => $actionType,
                ':action_value' => $actionValue,
                ':tag_id' => $tagId
            ]);

            if ($stmt->rowCount() === 0) {
                return [
                    'status' => STATUS_ERROR,
                    'message' => 'Tag not found or no changes made'
                ];
            }

            return [
                'status' => STATUS_SUCCESS,
                'message' => 'Tag action updated successfully'
            ];
        } catch (PDOException $e) {
            error_log("Error updating tag action: " . $e->getMessage());
            return [
                'status' => STATUS_ERROR,
                'message' => 'Failed to update tag action'
            ];
        }
    }

    /**
     * Create a new NFC tag
     */
    public function createTag(string $tagId, string $actionType, string $actionValue, string $description = ''): array {
        try {
            // Validate action type
            $validActions = ['url', 'text', 'email', 'phone'];
            if (!in_array($actionType, $validActions)) {
                return [
                    'status' => STATUS_ERROR,
                    'message' => 'Invalid action type'
                ];
            }

            $stmt = $this->db->prepare(
                "INSERT INTO nfc_tags (tag_id, action_type, action_value, description, created_at, updated_at) 
                VALUES (:tag_id, :action_type, :action_value, :description, NOW(), NOW())"
            );

            $stmt->execute([
                ':tag_id' => $tagId,
                ':action_type' => $actionType,
                ':action_value' => $actionValue,
                ':description' => $description
            ]);

            return [
                'status' => STATUS_SUCCESS,
                'message' => 'Tag created successfully',
                'tag_id' => $tagId
            ];
        } catch (PDOException $e) {
            if ($e->getCode() === '23000') {
                return [
                    'status' => STATUS_ERROR,
                    'message' => 'Tag ID already exists'
                ];
            }
            error_log("Error creating tag: " . $e->getMessage());
            return [
                'status' => STATUS_ERROR,
                'message' => 'Failed to create tag'
            ];
        }
    }

    /**
     * Delete a tag
     */
    public function deleteTag(string $tagId): array {
        try {
            $stmt = $this->db->prepare("DELETE FROM nfc_tags WHERE tag_id = :tag_id");
            $stmt->execute([':tag_id' => $tagId]);

            if ($stmt->rowCount() === 0) {
                return [
                    'status' => STATUS_ERROR,
                    'message' => 'Tag not found'
                ];
            }

            return [
                'status' => STATUS_SUCCESS,
                'message' => 'Tag deleted successfully'
            ];
        } catch (PDOException $e) {
            error_log("Error deleting tag: " . $e->getMessage());
            return [
                'status' => STATUS_ERROR,
                'message' => 'Failed to delete tag'
            ];
        }
    }
}

/**
 * API Request Handler
 */
class APIHandler {
    private $tagManager;

    public function __construct() {
        $this->tagManager = new NFCTagManager();
        $this->handleRequest();
    }

    private function handleRequest(): void {
        header('Content-Type: application/json');

        try {
            $method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
            $request = $_REQUEST;

            switch ($method) {
                case 'GET':
                    $this->handleGetRequest($request);
                    break;
                case 'POST':
                    $this->handlePostRequest($request);
                    break;
                case 'PUT':
                    $this->handlePutRequest($request);
                    break;
                case 'DELETE':
                    $this->handleDeleteRequest($request);
                    break;
                default:
                    $this->sendResponse(STATUS_ERROR, 'Method not allowed', 405);
            }
        } catch (Exception $e) {
            $this->sendResponse(STATUS_ERROR, 'Internal server error: ' . $e->getMessage(), 500);
        }
    }

    private function handleGetRequest(array $request): void {
        if (!isset($request['tag_id'])) {
            $this->sendResponse(STATUS_ERROR, 'Missing tag_id parameter', 400);
            return;
        }

        $result = $this->tagManager->getTagData($request['tag_id']);
        $this->sendResponse($result['status'], $result['message'] ?? '', 200, $result['data'] ?? null);
    }

    private function handlePostRequest(array $request): void {
        $required = ['tag_id', 'action_type', 'action_value'];
        foreach ($required as $field) {
            if (!isset($request[$field])) {
                $this->sendResponse(STATUS_ERROR, "Missing required field: $field", 400);
                return;
            }
        }

        $result = $this->tagManager->createTag(
            $request['tag_id'],
            $request['action_type'],
            $request['action_value'],
            $request['description'] ?? ''
        );

        $this->sendResponse($result['status'], $result['message'], $result['status'] === STATUS_SUCCESS ? 201 : 400, $result['tag_id'] ?? null);
    }

    private function handlePutRequest(array $request): void {
        $required = ['tag_id', 'action_type', 'action_value'];
        foreach ($
