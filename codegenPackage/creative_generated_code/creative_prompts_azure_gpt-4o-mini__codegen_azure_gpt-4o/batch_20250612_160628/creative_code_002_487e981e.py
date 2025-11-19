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

// Import the necessary namespace for ThinkORM
use think\orm\db\Query;

/**
 * Fetch records from the database using ThinkORM with conditions.
 *
 * @param array $conditions Array of conditions for filtering the query (e.g., ['status' => 'active']).
 * @param string $tableName Name of the database table to query.
 * @param array $fields Array of fields to select (optional). Defaults to all fields.
 * @return array Returns the fetched records as an associative array.
 * @throws Exception Throws an exception if the query fails.
 */
function fetchRecordsWithConditions(array $conditions, string $tableName, array $fields = ['*']): array
{
    try {
        // Create a new Query instance
        $query = new Query();

        // Build the query with the given table name and conditions
        $result = $query->table($tableName)
                        ->where($conditions) // Apply filtering conditions
                        ->field($fields)     // Specify fields to fetch
                        ->select();          // Execute the query and fetch results

        // Convert the result to an array and return
        return $result->toArray();
    } catch (\Exception $e) {
        // Handle exceptions and rethrow with a custom message
        throw new Exception('Error fetching records: ' . $e->getMessage());
    }
}

// Example Usage:
try {
    $tableName = 'users';
    $conditions = ['status' => 'active']; // Example condition: Fetch active users
    $fields = ['id', 'name', 'email'];   // Example fields to select

    $records = fetchRecordsWithConditions($conditions, $tableName, $fields);

    // Print the fetched records
    print_r($records);
} catch (\Exception $e) {
    // Handle errors gracefully
    echo 'Failed to fetch records: ' . $e->getMessage();
}
```
