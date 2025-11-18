"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Suggest an approach to implement a calendar feature for tracking dates and anniversaries on a genealogy website using PHP or JavaScript.
Generated: DETERMINISTIC_14ce6e566efd81ad
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection settings
$host = 'localhost';
$dbname = 'genealogy';
$username = 'root';
$password = '';

// Create a new PDO instance for database interaction
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set PDO error mode to exception for better error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Function to add a new anniversary to the database
function addAnniversary($name, $date, $description) {
    global $pdo;

    $sql = "INSERT INTO anniversaries (name, date, description) VALUES (:name, :date, :description)";
    
    try {
        $stmt = $pdo->prepare($sql);
        // Binding parameters to prevent SQL injection
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':date', $date);
        $stmt->bindParam(':description', $description);
        $stmt->execute();
        return "Anniversary added successfully!";
    } catch (PDOException $e) {
        return "Error adding anniversary: " . $e->getMessage();
    }
}

// Function to retrieve all anniversaries from the database
function getAnniversaries() {
    global $pdo;

    $sql = "SELECT * FROM anniversaries ORDER BY date ASC";
    
    try {
        $stmt = $pdo->query($sql);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        return "Error retrieving anniversaries: " . $e->getMessage();
    }
}

// Function to delete an anniversary based on ID
function deleteAnniversary($id) {
    global $pdo;

    $sql = "DELETE FROM anniversaries WHERE id = :id";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return "Anniversary deleted successfully!";
    } catch (PDOException $e) {
        return "Error deleting anniversary: " . $e->getMessage();
    }
}

// Example usage:
// Adding a new anniversary
echo addAnniversary('John and Jane Doe', '2023-09-15', 'Wedding Anniversary');

// Retrieving all anniversaries
$anniversaries = getAnniversaries();
echo json_encode($anniversaries);

// Deleting an anniversary with ID 1
echo deleteAnniversary(1);
?>
```

```javascript
// calendar.js

// Function to display anniversaries in the calendar
function displayAnniversaries(anniversaries) {
    const calendarElement = document.getElementById('calendar');
    calendarElement.innerHTML = ''; // Clear previous content

    anniversaries.forEach(anniversary => {
        const anniversaryElement = document.createElement('div');
        anniversaryElement.className = 'anniversary';
        anniversaryElement.innerHTML = `
            <strong>${anniversary.name}</strong> - ${new Date(anniversary.date).toLocaleDateString()}<br>
            <em>${anniversary.description}</em>
        `;
        calendarElement.appendChild(anniversaryElement);
    });
}

// Function to fetch anniversaries from the server
async function fetchAnniversaries() {
    try {
        const response = await fetch('/path/to/api/get_anniversaries.php');
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const anniversaries = await response.json();
        displayAnniversaries(anniversaries);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

// Call fetchAnniversaries on page load to display anniversaries
document.addEventListener('DOMContentLoaded', fetchAnniversaries);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Genealogy Calendar</title>
    <link rel="stylesheet" href="styles.css">
    <script src="calendar.js" defer></script>
</head>
<body>
    <h1>Anniversary Calendar</h1>
    <div id="calendar"></div>
</body>
</html>
```

```sql
-- SQL Schema for the anniversaries table

CREATE TABLE anniversaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    description TEXT
);
```
