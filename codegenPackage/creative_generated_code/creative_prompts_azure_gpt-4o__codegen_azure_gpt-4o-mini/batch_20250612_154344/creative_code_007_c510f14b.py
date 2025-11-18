"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infy.uk
Prompt: Explain how to set up a free InfinityFree hosting account and deploy a custom PHP application.
Generated: DETERMINISTIC_c510f14b2c7e4e01
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * index.php
 * A simple example of a custom PHP application to be deployed on InfinityFree hosting.
 * This script demonstrates basic CRUD operations with error handling.
 */

// Database connection parameters
$servername = "localhost"; // InfinityFree uses localhost for database connection
$username = "your_db_username"; // Replace with your database username
$password = "your_db_password"; // Replace with your database password
$dbname = "your_db_name"; // Replace with your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to create a new record
function createRecord($conn, $data) {
    $stmt = $conn->prepare("INSERT INTO your_table_name (column1, column2) VALUES (?, ?)");
    $stmt->bind_param("ss", $data['column1'], $data['column2']);
    
    if ($stmt->execute()) {
        return "New record created successfully";
    } else {
        return "Error: " . $stmt->error;
    }
}

// Function to read records
function readRecords($conn) {
    $sql = "SELECT id, column1, column2 FROM your_table_name";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Output data of each row
        while($row = $result->fetch_assoc()) {
            echo "id: " . $row["id"]. " - Column1: " . $row["column1"]. " - Column2: " . $row["column2"]. "<br>";
        }
    } else {
        echo "0 results";
    }
}

// Function to update a record
function updateRecord($conn, $id, $data) {
    $stmt = $conn->prepare("UPDATE your_table_name SET column1 = ?, column2 = ? WHERE id = ?");
    $stmt->bind_param("ssi", $data['column1'], $data['column2'], $id);
    
    if ($stmt->execute()) {
        return "Record updated successfully";
    } else {
        return "Error: " . $stmt->error;
    }
}

// Function to delete a record
function deleteRecord($conn, $id) {
    $stmt = $conn->prepare("DELETE FROM your_table_name WHERE id = ?");
    $stmt->bind_param("i", $id);
    
    if ($stmt->execute()) {
        return "Record deleted successfully";
    } else {
        return "Error: " . $stmt->error;
    }
}

// Example usage
$data = ['column1' => 'Value1', 'column2' => 'Value2'];
echo createRecord($conn, $data);
readRecords($conn);
echo updateRecord($conn, 1, ['column1' => 'UpdatedValue1', 'column2' => 'UpdatedValue2']);
echo deleteRecord($conn, 1);

// Close connection
$conn->close();
?>
```

**Note:** 
- Replace `your_db_username`, `your_db_password`, `your_db_name`, `your_table_name`, `column1`, and `column2` with actual values specific to your InfinityFree account and database schema.
- Ensure that you have set up a MySQL database on InfinityFree and created the necessary table to receive the data.
