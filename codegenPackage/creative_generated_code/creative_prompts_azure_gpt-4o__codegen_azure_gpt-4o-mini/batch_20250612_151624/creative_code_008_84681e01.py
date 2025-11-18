"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingreseaquii.webcindario.com
Prompt: Write code to implement a basic content management system (CMS) using PHP and MySQL, suitable for deployment on free hosting platforms.
Generated: DETERMINISTIC_84681e0121ea35dd
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Basic Content Management System (CMS) using PHP and MySQL

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'cms_db';  // Database name
$username = 'root';  // Database username
$password = '';      // Database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Function to create a new post
function createPost($title, $content) {
    global $pdo;
    $sql = "INSERT INTO posts (title, content, created_at) VALUES (:title, :content, NOW())";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':title', $title);
    $stmt->bindParam(':content', $content);
    
    try {
        return $stmt->execute();
    } catch (Exception $e) {
        echo "Error creating post: " . $e->getMessage();
    }
}

// Function to retrieve all posts
function getPosts() {
    global $pdo;
    $sql = "SELECT * FROM posts ORDER BY created_at DESC";
    $stmt = $pdo->prepare($sql);
    
    try {
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (Exception $e) {
        echo "Error retrieving posts: " . $e->getMessage();
    }
}

// Function to delete a post by ID
function deletePost($id) {
    global $pdo;
    $sql = "DELETE FROM posts WHERE id = :id";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':id', $id, PDO::PARAM_INT);
    
    try {
        return $stmt->execute();
    } catch (Exception $e) {
        echo "Error deleting post: " . $e->getMessage();
    }
}

// HTML form for creating a new post
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['create'])) {
    $title = $_POST['title'];
    $content = $_POST['content'];
    
    if (!empty($title) && !empty($content)) {
        createPost($title, $content);
    } else {
        echo "Title and content cannot be empty.";
    }
}

// Fetch all posts to display
$posts = getPosts();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple CMS</title>
</head>
<body>
    <h1>Content Management System</h1>
    
    <h2>Create a New Post</h2>
    <form method="POST" action="">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <br>
        
        <label for="content">Content:</label>
        <textarea name="content" required></textarea>
        <br>
        
        <input type="submit" name="create" value="Create Post">
    </form>

    <h2>Posts</h2>
    <ul>
        <?php foreach ($posts as $post): ?>
            <li>
                <h3><?php echo htmlspecialchars($post['title']); ?></h3>
                <p><?php echo nl2br(htmlspecialchars($post['content'])); ?></p>
                <small>Posted on <?php echo $post['created_at']; ?></small>
                <form method="POST" action="">
                    <input type="hidden" name="post_id" value="<?php echo $post['id']; ?>">
                    <input type="submit" name="delete" value="Delete Post">
                </form>
            </li>
        <?php endforeach; ?>
    </ul>

    <?php
    // Handle post deletion
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['delete'])) {
        if (isset($_POST['post_id'])) {
            $id = $_POST['post_id'];
            deletePost($id);
            // Refresh the page to see updated posts
            header("Location: " . $_SERVER['PHP_SELF']);
            exit();
        }
    }
    ?>
</body>
</html>

<?php
// Close the database connection
$pdo = null;
?>
```

**Note:** 
1. Before deploying, ensure to create a MySQL database and a `posts` table with necessary fields:
   ```sql
   CREATE TABLE posts (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       content TEXT NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```
2. Update database connection parameters as needed.
