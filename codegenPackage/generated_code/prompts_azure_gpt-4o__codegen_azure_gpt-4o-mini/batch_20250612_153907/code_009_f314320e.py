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
$host = 'localhost'; // Database host
$dbname = 'profiles_db'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

/**
 * Function to create a new profile
 *
 * @param string $name Name of the profile
 * @param string $profession Profession of the profile
 * @param string $description Description of the profile
 * @return bool True on success, false on failure
 */
function createProfile($name, $profession, $description) {
    global $pdo;

    // Prepare SQL statement
    $sql = "INSERT INTO profiles (name, profession, description) VALUES (:name, :profession, :description)";
    $stmt = $pdo->prepare($sql);

    // Bind parameters
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':profession', $profession);
    $stmt->bindParam(':description', $description);

    // Execute the statement and return the result
    return $stmt->execute();
}

/**
 * Function to retrieve profiles by profession
 *
 * @param string $profession Profession to filter profiles
 * @return array Array of profiles
 */
function getProfilesByProfession($profession) {
    global $pdo;

    // Prepare SQL statement
    $sql = "SELECT * FROM profiles WHERE profession = :profession";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':profession', $profession);
    $stmt->execute();

    // Fetch all profiles as an associative array
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $profession = filter_input(INPUT_POST, 'profession', FILTER_SANITIZE_STRING);
    $description = filter_input(INPUT_POST, 'description', FILTER_SANITIZE_STRING);

    // Create a new profile
    if (createProfile($name, $profession, $description)) {
        echo "Profile created successfully.";
    } else {
        echo "Error creating profile.";
    }
}

// Retrieve profiles by profession if profession is set
if (isset($_GET['profession'])) {
    $profession = filter_input(INPUT_GET, 'profession', FILTER_SANITIZE_STRING);
    $profiles = getProfilesByProfession($profession);

    // Display profiles
    if ($profiles) {
        foreach ($profiles as $profile) {
            echo "Name: " . htmlspecialchars($profile['name']) . "<br>";
            echo "Profession: " . htmlspecialchars($profile['profession']) . "<br>";
            echo "Description: " . htmlspecialchars($profile['description']) . "<br><br>";
        }
    } else {
        echo "No profiles found for this profession.";
    }
}
?>
```

```sql
-- SQL to create the profiles table
CREATE TABLE profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    profession VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);
```

**Note:** Ensure to create the database and the `profiles` table using the provided SQL before running the PHP code. Adjust the database connection parameters as necessary.
