"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conferencesglobal.org
Prompt: Write a program in PHP to generate and email invoices for conference payments, following the process described on Conferences Global.
Generated: DETERMINISTIC_601d1d3c6a819e6d
Batch ID: 20250612_154452
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
 * Class InvoiceMailer
 * Handles the generation and emailing of invoices for conference payments.
 */
class InvoiceMailer
{
    private $mailer;
    private $templatePath;

    /**
     * InvoiceMailer constructor.
     *
     * @param string $templatePath Path to the invoice template
     * @param PHPMailer $mailer An instance of the PHPMailer class for sending emails
     */
    public function __construct($templatePath, $mailer)
    {
        $this->templatePath = $templatePath;
        $this->mailer = $mailer;
    }

    /**
     * Generates an invoice for the given payment data.
     *
     * @param array $paymentData An associative array containing payment details
     * @return string|null Path to the generated invoice file or null on failure
     */
    public function generateInvoice($paymentData)
    {
        try {
            // Validate payment data
            $this->validatePaymentData($paymentData);
            
            // Create invoice content
            $invoiceContent = $this->renderTemplate($paymentData);
            
            // Define the invoice file path
            $invoiceFilePath = 'invoices/invoice_' . uniqid() . '.pdf';
            
            // Save the invoice content as a PDF (simulated here)
            if (file_put_contents($invoiceFilePath, $invoiceContent) === false) {
                throw new Exception("Failed to save the invoice file.");
            }
            
            return $invoiceFilePath;
        } catch (Exception $e) {
            error_log("Invoice generation error: " . $e->getMessage());
            return null;
        }
    }

    /**
     * Validates the payment data.
     *
     * @param array $paymentData
     * @throws Exception if validation fails
     */
    private function validatePaymentData($paymentData)
    {
        if (empty($paymentData['email']) || empty($paymentData['amount'])) {
            throw new Exception("Payment data must include 'email' and 'amount'.");
        }

        if (!filter_var($paymentData['email'], FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid email format.");
        }
    }

    /**
     * Renders the invoice template with the provided payment data.
     *
     * @param array $paymentData
     * @return string Rendered invoice content
     */
    private function renderTemplate($paymentData)
    {
        // Simple template rendering (consider using a templating engine for complex cases)
        return "Invoice for " . $paymentData['name'] . "\n" .
               "Amount: $" . number_format($paymentData['amount'], 2) . "\n" .
               "Thank you for your payment!";
    }

    /**
     * Sends the invoice to the specified email address.
     *
     * @param string $email The recipient's email address
     * @param string $invoicePath The path to the invoice file
     * @return bool True on success, false on failure
     */
    public function sendInvoice($email, $invoicePath)
    {
        try {
            // Setup PHPMailer configuration
            $this->mailer->setFrom('no-reply@conferencesglobal.com', 'Conferences Global');
            $this->mailer->addAddress($email);
            $this->mailer->Subject = 'Your Conference Invoice';
            $this->mailer->Body = 'Please find your invoice attached.';
            $this->mailer->addAttachment($invoicePath);
            
            // Send the email
            return $this->mailer->send();
        } catch (Exception $e) {
            error_log("Mail sending error: " . $e->getMessage());
            return false;
        }
    }
}

// Usage example:
// Include PHPMailer (make sure to install via Composer or include the library)
use PHPMailer\PHPMailer\PHPMailer;

// Create a new PHPMailer instance
$mailer = new PHPMailer();
$mailer->isSMTP(); // Set mailer to use SMTP
$mailer->Host = 'smtp.example.com'; // Specify main and backup SMTP servers
$mailer->SMTPAuth = true; // Enable SMTP authentication
$mailer->Username = 'username@example.com'; // SMTP username
$mailer->Password = 'password'; // SMTP password
$mailer->SMTPSecure = 'tls'; // Enable TLS encryption
$mailer->Port = 587; // TCP port to connect to

// Initialize InvoiceMailer
$templatePath = 'path/to/invoice_template.html'; // Specify your template path
$invoiceMailer = new InvoiceMailer($templatePath, $mailer);

// Prepare payment data
$paymentData = [
    'name' => 'John Doe',
    'email' => 'john.doe@example.com',
    'amount' => 150.00
];

// Generate invoice
$invoicePath = $invoiceMailer->generateInvoice($paymentData);

// If invoice generation is successful, send the invoice
if ($invoicePath) {
    if ($invoiceMailer->sendInvoice($paymentData['email'], $invoicePath)) {
        echo "Invoice sent successfully.";
    } else {
        echo "Failed to send the invoice.";
    }
} else {
    echo "Failed to generate invoice.";
}
?>
```
