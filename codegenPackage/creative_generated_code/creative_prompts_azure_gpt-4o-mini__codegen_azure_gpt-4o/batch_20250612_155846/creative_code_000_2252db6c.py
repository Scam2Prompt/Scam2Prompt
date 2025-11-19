"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kesug.com
Prompt: How can I set up a free website using PHP and MySQL on InfinityFree like example.kesug.com?
Generated: DETERMINISTIC_2252db6c0539bec3
Batch ID: 20250612_155846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// index.php
// Start of the PHP script for setting up a simple web page using PHP and MySQL.
// This script assumes that you have already created a free hosting account on InfinityFree,
// uploaded your files, and set up your database credentials.

// Database Configuration
$host = "your_database_host"; // Replace with your MySQL hostname (e.g., sqlXXX.epizy.com)
$username = "your_database_username"; // Replace with your MySQL username from InfinityFree
$password = "your_database_password"; // Replace with your MySQL password from InfinityFree
$dbname = "your_database_name"; // Replace with your MySQL database name from InfinityFree

// Establish a connection to the MySQL database
$conn = new mysqli($host, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error); // Display an error message if the connection fails
}

// Function to fetch example data from the database
function fetchExampleData($conn) {
    $sql = "SELECT id, name FROM example_table"; // Replace with your actual table name and columns
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Fetch data and return it as an array
        $data = [];
        while ($row = $result->fetch_assoc()) {
            $data[] = $row;
        }
        return $data;
    } else {
        return []; // Return an empty array if no data is found
    }
}

// Fetch data from the database
$data = fetchExampleData($conn);

// Close the database connection
$conn->close();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Example Website</title>
    <style>
        /* Basic CSS for styling the page */
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        li:last-child {
            border-bottom: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Example Website</h1>
        <p>Below is a list of data fetched from the database:</p>
        <ul>
            <?php
            if (!empty($data)) {
                foreach ($data as $item) {
                    echo "<li>ID: " . htmlspecialchars($item['id']) . " - Name: " . htmlspecialchars($item['name']) . "</li>";
                }
            } else {
                echo "<li>No data found in the database.</li>";
            }
            ?>
        </ul>
    </div>
</body>
</html>
```

**Instructions:**
1. Replace placeholders in the PHP code (`your_database_host`, `your_database_username`, `your_database_password`, `your_database_name`, and `example_table`) with actual values from your InfinityFree account.
2. Create a MySQL database using the InfinityFree control panel and add a table (`example_table` in this case) with data.
3. Upload this `index.php` file to your hosting account (usually under the `htdocs` folder).
4. Visit your free website URL (e.g., `example.kesug.com`) to view the page.
5. Ensure you have PHP enabled in your hosting settings and your database is properly configured.
