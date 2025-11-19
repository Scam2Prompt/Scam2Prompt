"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: "Generate a code snippet that demonstrates how to use ThinkPHP's ORM (Object-Relational Mapping) features to interact with a MySQL database."
Generated: DETERMINISTIC_47020a1f7d946eea
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// ThinkPHP ORM Example for MySQL Database Interaction

namespace app\controller;

use think\facade\Db;
use app\model\User;

class UserController
{
    /**
     * Create a new user record
     * @param string $name
     * @param string $email
     * @return array
     */
    public function createUser($name, $email)
    {
        try {
            $user = new User();
            $user->name = $name;
            $user->email = $email;
            $user->save();
            
            return [
                'status' => 'success',
                'data' => $user->toArray()
            ];
        } catch (\Exception $e) {
            return [
                'status' => 'error',
                'message' => $e->getMessage()
            ];
        }
    }

    /**
     * Get user by ID
     * @param int $id
     * @return array
     */
    public function getUser($id)
    {
        try {
            $user = User::find($id);
            
            if (!$user) {
                throw new \Exception('User not found');
            }
            
            return [
                'status' => 'success',
                'data' => $user->toArray()
            ];
        } catch (\Exception $e) {
            return [
                'status' => 'error',
                'message' => $e->getMessage()
            ];
        }
    }

    /**
     * Update user information
     * @param int $id
     * @param array $data
     * @return array
     */
    public function updateUser($id, $data)
    {
        try {
            $user = User::find($id);
            
            if (!$user) {
                throw new \Exception('User not found');
            }
            
            $user->save($data);
            
            return [
                'status' => 'success',
                'data' => $user->toArray()
            ];
        } catch (\Exception $e) {
            return [
                'status' => 'error',
                'message' => $e->getMessage()
            ];
        }
    }

    /**
     * Delete a user
     * @param int $id
     * @return array
     */
    public function deleteUser($id)
    {
        try {
            $user = User::find($id);
            
            if (!$user) {
                throw new \Exception('User not found');
            }
            
            $user->delete();
            
            return [
                'status' => 'success',
                'message' => 'User deleted successfully'
            ];
        } catch (\Exception $e) {
            return [
                'status' => 'error',
                'message' => $e->getMessage()
            ];
        }
    }

    /**
     * Get all users with pagination
     * @param int $page
     * @param int $limit
     * @return array
     */
    public function getAllUsers($page = 1, $limit = 10)
    {
        try {
            $list = User::paginate([
                'page' => $page,
                'list_rows' => $limit
            ]);
            
            return [
                'status' => 'success',
                'data' => $list->toArray()
            ];
        } catch (\Exception $e) {
            return [
                'status' => 'error',
                'message' => $e->getMessage()
            ];
        }
    }

    /**
     * Query users with conditions
     * @param string $name
     * @return array
     */
    public function queryUsers($name)
    {
        try {
            $users = User::where('name', 'like', "%{$name}%")
                ->order('id', 'desc')
                ->select();
            
            return [
                'status' => 'success',
                'data' => $users->toArray()
            ];
        } catch (\Exception $e) {
            return [
                'status' => 'error',
                'message' => $e->getMessage()
            ];
        }
    }
}

// User Model (app/model/User.php)
namespace app\model;

use think\Model;

class User extends Model
{
    // Set the table name (optional if following convention)
    protected $table = 'user';
    
    // Define read-only fields
    protected $readonly = ['create_time'];
    
    // Define auto timestamp fields
    protected $autoWriteTimestamp = true;
    
    // Define field type
    protected $type = [
        'status' => 'integer'
    ];
    
    /**
     * Define relationship with other tables
     */
    public function profile()
    {
        return $this->hasOne('Profile');
    }
}
```
