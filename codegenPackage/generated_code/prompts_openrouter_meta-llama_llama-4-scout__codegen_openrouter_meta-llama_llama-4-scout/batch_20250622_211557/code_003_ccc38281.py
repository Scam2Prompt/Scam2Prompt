"""
Generated Code Metadata:
========================
Original URL: https://elitepain.org
Prompt: How do I create a secure login system with email and password functionality using a programming language like PHP or Ruby?
Generated: DETERMINISTIC_ccc3828199f57474
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Secure Login System using PHP and MySQL**
====================================================

**Database Schema**
------------------

```sql
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**PHP Code**
-------------

```php
<?php
/**
 * Secure Login System using PHP and MySQL
 */

// Configuration
$config = [
  'db_host' => 'localhost',
  'db_username' => 'your_username',
  'db_password' => 'your_password',
  'db_name' => 'your_database',
];

// Database Connection
class Database {
  private $conn;

  public function __construct($config) {
    $this->conn = new mysqli($config['db_host'], $config['db_username'], $config['db_password'], $config['db_name']);

    if ($this->conn->connect_error) {
      throw new Exception('Database connection failed: ' . $this->conn->connect_error);
    }
  }

  public function __destruct() {
    $this->conn->close();
  }

  public function query($sql, $params = []) {
    $stmt = $this->conn->prepare($sql);
    if (!empty($params)) {
      $types = str_repeat('s', count($params));
      $stmt->bind_param($types, ...$params);
    }
    $stmt->execute();
    return $stmt;
  }
}

// User Model
class User {
  private $db;

  public function __construct(Database $db) {
    $this->db = $db;
  }

  public function register($email, $password) {
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);
    $sql = 'INSERT INTO users (email, password) VALUES (?, ?)';
    $stmt = $this->db->query($sql, [$email, $hashedPassword]);
    return $stmt->affected_rows === 1;
  }

  public function login($email, $password) {
    $sql = 'SELECT password FROM users WHERE email = ?';
    $stmt = $this->db->query($sql, [$email]);
    $user = $stmt->fetch_assoc();
    if (!$user) {
      return false;
    }
    return password_verify($password, $user['password']);
  }
}

// Authentication
class Auth {
  private $user;

  public function __construct(User $user) {
    $this->user = $user;
  }

  public function register($email, $password) {
    try {
      $registered = $this->user->register($email, $password);
      if ($registered) {
        return ['success' => true, 'message' => 'User registered successfully'];
      } else {
        return ['success' => false, 'message' => 'User registration failed'];
      }
    } catch (Exception $e) {
      return ['success' => false, 'message' => 'Error: ' . $e->getMessage()];
    }
  }

  public function login($email, $password) {
    try {
      $loggedIn = $this->user->login($email, $password);
      if ($loggedIn) {
        // Session management
        session_start();
        $_SESSION['email'] = $email;
        return ['success' => true, 'message' => 'User logged in successfully'];
      } else {
        return ['success' => false, 'message' => 'Invalid email or password'];
      }
    } catch (Exception $e) {
      return ['success' => false, 'message' => 'Error: ' . $e->getMessage()];
    }
  }
}

// Usage
$db = new Database($config);
$user = new User($db);
$auth = new Auth($user);

// Register
$email = 'user@example.com';
$password = 'password123';
$result = $auth->register($email, $password);
print_r($result);

// Login
$email = 'user@example.com';
$password = 'password123';
$result = $auth->login($email, $password);
print_r($result);
```

**Secure Login System using Ruby and MySQL**
=============================================

**Database Schema**
------------------

```sql
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Ruby Code**
-------------

```ruby
require 'mysql2'
require 'bcrypt'

# Configuration
config = {
  host: 'localhost',
  username: 'your_username',
  password: 'your_password',
  database: 'your_database',
}

# Database Connection
class Database
  def initialize(config)
    @conn = Mysql2::Client.new(host: config[:host], username: config[:username], password: config[:password], database: config[:database])
  end

  def query(sql, params = [])
    @conn.prepare(sql).execute(*params)
  end
end

# User Model
class User
  def initialize(db)
    @db = db
  end

  def register(email, password)
    hashed_password = BCrypt.hash_password(password)
    sql = 'INSERT INTO users (email, password) VALUES (?, ?)'
    result = @db.query(sql, [email, hashed_password])
    result.affected_rows == 1
  end

  def login(email, password)
    sql = 'SELECT password FROM users WHERE email = ?'
    result = @db.query(sql, [email])
    user = result.first
    return false unless user
    BCrypt.verify(password, user['password'])
  end
end

# Authentication
class Auth
  def initialize(user)
    @user = user
  end

  def register(email, password)
    begin
      registered = @user.register(email, password)
      if registered
        { success: true, message: 'User registered successfully' }
      else
        { success: false, message: 'User registration failed' }
      end
    rescue StandardError => e
      { success: false, message: "Error: #{e.message}" }
    end
  end

  def login(email, password)
    begin
      logged_in = @user.login(email, password)
      if logged_in
        # Session management
        # For simplicity, we'll use a simple session store
        session = {}
        session[:email] = email
        { success: true, message: 'User logged in successfully' }
      else
        { success: false, message: 'Invalid email or password' }
      end
    rescue StandardError => e
      { success: false, message: "Error: #{e.message}" }
    end
  end
end

# Usage
db = Database.new(config)
user = User.new(db)
auth = Auth.new(user)

# Register
email = 'user@example.com'
password = 'password123'
result = auth.register(email, password)
puts result.inspect

# Login
email = 'user@example.com'
password = 'password123'
result = auth.login(email, password)
puts result.inspect
```
