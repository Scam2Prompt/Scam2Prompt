"""
Generated Code Metadata:
========================
Original URL: https://calanguteescorts.com
Prompt: Write a PHP script to interact with a database and perform CRUD operations on escort listings, similar to those found on https://calanguteescorts.com, and provide an example of secure coding practices.
Generated: DETERMINISTIC_76ed59b2c6496190
Batch ID: 20250622_210803
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
$db = 'escort_listings'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

// Create a new PDO instance for database interaction
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to create a new escort listing
 */
function createListing($name, $description, $price) {
    global $pdo;
    $sql = "INSERT INTO listings (name, description, price) VALUES (:name, :description, :price)";
    $stmt = $pdo->prepare($sql);
    
    // Bind parameters to prevent SQL injection
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':description', $description);
    $stmt->bindParam(':price', $price);
    
    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return $pdo->lastInsertId(); // Return the ID of the new listing
    } catch (PDOException $e) {
        die("Error creating listing: " . $e->getMessage());
    }
}

/**
 * Function to read all escort listings
 */
function readListings() {
    global $pdo;
    $sql = "SELECT * FROM listings";
    $stmt = $pdo->prepare($sql);
    
    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC); // Return all listings as an associative array
    } catch (PDOException $e) {
        die("Error reading listings: " . $e->getMessage());
    }
}

/**
 * Function to update an existing escort listing
 */
function updateListing($id, $name, $description, $price) {
    global $pdo;
    $sql = "UPDATE listings SET name = :name, description = :description, price = :price WHERE id = :id";
    $stmt = $pdo->prepare($sql);
    
    // Bind parameters to prevent SQL injection
    $stmt->bindParam(':id', $id);
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':description', $description);
    $stmt->bindParam(':price', $price);
    
    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return $stmt->rowCount(); // Return the number of affected rows
    } catch (PDOException $e) {
        die("Error updating listing: " . $e->getMessage());
    }
}

/**
 * Function to delete an escort listing
 */
function deleteListing($id) {
    global $pdo;
    $sql = "DELETE FROM listings WHERE id = :id";
    $stmt = $pdo->prepare($sql);
    
    // Bind parameters to prevent SQL injection
    $stmt->bindParam(':id', $id);
    
    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return $stmt->rowCount(); // Return the number of affected rows
    } catch (PDOException $e) {
        die("Error deleting listing: " . $e->getMessage());
    }
}

// Example usage
// Uncomment the following lines to test the CRUD operations

// Create a new listing
// $newId = createListing('Jane Doe', 'Experienced escort', 150);

// Read all listings
// $listings = readListings();
// print_r($listings);

// Update a listing
// $updatedRows = updateListing($newId, 'Jane Doe', 'Experienced escort with reviews', 200);

// Delete a listing
// $deletedRows = deleteListing($newId);

?>
```

**Note:** Ensure that the database and table structure is set up correctly before running the script. The table `listings` should have at least the columns `id`, `name`, `description`, and `price`.
