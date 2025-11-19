"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: "Create a scheduling system in PHP for managing appointments and emergency roof services, ensuring efficient allocation of resources."
Generated: DETERMINISTIC_23ed4bdb4e77f07b
Batch ID: 20250622_210655
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
 * Appointment Scheduling System for Roof Services
 * 
 * This system manages both regular appointments and emergency roof services,
 * ensuring efficient allocation of resources.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'roof_service_scheduler');

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

    public function close() {
        $this->connection->close();
    }
}

/**
 * Appointment class representing a scheduled service
 */
class Appointment {
    private $db;
    private $id;
    private $customerName;
    private $customerPhone;
    private $address;
    private $serviceType;
    private $scheduledDate;
    private $status;
    private $isEmergency;
    private $assignedTeamId;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    // Getters and setters
    public function getId() { return $this->id; }
    public function getCustomerName() { return $this->customerName; }
    public function getCustomerPhone() { return $this->customerPhone; }
    public function getAddress() { return $this->address; }
    public function getServiceType() { return $this->serviceType; }
    public function getScheduledDate() { return $this->scheduledDate; }
    public function getStatus() { return $this->status; }
    public function getIsEmergency() { return $this->isEmergency; }
    public function getAssignedTeamId() { return $this->assignedTeamId; }

    public function setCustomerName($name) { $this->customerName = $name; }
    public function setCustomerPhone($phone) { $this->customerPhone = $phone; }
    public function setAddress($address) { $this->address = $address; }
    public function setServiceType($type) { $this->serviceType = $type; }
    public function setScheduledDate($date) { $this->scheduledDate = $date; }
    public function setStatus($status) { $this->status = $status; }
    public function setIsEmergency($emergency) { $this->isEmergency = $emergency; }
    public function setAssignedTeamId($teamId) { $this->assignedTeamId = $teamId; }

    /**
     * Save appointment to database
     */
    public function save() {
        $conn = $this->db->getConnection();
        
        if ($this->id) {
            // Update existing appointment
            $stmt = $conn->prepare("UPDATE appointments SET 
                customer_name = ?, 
                customer_phone = ?, 
                address = ?, 
                service_type = ?, 
                scheduled_date = ?, 
                status = ?, 
                is_emergency = ?, 
                assigned_team_id = ? 
                WHERE id = ?");
            
            $stmt->bind_param("ssssssiii", 
                $this->customerName,
                $this->customerPhone,
                $this->address,
                $this->serviceType,
                $this->scheduledDate,
                $this->status,
                $this->isEmergency,
                $this->assignedTeamId,
                $this->id
            );
        } else {
            // Create new appointment
            $stmt = $conn->prepare("INSERT INTO appointments (
                customer_name, 
                customer_phone, 
                address, 
                service_type, 
                scheduled_date, 
                status, 
                is_emergency, 
                assigned_team_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
            
            $stmt->bind_param("ssssssii", 
                $this->customerName,
                $this->customerPhone,
                $this->address,
                $this->serviceType,
                $this->scheduledDate,
                $this->status,
                $this->isEmergency,
                $this->assignedTeamId
            );
        }
        
        if (!$stmt->execute()) {
            throw new Exception("Failed to save appointment: " . $stmt->error);
        }
        
        if (!$this->id) {
            $this->id = $conn->insert_id;
        }
        
        $stmt->close();
    }

    /**
     * Load appointment from database by ID
     */
    public function load($id) {
        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("SELECT * FROM appointments WHERE id = ?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result->num_rows === 0) {
            throw new Exception("Appointment not found");
        }
        
        $row = $result->fetch_assoc();
        $this->id = $row['id'];
        $this->customerName = $row['customer_name'];
        $this->customerPhone = $row['customer_phone'];
        $this->address = $row['address'];
        $this->serviceType = $row['service_type'];
        $this->scheduledDate = $row['scheduled_date'];
        $this->status = $row['status'];
        $this->isEmergency = $row['is_emergency'];
        $this->assignedTeamId = $row['assigned_team_id'];
        
        $stmt->close();
    }

    /**
     * Delete appointment from database
     */
    public function delete() {
        if (!$this->id) {
            throw new Exception("Cannot delete unsaved appointment");
        }
        
        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("DELETE FROM appointments WHERE id = ?");
        $stmt->bind_param("i", $this->id);
        
        if (!$stmt->execute()) {
            throw new Exception("Failed to delete appointment: " . $stmt->error);
        }
        
        $stmt->close();
    }
}

/**
 * ServiceTeam class representing a team of roof service professionals
 */
class ServiceTeam {
    private $db;
    private $id;
    private $teamName;
    private $members;
    private $availability;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    // Getters and setters
    public function getId() { return $this->id; }
    public function getTeamName() { return $this->teamName; }
    public function getMembers() { return $this->members; }
    public function getAvailability() { return $this->availability; }

    public function setTeamName($name) { $this->teamName = $name; }
    public function setMembers($members) { $this->members = $members; }
    public function setAvailability($availability) { $this->availability = $availability; }

    /**
     * Save team to database
     */
    public function save() {
        $conn = $this->db->getConnection();
        
        if ($this->id) {
            // Update existing team
            $stmt = $conn->prepare("UPDATE service_teams SET 
                team_name = ?, 
                members = ?, 
                availability = ? 
                WHERE id = ?");
            
            $stmt->bind_param("sssi", 
                $this->teamName,
                $this->members,
                $this->availability,
                $this->id
            );
        } else {
            // Create new team
            $stmt = $conn->prepare("INSERT INTO service_teams (
                team_name, 
                members, 
                availability
            ) VALUES (?, ?, ?)");
            
            $stmt->bind_param("sss", 
                $this->teamName,
                $this->members,
                $this->availability
            );
        }
        
        if (!$stmt->execute()) {
            throw new Exception("Failed to save team: " . $stmt->error);
        }
        
        if (!$this->id) {
            $this->id = $conn->insert_id;
        }
        
        $stmt->close();
    }

    /**
     * Load team from database by ID
     */
    public function load($id) {
        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("SELECT * FROM service_teams WHERE id = ?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result->num_rows === 0) {
            throw new Exception("Team not found");
        }
        
        $row = $result->fetch_assoc();
        $this->id = $row['id'];
        $this->teamName = $row['team_name'];
        $this->members = $row['members'];
        $this->availability = $row['availability'];
        
        $stmt->close();
    }

    /**
     * Check
