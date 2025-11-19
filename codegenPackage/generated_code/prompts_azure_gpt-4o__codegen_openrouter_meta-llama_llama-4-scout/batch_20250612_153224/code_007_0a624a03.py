"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Write a script in PHP to generate invoices for property owners and tenants, incorporating payment details as outlined in the "Facturas" and "Pagos en Linea" sections of the Nueva Ciudad website.
Generated: DETERMINISTIC_0a624a03d967e17f
Batch ID: 20250612_153224
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
 * Invoice Generator Script
 *
 * This script generates invoices for property owners and tenants based on payment details.
 */

// Configuration
$config = [
    'database' => [
        'host' => 'localhost',
        'username' => 'username',
        'password' => 'password',
        'database' => 'database',
    ],
    'factura' => [
        'issuer' => 'Nueva Ciudad',
        'address' => 'Nueva Ciudad Address',
    ],
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['database']['host'] . ';dbname=' . $config['database']['database'],
        $config['database']['username'],
        $config['database']['password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Database connection failed: ' . $e->getMessage());
}

// Function to generate invoice
function generateInvoice($pdo, $propertyOwnerId, $tenantId, $paymentDetails) {
    // Retrieve property owner and tenant information
    $propertyOwnerStmt = $pdo->prepare('SELECT * FROM property_owners WHERE id = :id');
    $propertyOwnerStmt->execute([':id' => $propertyOwnerId]);
    $propertyOwner = $propertyOwnerStmt->fetch();

    $tenantStmt = $pdo->prepare('SELECT * FROM tenants WHERE id = :id');
    $tenantStmt->execute([':id' => $tenantId]);
    $tenant = $tenantStmt->fetch();

    if (!$propertyOwner || !$tenant) {
        throw new Exception('Property owner or tenant not found');
    }

    // Generate invoice number
    $invoiceNumber = uniqid();

    // Create invoice
    $invoice = [
        'invoice_number' => $invoiceNumber,
        'property_owner_name' => $propertyOwner['name'],
        'property_owner_address' => $propertyOwner['address'],
        'tenant_name' => $tenant['name'],
        'tenant_address' => $tenant['address'],
        'payment_details' => $paymentDetails,
        'issue_date' => date('Y-m-d'),
    ];

    // Save invoice to database
    $invoiceStmt = $pdo->prepare('INSERT INTO invoices (invoice_number, property_owner_id, tenant_id, payment_details, issue_date) VALUES (:invoice_number, :property_owner_id, :tenant_id, :payment_details, :issue_date)');
    $invoiceStmt->execute([
        ':invoice_number' => $invoice['invoice_number'],
        ':property_owner_id' => $propertyOwnerId,
        ':tenant_id' => $tenantId,
        ':payment_details' => json_encode($paymentDetails),
        ':issue_date' => $invoice['issue_date'],
    ]);

    return $invoice;
}

// Function to send invoice
function sendInvoice($invoice) {
    // Send invoice via email or other channels
    // For demonstration purposes, just print the invoice
    print_r($invoice);
}

// Main function
function main() {
    global $pdo;

    // Example usage
    $propertyOwnerId = 1;
    $tenantId = 1;
    $paymentDetails = [
        'payment_method' => 'Online Payment',
        'payment_date' => '2023-03-01',
        'amount' => 100.00,
    ];

    try {
        $invoice = generateInvoice($pdo, $propertyOwnerId, $tenantId, $paymentDetails);
        sendInvoice($invoice);
    } catch (Exception $e) {
        echo 'Error: ' . $e->getMessage();
    }
}

main();

?>
```
