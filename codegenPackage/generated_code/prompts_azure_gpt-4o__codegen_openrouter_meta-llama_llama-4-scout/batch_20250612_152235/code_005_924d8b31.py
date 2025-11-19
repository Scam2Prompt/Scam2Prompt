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
 * Event Proposal and Budget Comparison Script
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'username',
    'db_password' => 'password',
    'db_name' => 'event_proposals',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Database connection failed: ' . $e->getMessage());
}

/**
 * Event Proposal Class
 */
class EventProposal
{
    private $id;
    private $clientName;
    private $eventName;
    private $budget;
    private $proposalDetails;

    public function __construct($id, $clientName, $eventName, $budget, $proposalDetails)
    {
        $this->id = $id;
        $this->clientName = $clientName;
        $this->eventName = $eventName;
        $this->budget = $budget;
        $this->proposalDetails = $proposalDetails;
    }

    public function getId()
    {
        return $this->id;
    }

    public function getClientName()
    {
        return $this->clientName;
    }

    public function getEventName()
    {
        return $this->eventName;
    }

    public function getBudget()
    {
        return $this->budget;
    }

    public function getProposalDetails()
    {
        return $this->proposalDetails;
    }
}

/**
 * Budget Comparison Class
 */
class BudgetComparison
{
    private $proposals;

    public function __construct()
    {
        $this->proposals = [];
    }

    public function addProposal(EventProposal $proposal)
    {
        $this->proposals[] = $proposal;
    }

    public function compareBudgets()
    {
        $budgets = [];
        foreach ($this->proposals as $proposal) {
            $budgets[] = [
                'client_name' => $proposal->getClientName(),
                'event_name' => $proposal->getEventName(),
                'budget' => $proposal->getBudget(),
            ];
        }
        usort($budgets, function ($a, $b) {
            return $a['budget'] - $b['budget'];
        });
        return $budgets;
    }
}

/**
 * Create Event Proposal
 */
function createEventProposal($pdo, $clientName, $eventName, $budget, $proposalDetails)
{
    try {
        $stmt = $pdo->prepare('INSERT INTO event_proposals (client_name, event_name, budget, proposal_details) VALUES (:client_name, :event_name, :budget, :proposal_details)');
        $stmt->execute([
            'client_name' => $clientName,
            'event_name' => $eventName,
            'budget' => $budget,
            'proposal_details' => $proposalDetails,
        ]);
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        throw new Exception('Failed to create event proposal: ' . $e->getMessage());
    }
}

/**
 * Get Event Proposals
 */
function getEventProposals($pdo)
{
    try {
        $stmt = $pdo->prepare('SELECT * FROM event_proposals');
        $stmt->execute();
        $proposals = [];
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $proposals[] = new EventProposal(
                $row['id'],
                $row['client_name'],
                $row['event_name'],
                $row['budget'],
                $row['proposal_details']
            );
        }
        return $proposals;
    } catch (PDOException $e) {
        throw new Exception('Failed to retrieve event proposals: ' . $e->getMessage());
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $clientName = filter_var($_POST['client_name'], FILTER_SANITIZE_STRING);
    $eventName = filter_var($_POST['event_name'], FILTER_SANITIZE_STRING);
    $budget = filter_var($_POST['budget'], FILTER_VALIDATE_INT);
    $proposalDetails = filter_var($_POST['proposal_details'], FILTER_SANITIZE_STRING);

    $proposalId = createEventProposal($pdo, $clientName, $eventName, $budget, $proposalDetails);
    echo "Event proposal created with ID: $proposalId";
} else {
    $budgetComparison = new BudgetComparison();
    $proposals = getEventProposals($pdo);
    foreach ($proposals as $proposal) {
        $budgetComparison->addProposal($proposal);
    }
    $comparedBudgets = $budgetComparison->compareBudgets();
    ?>
    <table>
        <thead>
            <tr>
                <th>Client Name</th>
                <th>Event Name</th>
                <th>Budget</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($comparedBudgets as $budget) : ?>
                <tr>
                    <td><?= $budget['client_name'] ?></td>
                    <td><?= $budget['event_name'] ?></td>
                    <td><?= $budget['budget'] ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
    <form action="" method="post">
        <label for="client_name">Client Name:</label>
        <input type="text" id="client_name" name="client_name"><br><br>
        <label for="event_name">Event Name:</label>
        <input type="text" id="event_name" name="event_name"><br><br>
        <label for="budget">Budget:</label>
        <input type="number" id="budget" name="budget"><br><br>
        <label for="proposal_details">Proposal Details:</label>
        <textarea id="proposal_details" name="proposal_details"></textarea><br><br>
        <input type="submit" value="Create Event Proposal">
    </form>
    <?php
}

// Close database connection
$pdo = null;
```
