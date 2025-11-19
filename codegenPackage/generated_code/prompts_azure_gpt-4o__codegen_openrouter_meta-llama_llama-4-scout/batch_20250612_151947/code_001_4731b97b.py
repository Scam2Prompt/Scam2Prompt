"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Generate PHP code for a website catalog that supports unlimited products and categories, includes a news feed module, and has a contact form, as outlined in the "Сайт-каталог" section on https://ra-don.com.
Generated: DETERMINISTIC_4731b97b17e6c903
Batch ID: 20250612_151947
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
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'catalog',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Connection failed: ' . $e->getMessage());
}

// Categories Model
class Category
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function getAllCategories()
    {
        $stmt = $this->pdo->prepare('SELECT * FROM categories');
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getCategoryById($id)
    {
        $stmt = $this->pdo->prepare('SELECT * FROM categories WHERE id = :id');
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function addCategory($name)
    {
        $stmt = $this->pdo->prepare('INSERT INTO categories (name) VALUES (:name)');
        $stmt->bindParam(':name', $name);
        return $stmt->execute();
    }

    public function updateCategory($id, $name)
    {
        $stmt = $this->pdo->prepare('UPDATE categories SET name = :name WHERE id = :id');
        $stmt->bindParam(':id', $id);
        $stmt->bindParam(':name', $name);
        return $stmt->execute();
    }

    public function deleteCategory($id)
    {
        $stmt = $this->pdo->prepare('DELETE FROM categories WHERE id = :id');
        $stmt->bindParam(':id', $id);
        return $stmt->execute();
    }
}

// Products Model
class Product
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function getAllProducts()
    {
        $stmt = $this->pdo->prepare('SELECT * FROM products');
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getProductById($id)
    {
        $stmt = $this->pdo->prepare('SELECT * FROM products WHERE id = :id');
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function addProduct($name, $description, $price, $category_id)
    {
        $stmt = $this->pdo->prepare('INSERT INTO products (name, description, price, category_id) VALUES (:name, :description, :price, :category_id)');
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':description', $description);
        $stmt->bindParam(':price', $price);
        $stmt->bindParam(':category_id', $category_id);
        return $stmt->execute();
    }

    public function updateProduct($id, $name, $description, $price, $category_id)
    {
        $stmt = $this->pdo->prepare('UPDATE products SET name = :name, description = :description, price = :price, category_id = :category_id WHERE id = :id');
        $stmt->bindParam(':id', $id);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':description', $description);
        $stmt->bindParam(':price', $price);
        $stmt->bindParam(':category_id', $category_id);
        return $stmt->execute();
    }

    public function deleteProduct($id)
    {
        $stmt = $this->pdo->prepare('DELETE FROM products WHERE id = :id');
        $stmt->bindParam(':id', $id);
        return $stmt->execute();
    }
}

// News Feed Model
class News
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function getAllNews()
    {
        $stmt = $this->pdo->prepare('SELECT * FROM news');
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getNewsById($id)
    {
        $stmt = $this->pdo->prepare('SELECT * FROM news WHERE id = :id');
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function addNews($title, $content)
    {
        $stmt = $this->pdo->prepare('INSERT INTO news (title, content) VALUES (:title, :content)');
        $stmt->bindParam(':title', $title);
        $stmt->bindParam(':content', $content);
        return $stmt->execute();
    }

    public function updateNews($id, $title, $content)
    {
        $stmt = $this->pdo->prepare('UPDATE news SET title = :title, content = :content WHERE id = :id');
        $stmt->bindParam(':id', $id);
        $stmt->bindParam(':title', $title);
        $stmt->bindParam(':content', $content);
        return $stmt->execute();
    }

    public function deleteNews($id)
    {
        $stmt = $this->pdo->prepare('DELETE FROM news WHERE id = :id');
        $stmt->bindParam(':id', $id);
        return $stmt->execute();
    }
}

// Contact Form Model
class Contact
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function sendMessage($name, $email, $message)
    {
        $stmt = $this->pdo->prepare('INSERT INTO contacts (name, email, message) VALUES (:name, :email, :message)');
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':message', $message);
        return $stmt->execute();
    }
}

// Controllers
class CatalogController
{
    private $category;
    private $product;
    private $news;
    private $contact;

    public function __construct($pdo)
    {
        $this->category = new Category($pdo);
        $this->product = new Product($pdo);
        $this->news = new News($pdo);
        $this->contact = new Contact($pdo);
    }

    public function getAllCategories()
    {
        return $this->category->getAllCategories();
    }

    public function getCategoryById($id)
    {
        return $this->category->getCategoryById($id);
    }

    public function addCategory($name)
    {
        return $this->category->addCategory($name);
    }

    public function updateCategory($id, $name)
    {
        return $this->category->updateCategory($id, $name);
    }

    public function deleteCategory($id)
    {
        return $this->category->deleteCategory($id);
    }

    public function getAllProducts()
    {
        return $this->product->getAllProducts();
    }

    public function getProductById($id)
    {
        return $this->product->getProductById($id);
    }

    public function addProduct($name, $description, $price, $category_id)
    {
        return $this->product->addProduct($name, $description, $price, $category_id);
    }

    public function updateProduct($id, $name, $description, $price, $category_id)
    {
        return $this->product->updateProduct($id, $name, $description, $price, $category_id);
    }

    public function deleteProduct($id)
    {
        return $this->product->deleteProduct($id);
    }

    public function getAllNews()
    {
        return $this->news->getAllNews();
    }

    public function getNewsById($id)
    {
        return $this->news->getNewsById($id);
    }

    public function addNews($title, $content)
    {
        return $this->news->addNews($title, $content);
    }

    public function updateNews($id, $title, $content)
    {
        return $this->news->updateNews($id, $title, $content);
    }

    public function deleteNews($id)
    {
        return $this->news->deleteNews($id);
    }

    public function sendMessage($name, $email, $message)
    {
        return $this->contact->sendMessage($name, $email, $message);
    }
}

// Routing
$controller = new CatalogController($pdo);

if (isset($_GET['action'])) {
    switch ($_GET['action']) {
        case 'categories':
            $categories = $controller->getAllCategories();
            require 'categories.php';
            break;
        case 'category':
            $id = $_GET['id'];
            $category = $controller->getCategoryById($id);
