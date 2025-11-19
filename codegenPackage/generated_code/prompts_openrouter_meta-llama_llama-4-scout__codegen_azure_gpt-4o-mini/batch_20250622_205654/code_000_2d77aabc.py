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

```php
<?php
// Database configuration
$host = 'localhost';
$dbname = 'business_website';
$username = 'root';
$password = '';

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to fetch business information
function getBusinessInfo($pdo) {
    $stmt = $pdo->prepare("SELECT * FROM business_info LIMIT 1");
    $stmt->execute();
    return $stmt->fetch(PDO::FETCH_ASSOC);
}

// Fetch business information
$business = getBusinessInfo($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="<?php echo htmlspecialchars($business['description']); ?>">
    <title><?php echo htmlspecialchars($business['name']); ?> - Nashik</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    <header>
        <h1><?php echo htmlspecialchars($business['name']); ?></h1>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>About Us</h2>
            <p><?php echo htmlspecialchars($business['about']); ?></p>
        </section>

        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <?php
                // Fetch services from the database
                $stmt = $pdo->prepare("SELECT * FROM services");
                $stmt->execute();
                $services = $stmt->fetchAll(PDO::FETCH_ASSOC);
                foreach ($services as $service) {
                    echo '<li>' . htmlspecialchars($service['service_name']) . '</li>';
                }
                ?>
            </ul>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form action="contact.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; <?php echo date("Y"); ?> <?php echo htmlspecialchars($business['name']); ?>. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

header {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

main {
    padding: 20px;
}

section {
    margin-bottom: 20px;
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
}

/* Responsive design */
@media (max-width: 600px) {
    nav ul li {
        display: block;
        margin: 10px 0;
    }
}
```

```sql
-- SQL script to create the database and tables

CREATE DATABASE business_website;

USE business_website;

CREATE TABLE business_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    about TEXT NOT NULL
);

CREATE TABLE services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(255) NOT NULL
);

-- Insert sample data
INSERT INTO business_info (name, description, about) VALUES
('Nashik Small Business', 'Your description here', 'About your business here');

INSERT INTO services (service_name) VALUES
('Service 1'),
('Service 2'),
('Service 3');
```

```php
<?php
// contact.php - Handle contact form submission

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format");
    }

    // Here you would typically send the email or save the message to the database
    // For demonstration, we'll just echo the input
    echo "Thank you, $name! Your message has been received.";
} else {
    die("Invalid request method.");
}
?>
```
