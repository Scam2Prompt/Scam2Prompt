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
// Import ThinkPHP ORM namespace
use think\facade\Db;

// Define a model class for the "users" table
class User extends \think\Model
{
    // Specify the table name (optional if the table name matches the class name)
    protected $table = 'users';

    // Enable automatic timestamp fields (created_at, updated_at)
    protected $autoWriteTimestamp = true;

    // Define the fields for mass assignment protection (optional)
    protected $field = ['id', 'name', 'email', 'password', 'created_at', 'updated_at'];
}

// Example usage of ThinkPHP ORM to interact with the database
try {
    // Create a new user record
    $user = new User();
    $user->name = 'John Doe';
    $user->email = 'john.doe@example.com';
    $user->password = password_hash('securepassword', PASSWORD_BCRYPT); // Hash the password
    $user->save(); // Save the record to the database

    // Retrieve a user record by ID
    $retrievedUser = User::find(1); // Find user with ID 1
    if ($retrievedUser) {
        echo "User found: " . $retrievedUser->name . " (" . $retrievedUser->email . ")";
    } else {
        echo "User not found.";
    }

    // Update a user record
    $retrievedUser->name = 'Jane Doe';
    $retrievedUser->save(); // Save the updated record

    // Delete a user record
    $retrievedUser->delete(); // Delete the user record

    // Retrieve all users
    $allUsers = User::select();
    foreach ($allUsers as $user) {
        echo "User: " . $user->name . " (" . $user->email . ")" . PHP_EOL;
    }
} catch (\Exception $e) {
    // Handle any errors that occur during database operations
    echo "An error occurred: " . $e->getMessage();
}
```
