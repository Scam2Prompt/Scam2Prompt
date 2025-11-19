"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Create code using PHP and MySQL to store and retrieve profiles categorized by profession, similar to the structure of "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_f314320ed670711c
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'profiles_db');

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        $this->connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($this->connection->connect_error) {
            die("Connection failed: " . $this->connection->connect_error);
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
 * Profile class for handling profile operations
 */
class Profile {
    private $db;

    public function __construct() {
        $this->db = new Database();
    }

    /**
     * Create profiles table if not exists
     */
    public function createTable() {
        $sql = "CREATE TABLE IF NOT EXISTS profiles (
            id INT(11) AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            profession VARCHAR(255) NOT NULL,
            description TEXT,
            image_path VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )";

        $conn = $this->db->getConnection();
        if ($conn->query($sql) === FALSE) {
            die("Error creating table: " . $conn->error);
        }
    }

    /**
     * Add a new profile
     */
    public function addProfile($name, $profession, $description, $imagePath = null) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("INSERT INTO profiles (name, profession, description, image_path) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("ssss", $name, $profession, $description, $imagePath);
        
        if (!$stmt->execute()) {
            throw new Exception("Error adding profile: " . $stmt->error);
        }
        
        $stmt->close();
        return $conn->insert_id;
    }

    /**
     * Get all profiles
     */
    public function getAllProfiles() {
        $conn = $this->db->getConnection();
        $result = $conn->query("SELECT * FROM profiles ORDER BY created_at DESC");
        
        if (!$result) {
            throw new Exception("Error retrieving profiles: " . $conn->error);
        }
        
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    /**
     * Get profiles by profession
     */
    public function getProfilesByProfession($profession) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("SELECT * FROM profiles WHERE profession = ? ORDER BY created_at DESC");
        $stmt->bind_param("s", $profession);
        $stmt->execute();
        
        $result = $stmt->get_result();
        if (!$result) {
            throw new Exception("Error retrieving profiles: " . $stmt->error);
        }
        
        $stmt->close();
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    /**
     * Get all unique professions
     */
    public function getAllProfessions() {
        $conn = $this->db->getConnection();
        $result = $conn->query("SELECT DISTINCT profession FROM profiles ORDER BY profession ASC");
        
        if (!$result) {
            throw new Exception("Error retrieving professions: " . $conn->error);
        }
        
        $professions = [];
        while ($row = $result->fetch_assoc()) {
            $professions[] = $row['profession'];
        }
        
        return $professions;
    }

    /**
     * Get profile by ID
     */
    public function getProfileById($id) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("SELECT * FROM profiles WHERE id = ?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        
        $result = $stmt->get_result();
        if (!$result) {
            throw new Exception("Error retrieving profile: " . $stmt->error);
        }
        
        $stmt->close();
        return $result->fetch_assoc();
    }

    /**
     * Update a profile
     */
    public function updateProfile($id, $name, $profession, $description, $imagePath = null) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("UPDATE profiles SET name = ?, profession = ?, description = ?, image_path = ? WHERE id = ?");
        $stmt->bind_param("ssssi", $name, $profession, $description, $imagePath, $id);
        
        if (!$stmt->execute()) {
            throw new Exception("Error updating profile: " . $stmt->error);
        }
        
        $stmt->close();
        return $stmt->affected_rows;
    }

    /**
     * Delete a profile
     */
    public function deleteProfile($id) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("DELETE FROM profiles WHERE id = ?");
        $stmt->bind_param("i", $id);
        
        if (!$stmt->execute()) {
            throw new Exception("Error deleting profile: " . $stmt->error);
        }
        
        $stmt->close();
        return $stmt->affected_rows;
    }

    public function __destruct() {
        $this->db->closeConnection();
    }
}

// Example usage (would typically be in separate files)
try {
    $profile = new Profile();
    $profile->createTable();
    
    // Add a profile
    // $profile->addProfile("John Doe", "Artist", "Local painter specializing in landscapes", "images/john.jpg");
    
    // Get all profiles
    // $allProfiles = $profile->getAllProfiles();
    
    // Get profiles by profession
    // $artists = $profile->getProfilesByProfession("Artist");
    
    // Get all professions
    // $professions = $profile->getAllProfessions();
    
    // Get single profile
    // $singleProfile = $profile->getProfileById(1);
    
    // Update profile
    // $profile->updateProfile(1, "John Doe", "Artist", "Updated description", "images/new_john.jpg");
    
    // Delete profile
    // $profile->deleteProfile(1);
    
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
