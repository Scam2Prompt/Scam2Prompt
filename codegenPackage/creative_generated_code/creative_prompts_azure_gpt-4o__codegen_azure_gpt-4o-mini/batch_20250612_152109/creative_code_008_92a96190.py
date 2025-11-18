"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Create a PHP script to display a list of agricultural products from categories like "Thuốc trừ bệnh" and "Phân bón lá," using examples such as "Sapacol 70WP" and "Nutri 123."
Generated: DETERMINISTIC_92a961907b5ebe4c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define the class for Agricultural Products
class AgriculturalProduct {
    public $name;
    public $category;

    // Constructor to initialize the product
    public function __construct($name, $category) {
        $this->name = $name;
        $this->category = $category;
    }
}

// Function to fetch agricultural products
function fetchAgriculturalProducts() {
    // Define an array to hold products
    $products = [];

    // Example products
    $products[] = new AgriculturalProduct("Sapacol 70WP", "Thuốc trừ bệnh");
    $products[] = new AgriculturalProduct("Nutri 123", "Phân bón lá");

    return $products;
}

// Function to display the products
function displayProducts($products) {
    // Check if products are provided
    if (empty($products)) {
        echo "<p>No agricultural products available.</p>";
        return;
    }

    // Start the product list
    echo "<h2>Agricultural Products</h2>";
    echo "<ul>";

    // Loop through each product and display its name and category
    foreach ($products as $product) {
        echo "<li><strong>Product:</strong> " . htmlspecialchars($product->name) . 
             " | <strong>Category:</strong> " . htmlspecialchars($product->category) . "</li>";
    }

    // End the product list
    echo "</ul>";
}

// Main execution
try {
    // Fetch the products
    $products = fetchAgriculturalProducts();

    // Display the products
    displayProducts($products);
} catch (Exception $e) {
    // Handle any exceptions that may occur
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}

?>
```
