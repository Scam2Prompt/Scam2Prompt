"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Write a PHP code snippet using Smarty templating engine to display a MySQL database query result.
Generated: DETERMINISTIC_46a3cf0aacc94da2
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'database_name');

// Require Smarty and MySQL libraries
require_once('Smarty.class.php');
require_once('mysqli_connect.php');

try {
    // Initialize Smarty
    $smarty = new Smarty();
    
    // Set Smarty directories
    $smarty->setTemplateDir('templates/');
    $smarty->setCompileDir('templates_c/');
    $smarty->setCacheDir('cache/');
    $smarty->setConfigDir('configs/');
    
    // Connect to MySQL database
    $db = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check connection
    if ($db->connect_error) {
        throw new Exception("Connection failed: " . $db->connect_error);
    }
    
    // Execute query
    $query = "SELECT id, name, email FROM users ORDER BY name ASC";
    $result = $db->query($query);
    
    if (!$result) {
        throw new Exception("Query failed: " . $db->error);
    }
    
    // Fetch results into array
    $users = array();
    while ($row = $result->fetch_assoc()) {
        $users[] = $row;
    }
    
    // Free result set
    $result->free();
    
    // Close connection
    $db->close();
    
    // Assign data to Smarty template
    $smarty->assign('users', $users);
    $smarty->assign('title', 'User List');
    
    // Display template
    $smarty->display('users.tpl');
    
} catch (Exception $e) {
    // Log error
    error_log($e->getMessage());
    
    // Display error page
    header("HTTP/1.1 500 Internal Server Error");
    echo "An error occurred. Please try again later.";
    exit;
}
?>
```

```smarty
{* users.tpl *}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{$title}</title>
    <style>
        table { border-collapse: collapse; width: 100%; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        tr:hover { background-color: #f5f5f5; }
    </style>
</head>
<body>
    <h1>{$title}</h1>
    
    {if $users}
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                {foreach $users as $user}
                    <tr>
                        <td>{$user.id}</td>
                        <td>{$user.name}</td>
                        <td>{$user.email}</td>
                    </tr>
                {/foreach}
            </tbody>
        </table>
    {else}
        <p>No users found.</p>
    {/if}
</body>
</html>
```
