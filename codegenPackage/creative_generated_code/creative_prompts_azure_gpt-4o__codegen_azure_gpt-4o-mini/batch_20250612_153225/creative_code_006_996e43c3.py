"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Write code in PHP to implement a subscription system for fitness consultancy plans, including monthly, quarterly, and in-person options, with features for payment processing and plan management.
Generated: DETERMINISTIC_996e43c3af02953e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// SubscriptionSystem.php

class SubscriptionSystem {
    private $db; // Database connection
    private $plans; // Available plans

    public function __construct($dbConnection) {
        $this->db = $dbConnection;
        $this->plans = [
            'monthly' => ['price' => 50, 'duration' => 1],
            'quarterly' => ['price' => 135, 'duration' => 3],
            'in_person' => ['price' => 200, 'duration' => 1, 'type' => 'in_person']
        ];
    }

    // Fetch available plans
    public function getPlans() {
        return $this->plans;
    }

    // Process payment for a subscription
    public function processPayment($planType, $userId) {
        if (!isset($this->plans[$planType])) {
            throw new Exception("Invalid subscription plan selected.");
        }

        // Simulated payment processing (replace with actual payment gateway logic)
        $paymentSuccess = $this->simulatePayment($this->plans[$planType]['price']);
        
        if (!$paymentSuccess) {
            throw new Exception("Payment processing failed.");
        }

        // Store subscription to the database
        $this->storeSubscription($planType, $userId);
    }

    // Simulate payment processing (dummy function for demonstration)
    private function simulatePayment($amount) {
        // In production, integrate with a payment gateway like Stripe or PayPal
        return true; // Assume payment is successful
    }

    // Store subscription information in the database
    private function storeSubscription($planType, $userId) {
        $duration = $this->plans[$planType]['duration'];
        $expiryDate = date('Y-m-d', strtotime("+$duration months"));

        $stmt = $this->db->prepare("INSERT INTO subscriptions (user_id, plan_type, expiry_date) VALUES (?, ?, ?)");
        if (!$stmt) {
            throw new Exception("Database query failed: " . $this->db->error);
        }

        if (!$stmt->bind_param("iss", $userId, $planType, $expiryDate)) {
            throw new Exception("Parameter binding failed: " . $stmt->error);
        }

        if (!$stmt->execute()) {
            throw new Exception("Subscription storage failed: " . $stmt->error);
        }

        $stmt->close();
    }

    // Check subscription status
    public function checkSubscriptionStatus($userId) {
        $stmt = $this->db->prepare("SELECT plan_type, expiry_date FROM subscriptions WHERE user_id = ?");
        if (!$stmt) {
            throw new Exception("Database query failed: " . $this->db->error);
        }

        if (!$stmt->bind_param("i", $userId)) {
            throw new Exception("Parameter binding failed: " . $stmt->error);
        }

        if (!$stmt->execute()) {
            throw new Exception("Subscription check failed: " . $stmt->error);
        }

        $result = $stmt->get_result();
        return $result->fetch_all(MYSQLI_ASSOC);
    }
}

// Usage example
try {
    // Create a MySQLi connection (replace with your own connection details)
    $mysqli = new mysqli("localhost", "username", "password", "fitness");

    // Check connection
    if ($mysqli->connect_error) {
        throw new Exception("Connection failed: " . $mysqli->connect_error);
    }

    $subscriptionSystem = new SubscriptionSystem($mysqli);

    // Fetch available plans
    $availablePlans = $subscriptionSystem->getPlans();
    print_r($availablePlans);

    // Process a subscription payment
    $subscriptionSystem->processPayment('monthly', 1);

    // Check subscription status
    $status = $subscriptionSystem->checkSubscriptionStatus(1);
    print_r($status);

} catch (Exception $e) {
    // Handle any errors that occurred
    echo 'Error: ' . $e->getMessage();
} finally {
    // Close the database connection
    if (isset($mysqli) && $mysqli) {
        $mysqli->close();
    }
}
?>
```
