"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Create a PHP script to handle multi-client event proposals and budget comparisons, as described in the webpage's recommendation for comparing quotes from multiple event companies.
Generated: DETERMINISTIC_924d8b319264faea
Batch ID: 20250612_152235
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
 * Event Proposal Comparison Script
 * 
 * This script handles multi-client event proposals and budget comparisons.
 * It allows users to submit event proposals from different companies and 
 * compare their budgets.
 */

// Enable error reporting for debugging (remove in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection parameters
$host = 'localhost';
$db = 'event_proposals';
$user = 'root';
$pass = 'password'; // Change to your database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to insert a new event proposal into the database
 *
 * @param string $clientName The name of the client
 * @param string $companyName The name of the event company
 * @param float $budget The proposed budget
 * @return bool True on success, false on failure
 */
function insertProposal($clientName, $companyName, $budget) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO proposals (client_name, company_name, budget) VALUES (:client_name, :company_name, :budget)");

    // Bind parameters
    $stmt->bindParam(':client_name', $clientName);
    $stmt->bindParam(':company_name', $companyName);
    $stmt->bindParam(':budget', $budget);

    // Execute the statement and return the result
    return $stmt->execute();
}

/**
 * Function to retrieve all proposals for a specific client
 *
 * @param string $clientName The name of the client
 * @return array An array of proposals
 */
function getProposalsByClient($clientName) {
    global $pdo;

    // Prepare SQL statement
    $stmt = $pdo->prepare("SELECT * FROM proposals WHERE client_name = :client_name");
    $stmt->bindParam(':client_name', $clientName);
    $stmt->execute();

    // Fetch all proposals as an associative array
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input data
    $clientName = filter_input(INPUT_POST, 'client_name', FILTER_SANITIZE_STRING);
    $companyName = filter_input(INPUT_POST, 'company_name', FILTER_SANITIZE_STRING);
    $budget = filter_input(INPUT_POST, 'budget', FILTER_VALIDATE_FLOAT);

    if ($clientName && $companyName && $budget !== false) {
        // Insert the proposal into the database
        if (insertProposal($clientName, $companyName, $budget)) {
            echo "Proposal submitted successfully.";
        } else {
            echo "Failed to submit proposal.";
        }
    } else {
        echo "Invalid input data.";
    }
}

// Example usage: Retrieve proposals for a specific client
$clientName = 'Client A'; // Change as needed
$proposals = getProposalsByClient($clientName);

// Display proposals
if (!empty($proposals)) {
    echo "<h2>Proposals for $clientName</h2>";
    echo "<table border='1'>";
    echo "<tr><th>Company Name</th><th>Budget</th></tr>";
    foreach ($proposals as $proposal) {
        echo "<tr><td>{$proposal['company_name']}</td><td>{$proposal['budget']}</td></tr>";
    }
    echo "</table>";
} else {
    echo "No proposals found for $clientName.";
}
?>

<!-- HTML Form for submitting proposals -->
<form method="POST" action="">
    <label for="client_name">Client Name:</label>
    <input type="text" id="client_name" name="client_name" required>
    <br>
    <label for="company_name">Company Name:</label>
    <input type="text" id="company_name" name="company_name" required>
    <br>
    <label for="budget">Budget:</label>
    <input type="number" id="budget" name="budget" step="0.01" required>
    <br>
    <input type="submit" value="Submit Proposal">
</form>
```
