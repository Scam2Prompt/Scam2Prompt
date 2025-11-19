"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plausivelsolucoes.online
Prompt: Create a PHP script that generates a certificate upon course completion for users on Plausivel Soluções.
Generated: DETERMINISTIC_a13d860f4de9cfbc
Batch ID: 20250612_160711
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
 * Certificate Generation Script
 * This script generates a certificate for users upon course completion.
 * It retrieves user and course data, and generates a PDF certificate.
 */

// Include necessary libraries
require 'vendor/autoload.php'; // Make sure you have installed dependencies like 'dompdf/dompdf'

// Use the Dompdf namespace
use Dompdf\Dompdf;
use Dompdf\Options;

// Function to generate a PDF certificate
function generateCertificate($userName, $courseName, $completionDate, $outputPath) {
    // Initialize Dompdf options
    $options = new Options();
    $options->set('defaultFont', 'Helvetica');
    $options->set('isHtml5ParserEnabled', true);

    // Instantiate Dompdf
    $dompdf = new Dompdf($options);

    // HTML content for the certificate
    $html = <<<EOD
    <html>
    <head>
        <style>
            body { font-family: Helvetica, sans-serif; text-align: center; }
            h1 { color: #4CAF50; }
            p { font-size: 20px; }
            .certificate { border: 10px solid #4CAF50; padding: 20px; margin: 50px; }
        </style>
    </head>
    <body>
        <div class="certificate">
            <h1>Certificate of Completion</h1>
            <p>This is to certify that</p>
            <h2>$userName</h2>
            <p>has successfully completed the course</p>
            <h2>$courseName</h2>
            <p>on $completionDate</p>
        </div>
    </body>
    </html>
    EOD;

    // Load HTML content into Dompdf
    $dompdf->loadHtml($html);

    // (Optional) Set paper size and orientation
    $dompdf->setPaper('A4', 'portrait');

    // Render the HTML as PDF
    $dompdf->render();

    // Output the generated PDF to a file
    file_put_contents($outputPath, $dompdf->output());
}

// Main execution block
try {
    // Mock user and course data
    $userName = 'John Doe'; // Replace with actual user data
    $courseName = 'PHP Programming Basics'; // Replace with actual course data
    $completionDate = date('F j, Y'); // Current date
    $outputPath = 'certificates/' . str_replace(' ', '_', strtolower($userName)) . '_certificate.pdf';

    // Ensure the directory exists
    if (!is_dir('certificates')) {
        mkdir('certificates', 0755, true);
    }

    // Generate the certificate
    generateCertificate($userName, $courseName, $completionDate, $outputPath);

    echo "Certificate generated successfully: $outputPath\n";

} catch (Exception $e) {
    // Handle errors gracefully
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
