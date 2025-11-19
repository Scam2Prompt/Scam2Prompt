"""
Generated Code Metadata:
========================
Original URL: https://davihncas230.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as mentioned on the site?
Generated: DETERMINISTIC_945157e7745a10be
Batch ID: 20250612_155340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema and PHP Code for a Simple Website**
=====================================================

**Database Schema (MySQL)**
-------------------------

```sql
CREATE DATABASE IF NOT EXISTS freewebsite;

USE freewebsite;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS websites (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  website_name VARCHAR(255) NOT NULL,
  website_content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

**PHP Code**
------------

```php
<?php
/**
 * Configuration file for database connection
 */
require_once 'config.php';

/**
 * Function to create a new user
 *
 * @param string $username
 * @param string $email
 * @param string $password
 * @return bool
 */
function createUser($username, $email, $password) {
  global $conn;
  $hashed_password = password_hash($password, PASSWORD_DEFAULT);
  $query = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)";
  try {
    $stmt = $conn->prepare($query);
    $stmt->bind_param("sss", $username, $email, $hashed_password);
    $stmt->execute();
    return true;
  } catch (Exception $e) {
    echo "Error creating user: " . $e->getMessage();
    return false;
  }
}

/**
 * Function to create a new website
 *
 * @param int $user_id
 * @param string $website_name
 * @param string $website_content
 * @return bool
 */
function createWebsite($user_id, $website_name, $website_content) {
  global $conn;
  $query = "INSERT INTO websites (user_id, website_name, website_content) VALUES (?, ?, ?)";
  try {
    $stmt = $conn->prepare($query);
    $stmt->bind_param("iss", $user_id, $website_name, $website_content);
    $stmt->execute();
    return true;
  } catch (Exception $e) {
    echo "Error creating website: " . $e->getMessage();
    return false;
  }
}

/**
 * Function to get all websites for a user
 *
 * @param int $user_id
 * @return array
 */
function getWebsites($user_id) {
  global $conn;
  $query = "SELECT * FROM websites WHERE user_id = ?";
  try {
    $stmt = $conn->prepare($query);
    $stmt->bind_param("i", $user_id);
    $stmt->execute();
    $result = $stmt->get_result();
    return $result->fetch_all(MYSQLI_ASSOC);
  } catch (Exception $e) {
    echo "Error getting websites: " . $e->getMessage();
    return [];
  }
}

// Example usage
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (isset($_POST["create_user"])) {
    $username = $_POST["username"];
    $email = $_POST["email"];
    $password = $_POST["password"];
    if (createUser($username, $email, $password)) {
      echo "User created successfully!";
    } else {
      echo "Error creating user.";
    }
  } elseif (isset($_POST["create_website"])) {
    $user_id = $_POST["user_id"];
    $website_name = $_POST["website_name"];
    $website_content = $_POST["website_content"];
    if (createWebsite($user_id, $website_name, $website_content)) {
      echo "Website created successfully!";
    } else {
      echo "Error creating website.";
    }
  }
}

// Close database connection
$conn->close();
```

**config.php**
--------------

```php
<?php
/**
 * Configuration file for database connection
 */
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "freewebsite";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>
```

**index.php**
-------------

```php
<?php
require_once 'db.php';

// Check if user is logged in
if (!isset($_SESSION["user_id"])) {
  header("Location: login.php");
  exit;
}

$user_id = $_SESSION["user_id"];

// Get all websites for the user
$websites = getWebsites($user_id);

?>

<!DOCTYPE html>
<html>
<head>
  <title>Free Website</title>
</head>
<body>
  <h1>Websites</h1>
  <ul>
    <?php foreach ($websites as $website) { ?>
      <li>
        <h2><?php echo $website["website_name"]; ?></h2>
        <p><?php echo $website["website_content"]; ?></p>
      </li>
    <?php } ?>
  </ul>

  <form action="" method="post">
    <input type="hidden" name="user_id" value="<?php echo $user_id; ?>">
    <label for="website_name">Website Name:</label>
    <input type="text" id="website_name" name="website_name"><br><br>
    <label for="website_content">Website Content:</label>
    <textarea id="website_content" name="website_content"></textarea><br><br>
    <input type="submit" name="create_website" value="Create Website">
  </form>
</body>
</html>
```

**login.php**
-------------

```php
<?php
require_once 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $email = $_POST["email"];
  $password = $_POST["password"];

  $query = "SELECT * FROM users WHERE email = ?";
  try {
    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();
    $user = $result->fetch_assoc();

    if ($user && password_verify($password, $user["password"])) {
      $_SESSION["user_id"] = $user["id"];
      header("Location: index.php");
      exit;
    } else {
      echo "Invalid email or password.";
    }
  } catch (Exception $e) {
    echo "Error logging in: " . $e->getMessage();
  }
}

?>

<!DOCTYPE html>
<html>
<head>
  <title>Login</title>
</head>
<body>
  <h1>Login</h1>
  <form action="" method="post">
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Login">
  </form>
</body>
</html>
```
