"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Create a PHP application that allows users to book guided tours at Armourers' Hall, including features for selecting dates and managing bookings.
Generated: DETERMINISTIC_526509bf064f718b
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Armourers' Hall Guided Tour Booking Application

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'armourers_hall');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish database connection
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to fetch available tour dates
function getAvailableDates($pdo) {
    $stmt = $pdo->prepare("SELECT id, tour_date FROM tours WHERE available_slots > 0 ORDER BY tour_date ASC");
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Function to book a tour
function bookTour($pdo, $tourId, $userName, $userEmail) {
    try {
        // Start transaction
        $pdo->beginTransaction();

        // Check availability
        $stmt = $pdo->prepare("SELECT available_slots FROM tours WHERE id = :tourId");
        $stmt->execute(['tourId' => $tourId]);
        $tour = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$tour || $tour['available_slots'] <= 0) {
            throw new Exception("Selected tour is fully booked or does not exist.");
        }

        // Insert booking
        $stmt = $pdo->prepare("INSERT INTO bookings (tour_id, user_name, user_email) VALUES (:tourId, :userName, :userEmail)");
        $stmt->execute([
            'tourId' => $tourId,
            'userName' => $userName,
            'userEmail' => $userEmail
        ]);

        // Update available slots
        $stmt = $pdo->prepare("UPDATE tours SET available_slots = available_slots - 1 WHERE id = :tourId");
        $stmt->execute(['tourId' => $tourId]);

        // Commit transaction
        $pdo->commit();
        return "Booking successful!";
    } catch (Exception $e) {
        // Rollback transaction on error
        $pdo->rollBack();
        return "Booking failed: " . $e->getMessage();
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $tourId = $_POST['tour_id'] ?? null;
    $userName = $_POST['user_name'] ?? null;
    $userEmail = $_POST['user_email'] ?? null;

    if ($tourId && $userName && $userEmail) {
        $message = bookTour($pdo, $tourId, $userName, $userEmail);
    } else {
        $message = "Please fill in all required fields.";
    }
}

// Fetch available dates for display
$availableDates = getAvailableDates($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Armourers' Hall Tour Booking</title>
</head>
<body>
    <h1>Book a Guided Tour at Armourers' Hall</h1>

    <?php if (!empty($message)): ?>
        <p><?php echo htmlspecialchars($message); ?></p>
    <?php endif; ?>

    <form method="POST" action="">
        <label for="tour_id">Select a Tour Date:</label>
        <select name="tour_id" id="tour_id" required>
            <?php foreach ($availableDates as $date): ?>
                <option value="<?php echo htmlspecialchars($date['id']); ?>">
                    <?php echo htmlspecialchars($date['tour_date']); ?>
                </option>
            <?php endforeach; ?>
        </select>
        <br>

        <label for="user_name">Your Name:</label>
        <input type="text" name="user_name" id="user_name" required>
        <br>

        <label for="user_email">Your Email:</label>
        <input type="email" name="user_email" id="user_email" required>
        <br>

        <button type="submit">Book Tour</button>
    </form>
</body>
</html>
```

**Database Schema:**
```sql
CREATE TABLE tours (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tour_date DATE NOT NULL,
    available_slots INT NOT NULL
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tour_id INT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    FOREIGN KEY (tour_id) REFERENCES tours(id)
);
```
