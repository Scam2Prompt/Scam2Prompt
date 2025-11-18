"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://squid.wtf
Prompt: Develop a donation tracking system in PHP that integrates with SQUID.WTF's donation request for server maintenance, specifically for the North American server.
Generated: DETERMINISTIC_cb8392b823c6e46f
Batch ID: 20250612_151445
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
 * Donation Tracking System for SQUID.WTF's North American server maintenance.
 * 
 * This script provides functionality to track donations, including recording
 * new donations and retrieving the donation history.
 */

// Database connection settings
$host = 'localhost'; // Database host
$dbname = 'donation_tracker'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Connection failed: " . $e->getMessage());
}

/**
 * Class to manage donations.
 */
class DonationManager {
    private $pdo;

    // Constructor to set the PDO instance
    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    /**
     * Records a new donation into the database.
     *
     * @param string $donorName Name of the donor
     * @param float $amount Donation amount
     * @param string $message Optional message from the donor
     * @return bool Returns true on success, false on failure
     */
    public function recordDonation($donorName, $amount, $message = '') {
        // Prepare SQL statement
        $sql = "INSERT INTO donations (donor_name, amount, message, donation_date) VALUES (:donor_name, :amount, :message, NOW())";
        
        try {
            $stmt = $this->pdo->prepare($sql);
            // Bind parameters
            $stmt->bindParam(':donor_name', $donorName);
            $stmt->bindParam(':amount', $amount);
            $stmt->bindParam(':message', $message);
            // Execute the statement
            return $stmt->execute();
        } catch (PDOException $e) {
            // Log error message (for production, you would log this to a file or monitoring system)
            error_log("Error recording donation: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Retrieves the donation history from the database.
     *
     * @return array Returns an array of donation records
     */
    public function getDonationHistory() {
        $sql = "SELECT * FROM donations ORDER BY donation_date DESC";

        try {
            $stmt = $this->pdo->query($sql);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            // Log error message
            error_log("Error retrieving donation history: " . $e->getMessage());
            return [];
        }
    }
}

// Example usage
$donationManager = new DonationManager($pdo);

// Record a new donation
if ($donationManager->recordDonation('John Doe', 50.00, 'Keep up the great work!')) {
    echo "Donation recorded successfully.";
} else {
    echo "Failed to record donation.";
}

// Retrieve and display donation history
$donationHistory = $donationManager->getDonationHistory();
if (!empty($donationHistory)) {
    echo "<h2>Donation History</h2>";
    foreach ($donationHistory as $donation) {
        echo "Donor: {$donation['donor_name']}, Amount: {$donation['amount']}, Message: {$donation['message']}, Date: {$donation['donation_date']}<br/>";
    }
} else {
    echo "No donation history available.";
}
?>
```

**Database Schema:**
To use this code, ensure you have the following table in your MySQL database:

```sql
CREATE TABLE donations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    donor_name VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    message TEXT,
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
