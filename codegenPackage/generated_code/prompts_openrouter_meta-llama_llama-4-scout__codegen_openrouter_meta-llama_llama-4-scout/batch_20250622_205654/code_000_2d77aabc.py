"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: "Develop a customized website for a small business in Nashik using PHP and MySQL, incorporating SEO optimization and responsive design."
Generated: DETERMINISTIC_2d77aabcb3b52249
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.php**
```php
<?php
/**
 * Index page of the website
 */

// Configuration
require_once 'config.php';

// Initialize session
session_start();

// Check if user is logged in
if (isset($_SESSION['logged_in'])) {
    header('Location: dashboard.php');
    exit;
}

// Include header and footer
require_once 'header.php';
require_once 'footer.php';

// SEO optimization
$page_title = 'Home | Small Business Website';
$page_description = 'Small business website in Nashik';

// Display content
?>

<!-- Hero Section -->
<section class="hero">
    <h1>Welcome to <?php echo $business_name; ?></h1>
    <p>We are a small business based in Nashik, providing [services/products].</p>
</section>

<!-- Services Section -->
<section class="services">
    <h2>Our Services</h2>
    <ul>
        <?php
        // Retrieve services from database
        $services = get_services();
        foreach ($services as $service) {
            echo '<li>' . $service['name'] . '</li>';
        }
        ?>
    </ul>
</section>

<!-- Contact Section -->
<section class="contact">
    <h2>Get in Touch</h2>
    <p>Contact us for more information:</p>
    <ul>
        <li>Email: <a href="mailto:<?php echo $email; ?>"><?php echo $email; ?></a></li>
        <li>Phone: <a href="tel:<?php echo $phone; ?>"><?php echo $phone; ?></a></li>
    </ul>
</section>
```

**config.php**
```php
<?php
/**
 * Configuration file
 */

// Database connection settings
$db_host = 'localhost';
$db_username = 'root';
$db_password = '';
$db_name = 'small_business';

// Business information
$business_name = 'ABC Enterprises';
$email = 'info@abc.com';
$phone = '1234567890';

// SEO optimization
$page_title = '';
$page_description = '';

// Function to get services from database
function get_services() {
    try {
        $conn = new PDO("mysql:host=$GLOBALS[db_host];dbname=$GLOBALS[db_name]", $GLOBALS[db_username], $GLOBALS[db_password]);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $stmt = $conn->prepare('SELECT * FROM services');
        $stmt->execute();
        $services = $stmt->fetchAll(PDO::FETCH_ASSOC);
        return $services;
    } catch (PDOException $e) {
        error_log($e->getMessage());
        return array();
    }
}
```

**header.php**
```php
<?php
/**
 * Header section of the website
 */

// Include CSS and JS files
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $page_title; ?></title>
    <meta name="description" content="<?php echo $page_description; ?>">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
```

**footer.php**
```php
<?php
/**
 * Footer section of the website
 ?>
<footer>
    <p>&copy; <?php echo date('Y'); ?> <?php echo $business_name; ?></p>
    <ul>
        <li><a href="#" target="_blank">Facebook</a></li>
        <li><a href="#" target="_blank">Twitter</a></li>
        <li><a href="#" target="_blank">Instagram</a></li>
    </ul>
</footer>

<script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
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

/* Hero Section */
.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    color: #fff;
    padding: 100px 0;
    text-align: center;
}

.hero h1 {
    font-size: 36px;
    margin-bottom: 20px;
}

/* Services Section */
.services {
    padding: 50px 0;
}

.services h2 {
    font-size: 24px;
    margin-bottom: 20px;
}

.services ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.services li {
    margin-bottom: 10px;
}

/* Contact Section */
.contact {
    padding: 50px 0;
}

.contact h2 {
    font-size: 24px;
    margin-bottom: 20px;
}

.contact ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.contact li {
    margin-bottom: 10px;
}

/* Responsive Design */
@media (max-width: 768px) {
    .hero {
        padding: 50px 0;
    }
    .services, .contact {
        padding: 30px 0;
    }
}
```

**script.js**
```javascript
// Add event listeners to navigation links
document.querySelectorAll('nav ul li a').forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const href = link.getAttribute('href');
        document.querySelector(href).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
```

**database.sql**
```sql
CREATE TABLE services (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

INSERT INTO services (name, description) VALUES
('Service 1', 'This is service 1'),
('Service 2', 'This is service 2'),
('Service 3', 'This is service 3');
```

**dashboard.php**
```php
<?php
/**
 * Dashboard page for logged in users
 */

// Configuration
require_once 'config.php';

// Initialize session
session_start();

// Check if user is logged in
if (!isset($_SESSION['logged_in'])) {
    header('Location: index.php');
    exit;
}

// Include header and footer
require_once 'header.php';
require_once 'footer.php';

// Display content
?>

<!-- Dashboard Content -->
<section class="dashboard">
    <h1>Welcome, <?php echo $_SESSION['username']; ?></h1>
    <p>This is your dashboard.</p>
</section>
```

**login.php**
```php
<?php
/**
 * Login page
 */

// Configuration
require_once 'config.php';

// Initialize session
session_start();

// Check if user is logged in
if (isset($_SESSION['logged_in'])) {
    header('Location: dashboard.php');
    exit;
}

// Handle login form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    try {
        $conn = new PDO("mysql:host=$db_host;dbname=$db_name", $db_username, $db_password);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $stmt = $conn->prepare('SELECT * FROM users WHERE username = :username');
        $stmt->bindParam(':username', $username);
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($password, $user['password'])) {
            $_SESSION['logged_in'] = true;
            $_SESSION['username'] = $username;
            header('Location: dashboard.php');
            exit;
        } else {
            $error = 'Invalid username or password';
        }
    } catch (PDOException $e) {
        error_log($e->getMessage());
        $error = 'Database error';
    }
}
?>

<!-- Login Form -->
<form action="" method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Login">
    <?php if (isset($error)) { echo '<p style="color: red;">' . $error . '</p>'; } ?>
</form>
```
