"""
Generated Code Metadata:
========================
Original URL: https://coosella5554.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as mentioned on coosella5554.webcindario.com?
Generated: DETERMINISTIC_366846022b69a749
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Configuration (config.php)
<?php
// Database connection settings
define('DB_HOST', 'localhost');
define('DB_USER', 'username'); // Replace with your MySQL username
define('DB_PASS', 'password'); // Replace with your MySQL password
define('DB_NAME', 'free_website_db'); // Replace with your database name

// Establish database connection
try {
    $db = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
?>

# Database Schema Setup (setup.php)
<?php
require_once 'config.php';

try {
    // Create pages table
    $db->exec("CREATE TABLE IF NOT EXISTS pages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT,
        slug VARCHAR(255) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )");

    // Create settings table
    $db->exec("CREATE TABLE IF NOT EXISTS settings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        site_name VARCHAR(255) NOT NULL,
        site_description TEXT,
        theme VARCHAR(50) DEFAULT 'default'
    )");

    // Insert default settings if not exists
    $stmt = $db->prepare("INSERT IGNORE INTO settings (site_name, site_description) VALUES (?, ?)");
    $stmt->execute(['My Free Website', 'A simple website built with PHP and MySQL']);

    echo "Database setup completed successfully.";
} catch(PDOException $e) {
    die("Database setup failed: " . $e->getMessage());
}
?>

# Website Functions (functions.php)
<?php
require_once 'config.php';

function get_page_by_slug($slug) {
    global $db;
    try {
        $stmt = $db->prepare("SELECT * FROM pages WHERE slug = ?");
        $stmt->execute([$slug]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    } catch(PDOException $e) {
        error_log("Error fetching page: " . $e->getMessage());
        return false;
    }
}

function get_site_settings() {
    global $db;
    try {
        $stmt = $db->query("SELECT * FROM settings LIMIT 1");
        return $stmt->fetch(PDO::FETCH_ASSOC);
    } catch(PDOException $e) {
        error_log("Error fetching settings: " . $e->getMessage());
        return false;
    }
}

function get_all_pages() {
    global $db;
    try {
        $stmt = $db->query("SELECT id, title, slug FROM pages ORDER BY created_at DESC");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch(PDOException $e) {
        error_log("Error fetching pages: " . $e->getMessage());
        return [];
    }
}
?>

# Main Website Template (index.php)
<?php
require_once 'config.php';
require_once 'functions.php';

// Get requested page slug
$slug = isset($_GET['page']) ? trim($_GET['page']) : 'home';

// Get page content
$page = get_page_by_slug($slug);
if (!$page) {
    $slug = 'home';
    $page = get_page_by_slug($slug);
    if (!$page) {
        die("Home page not found. Please run setup.php first.");
    }
}

// Get site settings
$settings = get_site_settings();
if (!$settings) {
    die("Site settings not found. Please run setup.php first.");
}

// Get all pages for navigation
$pages = get_all_pages();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo htmlspecialchars($settings['site_name']); ?> - <?php echo htmlspecialchars($page['title']); ?></title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; }
        header { background: #333; color: #fff; padding: 1rem; }
        nav ul { list-style: none; padding: 0; display: flex; }
        nav ul li { margin-right: 1rem; }
        nav ul li a { color: #fff; text-decoration: none; }
        main { padding: 1rem; }
        footer { background: #333; color: #fff; text-align: center; padding: 1rem; margin-top: 1rem; }
    </style>
</head>
<body>
    <header>
        <h1><?php echo htmlspecialchars($settings['site_name']); ?></h1>
        <nav>
            <ul>
                <?php foreach ($pages as $p): ?>
                    <li><a href="?page=<?php echo htmlspecialchars($p['slug']); ?>"><?php echo htmlspecialchars($p['title']); ?></a></li>
                <?php endforeach; ?>
            </ul>
        </nav>
    </header>
    
    <main>
        <h2><?php echo htmlspecialchars($page['title']); ?></h2>
        <div><?php echo nl2br(htmlspecialchars($page['content'])); ?></div>
    </main>
    
    <footer>
        <p><?php echo htmlspecialchars($settings['site_description']); ?></p>
    </footer>
</body>
</html>

# Admin Panel (admin.php)
<?php
require_once 'config.php';
require_once 'functions.php';

session_start();

// Check if user is logged in
if (!isset($_SESSION['admin_logged_in'])) {
    header('Location: admin_login.php');
    exit;
}

$settings = get_site_settings();
$pages = get_all_pages();

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        if (isset($_POST['update_settings'])) {
            $stmt = $db->prepare("UPDATE settings SET site_name = ?, site_description = ? WHERE id = 1");
            $stmt->execute([$_POST['site_name'], $_POST['site_description']]);
            $message = "Settings updated successfully!";
            $settings = get_site_settings(); // Refresh settings
        } elseif (isset($_POST['add_page'])) {
            $stmt = $db->prepare("INSERT INTO pages (title, content, slug) VALUES (?, ?, ?)");
            $stmt->execute([
                $_POST['title'],
                $_POST['content'],
                $_POST['slug']
            ]);
            $message = "Page added successfully!";
            $pages = get_all_pages(); // Refresh pages list
        }
    } catch(PDOException $e) {
        $error = "Database error: " . $e->getMessage();
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        .container { max-width: 1200px; margin: 0 auto; padding: 1rem; }
        .form-group { margin-bottom: 1rem; }
        label { display: block; margin-bottom: 0.5rem; }
        input, textarea { width: 100%; padding: 0.5rem; }
        textarea { min-height: 200px; }
        .message { padding: 1rem; margin-bottom: 1rem; background: #dff0d8; color: #3c763d; }
        .error { background: #f2dede; color: #a94442; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Admin Panel</h1>
        
        <?php if (isset($message)): ?>
            <div class="message"><?php echo htmlspecialchars($message); ?></div>
        <?php endif; ?>
        
        <?php if (isset($error)): ?>
            <div class="message error"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>
        
        <h2>Update Site Settings</h2>
        <form method="post">
            <div class="form-group">
                <label for="site_name">Site Name</label>
                <input type="text" id="site_name" name="site_name" value="<?php echo htmlspecialchars($settings['site_name']); ?>" required>
            </div>
            <div class="form-group">
                <label for="site_description">Site Description</label>
                <textarea id="site_description" name="site_description" required><?
