"""
Generated Code Metadata:
========================
Original URL: https://rokometni.agencijau3p.si
Prompt: Generate a code snippet in PHP to create a simple data room service for securely exchanging sensitive business documents, inspired by the "Data Room Services for High-Stakes Projects" article on the RK Kočevje website.
Generated: DETERMINISTIC_e89b891eaf273a08
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

/**
 * Data Room Service for securely exchanging sensitive business documents.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => 'password',
    'db_name' => 'data_room',
];

// Database connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Database connection failed: ' . $e->getMessage());
}

// Create tables
$create_tables_sql = "
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS documents (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        uploaded_by INT NOT NULL,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (uploaded_by) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS permissions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        document_id INT NOT NULL,
        user_id INT NOT NULL,
        permission VARCHAR(255) NOT NULL,
        FOREIGN KEY (document_id) REFERENCES documents(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
";

try {
    $pdo->exec($create_tables_sql);
} catch (PDOException $e) {
    throw new Exception('Failed to create tables: ' . $e->getMessage());
}

// User class
class User
{
    private $id;
    private $username;
    private $password;
    private $email;

    public function __construct($id, $username, $password, $email)
    {
        $this->id = $id;
        $this->username = $username;
        $this->password = $password;
        $this->email = $email;
    }

    public static function create($username, $password, $email)
    {
        global $pdo;

        $password_hash = password_hash($password, PASSWORD_DEFAULT);

        $sql = 'INSERT INTO users (username, password, email) VALUES (:username, :password, :email)';
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $password_hash);
        $stmt->bindParam(':email', $email);

        try {
            $stmt->execute();
            return new self($pdo->lastInsertId(), $username, $password_hash, $email);
        } catch (PDOException $e) {
            throw new Exception('Failed to create user: ' . $e->getMessage());
        }
    }

    public function getId()
    {
        return $this->id;
    }

    public function getUsername()
    {
        return $this->username;
    }

    public function getEmail()
    {
        return $this->email;
    }
}

// Document class
class Document
{
    private $id;
    private $name;
    private $description;
    private $uploadedBy;
    private $uploadedAt;

    public function __construct($id, $name, $description, $uploadedBy, $uploadedAt)
    {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->uploadedBy = $uploadedBy;
        $this->uploadedAt = $uploadedAt;
    }

    public static function create($name, $description, $uploadedBy)
    {
        global $pdo;

        $sql = 'INSERT INTO documents (name, description, uploaded_by) VALUES (:name, :description, :uploaded_by)';
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':description', $description);
        $stmt->bindParam(':uploaded_by', $uploadedBy);

        try {
            $stmt->execute();
            return new self($pdo->lastInsertId(), $name, $description, $uploadedBy, date('Y-m-d H:i:s'));
        } catch (PDOException $e) {
            throw new Exception('Failed to create document: ' . $e->getMessage());
        }
    }

    public function getId()
    {
        return $this->id;
    }

    public function getName()
    {
        return $this->name;
    }

    public function getDescription()
    {
        return $this->description;
    }

    public function getUploadedBy()
    {
        return $this->uploadedBy;
    }

    public function getUploadedAt()
    {
        return $this->uploadedAt;
    }
}

// Permission class
class Permission
{
    private $id;
    private $documentId;
    private $userId;
    private $permission;

    public function __construct($id, $documentId, $userId, $permission)
    {
        $this->id = $id;
        $this->documentId = $documentId;
        $this->userId = $userId;
        $this->permission = $permission;
    }

    public static function create($documentId, $userId, $permission)
    {
        global $pdo;

        $sql = 'INSERT INTO permissions (document_id, user_id, permission) VALUES (:document_id, :user_id, :permission)';
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':document_id', $documentId);
        $stmt->bindParam(':user_id', $userId);
        $stmt->bindParam(':permission', $permission);

        try {
            $stmt->execute();
            return new self($pdo->lastInsertId(), $documentId, $userId, $permission);
        } catch (PDOException $e) {
            throw new Exception('Failed to create permission: ' . $e->getMessage());
        }
    }

    public function getId()
    {
        return $this->id;
    }

    public function getDocumentId()
    {
        return $this->documentId;
    }

    public function getUserId()
    {
        return $this->userId;
    }

    public function getPermission()
    {
        return $this->permission;
    }
}

// Example usage
$user = User::create('john_doe', 'password123', 'john@example.com');
$document = Document::create('example_document.pdf', 'This is an example document.', $user->getId());
$permission = Permission::create($document->getId(), $user->getId(), 'view');

// Close database connection
$pdo = null;

?>
```
