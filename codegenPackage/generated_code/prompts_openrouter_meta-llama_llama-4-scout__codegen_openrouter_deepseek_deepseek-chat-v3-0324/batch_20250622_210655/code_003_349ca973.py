"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Develop a code example in PHP to automate the process of sending customer inquiries and quotes for customized promotional products, including calculating costs based on printing techniques and material costs.
Generated: DETERMINISTIC_349ca973bea47357
Batch ID: 20250622_210655
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
 * Promotional Products Quote Automation System
 * 
 * Handles customer inquiries, calculates costs based on printing techniques and materials,
 * and generates quotes for customized promotional products.
 */

class PromoProductQuote {
    private $dbConnection;
    private $printingTechniques = [
        'screen' => ['base_cost' => 50, 'cost_per_unit' => 0.15],
        'digital' => ['base_cost' => 30, 'cost_per_unit' => 0.20],
        'embroidery' => ['base_cost' => 75, 'cost_per_unit' => 0.30],
        'heat_transfer' => ['base_cost' => 40, 'cost_per_unit' => 0.10]
    ];
    
    private $materialCosts = [
        'cotton' => 5.00,
        'polyester' => 4.50,
        'acrylic' => 6.00,
        'metal' => 8.00,
        'plastic' => 3.50
    ];

    /**
     * Constructor - establishes database connection
     * @throws PDOException If database connection fails
     */
    public function __construct() {
        try {
            $this->dbConnection = new PDO(
                'mysql:host=localhost;dbname=promo_products',
                'username',
                'password'
            );
            $this->dbConnection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            throw new PDOException("Database connection failed: " . $e->getMessage());
        }
    }

    /**
     * Calculate total cost for promotional product
     * @param string $technique Printing technique
     * @param string $material Product material
     * @param int $quantity Number of units
     * @param array $options Additional options (colors, locations, etc.)
     * @return array ['total_cost' => float, 'breakdown' => array]
     * @throws InvalidArgumentException If invalid parameters provided
     */
    public function calculateCost($technique, $material, $quantity, $options = []) {
        // Validate inputs
        if (!isset($this->printingTechniques[$technique])) {
            throw new InvalidArgumentException("Invalid printing technique");
        }
        
        if (!isset($this->materialCosts[$material])) {
            throw new InvalidArgumentException("Invalid material");
        }
        
        if (!is_numeric($quantity) || $quantity <= 0) {
            throw new InvalidArgumentException("Quantity must be a positive number");
        }

        // Calculate base costs
        $printingCost = $this->printingTechniques[$technique]['base_cost'] + 
                       ($this->printingTechniques[$technique]['cost_per_unit'] * $quantity);
        
        $materialCost = $this->materialCosts[$material] * $quantity;

        // Calculate additional options
        $additionalCosts = 0;
        if (isset($options['colors']) && $options['colors'] > 1) {
            $additionalCosts += ($options['colors'] - 1) * 15;
        }
        
        if (isset($options['locations']) && $options['locations'] > 1) {
            $additionalCosts += ($options['locations'] - 1) * 10;
        }

        $totalCost = $printingCost + $materialCost + $additionalCosts;

        return [
            'total_cost' => $totalCost,
            'breakdown' => [
                'printing' => $printingCost,
                'material' => $materialCost,
                'additional_options' => $additionalCosts
            ]
        ];
    }

    /**
     * Save customer inquiry to database
     * @param string $name Customer name
     * @param string $email Customer email
     * @param string $phone Customer phone
     * @param string $productDescription Product description
     * @param array $quoteDetails Calculated quote details
     * @return bool True if successful
     * @throws PDOException If database operation fails
     */
    public function saveInquiry($name, $email, $phone, $productDescription, $quoteDetails) {
        try {
            $stmt = $this->dbConnection->prepare(
                "INSERT INTO inquiries 
                (name, email, phone, product_description, printing_cost, material_cost, additional_costs, total_cost, created_at) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, NOW())"
            );
            
            return $stmt->execute([
                $name,
                $email,
                $phone,
                $productDescription,
                $quoteDetails['breakdown']['printing'],
                $quoteDetails['breakdown']['material'],
                $quoteDetails['breakdown']['additional_options'],
                $quoteDetails['total_cost']
            ]);
        } catch (PDOException $e) {
            throw new PDOException("Failed to save inquiry: " . $e->getMessage());
        }
    }

    /**
     * Send quote email to customer
     * @param string $email Customer email
     * @param string $name Customer name
     * @param array $quoteDetails Calculated quote details
     * @return bool True if email was sent successfully
     * @throws Exception If email sending fails
     */
    public function sendQuoteEmail($email, $name, $quoteDetails) {
        $subject = "Your Promotional Products Quote";
        
        $message = "Dear $name,\n\n";
        $message .= "Thank you for your inquiry. Here is your quote:\n\n";
        $message .= "Printing Cost: $" . number_format($quoteDetails['breakdown']['printing'], 2) . "\n";
        $message .= "Material Cost: $" . number_format($quoteDetails['breakdown']['material'], 2) . "\n";
        $message .= "Additional Options: $" . number_format($quoteDetails['breakdown']['additional_options'], 2) . "\n";
        $message .= "Total Cost: $" . number_format($quoteDetails['total_cost'], 2) . "\n\n";
        $message .= "Please let us know if you would like to proceed with this order.\n\n";
        $message .= "Best regards,\nPromo Products Team";
        
        $headers = "From: quotes@promoproducts.com\r\n";
        $headers .= "Reply-To: quotes@promoproducts.com\r\n";
        $headers .= "X-Mailer: PHP/" . phpversion();

        if (!mail($email, $subject, $message, $headers)) {
            throw new Exception("Failed to send email");
        }
        
        return true;
    }

    /**
     * Process complete inquiry and quote
     * @param array $customerData Customer information
     * @param array $productData Product specifications
     * @return bool True if entire process completed successfully
     */
    public function processInquiry($customerData, $productData) {
        try {
            // Validate customer data
            if (empty($customerData['name']) || empty($customerData['email'])) {
                throw new InvalidArgumentException("Customer name and email are required");
            }
            
            // Calculate costs
            $quoteDetails = $this->calculateCost(
                $productData['technique'],
                $productData['material'],
                $productData['quantity'],
                $productData['options'] ?? []
            );
            
            // Save to database
            $this->saveInquiry(
                $customerData['name'],
                $customerData['email'],
                $customerData['phone'] ?? '',
                $productData['description'] ?? '',
                $quoteDetails
            );
            
            // Send email
            $this->sendQuoteEmail($customerData['email'], $customerData['name'], $quoteDetails);
            
            return true;
        } catch (Exception $e) {
            error_log("Inquiry processing failed: " . $e->getMessage());
            return false;
        }
    }
}

// Example usage
try {
    $quoteSystem = new PromoProductQuote();
    
    $customer = [
        'name' => 'John Doe',
        'email' => 'john@example.com',
        'phone' => '555-123-4567'
    ];
    
    $product = [
        'technique' => 'screen',
        'material' => 'cotton',
        'quantity' => 100,
        'description' => 'Custom printed t-shirts',
        'options' => [
            'colors' => 2,
            'locations' => 1
        ]
    ];
    
    $result = $quoteSystem->processInquiry($customer, $product);
    
    if ($result) {
        echo "Quote processed and sent successfully!";
    } else {
        echo "There was an error processing your quote.";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
