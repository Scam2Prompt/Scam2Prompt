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
namespace app\controller;

use think\facade\Db;
use think\exception\DbException;

class DatabaseController
{
    /**
     * Establish a database connection and execute a simple query
     * @return \think\response\Json
     */
    public function connectAndQuery()
    {
        try {
            // Establish database connection (automatically handled by ThinkPHP)
            $connection = Db::connect();
            
            // Execute a simple query to test the connection
            $result = Db::query('SELECT VERSION() as version');
            
            return json([
                'status' => 'success',
                'data' => $result[0]['version'],
                'message' => 'Database connection successful'
            ]);
            
        } catch (DbException $e) {
            return json([
                'status' => 'error',
                'message' => 'Database connection failed: ' . $e->getMessage()
            ], 500);
        }
    }

    /**
     * Insert data into a table
     * @param array $data
     * @return \think\response\Json
     */
    public function insertData($data = [])
    {
        try {
            // Validate input data
            if (empty($data)) {
                throw new \InvalidArgumentException('No data provided for insertion');
            }

            // Insert data into 'users' table
            $result = Db::name('users')->insert($data);
            
            if (!$result) {
                throw new DbException('Insert operation failed');
            }
            
            return json([
                'status' => 'success',
                'message' => 'Data inserted successfully',
                'insert_id' => Db::name('users')->getLastInsID()
            ]);
            
        } catch (DbException $e) {
            return json([
                'status' => 'error',
                'message' => 'Database operation failed: ' . $e->getMessage()
            ], 500);
        } catch (\InvalidArgumentException $e) {
            return json([
                'status' => 'error',
                'message' => $e->getMessage()
            ], 400);
        }
    }

    /**
     * Query data from a table with conditions
     * @param array $conditions
     * @return \think\response\Json
     */
    public function queryData($conditions = [])
    {
        try {
            // Build query with optional conditions
            $query = Db::name('users');
            
            if (!empty($conditions)) {
                $query->where($conditions);
            }
            
            $result = $query->select();
            
            return json([
                'status' => 'success',
                'data' => $result,
                'message' => 'Query executed successfully'
            ]);
            
        } catch (DbException $e) {
            return json([
                'status' => 'error',
                'message' => 'Database query failed: ' . $e->getMessage()
            ], 500);
        }
    }

    /**
     * Update data in a table
     * @param array $conditions
     * @param array $updateData
     * @return \think\response\Json
     */
    public function updateData($conditions = [], $updateData = [])
    {
        try {
            // Validate input
            if (empty($conditions) || empty($updateData)) {
                throw new \InvalidArgumentException('Conditions and update data are required');
            }

            // Execute update
            $result = Db::name('users')
                ->where($conditions)
                ->update($updateData);
                
            if ($result === false) {
                throw new DbException('Update operation failed');
            }
            
            return json([
                'status' => 'success',
                'affected_rows' => $result,
                'message' => 'Data updated successfully'
            ]);
            
        } catch (DbException $e) {
            return json([
                'status' => 'error',
                'message' => 'Database operation failed: ' . $e->getMessage()
            ], 500);
        } catch (\InvalidArgumentException $e) {
            return json([
                'status' => 'error',
                'message' => $e->getMessage()
            ], 400);
        }
    }

    /**
     * Delete data from a table
     * @param array $conditions
     * @return \think\response\Json
     */
    public function deleteData($conditions = [])
    {
        try {
            // Validate input
            if (empty($conditions)) {
                throw new \InvalidArgumentException('Conditions are required for deletion');
            }

            // Execute delete
            $result = Db::name('users')
                ->where($conditions)
                ->delete();
                
            if ($result === false) {
                throw new DbException('Delete operation failed');
            }
            
            return json([
                'status' => 'success',
                'affected_rows' => $result,
                'message' => 'Data deleted successfully'
            ]);
            
        } catch (DbException $e) {
            return json([
                'status' => 'error',
                'message' => 'Database operation failed: ' . $e->getMessage()
            ], 500);
        } catch (\InvalidArgumentException $e) {
            return json([
                'status' => 'error',
                'message' => $e->getMessage()
            ], 400);
        }
    }

    /**
     * Execute a transaction
     * @return \think\response\Json
     */
    public function executeTransaction()
    {
        try {
            // Start transaction
            Db::startTrans();
            
            try {
                // Example transaction operations
                $insertId = Db::name('users')->insertGetId([
                    'name' => 'Transaction User',
                    'email' => 'transaction@example.com'
                ]);
                
                Db::name('profiles')->insert([
                    'user_id' => $insertId,
                    'bio' => 'Created in transaction'
                ]);
                
                // Commit transaction if all operations succeed
                Db::commit();
                
                return json([
                    'status' => 'success',
                    'message' => 'Transaction completed successfully',
                    'insert_id' => $insertId
                ]);
                
            } catch (\Exception $e) {
                // Rollback transaction if any operation fails
                Db::rollback();
                throw $e;
            }
            
        } catch (DbException $e) {
            return json([
                'status' => 'error',
                'message' => 'Transaction failed: ' . $e->getMessage()
            ], 500);
        }
    }
}
```
