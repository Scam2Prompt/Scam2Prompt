"""
Generated Code Metadata:
========================
Original URL: https://www.cc-community.net
Prompt: Write code to implement a bug tracker system for a XenForo-based forum, inspired by the CC-Community Board's "Bugtracker" section.
Generated: DETERMINISTIC_31f45e148ee0a724
Batch ID: 20250612_151119
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
 * BugTracker Class
 * This class handles the operations related to bug tracking in a XenForo-based forum.
 */
class BugTracker
{
    private $db; // Database connection
    private $table = 'bug_reports'; // Table name for bug reports

    /**
     * Constructor to initialize the database connection.
     *
     * @param PDO $db Database connection instance
     */
    public function __construct(PDO $db)
    {
        $this->db = $db;
    }

    /**
     * Method to create a new bug report.
     *
     * @param string $title Title of the bug
     * @param string $description Description of the bug
     * @param string $reporter Reporter of the bug
     * @return bool True on success, false on failure
     */
    public function createBugReport($title, $description, $reporter)
    {
        try {
            $stmt = $this->db->prepare("INSERT INTO {$this->table} (title, description, reporter, status, created_at) VALUES (:title, :description, :reporter, 'open', NOW())");
            $stmt->bindParam(':title', $title);
            $stmt->bindParam(':description', $description);
            $stmt->bindParam(':reporter', $reporter);
            return $stmt->execute();
        } catch (PDOException $e) {
            // Log error message
            error_log("Error creating bug report: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Method to retrieve all bug reports.
     *
     * @return array Array of bug reports
     */
    public function getAllBugReports()
    {
        try {
            $stmt = $this->db->query("SELECT * FROM {$this->table} ORDER BY created_at DESC");
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            // Log error message
            error_log("Error fetching bug reports: " . $e->getMessage());
            return [];
        }
    }

    /**
     * Method to update the status of a bug report.
     *
     * @param int $id Bug report ID
     * @param string $status New status of the bug report
     * @return bool True on success, false on failure
     */
    public function updateBugStatus($id, $status)
    {
        try {
            $stmt = $this->db->prepare("UPDATE {$this->table} SET status = :status WHERE id = :id");
            $stmt->bindParam(':status', $status);
            $stmt->bindParam(':id', $id);
            return $stmt->execute();
        } catch (PDOException $e) {
            // Log error message
            error_log("Error updating bug status: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Method to delete a bug report.
     *
     * @param int $id Bug report ID
     * @return bool True on success, false on failure
     */
    public function deleteBugReport($id)
    {
        try {
            $stmt = $this->db->prepare("DELETE FROM {$this->table} WHERE id = :id");
            $stmt->bindParam(':id', $id);
            return $stmt->execute();
        } catch (PDOException $e) {
            // Log error message
            error_log("Error deleting bug report: " . $e->getMessage());
            return false;
        }
    }
}

// Example usage
try {
    // Database connection (replace with your actual database credentials)
    $db = new PDO('mysql:host=localhost;dbname=your_database', 'username', 'password');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Instantiate BugTracker
    $bugTracker = new BugTracker($db);

    // Create a new bug report
    $bugTracker->createBugReport('Sample Bug', 'This is a sample bug description.', 'user123');

    // Fetch all bug reports
    $reports = $bugTracker->getAllBugReports();
    print_r($reports);

    // Update a bug report status
    $bugTracker->updateBugStatus(1, 'resolved');

    // Delete a bug report
    $bugTracker->deleteBugReport(1);
} catch (PDOException $e) {
    // Log connection error
    error_log("Database connection error: " . $e->getMessage());
}
```
