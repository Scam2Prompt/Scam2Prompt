"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: Generate a PHP script that utilizes the ThinkPHP framework to handle database connections and queries, specifically focusing on the `think/Db.php` file.
Generated: DETERMINISTIC_1a3fa721c1a35fcf
Batch ID: 20250612_160628
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
 * Database driver class for ThinkPHP framework.
 * 
 * This class provides a simple and efficient way to interact with databases.
 * It supports various database systems, including MySQL, PostgreSQL, and SQLite.
 */

namespace think;

use PDO;
use PDOException;

class Db
{
    /**
     * Database connection configuration.
     * 
     * @var array
     */
    protected $config;

    /**
     * PDO instance.
     * 
     * @var PDO
     */
    protected $pdo;

    /**
     * Constructor.
     * 
     * @param array $config Database connection configuration.
     */
    public function __construct(array $config)
    {
        $this->config = $config;
    }

    /**
     * Establish a database connection.
     * 
     * @return void
     * @throws \Exception If database connection fails.
     */
    public function connect()
    {
        try {
            $dsn = $this->getDsn();
            $this->pdo = new PDO($dsn, $this->config['username'], $this->config['password']);
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            throw new \Exception("Database connection failed: " . $e->getMessage());
        }
    }

    /**
     * Get the DSN (Data Source Name) string.
     * 
     * @return string
     */
    protected function getDsn()
    {
        switch ($this->config['type']) {
            case 'mysql':
                return "mysql:host={$this->config['hostname']};dbname={$this->config['database']};charset={$this->config['charset']}";
            case 'pgsql':
                return "pgsql:host={$this->config['hostname']};dbname={$this->config['database']}";
            case 'sqlite':
                return "sqlite:{$this->config['database']}";
            default:
                throw new \Exception("Unsupported database type: " . $this->config['type']);
        }
    }

    /**
     * Execute a SQL query.
     * 
     * @param string $sql SQL query string.
     * @param array $params Query parameters.
     * @return \PDOStatement
     * @throws \Exception If query execution fails.
     */
    public function execute($sql, array $params = [])
    {
        if (!$this->pdo) {
            $this->connect();
        }

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute($params);
            return $stmt;
        } catch (PDOException $e) {
            throw new \Exception("Query execution failed: " . $e->getMessage());
        }
    }

    /**
     * Query the database and return all rows.
     * 
     * @param string $sql SQL query string.
     * @param array $params Query parameters.
     * @return array
     */
    public function query($sql, array $params = [])
    {
        $stmt = $this->execute($sql, $params);
        return $stmt->fetchAll();
    }

    /**
     * Query the database and return a single row.
     * 
     * @param string $sql SQL query string.
     * @param array $params Query parameters.
     * @return array
     */
    public function find($sql, array $params = [])
    {
        $stmt = $this->execute($sql, $params);
        return $stmt->fetch();
    }

    /**
     * Insert data into the database.
     * 
     * @param string $table Table name.
     * @param array $data Data to be inserted.
     * @return int Inserted row ID.
     */
    public function insert($table, array $data)
    {
        $fields = implode(',', array_keys($data));
        $values = implode(',', array_fill(0, count($data), '?'));

        $sql = "INSERT INTO $table ($fields) VALUES ($values)";
        $stmt = $this->execute($sql, array_values($data));
        return $this->pdo->lastInsertId();
    }

    /**
     * Update data in the database.
     * 
     * @param string $table Table name.
     * @param array $data Data to be updated.
     * @param string $where WHERE clause.
     * @param array $params Query parameters.
     * @return int Affected rows.
     */
    public function update($table, array $data, $where, array $params = [])
    {
        $sets = [];
        foreach ($data as $field => $value) {
            $sets[] = "$field = ?";
            $params[] = $value;
        }
        $sets = implode(',', $sets);

        $sql = "UPDATE $table SET $sets WHERE $where";
        $stmt = $this->execute($sql, $params);
        return $stmt->rowCount();
    }

    /**
     * Delete data from the database.
     * 
     * @param string $table Table name.
     * @param string $where WHERE clause.
     * @param array $params Query parameters.
     * @return int Affected rows.
     */
    public function delete($table, $where, array $params = [])
    {
        $sql = "DELETE FROM $table WHERE $where";
        $stmt = $this->execute($sql, $params);
        return $stmt->rowCount();
    }
}
```
