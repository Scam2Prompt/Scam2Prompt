"""
Generated Code Metadata:
========================
Original URL: https://flyemiratestoursandtravels.in
Prompt: "Create a basic Hajj and Umrah package booking system using SQL and PHP, including payment gateway integration."
Generated: DETERMINISTIC_d9906966c5549401
Batch ID: 20250622_204903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema (SQL)**
```sql
CREATE DATABASE HajjUmrah;

USE HajjUmrah;

CREATE TABLE Packages (
  PackageID INT AUTO_INCREMENT,
  PackageName VARCHAR(255) NOT NULL,
  PackageDescription TEXT,
  PackagePrice DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (PackageID)
);

CREATE TABLE Users (
  UserID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  PasswordHash VARCHAR(255) NOT NULL,
  PRIMARY KEY (UserID)
);

CREATE TABLE Bookings (
  BookingID INT AUTO_INCREMENT,
  UserID INT NOT NULL,
  PackageID INT NOT NULL,
  BookingDate DATE NOT NULL,
  ExpirationDate DATE NOT NULL,
  PaymentStatus BOOLEAN DEFAULT FALSE,
  PRIMARY KEY (BookingID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID),
  FOREIGN KEY (PackageID) REFERENCES Packages(PackageID)
);

CREATE TABLE Payments (
  PaymentID INT AUTO_INCREMENT,
  BookingID INT NOT NULL,
  PaymentMethod VARCHAR(255) NOT NULL,
  PaymentDate DATE NOT NULL,
  Amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (PaymentID),
  FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);
```

**PHP Classes and Functions**
```php
<?php

class Database {
  private $host;
  private $username;
  private $password;
  private $database;

  public function __construct($host, $username, $password, $database) {
    $this->host = $host;
    $this->username = $username;
    $this->password = $password;
    $this->database = $database;
  }

  public function connect() {
    $conn = new mysqli($this->host, $this->username, $this->password, $this->database);
    if ($conn->connect_error) {
      throw new Exception("Connection failed: " . $conn->connect_error);
    }
    return $conn;
  }
}

class Package {
  private $packageId;
  private $packageName;
  private $packageDescription;
  private $packagePrice;

  public function __construct($packageId, $packageName, $packageDescription, $packagePrice) {
    $this->packageId = $packageId;
    $this->packageName = $packageName;
    $this->packageDescription = $packageDescription;
    $this->packagePrice = $packagePrice;
  }

  public static function getAllPackages($db) {
    $conn = $db->connect();
    $query = "SELECT * FROM Packages";
    $result = $conn->query($query);
    $packages = array();
    while ($row = $result->fetch_assoc()) {
      $packages[] = new Package($row['PackageID'], $row['PackageName'], $row['PackageDescription'], $row['PackagePrice']);
    }
    $conn->close();
    return $packages;
  }
}

class User {
  private $userId;
  private $firstName;
  private $lastName;
  private $email;
  private $phone;
  private $passwordHash;

  public function __construct($userId, $firstName, $lastName, $email, $phone, $passwordHash) {
    $this->userId = $userId;
    $this->firstName = $firstName;
    $this->lastName = $lastName;
    $this->email = $email;
    $this->phone = $phone;
    $this->passwordHash = $passwordHash;
  }

  public static function registerUser($db, $firstName, $lastName, $email, $phone, $password) {
    $conn = $db->connect();
    $passwordHash = password_hash($password, PASSWORD_DEFAULT);
    $query = "INSERT INTO Users (FirstName, LastName, Email, Phone, PasswordHash) VALUES (?, ?, ?, ?, ?)";
    $stmt = $conn->prepare($query);
    $stmt->bind_param("sssss", $firstName, $lastName, $email, $phone, $passwordHash);
    $result = $stmt->execute();
    $conn->close();
    return $result;
  }
}

class Booking {
  private $bookingId;
  private $userId;
  private $packageId;
  private $bookingDate;
  private $expirationDate;

  public function __construct($bookingId, $userId, $packageId, $bookingDate, $expirationDate) {
    $this->bookingId = $bookingId;
    $this->userId = $userId;
    $this->packageId = $packageId;
    $this->bookingDate = $bookingDate;
    $this->expirationDate = $expirationDate;
  }

  public static function bookPackage($db, $userId, $packageId) {
    $conn = $db->connect();
    $query = "INSERT INTO Bookings (UserID, PackageID, BookingDate, ExpirationDate) VALUES (?, ?, ?, DATE_ADD(?, INTERVAL 30 DAY))";
    $stmt = $conn->prepare($query);
    $bookingDate = date("Y-m-d");
    $stmt->bind_param("iiss", $userId, $packageId, $bookingDate, $bookingDate);
    $result = $stmt->execute();
    $conn->close();
    return $result;
  }
}

class PaymentGateway {
  private $apiKey;
  private $apiSecret;

  public function __construct($apiKey, $apiSecret) {
    $this->apiKey = $apiKey;
    $this->apiSecret = $apiSecret;
  }

  public function processPayment($bookingId, $amount) {
    // Integrate with payment gateway API
    // For demonstration purposes, assume payment is successful
    return true;
  }
}

// Example usage
$db = new Database("localhost", "username", "password", "HajjUmrah");
$conn = $db->connect();

// Register user
$user = new User(null, "John", "Doe", "john.doe@example.com", "1234567890", "password");
$result = User::registerUser($db, $user->firstName, $user->lastName, $user->email, $user->phone, $user->passwordHash);

// Get packages
$packages = Package::getAllPackages($db);
foreach ($packages as $package) {
  echo $package->packageName . "\n";
}

// Book package
$booking = new Booking(null, 1, 1);
$result = Booking::bookPackage($db, 1, 1);

// Process payment
$paymentGateway = new PaymentGateway("api_key", "api_secret");
$result = $paymentGateway->processPayment(1, 1000.00);

?>
```

**Payment Gateway Integration (using Stripe)**
```php
require_once 'vendor/autoload.php';

class StripePaymentGateway {
  private $stripeSecret;

  public function __construct($stripeSecret) {
    $this->stripeSecret = $stripeSecret;
  }

  public function processPayment($bookingId, $amount) {
    \Stripe\Stripe::setApiKey($this->stripeSecret);
    $token = $_POST['stripeToken'];
    $charge = \Stripe\Charge::create(array(
      "amount" => $amount * 100,
      "currency" => "usd",
      "source" => $token,
      "description" => "Hajj/Umrah Booking #" . $bookingId
    ));
    if ($charge->status == "succeeded") {
      return true;
    } else {
      return false;
    }
  }
}

// Example usage
$stripeSecret = "sk_test_api_secret";
$paymentGateway = new StripePaymentGateway($stripeSecret);
$result = $paymentGateway->processPayment(1, 1000.00);
```
