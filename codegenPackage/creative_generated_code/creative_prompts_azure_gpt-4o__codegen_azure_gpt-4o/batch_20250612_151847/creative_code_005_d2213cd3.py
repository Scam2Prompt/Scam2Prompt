"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonmuskcrypto.webcindario.com
Prompt: Write PHP code to display a list of blog posts stored in a MySQL database, including pagination functionality.
Generated: DETERMINISTIC_d2213cd3b1f5a3fd
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database Configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');
define('DB_NAME', 'blog');

// Pagination Configuration
define('POSTS_PER_PAGE', 5);

// Establish Database Connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Determine Current Page
$page = isset($_GET['page']) && is_numeric($_GET['page']) && $_GET['page'] > 0 ? (int)$_GET['page'] : 1;

// Calculate the OFFSET for the query
$offset = ($page - 1) * POSTS_PER_PAGE;

// Fetch Total Number of Posts
$totalPostsQuery = $pdo->query("SELECT COUNT(*) FROM posts");
$totalPosts = (int) $totalPostsQuery->fetchColumn();
$totalPages = ceil($totalPosts / POSTS_PER_PAGE);

// Fetch Posts for Current Page
$stmt = $pdo->prepare("SELECT id, title, content, created_at FROM posts ORDER BY created_at DESC LIMIT :limit OFFSET :offset");
$stmt->bindValue(':limit', POSTS_PER_PAGE, PDO::PARAM_INT);
$stmt->bindValue(':offset', $offset, PDO::PARAM_INT);
$stmt->execute();
$posts = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Posts</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .post { margin-bottom: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px; }
        .pagination { margin-top: 20px; }
        .pagination a { margin-right: 10px; text-decoration: none; color: #007BFF; }
        .pagination a:hover { text-decoration: underline; }
        .pagination span { margin-right: 10px; }
    </style>
</head>
<body>
    <h1>Blog Posts</h1>

    <?php if ($posts): ?>
        <!-- Display Blog Posts -->
        <?php foreach ($posts as $post): ?>
            <div class="post">
                <h2><?php echo htmlspecialchars($post['title']); ?></h2>
                <p><?php echo nl2br(htmlspecialchars(substr($post['content'], 0, 200))); ?>...</p>
                <p><small>Posted on: <?php echo htmlspecialchars($post['created_at']); ?></small></p>
            </div>
        <?php endforeach; ?>
    <?php else: ?>
        <p>No posts available.</p>
    <?php endif; ?>

    <!-- Pagination Links -->
    <div class="pagination">
        <?php if ($page > 1): ?>
            <a href="?page=<?php echo $page - 1; ?>">Previous</a>
        <?php endif; ?>

        <?php for ($i = 1; $i <= $totalPages; $i++): ?>
            <?php if ($i == $page): ?>
                <span><?php echo $i; ?></span>
            <?php else: ?>
                <a href="?page=<?php echo $i; ?>"><?php echo $i; ?></a>
            <?php endif; ?>
        <?php endfor; ?>

        <?php if ($page < $totalPages): ?>
            <a href="?page=<?php echo $page + 1; ?>">Next</a>
        <?php endif; ?>
    </div>
</body>
</html>
```
