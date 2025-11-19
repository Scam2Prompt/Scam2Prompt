"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: Create a function in PHP that uses the ThinkORM to perform a database query with conditions, leveraging the `think/orm/src/db/Query.php` functionalities.
Generated: DETERMINISTIC_487e981e97793872
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

namespace App\Database;

use think\facade\Db;
use think\exception\DbException;

/**
 * Class DatabaseQuery
 * This class provides methods to perform database queries using ThinkORM.
 */
class DatabaseQuery
{
    /**
     * Fetch records from the database based on specified conditions.
     *
     * @param string $table The name of the table to query.
     * @param array $conditions An associative array of conditions for the query.
     * @param array $fields An array of fields to select. If empty, all fields will be selected.
     * @return array The result set as an array of records.
     * @throws DbException If there is an error during the query execution.
     */
    public function fetchRecords(string $table, array $conditions = [], array $fields = []): array
    {
        try {
            // Start the query on the specified table
            $query = Db::table($table);

            // Apply conditions if provided
            if (!empty($conditions)) {
                $query->where($conditions);
            }

            // Select specific fields if provided, otherwise select all
            if (!empty($fields)) {
                $query->field($fields);
            }

            // Execute the query and return the results
            return $query->select()->toArray();
        } catch (DbException $e) {
            // Log the error message for debugging purposes
            error_log('Database query error: ' . $e->getMessage());
            // Rethrow the exception for further handling
            throw new DbException('Failed to fetch records from the database.');
        }
    }
}

// Example usage
// $dbQuery = new DatabaseQuery();
// $results = $dbQuery->fetchRecords('users', ['status' => 'active'], ['id', 'name', 'email']);
```
