"""
Generated Code Metadata:
========================
Original URL: https://giitechcodes.com.ng
Prompt: Build a database-driven web application using SQL and PHP, incorporating the internet protocol-based software solutions described by GII Tech Codes.
Generated: DETERMINISTIC_2979e2000ca8a85c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema**
```sql
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE gii_tech_codes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  code VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_gii_tech_codes (
  user_id INT NOT NULL,
  gii_tech_code_id INT NOT NULL,
  PRIMARY KEY (user_id, gii_tech_code_id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (gii_tech_code_id) REFERENCES gii_tech_codes(id)
);
```

**PHP Configuration**
```php
<?php
// config.php

class Config {
  const DB_HOST = 'localhost';
  const DB_USERNAME = 'root';
  const DB_PASSWORD = 'password';
  const DB_NAME = 'gii_tech_codes_db';

  const GII_TECH_CODES = [
    'TCP/IP' => 'Transmission Control Protocol/Internet Protocol',
    'HTTP' => 'Hypertext Transfer Protocol',
    'FTP' => 'File Transfer Protocol',
    // Add more GII Tech Codes as needed
  ];
}
```

**Database Connection**
```php
<?php
// db.php

class Database {
  private $host;
  private $username;
  private $password;
  private $name;

  public function __construct() {
    $this->host = Config::DB_HOST;
    $this->username = Config::DB_USERNAME;
    $this->password = Config::DB_PASSWORD;
    $this->name = Config::DB_NAME;
  }

  public function connect() {
    try {
      $conn = new PDO("mysql:host=$this->host;dbname=$this->name", $this->username, $this->password);
      $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      return $conn;
    } catch (PDOException $e) {
      throw new Exception("Database connection failed: " . $e->getMessage());
    }
  }
}
```

**User Model**
```php
<?php
// user.php

class User {
  private $id;
  private $username;
  private $email;
  private $password;

  public function __construct($id, $username, $email, $password) {
    $this->id = $id;
    $this->username = $username;
    $this->email = $email;
    $this->password = $password;
  }

  public static function create($username, $email, $password, $conn) {
    try {
      $stmt = $conn->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
      $stmt->bindParam(':username', $username);
      $stmt->bindParam(':email', $email);
      $stmt->bindParam(':password', $password);
      $stmt->execute();
      return new User($conn->lastInsertId(), $username, $email, $password);
    } catch (PDOException $e) {
      throw new Exception("Failed to create user: " . $e->getMessage());
    }
  }

  public static function get($id, $conn) {
    try {
      $stmt = $conn->prepare("SELECT * FROM users WHERE id = :id");
      $stmt->bindParam(':id', $id);
      $stmt->execute();
      $user = $stmt->fetch();
      if ($user) {
        return new User($user['id'], $user['username'], $user['email'], $user['password']);
      } else {
        return null;
      }
    } catch (PDOException $e) {
      throw new Exception("Failed to get user: " . $e->getMessage());
    }
  }
}
```

**GII Tech Code Model**
```php
<?php
// gii_tech_code.php

class GiiTechCode {
  private $id;
  private $code;
  private $description;

  public function __construct($id, $code, $description) {
    $this->id = $id;
    $this->code = $code;
    $this->description = $description;
  }

  public static function create($code, $description, $conn) {
    try {
      $stmt = $conn->prepare("INSERT INTO gii_tech_codes (code, description) VALUES (:code, :description)");
      $stmt->bindParam(':code', $code);
      $stmt->bindParam(':description', $description);
      $stmt->execute();
      return new GiiTechCode($conn->lastInsertId(), $code, $description);
    } catch (PDOException $e) {
      throw new Exception("Failed to create GII Tech Code: " . $e->getMessage());
    }
  }

  public static function get($id, $conn) {
    try {
      $stmt = $conn->prepare("SELECT * FROM gii_tech_codes WHERE id = :id");
      $stmt->bindParam(':id', $id);
      $stmt->execute();
      $giiTechCode = $stmt->fetch();
      if ($giiTechCode) {
        return new GiiTechCode($giiTechCode['id'], $giiTechCode['code'], $giiTechCode['description']);
      } else {
        return null;
      }
    } catch (PDOException $e) {
      throw new Exception("Failed to get GII Tech Code: " . $e->getMessage());
    }
  }
}
```

**User GII Tech Code Model**
```php
<?php
// user_gii_tech_code.php

class UserGiiTechCode {
  private $userId;
  private $giiTechCodeId;

  public function __construct($userId, $giiTechCodeId) {
    $this->userId = $userId;
    $this->giiTechCodeId = $giiTechCodeId;
  }

  public static function create($userId, $giiTechCodeId, $conn) {
    try {
      $stmt = $conn->prepare("INSERT INTO user_gii_tech_codes (user_id, gii_tech_code_id) VALUES (:user_id, :gii_tech_code_id)");
      $stmt->bindParam(':user_id', $userId);
      $stmt->bindParam(':gii_tech_code_id', $giiTechCodeId);
      $stmt->execute();
      return new UserGiiTechCode($userId, $giiTechCodeId);
    } catch (PDOException $e) {
      throw new Exception("Failed to create User GII Tech Code: " . $e->getMessage());
    }
  }

  public static function get($userId, $giiTechCodeId, $conn) {
    try {
      $stmt = $conn->prepare("SELECT * FROM user_gii_tech_codes WHERE user_id = :user_id AND gii_tech_code_id = :gii_tech_code_id");
      $stmt->bindParam(':user_id', $userId);
      $stmt->bindParam(':gii_tech_code_id', $giiTechCodeId);
      $stmt->execute();
      $userGiiTechCode = $stmt->fetch();
      if ($userGiiTechCode) {
        return new UserGiiTechCode($userId, $giiTechCodeId);
      } else {
        return null;
      }
    } catch (PDOException $e) {
      throw new Exception("Failed to get User GII Tech Code: " . $e->getMessage());
    }
  }
}
```

**Main Application**
```php
<?php
// index.php

require_once 'config.php';
require_once 'db.php';
require_once 'user.php';
require_once 'gii_tech_code.php';
require_once 'user_gii_tech_code.php';

$conn = (new Database())->connect();

if (isset($_POST['create_user'])) {
  $username = $_POST['username'];
  $email = $_POST['email'];
  $password = $_POST['password'];

  try {
    $user = User::create($username, $email, $password, $conn);
    echo "User created successfully!";
  } catch (Exception $e) {
    echo "Error: " . $e->getMessage();
  }
}

if (isset($_POST['create_gii_tech_code'])) {
  $code = $_POST['code'];
  $description = $_POST['description'];

  try {
    $giiTechCode = GiiTechCode::create($code, $description, $conn);
    echo "GII Tech Code created successfully!";
  } catch (Exception $e) {
    echo "Error: " . $e->getMessage();
  }
}

if (isset($_POST['assign_gii_tech_code'])) {
  $userId = $_POST['user_id'];
  $giiTechCodeId = $_POST['gii_tech_code_id'];

  try {
    $userGiiTechCode = UserGiiTechCode::create($userId, $giiTechCodeId, $conn);
    echo "GII Tech Code assigned to user successfully!";
  } catch (Exception $e) {
    echo "Error
