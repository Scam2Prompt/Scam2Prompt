"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxosrew.com
Prompt: Create a function in PHP to display product details for automotive accessories, such as door speakers and bumper clips, referencing the product descriptions on paxosrew.com.
Generated: DETERMINISTIC_9a699c415b5b5f50
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Class Product
 * This class represents a product with details such as name, description, and price.
 */
class Product {
    private $name;
    private $description;
    private $price;

    /**
     * Constructor to initialize the product with name, description and price.
     *
     * @param string $name        The name of the product.
     * @param string $description The description of the product.
     * @param float  $price      The price of the product.
     */
    public function __construct($name, $description, $price) {
        $this->name = $name;
        $this->description = $description;
        $this->setPrice($price);
    }

    /**
     * Set the price of the product with validation.
     *
     * @param float $price The price to set.
     * @throws InvalidArgumentException If the price is negative.
     */
    public function setPrice($price) {
        if ($price < 0) {
            throw new InvalidArgumentException('Price cannot be negative.');
        }
        $this->price = $price;
    }

    /**
     * Get the product details as an associative array.
     *
     * @return array The product details.
     */
    public function getDetails() {
        return [
            'name' => $this->name,
            'description' => $this->description,
            'price' => number_format($this->price, 2) // Formatting price to 2 decimal places
        ];
    }
}

/**
 * Function to display product details.
 *
 * @param Product $product The product object.
 * @return void
 */
function displayProductDetails(Product $product) {
    $details = $product->getDetails();

    echo "<h2>Product Details</h2>";
    echo "<p><strong>Name:</strong> " . htmlspecialchars($details['name']) . "</p>";
    echo "<p><strong>Description:</strong> " . htmlspecialchars($details['description']) . "</p>";
    echo "<p><strong>Price:</strong> $" . htmlspecialchars($details['price']) . "</p>";
}

// Example usage
try {
    // Creating a product instance
    $product = new Product(
        'Door Speaker',
        'High-quality door speaker compatible with various automotive models.',
        149.99
    );

    // Displaying the product details
    displayProductDetails($product);
} catch (Exception $e) {
    // Error handling: Displaying a user-friendly error message
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}
?>
```
