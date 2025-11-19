"""
Generated Code Metadata:
========================
Original URL: https://enjin.pro
Prompt: Write PHP code to implement a booking system for car inspections and repairs, as offered by "縁陣 -ENJIN-".
Generated: DETERMINISTIC_ad5536f5944a1ca7
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Car Inspection and Repair Booking System for 縁陣 -ENJIN-

// Database connection settings
$host = 'localhost';
$db = 'car_inspection';
$user = 'root';
$pass = 'password'; // Change to your database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to create a new booking
function createBooking($customerName, $carModel, $inspectionDate) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO bookings (customer_name, car_model, inspection_date) VALUES (:customer_name, :car_model, :inspection_date)");

    // Bind parameters
    $stmt->bindParam(':customer_name', $customerName);
    $stmt->bindParam(':car_model', $carModel);
    $stmt->bindParam(':inspection_date', $inspectionDate);

    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return $pdo->lastInsertId(); // Return the ID of the new booking
    } catch (PDOException $e) {
        die("Error creating booking: " . $e->getMessage());
    }
}

// Function to retrieve all bookings
function getBookings() {
    global $pdo;

    // Prepare SQL statement
    $stmt = $pdo->prepare("SELECT * FROM bookings ORDER BY inspection_date ASC");

    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC); // Return all bookings as an associative array
    } catch (PDOException $e) {
        die("Error retrieving bookings: " . $e->getMessage());
    }
}

// Function to delete a booking by ID
function deleteBooking($bookingId) {
    global $pdo;

    // Prepare SQL statement
    $stmt = $pdo->prepare("DELETE FROM bookings WHERE id = :id");

    // Bind parameters
    $stmt->bindParam(':id', $bookingId, PDO::PARAM_INT);

    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return $stmt->rowCount(); // Return the number of deleted rows
    } catch (PDOException $e) {
        die("Error deleting booking: " . $e->getMessage());
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Create a new booking from POST data
    $customerName = $_POST['customer_name'] ?? '';
    $carModel = $_POST['car_model'] ?? '';
    $inspectionDate = $_POST['inspection_date'] ?? '';

    if ($customerName && $carModel && $inspectionDate) {
        $bookingId = createBooking($customerName, $carModel, $inspectionDate);
        echo "Booking created successfully with ID: $bookingId";
    } else {
        echo "Please provide all required fields.";
    }
}

// Retrieve and display all bookings
$bookings = getBookings();
foreach ($bookings as $booking) {
    echo "ID: {$booking['id']}, Customer: {$booking['customer_name']}, Car Model: {$booking['car_model']}, Inspection Date: {$booking['inspection_date']}<br>";
}

// Example of deleting a booking (uncomment to use)
// $deletedRows = deleteBooking(1); // Replace 1 with the actual booking ID to delete
// echo "$deletedRows booking(s) deleted.";
?>
```

**Note:** Ensure that you have a MySQL database set up with a `bookings` table that has the following structure:

```sql
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    car_model VARCHAR(255) NOT NULL,
    inspection_date DATE NOT NULL
);
```

Make sure to adjust the database connection settings and handle any additional security measures as needed for production.
