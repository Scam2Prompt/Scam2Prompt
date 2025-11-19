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

// Import the necessary namespace for ThinkORM
use think\orm\Db;
use think\orm\db\Query;

/**
 * Fetch records from the database using ThinkORM with specified conditions.
 *
 * @param string $tableName The name of the table to query.
 * @param array $conditions Associative array of conditions for the query (e.g., ['status' => 'active']).
 * @param array $fields Array of fields to select (e.g., ['id', 'name', 'status']). Defaults to all fields.
 * @param int|null $limit Optional limit for the number of records to fetch. Defaults to null (no limit).
 * @return array The result set as an array of records.
 * @throws Exception If the query fails or invalid parameters are provided.
 */
function fetchRecordsWithConditions(string $tableName, array $conditions = [], array $fields = ['*'], ?int $limit = null): array
{
    try {
        // Validate table name
        if (empty($tableName)) {
            throw new InvalidArgumentException('Table name cannot be empty.');
        }

        // Initialize the query builder
        $query = Db::table($tableName);

        // Apply conditions to the query
        foreach ($conditions as $field => $value) {
            $query->where($field, $value);
        }

        // Select specific fields
        $query->field($fields);

        // Apply limit if provided
        if ($limit !== null) {
            $query->limit($limit);
        }

        // Execute the query and fetch results
        $results = $query->select()->toArray();

        return $results;
    } catch (Exception $e) {
        // Log the error (assuming a logger is available)
        error_log('Database query error: ' . $e->getMessage());

        // Rethrow the exception for further handling
        throw $e;
    }
}

// Example usage:
// $records = fetchRecordsWithConditions('users', ['status' => 'active'], ['id', 'name'], 10);
// print_r($records);

?>
```
