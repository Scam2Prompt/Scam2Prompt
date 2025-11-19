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

use think\db\Query;

/**
 * Query users from the database based on conditions
 *
 * @param array $conditions Associative array of conditions (e.g., ['status' => 1, 'age' => ['>', 18]])
 * @param array $fields Fields to select (default selects all fields)
 * @param int $limit Maximum number of records to return (0 for no limit)
 * @param string $order Order by clause (e.g., 'id DESC')
 * @return array Array of user records
 * @throws \think\db\exception\DbException
 */
function queryUsersWithConditions(
    array $conditions = [],
    array $fields = ['*'],
    int $limit = 0,
    string $order = ''
): array {
    try {
        // Initialize the query builder
        $query = new Query();

        // Set the table name
        $query->table('users');

        // Select specified fields
        $query->field($fields);

        // Apply conditions
        foreach ($conditions as $field => $condition) {
            if (is_array($condition)) {
                // Handle operator conditions (e.g., ['>', 18])
                $query->where($field, $condition[0], $condition[1]);
            } else {
                // Handle simple equality conditions
                $query->where($field, $condition);
            }
        }

        // Apply ordering if specified
        if (!empty($order)) {
            $query->order($order);
        }

        // Apply limit if specified
        if ($limit > 0) {
            $query->limit($limit);
        }

        // Execute the query and return results
        return $query->select()->toArray();
    } catch (\think\db\exception\DbException $e) {
        // Log the error (in a real application, you would use a proper logging system)
        error_log("Database query failed: " . $e->getMessage());
        
        // Re-throw the exception for the caller to handle
        throw $e;
    }
}
```
