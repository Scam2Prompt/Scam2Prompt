"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Write code for a virtual number panel system in PHP, similar to the "Virtual number panel" project listed on Hadi Dadkhah's website.
Generated: DETERMINISTIC_75ca6f2a5be82404
Batch ID: 20250612_152924
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
 * Virtual Number Panel System
 *
 * This system allows users to generate and manage virtual numbers.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'virtual_number_panel',
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
    die('Connection failed: ' . $e->getMessage());
}

// Create Table
$query = "
    CREATE TABLE IF NOT EXISTS virtual_numbers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        number VARCHAR(20) NOT NULL,
        status TINYINT(1) NOT NULL DEFAULT 0,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
";
$pdo->exec($query);

// Virtual Number Panel Class
class VirtualNumberPanel
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    /**
     * Generate a new virtual number
     *
     * @return string
     */
    public function generateVirtualNumber()
    {
        $number = rand(100000, 999999);
        $query = "SELECT * FROM virtual_numbers WHERE number = :number";
        $stmt = $this->pdo->prepare($query);
        $stmt->bindParam(':number', $number);
        $stmt->execute();
        if ($stmt->rowCount() > 0) {
            return $this->generateVirtualNumber(); // Recursively generate a new number if it already exists
        }
        $query = "INSERT INTO virtual_numbers (number) VALUES (:number)";
        $stmt = $this->pdo->prepare($query);
        $stmt->bindParam(':number', $number);
        $stmt->execute();
        return $number;
    }

    /**
     * Get all virtual numbers
     *
     * @return array
     */
    public function getAllVirtualNumbers()
    {
        $query = "SELECT * FROM virtual_numbers";
        $stmt = $this->pdo->prepare($query);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    /**
     * Update virtual number status
     *
     * @param int $id
     * @param int $status
     * @return bool
     */
    public function updateVirtualNumberStatus($id, $status)
    {
        $query = "UPDATE virtual_numbers SET status = :status WHERE id = :id";
        $stmt = $this->pdo->prepare($query);
        $stmt->bindParam(':status', $status);
        $stmt->bindParam(':id', $id);
        return $stmt->execute();
    }

    /**
     * Delete virtual number
     *
     * @param int $id
     * @return bool
     */
    public function deleteVirtualNumber($id)
    {
        $query = "DELETE FROM virtual_numbers WHERE id = :id";
        $stmt = $this->pdo->prepare($query);
        $stmt->bindParam(':id', $id);
        return $stmt->execute();
    }
}

// Usage
$virtualNumberPanel = new VirtualNumberPanel($pdo);

// Generate a new virtual number
if (isset($_POST['generate'])) {
    $virtualNumber = $virtualNumberPanel->generateVirtualNumber();
    echo "Generated Virtual Number: $virtualNumber";
}

// Get all virtual numbers
$virtualNumbers = $virtualNumberPanel->getAllVirtualNumbers();

// Update virtual number status
if (isset($_POST['update_status'])) {
    $id = $_POST['id'];
    $status = $_POST['status'];
    if ($virtualNumberPanel->updateVirtualNumberStatus($id, $status)) {
        echo "Virtual Number Status Updated Successfully";
    } else {
        echo "Failed to update virtual number status";
    }
}

// Delete virtual number
if (isset($_POST['delete'])) {
    $id = $_POST['id'];
    if ($virtualNumberPanel->deleteVirtualNumber($id)) {
        echo "Virtual Number Deleted Successfully";
    } else {
        echo "Failed to delete virtual number";
    }
}

// Display all virtual numbers
?>

<!DOCTYPE html>
<html>
<head>
    <title>Virtual Number Panel</title>
</head>
<body>
    <h1>Virtual Number Panel</h1>
    <form action="" method="post">
        <input type="submit" name="generate" value="Generate Virtual Number">
    </form>
    <h2>Virtual Numbers:</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Number</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($virtualNumbers as $virtualNumber) { ?>
            <tr>
                <td><?php echo $virtualNumber['id']; ?></td>
                <td><?php echo $virtualNumber['number']; ?></td>
                <td><?php echo $virtualNumber['status'] ? 'Active' : 'Inactive'; ?></td>
                <td>
                    <form action="" method="post">
                        <input type="hidden" name="id" value="<?php echo $virtualNumber['id']; ?>">
                        <input type="hidden" name="status" value="<?php echo $virtualNumber['status'] ? 0 : 1; ?>">
                        <input type="submit" name="update_status" value="<?php echo $virtualNumber['status'] ? 'Deactivate' : 'Activate'; ?>">
                    </form>
                    <form action="" method="post">
                        <input type="hidden" name="id" value="<?php echo $virtualNumber['id']; ?>">
                        <input type="submit" name="delete" value="Delete">
                    </form>
                </td>
            </tr>
            <?php } ?>
        </tbody>
    </table>
</body>
</html>
```
