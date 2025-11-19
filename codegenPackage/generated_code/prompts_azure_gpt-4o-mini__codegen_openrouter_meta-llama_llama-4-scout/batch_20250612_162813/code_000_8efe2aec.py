"""
Generated Code Metadata:
========================
Original URL: https://ideru.com
Prompt: How can I create a responsive web design using PHP and MySQL that optimizes user experience across devices?
Generated: DETERMINISTIC_8efe2aec11c69dbe
Batch ID: 20250612_162813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Responsive Web Design using PHP and MySQL**
====================================================

**Database Schema**
------------------

```sql
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pages (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**config.php**
-------------

```php
<?php
/**
 * Configuration file for database connection
 */

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'your_database');

// Create a PDO instance
try {
  $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USERNAME, DB_PASSWORD);
  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
  exit();
}
```

**functions.php**
----------------

```php
<?php
/**
 * Functions for database operations
 */

/**
 * Get all pages from database
 * @return array
 */
function getPages($pdo) {
  try {
    $stmt = $pdo->prepare("SELECT * FROM pages ORDER BY created_at DESC");
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
    return [];
  }
}

/**
 * Get a page by id from database
 * @param int $id
 * @return array
 */
function getPage($pdo, $id) {
  try {
    $stmt = $pdo->prepare("SELECT * FROM pages WHERE id = :id");
    $stmt->bindParam(':id', $id);
    $stmt->execute();
    return $stmt->fetch(PDO::FETCH_ASSOC);
  } catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
    return [];
  }
}
```

**index.php**
-------------

```php
<?php
require_once 'config.php';
require_once 'functions.php';

// Get all pages
$pages = getPages($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Web Design</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <nav>
      <ul>
        <?php foreach ($pages as $page) : ?>
          <li><a href="page.php?id=<?php echo $page['id']; ?>"><?php echo $page['title']; ?></a></li>
        <?php endforeach; ?>
      </ul>
    </nav>
  </header>
  <main>
    <h1>Welcome to our website</h1>
  </main>
</body>
</html>
```

**page.php**
------------

```php
<?php
require_once 'config.php';
require_once 'functions.php';

// Get page id from query string
$id = filter_var($_GET['id'], FILTER_SANITIZE_NUMBER_INT);

// Get page data
$page = getPage($pdo, $id);
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><?php echo $page['title']; ?></title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <nav>
      <ul>
        <?php
        $pages = getPages($pdo);
        foreach ($pages as $p) :
        ?>
          <li><a href="page.php?id=<?php echo $p['id']; ?>"><?php echo $p['title']; ?></a></li>
        <?php endforeach; ?>
      </ul>
    </nav>
  </header>
  <main>
    <h1><?php echo $page['title']; ?></h1>
    <p><?php echo $page['content']; ?></p>
  </main>
</body>
</html>
```

**styles.css**
-------------

```css
/* Global styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

header {
  background-color: #333;
  color: #fff;
  padding: 1em;
  text-align: center;
}

header nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

header nav ul li {
  margin-right: 20px;
}

header nav a {
  color: #fff;
  text-decoration: none;
}

main {
  display: block;
  padding: 2em;
}

/* Responsive design */

/* Mobile devices */
@media only screen and (max-width: 768px) {
  header nav ul {
    flex-direction: column;
  }

  header nav ul li {
    margin-right: 0;
    margin-bottom: 10px;
  }
}

/* Tablet devices */
@media only screen and (min-width: 769px) and (max-width: 1024px) {
  header nav ul {
    justify-content: space-around;
  }
}

/* Desktop devices */
@media only screen and (min-width: 1025px) {
  header nav ul {
    justify-content: space-between;
  }
}
```
