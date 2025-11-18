"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Create code using PHP and MySQL to store and retrieve profiles categorized by profession, similar to the structure of "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_f314320ed670711c
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$host = 'localhost';
$db = 'profiles_db';
$user = 'username';
$pass = 'password';

try {
    // Establish a database connection using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to store a new profile in the database.
 *
 * @param string $name       The name of the individual.
 * @param string $profession The profession of the individual.
 * @param string $description A brief description of the individual.
 * @return bool True on success, false on failure.
 */
function storeProfile($name, $profession, $description) {
    global $pdo;

    // Prepare an SQL statement for execution
    $sql = "INSERT INTO profiles (name, profession, description) VALUES (:name, :profession, :description)";
    $stmt = $pdo->prepare($sql);

    // Bind parameters to prevent SQL injection
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':profession', $profession);
    $stmt->bindParam(':description', $description);

    // Execute the statement and handle errors
    return $stmt->execute();
}

/**
 * Function to retrieve profiles by profession from the database.
 *
 * @param string $profession The profession to filter profiles.
 * @return array An array of profiles matching the profession.
 */
function getProfilesByProfession($profession) {
    global $pdo;

    // Prepare an SQL statement for execution
    $sql = "SELECT * FROM profiles WHERE profession = :profession";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':profession', $profession);
    $stmt->execute();

    // Fetch profiles as an associative array
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Capture form data
    $name = $_POST['name'] ?? '';
    $profession = $_POST['profession'] ?? '';
    $description = $_POST['description'] ?? '';

    // Validate input
    if (!empty($name) && !empty($profession) && !empty($description)) {
        if (storeProfile($name, $profession, $description)) {
            echo "Profile stored successfully.";
        } else {
            echo "Failed to store profile.";
        }
    } else {
        echo "All fields are required.";
    }
}

// Retrieve profiles for a specific profession (e.g., 'Artist')
$profession = 'Artist'; // This can be dynamic based on user input
$profiles = getProfilesByProfession($profession);

// Display the retrieved profiles
if (!empty($profiles)) {
    foreach ($profiles as $profile) {
        echo "Name: " . htmlspecialchars($profile['name']) . "<br>";
        echo "Profession: " . htmlspecialchars($profile['profession']) . "<br>";
        echo "Description: " . htmlspecialchars($profile['description']) . "<br><br>";
    }
} else {
    echo "No profiles found for the profession: " . htmlspecialchars($profession);
}
?>
```

```sql
-- SQL Script to create the database and table
CREATE DATABASE profiles_db;

USE profiles_db;

CREATE TABLE profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    profession VARCHAR(100) NOT NULL,
    description TEXT NOT NULL
);
```

### Note:
- Replace `'username'` and `'password'` in the PHP code with your actual database username and password.
- Ensure that error reporting is appropriately set in production environments to prevent sensitive information from being displayed.
