"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://le13emeart.com
Prompt: Generate code in PHP to integrate a "Le 13e Art" event search feature into a website, allowing users to filter performances by date and genre.
Generated: DETERMINISTIC_5e7017e4e2bbe596
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// EventSearch.php

// Configuration settings for database connection
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'event_db'); // Database name
define('DB_USER', 'root'); // Database username
define('DB_PASS', ''); // Database password

/**
 * Connect to the database using PDO
 * @return PDO Database connection instance
 */
function connectToDatabase()
{
    try {
        $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8';
        $pdo = new PDO($dsn, DB_USER, DB_PASS, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
        return $pdo;
    } catch (PDOException $e) {
        die('Database connection failed: ' . $e->getMessage());
    }
}

/**
 * Fetch events filtered by date and genre
 * @param string|null $date Selected date (format: YYYY-MM-DD)
 * @param string|null $genre Selected genre
 * @return array List of filtered events
 */
function fetchFilteredEvents($date = null, $genre = null)
{
    $pdo = connectToDatabase();

    // Prepare SQL query with dynamic filtering
    $query = 'SELECT id, title, genre, event_date FROM events WHERE 1=1';
    $params = [];

    if ($date) {
        $query .= ' AND event_date = :date';
        $params[':date'] = $date;
    }

    if ($genre) {
        $query .= ' AND genre = :genre';
        $params[':genre'] = $genre;
    }

    $stmt = $pdo->prepare($query);
    $stmt->execute($params);

    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Check if filters are applied via GET parameters
$selectedDate = isset($_GET['date']) ? $_GET['date'] : null;
$selectedGenre = isset($_GET['genre']) ? $_GET['genre'] : null;

// Fetch filtered events
$events = fetchFilteredEvents($selectedDate, $selectedGenre);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Le 13e Art Event Search</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .event {
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <h1>Le 13e Art Event Search</h1>

    <!-- Filter Form -->
    <form method="GET" action="">
        <label for="date">Filter by Date:</label>
        <input type="date" id="date" name="date" value="<?php echo htmlspecialchars($selectedDate); ?>">

        <label for="genre">Filter by Genre:</label>
        <input type="text" id="genre" name="genre" value="<?php echo htmlspecialchars($selectedGenre); ?>">

        <button type="submit">Search</button>
    </form>

    <hr>

    <!-- Display Events -->
    <?php if (!empty($events)): ?>
        <?php foreach ($events as $event): ?>
            <div class="event">
                <h3><?php echo htmlspecialchars($event['title']); ?></h3>
                <p><strong>Genre:</strong> <?php echo htmlspecialchars($event['genre']); ?></p>
                <p><strong>Date:</strong> <?php echo htmlspecialchars($event['event_date']); ?></p>
            </div>
        <?php endforeach; ?>
    <?php else: ?>
        <p>No events found matching your criteria.</p>
    <?php endif; ?>
</body>
</html>
```
