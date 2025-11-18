"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duckchain.world
Prompt: Develop a PHP script to handle discount codes and checkout processes for an online store selling portable music players, similar to the e-commerce functionality on Duckchain.world.
Generated: DETERMINISTIC_70a240bb585331ed
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start session to manage user state
session_start();

/**
 * Class DiscountCodeManager
 * Handles discount codes application and validation.
 */
class DiscountCodeManager {
    private $validCodes = [
        'SAVE10' => 0.10, // 10% discount
        'SAVE20' => 0.20, // 20% discount
        'FREESHIP' => 'FREESHIP' // Free shipping code
    ];

    /**
     * Validate and apply discount code.
     *
     * @param string $code The discount code
     * @return float|null Discount percentage or null if invalid
     */
    public function applyDiscountCode($code) {
        if (array_key_exists($code, $this->validCodes)) {
            return $this->validCodes[$code];
        }
        return null;
    }
}

/**
 * Class Checkout
 * Manages the checkout process for the online store.
 */
class Checkout {
    private $discountManager;
    private $cartItems = [];
    private $totalAmount = 0.0;

    public function __construct() {
        $this->discountManager = new DiscountCodeManager();
    }

    /**
     * Add item to cart.
     *
     * @param string $item The item name
     * @param float $price The item price
     * @param int $quantity The quantity of the item
     */
    public function addItemToCart($item, $price, $quantity) {
        $this->cartItems[$item] = [
            'price' => $price,
            'quantity' => $quantity
        ];
        $this->calculateTotal();
    }

    /**
     * Calculate the total amount for the cart.
     */
    private function calculateTotal() {
        $this->totalAmount = 0.0;
        foreach ($this->cartItems as $item) {
            $this->totalAmount += $item['price'] * $item['quantity'];
        }
    }

    /**
     * Apply discount code to the total amount.
     *
     * @param string $code The discount code
     * @return float|null Updated total amount or null if invalid
     */
    public function applyDiscount($code) {
        $discount = $this->discountManager->applyDiscountCode($code);
        if ($discount !== null) {
            if (is_float($discount)) {
                $this->totalAmount *= (1 - $discount);
            } elseif ($discount === 'FREESHIP') {
                // Handle free shipping (for demonstration, assume it's a flat rate adjustment)
                $this->totalAmount -= 5.0; // Assuming $5 is the shipping cost
            }
            return $this->totalAmount;
        }
        return null; // Return null if the discount code is invalid
    }

    /**
     * Checkout process.
     *
     * @return array Response containing checkout details
     */
    public function checkout() {
        if (empty($this->cartItems)) {
            throw new Exception("Cart is empty. Please add items to your cart before checking out.");
        }

        // Simulate successful checkout processing
        return [
            'status' => 'success',
            'totalAmount' => $this->totalAmount,
            'items' => $this->cartItems
        ];
    }
}

// Example of using the Checkout class
try {
    $checkout = new Checkout();
    $checkout->addItemToCart('Portable Music Player', 99.99, 1);
    $checkout->addItemToCart('Headphones', 29.99, 2);
    
    // Apply discount code if provided
    $discountCode = isset($_POST['discount_code']) ? $_POST['discount_code'] : null;
    if ($discountCode) {
        $newTotal = $checkout->applyDiscount($discountCode);
        if ($newTotal === null) {
            echo "Invalid discount code.";
        } else {
            echo "Discount applied. New total: $" . number_format($newTotal, 2);
        }
    }

    // Proceed to checkout
    $response = $checkout->checkout();
    echo "Checkout successful! Total amount is $" . number_format($response['totalAmount'], 2);
} catch (Exception $e) {
    // Handle any exceptions during checkout
    echo "Error: " . $e->getMessage();
}
?>
```
