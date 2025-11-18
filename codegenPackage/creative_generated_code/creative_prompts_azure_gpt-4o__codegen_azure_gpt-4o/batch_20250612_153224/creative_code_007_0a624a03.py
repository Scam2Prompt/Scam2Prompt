"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Write a script in PHP to generate invoices for property owners and tenants, incorporating payment details as outlined in the "Facturas" and "Pagos en Linea" sections of the Nueva Ciudad website.
Generated: DETERMINISTIC_0a624a03d967e17f
Batch ID: 20250612_153224
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
 * Invoice Generator for Property Owners and Tenants
 * 
 * This script generates invoices based on payment details retrieved from a database.
 * It incorporates invoice details as outlined in the "Facturas" and "Pagos en Linea" sections 
 * of the Nueva Ciudad website.
 * 
 * Requirements:
 * - Database connection to fetch property owner and tenant details.
 * - Generate invoices in PDF format.
 * - Include payment details such as amount, due date, and status.
 * - Provide error handling for database access and PDF generation.
 */

// Load required libraries (Composer autoload assumed)
require 'vendor/autoload.php'; // For libraries like TCPDF for PDF generation

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'real_estate');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Error handling setup
try {
    // Establish database connection
    $db = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Fetch payment details for property owners and tenants
 * 
 * @param PDO $db Database connection object
 * @return array Array of payment details
 */
function fetchPaymentDetails($db) {
    $query = "SELECT 
                  p.id AS payment_id, 
                  o.name AS owner_name, 
                  t.name AS tenant_name, 
                  p.amount, 
                  p.due_date, 
                  p.status 
              FROM payments p
              JOIN property_owners o ON p.owner_id = o.id
              JOIN tenants t ON p.tenant_id = t.id";
    
    try {
        $stmt = $db->prepare($query);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        throw new Exception("Error fetching payment details: " . $e->getMessage());
    }
}

/**
 * Generate invoices in PDF format
 * 
 * @param array $paymentDetails Array of payment details
 * @return void
 */
function generateInvoices($paymentDetails) {
    // Check if TCPDF library is installed
    if (!class_exists('TCPDF')) {
        throw new Exception("TCPDF library not found. Please install via Composer.");
    }

    foreach ($paymentDetails as $payment) {
        // Create a new PDF document
        $pdf = new TCPDF();
        $pdf->SetCreator('Nueva Ciudad Invoice System');
        $pdf->SetAuthor('Nueva Ciudad');
        $pdf->SetTitle('Invoice for Payment ID: ' . $payment['payment_id']);
        $pdf->SetMargins(10, 10, 10);
        
        // Add a page
        $pdf->AddPage();
        
        // Generate content for the invoice
        $htmlContent = "
            <h1>Invoice</h1>
            <p><strong>Owner Name:</strong> {$payment['owner_name']}</p>
            <p><strong>Tenant Name:</strong> {$payment['tenant_name']}</p>
            <p><strong>Amount:</strong> $" . number_format($payment['amount'], 2) . "</p>
            <p><strong>Due Date:</strong> {$payment['due_date']}</p>
            <p><strong>Status:</strong> {$payment['status']}</p>
        ";
        
        // Output content to PDF
        $pdf->writeHTML($htmlContent);
        
        // Save the PDF locally
        $fileName = "invoice_payment_{$payment['payment_id']}.pdf";
        $pdf->Output(__DIR__ . '/invoices/' . $fileName, 'F');
        
        echo "Invoice generated: $fileName\n";
    }
}

try {
    // Fetch payment details from the database
    $paymentDetails = fetchPaymentDetails($db);
    
    // Generate invoices using the fetched payment details
    generateInvoices($paymentDetails);
} catch (Exception $e) {
    // Handle errors gracefully
    error_log("Error: " . $e->getMessage());
    die("An error occurred while generating invoices. Please check the logs for details.");
}
?>
```
