"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Write a PHP function to calculate the hash of a file and store it in a database for duplicate file detection, as demonstrated on Omidtak.ir.
Generated: DETERMINISTIC_6eda1cb7fa1db7c8
Batch ID: 20250612_142628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Function to calculate the hash of a file and store it in a database for duplicate file detection
function storeFileHash($filePath, $pdo) {
    // Check if the file exists
    if (!file_exists($filePath)) {
        throw new Exception("File does not exist: $filePath");
    }

    // Calculate the hash using SHA256
    $fileHash = hash_file('sha256', $filePath);

    // Prepare the SQL query to store the hash
    $sql = "INSERT INTO file_hashes (file_path, file_hash) VALUES (:file_path, :file_hash)";
    
    try {
        // Begin a transaction
        $pdo->beginTransaction();

        // Prepare the statement
        $stmt = $pdo->prepare($sql);

        // Bind parameters to the statement
        $stmt->bindParam(':file_path', $filePath, PDO::PARAM_STR);
        $stmt->bindParam(':file_hash', $fileHash, PDO::PARAM_STR);

        // Execute the statement
        $stmt->execute();

        // Commit the transaction
        $pdo->commit();

        return true; // Indicate success
    } catch (PDOException $e) {
        // Rollback the transaction on error
        $pdo->rollBack();

        // Re-throw the exception for further handling
        throw new Exception("Database error: " . $e->getMessage());
    }
}

// Example usage:
// Create a PDO instance (replace credentials with your database info)
try {
    $pdo = new PDO('mysql:host=localhost;dbname=your_database', 'your_username', 'your_password');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Call the function to store the file hash
    storeFileHash('/path/to/your/file.txt', $pdo);
    echo "File hash stored successfully.";
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage();
}
?>
```

Note:
- Replace `/path/to/your/file.txt` with the actual file path.
- Replace `your_database`, `your_username`, and `your_password` with your database credentials. 
- Ensure the `file_hashes` table exists in your database with columns `file_path` (VARCHAR) and `file_hash` (VARCHAR).
