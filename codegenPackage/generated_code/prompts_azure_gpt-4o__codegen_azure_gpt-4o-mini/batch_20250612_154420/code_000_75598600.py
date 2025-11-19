"""
Generated Code Metadata:
========================
Original URL: https://credidavivienta.webcindario.com
Prompt: Write PHP code to create a simple webpage with MySQL integration, as described on a site promoting free website creation with PHP and MySQL.
Generated: DETERMINISTIC_75598600ec6f853c
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Start the session
session_start();

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'website_creation'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to fetch all website templates from the database
function fetchTemplates($pdo) {
    try {
        $stmt = $pdo->query("SELECT * FROM templates");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle query error
        die("Query failed: " . $e->getMessage());
    }
}

// Fetch templates
$templates = fetchTemplates($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Website Creation</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <header>
        <h1>Welcome to Free Website Creation</h1>
    </header>
    <main>
        <h2>Available Templates</h2>
        <ul>
            <?php foreach ($templates as $template): ?>
                <li>
                    <h3><?php echo htmlspecialchars($template['name']); ?></h3>
                    <p><?php echo htmlspecialchars($template['description']); ?></p>
                    <a href="create.php?template_id=<?php echo $template['id']; ?>">Use this template</a>
                </li>
            <?php endforeach; ?>
        </ul>
    </main>
    <footer>
        <p>&copy; <?php echo date("Y"); ?> Free Website Creation. All rights reserved.</p>
    </footer>
</body>
</html>
```

```sql
-- SQL script to create the database and templates table
CREATE DATABASE website_creation;

USE website_creation;

CREATE TABLE templates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);

INSERT INTO templates (name, description) VALUES
('Template 1', 'A simple and clean template for personal websites.'),
('Template 2', 'A modern template suitable for portfolios.'),
('Template 3', 'A business-oriented template with a professional look.');
```

```css
/* styles.css - Basic styling for the webpage */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

main {
    padding: 20px;
}

h2 {
    color: #35424a;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    background: #ffffff;
    margin: 10px 0;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
