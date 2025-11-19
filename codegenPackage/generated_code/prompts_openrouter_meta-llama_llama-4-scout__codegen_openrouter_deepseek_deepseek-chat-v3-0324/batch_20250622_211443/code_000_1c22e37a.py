"""
Generated Code Metadata:
========================
Original URL: https://sophon-farming.pro
Prompt: How can I implement a farm management system using PHP, similar to what is seen on sophon-farming.pro, focusing on integrating key data like crop rotation and soil health?
Generated: DETERMINISTIC_1c22e37aed6cd940
Batch ID: 20250622_211443
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
 * Farm Management System
 * 
 * This script provides functionality to manage farm data including crop rotation and soil health.
 * It includes CRUD operations for farm records with proper error handling and data validation.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'farm_management');

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        $this->connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($this->connection->connect_error) {
            throw new Exception("Database connection failed: " . $this->connection->connect_error);
        }
    }

    public function getConnection() {
        return $this->connection;
    }

    public function closeConnection() {
        $this->connection->close();
    }
}

/**
 * Farm Management Class
 */
class FarmManagement {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Add a new farm record
     * 
     * @param string $name Farm name
     * @param string $location Farm location
     * @param float $size Farm size in acres
     * @param string $soilType Type of soil
     * @param string $rotationPlan Crop rotation plan
     * @return int ID of the inserted record
     * @throws Exception On validation or database error
     */
    public function addFarm($name, $location, $size, $soilType, $rotationPlan) {
        // Validate input
        if (empty($name) || empty($location) || $size <= 0) {
            throw new Exception("Invalid farm data provided");
        }

        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("INSERT INTO farms (name, location, size, soil_type, rotation_plan) VALUES (?, ?, ?, ?, ?)");
        
        if (!$stmt) {
            throw new Exception("Database preparation error: " . $conn->error);
        }

        $stmt->bind_param("ssdss", $name, $location, $size, $soilType, $rotationPlan);
        
        if (!$stmt->execute()) {
            throw new Exception("Database execution error: " . $stmt->error);
        }

        $insertId = $stmt->insert_id;
        $stmt->close();
        
        return $insertId;
    }

    /**
     * Get farm by ID
     * 
     * @param int $id Farm ID
     * @return array Farm data
     * @throws Exception On database error or if farm not found
     */
    public function getFarm($id) {
        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("SELECT * FROM farms WHERE id = ?");
        
        if (!$stmt) {
            throw new Exception("Database preparation error: " . $conn->error);
        }

        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result->num_rows === 0) {
            $stmt->close();
            throw new Exception("Farm not found");
        }

        $farm = $result->fetch_assoc();
        $stmt->close();
        
        return $farm;
    }

    /**
     * Update farm record
     * 
     * @param int $id Farm ID
     * @param array $data Associative array of fields to update
     * @return bool True on success
     * @throws Exception On validation or database error
     */
    public function updateFarm($id, $data) {
        if (empty($id) || empty($data)) {
            throw new Exception("Invalid data provided for update");
        }

        $allowedFields = ['name', 'location', 'size', 'soil_type', 'rotation_plan'];
        $updates = [];
        $params = [];
        $types = '';

        foreach ($data as $field => $value) {
            if (in_array($field, $allowedFields)) {
                $updates[] = "$field = ?";
                $params[] = $value;
                $types .= $field === 'size' ? 'd' : 's';
            }
        }

        if (empty($updates)) {
            throw new Exception("No valid fields to update");
        }

        $conn = $this->db->getConnection();
        $sql = "UPDATE farms SET " . implode(', ', $updates) . " WHERE id = ?";
        $stmt = $conn->prepare($sql);
        
        if (!$stmt) {
            throw new Exception("Database preparation error: " . $conn->error);
        }

        $params[] = $id;
        $types .= 'i';
        $stmt->bind_param($types, ...$params);
        
        if (!$stmt->execute()) {
            throw new Exception("Database execution error: " . $stmt->error);
        }

        $affectedRows = $stmt->affected_rows;
        $stmt->close();
        
        return $affectedRows > 0;
    }

    /**
     * Delete farm record
     * 
     * @param int $id Farm ID
     * @return bool True on success
     * @throws Exception On database error
     */
    public function deleteFarm($id) {
        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("DELETE FROM farms WHERE id = ?");
        
        if (!$stmt) {
            throw new Exception("Database preparation error: " . $conn->error);
        }

        $stmt->bind_param("i", $id);
        
        if (!$stmt->execute()) {
            throw new Exception("Database execution error: " . $stmt->error);
        }

        $affectedRows = $stmt->affected_rows;
        $stmt->close();
        
        return $affectedRows > 0;
    }

    /**
     * Get all farms with optional filters
     * 
     * @param array $filters Associative array of filters
     * @return array List of farms
     * @throws Exception On database error
     */
    public function getAllFarms($filters = []) {
        $conn = $this->db->getConnection();
        $sql = "SELECT * FROM farms";
        $where = [];
        $params = [];
        $types = '';

        // Build WHERE clause if filters are provided
        if (!empty($filters)) {
            foreach ($filters as $field => $value) {
                $where[] = "$field = ?";
                $params[] = $value;
                $types .= $field === 'size' ? 'd' : 's';
            }
            
            if (!empty($where)) {
                $sql .= " WHERE " . implode(' AND ', $where);
            }
        }

        $stmt = $conn->prepare($sql);
        
        if (!$stmt) {
            throw new Exception("Database preparation error: " . $conn->error);
        }

        if (!empty($params)) {
            $stmt->bind_param($types, ...$params);
        }

        $stmt->execute();
        $result = $stmt->get_result();
        $farms = $result->fetch_all(MYSQLI_ASSOC);
        $stmt->close();
        
        return $farms;
    }
}

/**
 * Soil Health Tracker Class
 */
class SoilHealthTracker {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Record soil health data for a farm
     * 
     * @param int $farmId Farm ID
     * @param float $ph Soil pH level
     * @param float $organicMatter Percentage of organic matter
     * @param float $nitrogen Nitrogen level
     * @param float $phosphorus Phosphorus level
     * @param float $potassium Potassium level
     * @param string $date Test date (YYYY-MM-DD)
     * @return int ID of the inserted record
     * @throws Exception On validation or database error
     */
    public function recordSoilHealth($farmId, $ph, $organicMatter, $nitrogen, $phosphorus, $potassium, $date) {
        // Validate input
        if ($farmId <= 0 || empty($date)) {
            throw new Exception("Invalid soil health data provided");
        }

        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("INSERT INTO soil_health (farm_id, ph, organic_matter, nitrogen, phosphorus, potassium, test_date) VALUES (?, ?, ?, ?, ?, ?, ?)");
        
        if (!$stmt) {
            throw new Exception("Database preparation error: " . $conn->error);
        }

        $stmt->bind_param("iddddds", $farmId, $ph, $organicMatter, $nitrogen, $phosphorus, $potassium, $date);
        
        if (!$stmt->execute()) {
            throw new Exception("Database execution error: " . $stmt->error);
        }

        $insertId = $stmt->insert_id;
        $stmt->close();
        
        return $insertId;
