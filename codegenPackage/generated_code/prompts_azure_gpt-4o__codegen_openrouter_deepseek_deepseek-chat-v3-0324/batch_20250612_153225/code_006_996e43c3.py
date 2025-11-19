"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Write code in PHP to implement a subscription system for fitness consultancy plans, including monthly, quarterly, and in-person options, with features for payment processing and plan management.
Generated: DETERMINISTIC_996e43c3af02953e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Fitness Consultancy Subscription System
 * 
 * This script handles subscription plans, payment processing, and plan management.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'fitness_consultancy');

// Stripe API configuration
define('STRIPE_SECRET_KEY', 'your_stripe_secret_key');
define('STRIPE_PUBLIC_KEY', 'your_stripe_public_key');

// Subscription plan types
abstract class SubscriptionPlan {
    const MONTHLY = 'monthly';
    const QUARTERLY = 'quarterly';
    const IN_PERSON = 'in_person';
}

// Subscription statuses
abstract class SubscriptionStatus {
    const ACTIVE = 'active';
    const CANCELLED = 'cancelled';
    const EXPIRED = 'expired';
}

class Database {
    private $connection;

    public function __construct() {
        $this->connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($this->connection->connect_error) {
            throw new Exception("Database connection failed: " . $this->connection->connect_error);
        }
    }

    public function query($sql, $params = []) {
        $stmt = $this->connection->prepare($sql);
        
        if (!$stmt) {
            throw new Exception("Prepare failed: " . $this->connection->error);
        }
        
        if (!empty($params)) {
            $types = str_repeat('s', count($params));
            $stmt->bind_param($types, ...$params);
        }
        
        $stmt->execute();
        return $stmt;
    }

    public function getLastInsertId() {
        return $this->connection->insert_id;
    }

    public function __destruct() {
        $this->connection->close();
    }
}

class Subscription {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    public function createSubscription($userId, $planType, $stripePaymentId) {
        $startDate = date('Y-m-d H:i:s');
        $endDate = $this->calculateEndDate($planType, $startDate);
        
        $sql = "INSERT INTO subscriptions (user_id, plan_type, status, start_date, end_date, stripe_payment_id) 
                VALUES (?, ?, ?, ?, ?, ?)";
        
        $params = [
            $userId,
            $planType,
            SubscriptionStatus::ACTIVE,
            $startDate,
            $endDate,
            $stripePaymentId
        ];
        
        $this->db->query($sql, $params);
        return $this->db->getLastInsertId();
    }

    public function cancelSubscription($subscriptionId) {
        $sql = "UPDATE subscriptions SET status = ? WHERE id = ?";
        $this->db->query($sql, [SubscriptionStatus::CANCELLED, $subscriptionId]);
    }

    public function getSubscription($subscriptionId) {
        $sql = "SELECT * FROM subscriptions WHERE id = ?";
        $result = $this->db->query($sql, [$subscriptionId]);
        return $result->get_result()->fetch_assoc();
    }

    public function getUserSubscriptions($userId) {
        $sql = "SELECT * FROM subscriptions WHERE user_id = ? ORDER BY start_date DESC";
        $result = $this->db->query($sql, [$userId]);
        return $result->get_result()->fetch_all(MYSQLI_ASSOC);
    }

    private function calculateEndDate($planType, $startDate) {
        $start = new DateTime($startDate);
        
        switch ($planType) {
            case SubscriptionPlan::MONTHLY:
                $start->add(new DateInterval('P1M'));
                break;
            case SubscriptionPlan::QUARTERLY:
                $start->add(new DateInterval('P3M'));
                break;
            case SubscriptionPlan::IN_PERSON:
                // In-person plans might have custom end dates
                $start->add(new DateInterval('P1D')); // Default to 1 day
                break;
            default:
                throw new Exception("Invalid plan type");
        }
        
        return $start->format('Y-m-d H:i:s');
    }
}

class PaymentProcessor {
    private $stripe;

