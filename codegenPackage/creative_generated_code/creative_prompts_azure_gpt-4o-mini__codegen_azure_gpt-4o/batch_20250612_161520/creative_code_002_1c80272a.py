"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elpicadito.com
Prompt: Create a PHP API endpoint that retrieves the latest articles from El Picadito, filtering for topics like gymnastics and athletics.
Generated: DETERMINISTIC_1c80272aac75daa6
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Set headers to allow CORS and indicate JSON response
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

// Database connection settings
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_USER', 'root');      // Replace with your database username
define('DB_PASS', '');          // Replace with your database password
define('DB_NAME', 'el_picadito'); // Replace with your database name

// Function to establish a database connection
function connectToDatabase()
{
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($conn->connect_error) {
        http_response_code(500);
        echo json_encode(["error" => "Database connection failed"]);
        exit();
    }

    return $conn;
}

// Connect to the database
$conn = connectToDatabase();

// Define the topics to filter articles
$allowedTopics = ['gymnastics', 'athletics'];

// Prepare SQL query to fetch the latest articles for the allowed topics
$sql = "SELECT id, title, content, topic, published_date 
        FROM articles 
        WHERE topic IN ('gymnastics', 'athletics') 
        ORDER BY published_date DESC 
        LIMIT 10";

// Execute the query
$result = $conn->query($sql);

// Check for SQL errors
if ($conn->error) {
    http_response_code(500);
    echo json_encode(["error" => "Failed to retrieve articles"]);
    exit();
}

// Fetch articles and prepare the JSON response
$articles = [];
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $articles[] = [
            "id" => $row["id"],
            "title" => $row["title"],
            "content" => $row["content"],
            "topic" => $row["topic"],
            "published_date" => $row["published_date"]
        ];
    }
}

// Close the database connection
$conn->close();

// Send the JSON response
http_response_code(200);
echo json_encode(["articles" => $articles]);

?>
```

This code sets up a PHP API endpoint that connects to a database, retrieves the latest articles related to gymnastics and athletics, and returns them in JSON format.
