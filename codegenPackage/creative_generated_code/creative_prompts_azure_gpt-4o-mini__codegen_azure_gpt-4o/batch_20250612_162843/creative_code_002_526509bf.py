"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Create a PHP application that allows users to book guided tours at Armourers' Hall, including features for selecting dates and managing bookings.
Generated: DETERMINISTIC_526509bf064f718b
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// tours_booking_system.php

// Configuration for database connection
define('DB_HOST', 'localhost');   // Database host
define('DB_NAME', 'armourers_hall'); // Database name
define('DB_USER', 'root');       // Database username
define('DB_PASS', '');           // Database password

// Establish a database connection
function getDatabaseConnection() {
    try {
        $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8';
        $pdo = new PDO($dsn, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]);
        return $pdo;
    } catch (PDOException $e) {
        die('Database connection failed: ' . $e->getMessage());
    }
}

// Function to fetch available tour dates
function getAvailableDates() {
    $pdo = getDatabaseConnection();
    $sql = "SELECT * FROM tour_dates WHERE is_available = 1 ORDER BY date ASC";
    $stmt = $pdo->query($sql);
    return $stmt->fetchAll();
}

// Function to create a new booking
function createBooking($name, $email, $date_id) {
    $pdo = getDatabaseConnection();

    // Check if the tour date is valid and available
    $sql = "SELECT * FROM tour_dates WHERE id = :date_id AND is_available = 1";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(['date_id' => $date_id]);

    if ($stmt->rowCount() === 0) {
        return "Selected tour date is unavailable.";
    }

    // Create the booking
    $sql = "INSERT INTO bookings (name, email, date_id, created_at) VALUES (:name, :email, :date_id, NOW())";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([
        'name' => htmlspecialchars($name),
        'email' => htmlspecialchars($email),
        'date_id' => $date_id,
    ]);

    return "Booking successful!";
}

// Function to fetch all bookings
function getBookings() {
    $pdo = getDatabaseConnection();
    $sql = "SELECT b.id, b.name, b.email, b.created_at, td.date 
            FROM bookings b 
            JOIN tour_dates td ON b.date_id = td.id 
            ORDER BY b.created_at DESC";
    $stmt = $pdo->query($sql);
    return $stmt->fetchAll();
}

// HTML template for displaying the booking form and data
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guided Tour Booking - Armourers' Hall</title>
</head>
<body>
    <h1>Book a Guided Tour at Armourers' Hall</h1>

    <!-- Booking Form -->
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="date">Select Tour Date:</label>
        <select id="date" name="date_id" required>
            <?php
            $dates = getAvailableDates();
            foreach ($dates as $date) {
                echo "<option value=\"{$date['id']}\">{$date['date']}</option>";
            }
            ?>
        </select>
        <br>
        <button type="submit" name="book">Book Now</button>
    </form>

    <?php
    // Handle form submission
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['book'])) {
        $name = $_POST['name'];
        $email = $_POST['email'];
        $date_id = $_POST['date_id'];

        $result = createBooking($name, $email, $date_id);
        echo "<p>{$result}</p>";
    }
    ?>

    <h2>Existing Bookings</h2>
    <ul>
        <?php
        $bookings = getBookings();
        foreach ($bookings as $booking) {
            echo "<li>{$booking['name']} ({$booking['email']}) - {$booking['date']} - Booked on {$booking['created_at']}</li>";
        }
        ?>
    </ul>
</body>
</html>
```

**Database Schema**
```sql
-- Table for tour dates
CREATE TABLE tour_dates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    is_available TINYINT(1) DEFAULT 1
);

-- Table for bookings
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    date_id INT NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (date_id) REFERENCES tour_dates(id)
);
```