    public function __construct() {
        \Stripe\Stripe::setApiKey(STRIPE_SECRET_KEY);
        $this->stripe = new \Stripe\StripeClient(STRIPE_SECRET_KEY);
    }

    public function createPaymentIntent($amount, $currency = 'usd', $metadata = []) {
        try {
            return $this->stripe->paymentIntents->create([
                'amount' => $amount,
                'currency' => $currency,
                'metadata' => $metadata
            ]);
        } catch (\Stripe\Exception\ApiErrorException $e) {
            throw new Exception("Payment processing failed: " . $e->getMessage());
        }
    }

    public function confirmPayment($paymentIntentId) {
        try {
            return $this->stripe->paymentIntents->retrieve($paymentIntentId);
        } catch (\Stripe\Exception\ApiErrorException $e) {
            throw new Exception("Payment confirmation failed: " . $e->getMessage());
        }
    }

    public function getPlanPrice($planType) {
        $prices = [
            SubscriptionPlan::MONTHLY => 2999, // $29.99
            SubscriptionPlan::QUARTERLY => 7999, // $79.99 (discounted)
            SubscriptionPlan::IN_PERSON => 15000 // $150.00
        ];
        
        if (!isset($prices[$planType])) {
            throw new Exception("Invalid plan type");
        }
        
        return $prices[$planType];
    }
}

class User {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    public function getUser($userId) {
        $sql = "SELECT * FROM users WHERE id = ?";
        $result = $this->db->query($sql, [$userId]);
        return $result->get_result()->fetch_assoc();
    }

    public function updateUserStripeId($userId, $stripeCustomerId) {
        $sql = "UPDATE users SET stripe_customer_id = ? WHERE id = ?";
        $this->db->query($sql, [$stripeCustomerId, $userId]);
    }
}

class SubscriptionManager {
    private $db;
    private $subscription;
    private $paymentProcessor;
    private $user;

    public function __construct() {
        $this->db = new Database();
        $this->subscription = new Subscription($this->db);
        $this->paymentProcessor = new PaymentProcessor();
        $this->user = new User($this->db);
    }

    public function subscribeUser($userId, $planType) {
        try {
            // Get plan price
            $amount = $this->paymentProcessor->getPlanPrice($planType);
            
            // Create payment intent
            $paymentIntent = $this->paymentProcessor->createPaymentIntent($amount, 'usd', [
                'user_id' => $userId,
                'plan_type' => $planType
            ]);
            
            // Process payment (in a real app, this would be handled client-side)
            // For demo purposes, we'll assume payment was successful
            
            // Create subscription
            $subscriptionId = $this->subscription->createSubscription(
                $userId, 
                $planType, 
                $paymentIntent->id
            );
            
            return [
                'success' => true,
                'subscription_id' => $subscriptionId,
                'client_secret' => $paymentIntent->client_secret
            ];
        } catch (Exception $e) {
            return [
                'success' => false,
                'error' => $e->getMessage()
            ];
        }
    }

    public function cancelUserSubscription($subscriptionId) {
        try {
            $this->subscription->cancelSubscription($subscriptionId);
            return ['success' => true];
        } catch (Exception $e) {
            return [
                'success' => false,
                'error' => $e->getMessage()
            ];
        }
    }

    public function getUserSubscriptions($userId) {
        try {
            $subscriptions = $this->subscription->getUserSubscriptions($userId);
            return [
                'success' => true,
                'subscriptions' => $subscriptions
            ];
        } catch (Exception $e) {
            return [
                'success' => false,
                'error' => $e->getMessage()
            ];
        }
    }
}

// Example usage
try {
    $subscriptionManager = new SubscriptionManager();
    
    // Simulate user subscription
    $result = $subscriptionManager->subscribeUser(1, SubscriptionPlan::MONTHLY);
    
    if ($result['success']) {
        echo "Subscription created successfully. ID: " . $result['subscription_id'];
    } else {
        echo "Error: " . $result['error'];
    }
    
    // Get user subscriptions
