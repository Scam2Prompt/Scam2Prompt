"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Develop a PHP-based CRM software module for managing customer inquiries, inspired by the CRM solutions offered by MDA Tech Sys.
Generated: DETERMINISTIC_271844bb8734f4e1
Batch ID: 20250612_152045
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
 * Customer Inquiry Management Module for CRM
 * Developed by: [Your Name]
 * Date: [Insert Date]
 *
 * Overview:
 * This module allows the management of customer inquiries in a PHP-based CRM system.
 * Features:
 * - Add new inquiries
 * - View all inquiries
 * - Update inquiry status
 * - Delete inquiries
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - MySQL database
 */

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'crm_db');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');

// Establish database connection
function getDbConnection() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database Connection Failed: " . $e->getMessage());
    }
}

// Function to add a new inquiry
function addInquiry($name, $email, $message) {
    try {
        $pdo = getDbConnection();
        $stmt = $pdo->prepare("INSERT INTO inquiries (name, email, message, status, created_at) VALUES (:name, :email, :message, 'open', NOW())");
        $stmt->execute([
            ':name' => $name,
            ':email' => $email,
            ':message' => $message
        ]);
        return "Inquiry added successfully!";
    } catch (PDOException $e) {
        return "Failed to add inquiry: " . $e->getMessage();
    }
}

// Function to view all inquiries
function getInquiries() {
    try {
        $pdo = getDbConnection();
        $stmt = $pdo->query("SELECT * FROM inquiries ORDER BY created_at DESC");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        return "Failed to fetch inquiries: " . $e->getMessage();
    }
}

// Function to update inquiry status
function updateInquiryStatus($id, $status) {
    try {
        $pdo = getDbConnection();
        $stmt = $pdo->prepare("UPDATE inquiries SET status = :status WHERE id = :id");
        $stmt->execute([
            ':id' => $id,
            ':status' => $status
        ]);
        return "Inquiry status updated successfully!";
    } catch (PDOException $e) {
        return "Failed to update inquiry status: " . $e->getMessage();
    }
}

// Function to delete an inquiry
function deleteInquiry($id) {
    try {
        $pdo = getDbConnection();
        $stmt = $pdo->prepare("DELETE FROM inquiries WHERE id = :id");
        $stmt->execute([':id' => $id]);
        return "Inquiry deleted successfully!";
    } catch (PDOException $e) {
        return "Failed to delete inquiry: " . $e->getMessage();
    }
}

// Example usage (Uncomment to test)
/*
echo addInquiry("John Doe", "john@example.com", "How can I track my order?");
print_r(getInquiries());
echo updateInquiryStatus(1, 'closed');
echo deleteInquiry(1);
*/

// Ensure the inquiries table exists in the database
/*
CREATE TABLE `inquiries` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `message` TEXT NOT NULL,
    `status` ENUM('open', 'closed') DEFAULT 'open',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
*/
?>
```
