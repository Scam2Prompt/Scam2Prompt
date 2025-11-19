"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Create a function in PHP that uses the ThinkORM to perform a database query with conditions, leveraging the `think/orm/src/db/Query.php` functionalities.
Generated: DETERMINISTIC_487e981e97793872
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

namespace App\Database;

use think\facade\Db;
use think\db\exception\DbException;

/**
 * Class DatabaseQuery
 * This class provides methods to perform database queries using ThinkORM.
 */
class DatabaseQuery
{
    /**
     * Retrieves records from the specified table with given conditions.
     *
     * @param string $table The name of the table to query from.
     * @param array $conditions An associative array of conditions for the query.
     * @param array $columns An array of columns to select. Defaults to all columns.
     * @return array The result set as an array of associative arrays.
     * @throws DbException If a database error occurs.
     */
    public function fetchRecords(string $table, array $conditions, array $columns = ['*']): array
    {
        try {
            // Building the query using ThinkORM
            $query = Db::table($table);

            // Applying conditions to the query
            foreach ($conditions as $key => $value) {
                $query->where($key, $value);
            }

            // Executing the query and returning the result
            return $query->select($columns)->toArray();
        } catch (DbException $e) {
            // Log the error or handle it as needed
            // For example, you might want to log the error message
            error_log('Database query error: ' . $e->getMessage());

            // Rethrow the exception to notify the calling code
            throw $e;
        }
    }
}

// Example usage
// $dbQuery = new DatabaseQuery();
// $results = $dbQuery->fetchRecords('users', ['status' => 'active']);
// print_r($results);

```
