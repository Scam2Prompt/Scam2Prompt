"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://royaumehotel.com
Prompt: Develop an API call in PHP to track orders for a shopping platform similar to RHINO88.
Generated: DETERMINISTIC_cfeff4552c91b261
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for development (disable in production by commenting out or setting display_errors to 0 in php.ini)
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Require Composer's autoload to use external libraries (if necessary)
// require 'vendor/autoload.php';

// Set content-type header for JSON response
header("Content-Type: application/json");

/**
 * Handles API requests for tracking orders.
 */
class OrderTrackingAPI
{
    private $db;

    /**
     * Constructor to initialize database connection.
     */
    public function __construct()
    {
        $this->db = $this->connectToDatabase();
    }

    /**
     * Connect to the database.
     * Replace with your database credentials.
     *
     * @return PDO Database connection object
     */
    private function connectToDatabase()
    {
        $host = '127.0.0.1';
        $dbName = 'shopping_platform';
        $username = 'db_user';
        $password = 'db_password';

        try {
            $dsn = "mysql:host=$host;dbname=$dbName;charset=utf8mb4";
            $options = [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES => false,
            ];
            return new PDO($dsn, $username, $password, $options);
        } catch (PDOException $e) {
            http_response_code(500);
            echo json_encode(["error" => "Database connection failed: " . $e->getMessage()]);
            exit;
        }
    }

    /**
     * Process the API request.
     */
    public function processRequest()
    {
        $method = $_SERVER['REQUEST_METHOD'];

        switch ($method) {
            case 'GET':
                $this->handleGetRequest();
                break;
            case 'POST':
                $this->handlePostRequest();
                break;
            default:
                http_response_code(405); // Method Not Allowed
                echo json_encode(["error" => "Method not allowed"]);
        }
    }

    /**
     * Handle GET requests to fetch order tracking information.
     */
    private function handleGetRequest()
    {
        // Validate and retrieve order ID from query parameters
        $orderId = filter_input(INPUT_GET, 'order_id', FILTER_SANITIZE_NUMBER_INT);

        if (!$orderId) {
            http_response_code(400); // Bad Request
            echo json_encode(["error" => "Invalid or missing order_id"]);
            return;
        }

        // Fetch order tracking information from the database
        try {
            $query = "SELECT * FROM orders WHERE order_id = :order_id";
            $stmt = $this->db->prepare($query);
            $stmt->bindParam(':order_id', $orderId, PDO::PARAM_INT);
            $stmt->execute();

            $order = $stmt->fetch();

            if ($order) {
                http_response_code(200); // OK
                echo json_encode($order);
            } else {
                http_response_code(404); // Not Found
                echo json_encode(["error" => "Order not found"]);
            }
        } catch (PDOException $e) {
            http_response_code(500); // Internal Server Error
            echo json_encode(["error" => "Failed to fetch order: " . $e->getMessage()]);
        }
    }

    /**
     * Handle POST requests to update order tracking information.
     */
    private function handlePostRequest()
    {
        // Get and validate POST data
        $input = json_decode(file_get_contents('php://input'), true);
        $orderId = isset($input['order_id']) ? intval($input['order_id']) : null;
        $status = isset($input['status']) ? trim($input['status']) : null;

        if (!$orderId || !$status) {
            http_response_code(400); // Bad Request
            echo json_encode(["error" => "Invalid or missing order_id or status"]);
            return;
        }

        // Update order tracking information in the database
        try {
            $query = "UPDATE orders SET status = :status WHERE order_id = :order_id";
            $stmt = $this->db->prepare($query);
            $stmt->bindParam(':status', $status, PDO::PARAM_STR);
            $stmt->bindParam(':order_id', $orderId, PDO::PARAM_INT);

            $stmt->execute();

            if ($stmt->rowCount() > 0) {
                http_response_code(200); // OK
                echo json_encode(["message" => "Order updated successfully"]);
            } else {
                http_response_code(404); // Not Found
                echo json_encode(["error" => "Order not found"]);
            }
        } catch (PDOException $e) {
            http_response_code(500); // Internal Server Error
            echo json_encode(["error" => "Failed to update order: " . $e->getMessage()]);
        }
    }
}

// Instantiate and process the API
$api = new OrderTrackingAPI();
$api->processRequest();
?>
```
