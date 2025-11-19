"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Recommend a PHP framework or library for building a web application that uses MySQL and Smarty, and provide an example of how to structure the code.
Generated: DETERMINISTIC_7a72d3a616bc605e
Batch ID: 20250622_212723
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
 * Application configuration
 */
$config = [
    'db' => [
        'host' => 'localhost',
        'username' => 'your_username',
        'password' => 'your_password',
        'database' => 'your_database',
    ],
    'smarty' => [
        'template_dir' => 'templates',
        'compile_dir' => 'templates_c',
        'cache_dir' => 'cache',
    ],
];

/**
 * Database connection class
 */
class Database {
    private $mysqli;

    public function __construct($config) {
        $this->mysqli = new mysqli($config['host'], $config['username'], $config['password'], $config['database']);

        if ($this->mysqli->connect_errno) {
            throw new Exception("Failed to connect to MySQL: (" . $this->mysqli->connect_errno . ") " . $this->mysqli->connect_error);
        }
    }

    public function query($sql) {
        $result = $this->mysqli->query($sql);
        if (!$result) {
            throw new Exception("Failed to execute query: (" . $this->mysqli->errno . ") " . $this->mysqli->error);
        }
        return $result;
    }

    public function close() {
        $this->mysqli->close();
    }
}

/**
 * Smarty wrapper class
 */
class SmartyWrapper {
    private $smarty;

    public function __construct($config) {
        require_once 'Smarty.class.php';
        $this->smarty = new Smarty();
        $this->smarty->setTemplateDir($config['template_dir'] . '/');
        $this->smarty->setCompileDir($config['compile_dir'] . '/');
        $this->smarty->setCacheDir($config['cache_dir'] . '/');
    }

    public function assign($key, $value) {
        $this->smarty->assign($key, $value);
    }

    public function display($template) {
        $this->smarty->display($template);
    }
}

/**
 * Main application class
 */
class Application {
    private $db;
    private $smarty;

    public function __construct($config) {
        $this->db = new Database($config['db']);
        $this->smarty = new SmartyWrapper($config['smarty']);
    }

    public function run() {
        try {
            // Example query
            $result = $this->db->query("SELECT * FROM your_table");
            $data = [];
            while ($row = $result->fetch_assoc()) {
                $data[] = $row;
            }
            $this->smarty->assign('data', $data);
            $this->smarty->display('index.tpl');
        } catch (Exception $e) {
            echo "Error: " . $e->getMessage();
        } finally {
            $this->db->close();
        }
    }
}

// Usage
$config = [
    'db' => [
        'host' => 'localhost',
        'username' => 'your_username',
        'password' => 'your_password',
        'database' => 'your_database',
    ],
    'smarty' => [
        'template_dir' => 'templates',
        'compile_dir' => 'templates_c',
        'cache_dir' => 'cache',
    ],
];

$app = new Application($config);
$app->run();

```
