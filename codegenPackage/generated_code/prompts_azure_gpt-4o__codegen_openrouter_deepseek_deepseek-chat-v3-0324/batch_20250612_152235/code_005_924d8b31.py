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
 * Event Proposal and Budget Comparison System
 * 
 * This script allows clients to submit event proposals and compare quotes from multiple event companies.
 * It includes features for proposal submission, quote comparison, and budget analysis.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'event_proposals');
define('TABLE_PROPOSALS', 'proposals');
define('TABLE_QUOTES', 'quotes');
define('TABLE_CLIENTS', 'clients');

// Error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Start session
session_start();

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        $this->connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($this->connection->connect_error) {
            die("Connection failed: " . $this->connection->connect_error);
        }
    }

    public function getConnection() {
        return $this->connection;
    }

    public function closeConnection() {
        $this->connection->close();
    }

    public function sanitizeInput($data) {
        return $this->connection->real_escape_string(htmlspecialchars(trim($data)));
    }
}

/**
 * Event Proposal Class
 */
class EventProposal {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Submit a new event proposal
     */
    public function submitProposal($clientId, $eventName, $eventType, $eventDate, $attendees, $budget, $requirements) {
        $conn = $this->db->getConnection();
        
        $clientId = $this->db->sanitizeInput($clientId);
        $eventName = $this->db->sanitizeInput($eventName);
        $eventType = $this->db->sanitizeInput($eventType);
        $eventDate = $this->db->sanitizeInput($eventDate);
        $attendees = $this->db->sanitizeInput($attendees);
        $budget = $this->db->sanitizeInput($budget);
        $requirements = $this->db->sanitizeInput($requirements);

        $sql = "INSERT INTO " . TABLE_PROPOSALS . " 
                (client_id, event_name, event_type, event_date, attendees, budget, requirements, created_at) 
                VALUES (?, ?, ?, ?, ?, ?, ?, NOW())";

        $stmt = $conn->prepare($sql);
        if (!$stmt) {
            return ['success' => false, 'message' => 'Database error: ' . $conn->error];
        }

        $stmt->bind_param("isssids", $clientId, $eventName, $eventType, $eventDate, $attendees, $budget, $requirements);
        
        if ($stmt->execute()) {
            $proposalId = $stmt->insert_id;
            $stmt->close();
            return ['success' => true, 'proposal_id' => $proposalId];
        } else {
            $error = $stmt->error;
            $stmt->close();
            return ['success' => false, 'message' => 'Failed to submit proposal: ' . $error];
        }
    }

    /**
     * Get proposals for a specific client
     */
    public function getClientProposals($clientId) {
        $conn = $this->db->getConnection();
        $clientId = $this->db->sanitizeInput($clientId);

        $sql = "SELECT * FROM " . TABLE_PROPOSALS . " WHERE client_id = ? ORDER BY created_at DESC";
        $stmt = $conn->prepare($sql);
        
        if (!$stmt) {
            return ['success' => false, 'message' => 'Database error: ' . $conn->error];
        }

        $stmt->bind_param("i", $clientId);
        $stmt->execute();
        $result = $stmt->get_result();
        
        $proposals = [];
        while ($row = $result->fetch_assoc()) {
            $proposals[] = $row;
        }
        
        $stmt->close();
        return ['success' => true, 'proposals' => $proposals];
    }
}

/**
 * Quote Management Class
 */
class QuoteManager {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Submit a quote for a proposal
     */
    public function submitQuote($proposalId, $companyId, $amount, $services, $notes) {
        $conn = $this->db->getConnection();
        
        $proposalId = $this->db->sanitizeInput($proposalId);
        $companyId = $this->db->sanitizeInput($companyId);
        $amount = $this->db->sanitizeInput($amount);
        $services = $this->db->sanitizeInput($services);
        $notes = $this->db->sanitizeInput($notes);

        $sql = "INSERT INTO " . TABLE_QUOTES . " 
                (proposal_id, company_id, amount, services, notes, submitted_at) 
                VALUES (?, ?, ?, ?, ?, NOW())";

        $stmt = $conn->prepare($sql);
        if (!$stmt) {
            return ['success' => false, 'message' => 'Database error: ' . $conn->error];
        }

        $stmt->bind_param("iidss", $proposalId, $companyId, $amount, $services, $notes);
        
        if ($stmt->execute()) {
            $quoteId = $stmt->insert_id;
            $stmt->close();
            return ['success' => true, 'quote_id' => $quoteId];
        } else {
            $error = $stmt->error;
            $stmt->close();
            return ['success' => false, 'message' => 'Failed to submit quote: ' . $error];
        }
    }

    /**
     * Get quotes for a specific proposal
     */
    public function getProposalQuotes($proposalId) {
        $conn = $this->db->getConnection();
        $proposalId = $this->db->sanitizeInput($proposalId);

        $sql = "SELECT q.*, c.company_name FROM " . TABLE_QUOTES . " q 
                LEFT JOIN " . TABLE_CLIENTS . " c ON q.company_id = c.id 
                WHERE q.proposal_id = ? ORDER BY q.amount ASC";
        
        $stmt = $conn->prepare($sql);
        if (!$stmt) {
            return ['success' => false, 'message' => 'Database error: ' . $conn->error];
        }

        $stmt->bind_param("i", $proposalId);
        $stmt->execute();
        $result = $stmt->get_result();
        
        $quotes = [];
        while ($row = $result->fetch_assoc()) {
            $quotes[] = $row;
        }
        
        $stmt->close();
        return ['success' => true, 'quotes' => $quotes];
    }

    /**
     * Compare quotes for a proposal
     */
    public function compareQuotes($proposalId) {
        $quotesResult = $this->getProposalQuotes($proposalId);
        
        if (!$quotesResult['success']) {
            return $quotesResult;
        }

        $quotes = $quotesResult['quotes'];
        
        if (empty($quotes)) {
            return ['success' => false, 'message' => 'No quotes found for this proposal'];
        }

        // Get proposal details
        $conn = $this->db->getConnection();
        $sql = "SELECT budget FROM " . TABLE_PROPOSALS . " WHERE id = ?";
        $stmt = $conn->prepare($sql);
        
        if (!$stmt) {
            return ['success' => false, 'message' => 'Database error: ' . $conn->error];
        }

        $stmt->bind_param("i", $proposalId);
        $stmt->execute();
        $result = $stmt->get_result();
        $proposal = $result->fetch_assoc();
        $stmt->close();

        if (!$proposal) {
            return ['success' => false, 'message' => 'Proposal not found'];
        }

        $budget = $proposal['budget'];
        $comparison = [
            'budget' => $budget,
            'quotes' => $quotes,
            'lowest_quote' => $quotes[0],
            'highest_quote' => end($quotes),
            'average_quote' => array_sum(array_column($quotes, 'amount')) / count($quotes),
            'within_budget' => array_filter($quotes, function($quote) use ($budget) {
                return $quote['amount'] <= $budget;
            })
        ];

        return ['success' => true, 'comparison' => $comparison];
    }
}

/**
 *
