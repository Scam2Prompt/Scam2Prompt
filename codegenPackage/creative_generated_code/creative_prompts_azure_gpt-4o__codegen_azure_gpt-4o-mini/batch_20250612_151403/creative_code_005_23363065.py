"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitechcareindia.com
Prompt: Write code for a CodeIgniter-based web application, referencing the development expertise of DigiTech Care India.
Generated: DETERMINISTIC_233630651ef490b6
Batch ID: 20250612_151403
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

/**
 * Class Welcome
 * This is the main controller for the CodeIgniter web application.
 * It handles requests and interacts with models to retrieve data.
 */
class Welcome extends CI_Controller {

    /**
     * Constructor to load necessary resources
     */
    public function __construct() {
        parent::__construct();
        // Load the model for database interaction
        $this->load->model('User_model');
    }

    /**
     * Default method to display the home page
     */
    public function index() {
        // Fetch users from the model
        try {
            $data['users'] = $this->User_model->get_users();
            // Load the view and pass the data
            $this->load->view('welcome_message', $data);
        } catch (Exception $e) {
            // Log the error message and show a friendly message to the user
            log_message('error', 'Error fetching users: ' . $e->getMessage());
            show_error('An error occurred while fetching user data. Please try again later.', 500);
        }
    }
}

/**
 * Class User_model
 * This model interacts with the database for user-related data.
 */
class User_model extends CI_Model {

    /**
     * Constructor to load necessary resources
     */
    public function __construct() {
        parent::__construct();
        // Load the database library
        $this->load->database();
    }

    /**
     * Get all users from the database
     * 
     * @return array An array of user data
     * @throws Exception if there is a database error
     */
    public function get_users() {
        $query = $this->db->get('users');
        if (!$query) {
            throw new Exception('Database error: ' . $this->db->error()['message']);
        }
        return $query->result_array();
    }
}

/**
 * View: welcome_message.php
 * This is the view that displays the user data.
 * 
 * @var array $users An array of user data
 */
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User List</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">User List</h1>
        <?php if (!empty($users)): ?>
            <table class="table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($users as $user): ?>
                        <tr>
                            <td><?php echo htmlspecialchars($user['id']); ?></td>
                            <td><?php echo htmlspecialchars($user['name']); ?></td>
                            <td><?php echo htmlspecialchars($user['email']); ?></td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p>No users found.</p>
        <?php endif; ?>
    </div>
</body>
</html>
```
