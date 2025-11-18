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
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'profiles_db');

// Establish the database connection
function getDatabaseConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check for connection errors
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }

    return $conn;
}

// Function to create the necessary table
function createTable() {
    $conn = getDatabaseConnection();
    $sql = "CREATE TABLE IF NOT EXISTS profiles (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                profession VARCHAR(255) NOT NULL,
                bio TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )";

    if ($conn->query($sql) === TRUE) {
        echo "Table 'profiles' created successfully.\n";
    } else {
        echo "Error creating table: " . $conn->error;
    }

    $conn->close();
}

// Function to add a profile
function addProfile($name, $profession, $bio) {
    $conn = getDatabaseConnection();
    $stmt = $conn->prepare("INSERT INTO profiles (name, profession, bio) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $name, $profession, $bio);

    if ($stmt->execute()) {
        echo "Profile added successfully.\n";
    } else {
        echo "Error adding profile: " . $stmt->error;
    }

    $stmt->close();
    $conn->close();
}

// Function to retrieve profiles by profession
function getProfilesByProfession($profession) {
    $conn = getDatabaseConnection();
    $stmt = $conn->prepare("SELECT id, name, bio, created_at FROM profiles WHERE profession = ?");
    $stmt->bind_param("s", $profession);

    if ($stmt->execute()) {
        $result = $stmt->get_result();
        $profiles = [];

        // Fetch all profiles
        while ($row = $result->fetch_assoc()) {
            $profiles[] = $row;
        }

        $stmt->close();
        $conn->close();
        return $profiles;
    } else {
        echo "Error retrieving profiles: " . $stmt->error;
        $stmt->close();
        $conn->close();
        return [];
    }
}

// Example usage
// Uncomment below lines to test the functionality

// Create the table
// createTable();

// Add profiles
// addProfile('Alice Doe', 'Photographer', 'Alice is a passionate photographer from Sedona.');
// addProfile('Bob Smith', 'Painter', 'Bob specializes in capturing the beauty of the Verde Valley through his paintings.');

// Retrieve and display profiles by profession
/*
$profession = 'Photographer';
$profiles = getProfilesByProfession($profession);
if (!empty($profiles)) {
    echo "Profiles categorized as '$profession':\n";
    foreach ($profiles as $profile) {
        echo "ID: {$profile['id']}\n";
        echo "Name: {$profile['name']}\n";
        echo "Bio: {$profile['bio']}\n";
        echo "Created At: {$profile['created_at']}\n";
        echo "-----------------\n";
    }
} else {
    echo "No profiles found for the profession: $profession.\n";
}
*/
?>
```
