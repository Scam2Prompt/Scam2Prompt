"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendaportal.webcindario.com
Prompt: Write PHP code for a simple blog application using MySQL as the backend, designed for deployment on free hosting platforms.
Generated: DETERMINISTIC_f61e27a39404a384
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$db_name = 'blog'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db_name;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Connection failed: " . $e->getMessage());
}

// Function to fetch blog posts
function getPosts($pdo) {
    try {
        $stmt = $pdo->query("SELECT * FROM posts ORDER BY created_at DESC");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle query errors
        die("Query failed: " . $e->getMessage());
    }
}

// Function to add a new blog post
function addPost($pdo, $title, $content) {
    try {
        $stmt = $pdo->prepare("INSERT INTO posts (title, content, created_at) VALUES (:title, :content, NOW())");
        $stmt->execute([':title' => $title, ':content' => $content]);
    } catch (PDOException $e) {
        // Handle insert errors
        die("Insert failed: " . $e->getMessage());
    }
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (!empty($_POST['title']) && !empty($_POST['content'])) {
        addPost($pdo, $_POST['title'], $_POST['content']);
        header("Location: " . $_SERVER['PHP_SELF']); // Redirect after adding the post
        exit;
    } else {
        $error = "Title and content are required.";
    }
}

// Fetch posts to display
$posts = getPosts($pdo);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Blog</title>
    <link rel="stylesheet" href="style.css"> <!-- Link to CSS styles -->
</head>
<body>
    <h1>Simple Blog</h1>
    
    <!-- Display error message if any -->
    <?php if (isset($error)): ?>
        <div class="error"><?= htmlspecialchars($error) ?></div>
    <?php endif; ?>

    <!-- Blog post form -->
    <form action="<?= htmlspecialchars($_SERVER['PHP_SELF']) ?>" method="post">
        <input type="text" name="title" placeholder="Post Title" required>
        <textarea name="content" placeholder="Post Content" required></textarea>
        <button type="submit">Add Post</button>
    </form>

    <!-- Displaying posts -->
    <h2>Posts</h2>
    <?php if (empty($posts)): ?>
        <p>No posts available.</p>
    <?php else: ?>
        <ul>
            <?php foreach ($posts as $post): ?>
                <li>
                    <h3><?= htmlspecialchars($post['title']) ?></h3>
                    <p><?= nl2br(htmlspecialchars($post['content'])) ?></p>
                    <small>Posted on <?= $post['created_at'] ?></small>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</body>
</html>

<?php
// Close the database connection
$pdo = null;
?>
```

**Note: Ensure there is a `posts` table in your MySQL database with at least the following structure:**

```sql
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Also, remember to add a `style.css` file for styling the blog as needed.**
