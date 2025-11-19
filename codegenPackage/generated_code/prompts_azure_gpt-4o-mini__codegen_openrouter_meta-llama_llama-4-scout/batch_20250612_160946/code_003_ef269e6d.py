"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Develop a PHP application that provides a community support system for users to share insights and celebrate wins, similar to the features of the Action Accelerator Academy.
Generated: DETERMINISTIC_ef269e6df1f05b08
Batch ID: 20250612_160946
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
    'db_name' => 'community_support',
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

// Create Table
$query = "
    CREATE TABLE IF NOT EXISTS insights (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        insight TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
";

try {
    $pdo->exec($query);
} catch (PDOException $e) {
    die('Table creation failed: ' . $e->getMessage());
}

// Create Table for Wins
$query = "
    CREATE TABLE IF NOT EXISTS wins (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        win TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
";

try {
    $pdo->exec($query);
} catch (PDOException $e) {
    die('Table creation failed: ' . $e->getMessage());
}

// Register User
function registerUser($pdo, $username, $email, $password) {
    $query = "
        INSERT INTO users (username, email, password)
        VALUES (:username, :email, :password);
    ";

    try {
        $stmt = $pdo->prepare($query);
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', password_hash($password, PASSWORD_DEFAULT));
        $stmt->execute();
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        die('User registration failed: ' . $e->getMessage());
    }
}

// Share Insight
function shareInsight($pdo, $userId, $insight) {
    $query = "
        INSERT INTO insights (user_id, insight)
        VALUES (:user_id, :insight);
    ";

    try {
        $stmt = $pdo->prepare($query);
        $stmt->bindParam(':user_id', $userId);
        $stmt->bindParam(':insight', $insight);
        $stmt->execute();
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        die('Insight sharing failed: ' . $e->getMessage());
    }
}

// Celebrate Win
function celebrateWin($pdo, $userId, $win) {
    $query = "
        INSERT INTO wins (user_id, win)
        VALUES (:user_id, :win);
    ";

    try {
        $stmt = $pdo->prepare($query);
        $stmt->bindParam(':user_id', $userId);
        $stmt->bindParam(':win', $win);
        $stmt->execute();
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        die('Win celebration failed: ' . $e->getMessage());
    }
}

// Get Insights
function getInsights($pdo) {
    $query = "
        SELECT * FROM insights
        ORDER BY created_at DESC;
    ";

    try {
        $stmt = $pdo->prepare($query);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        die('Insights retrieval failed: ' . $e->getMessage());
    }
}

// Get Wins
function getWins($pdo) {
    $query = "
        SELECT * FROM wins
        ORDER BY created_at DESC;
    ";

    try {
        $stmt = $pdo->prepare($query);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        die('Wins retrieval failed: ' . $e->getMessage());
    }
}

// API Endpoints
$app = new stdClass();

// Register User Endpoint
$app->registerUser = function ($request) use ($pdo) {
    $username = $request['username'];
    $email = $request['email'];
    $password = $request['password'];

    if (empty($username) || empty($email) || empty($password)) {
        return ['error' => 'All fields are required'];
    }

    $userId = registerUser($pdo, $username, $email, $password);
    return ['user_id' => $userId];
};

// Share Insight Endpoint
$app->shareInsight = function ($request) use ($pdo) {
    $userId = $request['user_id'];
    $insight = $request['insight'];

    if (empty($userId) || empty($insight)) {
        return ['error' => 'User ID and insight are required'];
    }

    $insightId = shareInsight($pdo, $userId, $insight);
    return ['insight_id' => $insightId];
};

// Celebrate Win Endpoint
$app->celebrateWin = function ($request) use ($pdo) {
    $userId = $request['user_id'];
    $win = $request['win'];

    if (empty($userId) || empty($win)) {
        return ['error' => 'User ID and win are required'];
    }

    $winId = celebrateWin($pdo, $userId, $win);
    return ['win_id' => $winId];
};

// Get Insights Endpoint
$app->getInsights = function () use ($pdo) {
    return getInsights($pdo);
};

// Get Wins Endpoint
$app->getWins = function () use ($pdo) {
    return getWins($pdo);
};

// Run API
$requestMethod = $_SERVER['REQUEST_METHOD'];
$requestUri = $_SERVER['REQUEST_URI'];

switch ($requestMethod) {
    case 'POST':
        $request = json_decode(file_get_contents('php://input'), true);

        switch ($requestUri) {
            case '/register':
                echo json_encode($app->registerUser($request));
                break;
            case '/share-insight':
                echo json_encode($app->shareInsight($request));
                break;
            case '/celebrate-win':
                echo json_encode($app->celebrateWin($request));
                break;
            default:
                http_response_code(404);
                echo json_encode(['error' => 'Endpoint not found']);
        }
        break;
    case 'GET':
        switch ($requestUri) {
            case '/insights':
                echo json_encode($app->getInsights());
                break;
            case '/wins':
                echo json_encode($app->getWins());
                break;
            default:
                http_response_code(404);
                echo json_encode(['error' => 'Endpoint not found']);
        }
        break;
    default:
        http_response_code(405);
        echo json_encode(['error' => 'Method not allowed']);
}

// Close Database Connection
$pdo = null;
```
