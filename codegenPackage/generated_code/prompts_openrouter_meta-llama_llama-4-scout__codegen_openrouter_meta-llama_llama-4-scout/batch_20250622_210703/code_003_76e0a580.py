"""
Generated Code Metadata:
========================
Original URL: https://delikbuana.com
Prompt: Write a code block in PHP to create a basic web application for displaying news articles from Delik Buana, using a database to store article metadata.
Generated: DETERMINISTIC_76e0a58006f45dfa
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Configuration
$dbHost = 'localhost';
$dbUsername = 'your_username';
$dbPassword = 'your_password';
$dbName = 'delik_buana';

// Create a PDO instance
try {
    $pdo = new PDO("mysql:host=$dbHost;dbname=$dbName", $dbUsername, $dbPassword);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}

// Create table if not exists
try {
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS articles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ");
} catch (PDOException $e) {
    die("ERROR: Could not create table. " . $e->getMessage());
}

// Function to get all articles
function getArticles($pdo) {
    try {
        $stmt = $pdo->prepare("SELECT * FROM articles ORDER BY created_at DESC");
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        die("ERROR: Could not retrieve articles. " . $e->getMessage());
    }
}

// Function to get article by id
function getArticle($pdo, $id) {
    try {
        $stmt = $pdo->prepare("SELECT * FROM articles WHERE id = :id");
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return $stmt->fetch(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        die("ERROR: Could not retrieve article. " . $e->getMessage());
    }
}

// Function to create a new article
function createArticle($pdo, $title, $content) {
    try {
        $stmt = $pdo->prepare("INSERT INTO articles (title, content) VALUES (:title, :content)");
        $stmt->bindParam(':title', $title);
        $stmt->bindParam(':content', $content);
        $stmt->execute();
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        die("ERROR: Could not create article. " . $e->getMessage());
    }
}

// Function to update an article
function updateArticle($pdo, $id, $title, $content) {
    try {
        $stmt = $pdo->prepare("UPDATE articles SET title = :title, content = :content WHERE id = :id");
        $stmt->bindParam(':id', $id);
        $stmt->bindParam(':title', $title);
        $stmt->bindParam(':content', $content);
        $stmt->execute();
    } catch (PDOException $e) {
        die("ERROR: Could not update article. " . $e->getMessage());
    }
}

// Function to delete an article
function deleteArticle($pdo, $id) {
    try {
        $stmt = $pdo->prepare("DELETE FROM articles WHERE id = :id");
        $stmt->bindParam(':id', $id);
        $stmt->execute();
    } catch (PDOException $e) {
        die("ERROR: Could not delete article. " . $e->getMessage());
    }
}

// Web application
require_once 'vendor/autoload.php';
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

$app = AppFactory::create();

// Get all articles
$app->get('/articles', function (Request $request, Response $response) use ($pdo) {
    $articles = getArticles($pdo);
    return $response->withJson($articles, 200);
});

// Get article by id
$app->get('/articles/{id}', function (Request $request, Response $response, $id) use ($pdo) {
    $article = getArticle($pdo, $id);
    if (!$article) {
        return $response->withStatus(404)->withJson(['error' => 'Article not found'], 404);
    }
    return $response->withJson($article, 200);
});

// Create a new article
$app->post('/articles', function (Request $request, Response $response) use ($pdo) {
    $data = $request->getParsedBody();
    $title = $data['title'] ?? null;
    $content = $data['content'] ?? null;
    if (!$title || !$content) {
        return $response->withStatus(400)->withJson(['error' => 'Title and content are required'], 400);
    }
    $id = createArticle($pdo, $title, $content);
    return $response->withJson(['id' => $id], 201);
});

// Update an article
$app->put('/articles/{id}', function (Request $request, Response $response, $id) use ($pdo) {
    $article = getArticle($pdo, $id);
    if (!$article) {
        return $response->withStatus(404)->withJson(['error' => 'Article not found'], 404);
    }
    $data = $request->getParsedBody();
    $title = $data['title'] ?? $article['title'];
    $content = $data['content'] ?? $article['content'];
    updateArticle($pdo, $id, $title, $content);
    return $response->withJson(['message' => 'Article updated'], 200);
});

// Delete an article
$app->delete('/articles/{id}', function (Request $request, Response $response, $id) use ($pdo) {
    $article = getArticle($pdo, $id);
    if (!$article) {
        return $response->withStatus(404)->withJson(['error' => 'Article not found'], 404);
    }
    deleteArticle($pdo, $id);
    return $response->withJson(['message' => 'Article deleted'], 200);
});

$app->run();
```
