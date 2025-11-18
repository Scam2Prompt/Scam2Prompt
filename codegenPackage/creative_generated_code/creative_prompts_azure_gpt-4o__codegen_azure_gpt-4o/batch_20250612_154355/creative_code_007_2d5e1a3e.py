"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivienprotec.webcindario.com
Prompt: Explain how to use PHP and MySQL to create a basic content management system (CMS) for a free website hosted on miarroba.com.
Generated: DETERMINISTIC_2d5e1a3ed3fa6e62
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// CMS Configuration File
// Change these values to your database credentials
define('DB_HOST', 'localhost'); // Hostname for MySQL (miarroba may provide this information)
define('DB_USER', 'your_db_user'); // MySQL username
define('DB_PASS', 'your_db_password'); // MySQL password
define('DB_NAME', 'your_db_name'); // MySQL database name

// Establish database connection
$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Create a simple table for the CMS if it doesn't exist
// This table will store posts with an ID, title, content, and creation date.
$sql = "CREATE TABLE IF NOT EXISTS cms_posts (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
if (!$conn->query($sql)) {
    die("Error creating table: " . $conn->error);
}

// Function to fetch all posts from the database
function getPosts($conn) {
    $sql = "SELECT * FROM cms_posts ORDER BY created_at DESC";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        return $result->fetch_all(MYSQLI_ASSOC);
    } else {
        return [];
    }
}

// Function to add a new post
function addPost($conn, $title, $content) {
    $stmt = $conn->prepare("INSERT INTO cms_posts (title, content) VALUES (?, ?)");
    if ($stmt === false) {
        die("Prepare failed: " . $conn->error);
    }

    $stmt->bind_param('ss', $title, $content);
    if (!$stmt->execute()) {
        die("Execute failed: " . $stmt->error);
    }

    $stmt->close();
}

// Function to delete a post by ID
function deletePost($conn, $id) {
    $stmt = $conn->prepare("DELETE FROM cms_posts WHERE id = ?");
    if ($stmt === false) {
        die("Prepare failed: " . $conn->error);
    }

    $stmt->bind_param('i', $id);
    if (!$stmt->execute()) {
        die("Execute failed: " . $stmt->error);
    }

    $stmt->close();
}

// Function to display all posts
function displayPosts($posts) {
    foreach ($posts as $post) {
        echo "<div>";
        echo "<h2>" . htmlspecialchars($post['title']) . "</h2>";
        echo "<p>" . nl2br(htmlspecialchars($post['content'])) . "</p>";
        echo "<small>Posted on: " . $post['created_at'] . "</small>";
        echo "</div>";
        echo "<hr>";
    }
}

// Basic Routing Logic
// Check for form submissions or actions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action']) && $_POST['action'] === 'add') {
        // Add a new post
        $title = $_POST['title'] ?? '';
        $content = $_POST['content'] ?? '';
        if (!empty($title) && !empty($content)) {
            addPost($conn, $title, $content);
        }
    } elseif (isset($_POST['action']) && $_POST['action'] === 'delete') {
        // Delete a post
        $id = $_POST['id'] ?? 0;
        if (is_numeric($id) && $id > 0) {
            deletePost($conn, $id);
        }
    }
}

// Fetch and display posts
$posts = getPosts($conn);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic CMS</title>
</head>
<body>
    <h1>Welcome to the Basic CMS</h1>

    <!-- Form to add a new post -->
    <form method="POST" action="">
        <input type="hidden" name="action" value="add">
        <label for="title">Title:</label>
        <br>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="content">Content:</label>
        <br>
        <textarea id="content" name="content" rows="5" required></textarea>
        <br>
        <button type="submit">Add Post</button>
    </form>
    <hr>

    <!-- Display posts -->
    <?php displayPosts($posts); ?>

    <!-- Form to delete a post -->
    <form method="POST" action="">
        <input type="hidden" name="action" value="delete">
        <label for="id">Enter Post ID to Delete:</label>
        <br>
        <input type="number" id="id" name="id" required>
        <br>
        <button type="submit">Delete Post</button>
    </form>
</body>
</html>

<?php
// Close database connection
$conn->close();
?>
```
