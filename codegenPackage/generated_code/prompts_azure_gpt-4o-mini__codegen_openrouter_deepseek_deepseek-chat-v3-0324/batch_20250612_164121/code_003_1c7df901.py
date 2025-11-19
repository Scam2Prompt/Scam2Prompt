"""
Generated Code Metadata:
========================
Original URL: https://beltsmania.com
Prompt: Develop a code snippet in PHP that processes a customer’s order for a custom belt, including validation for logo uploads and title inputs as described by Belts Mania.
Generated: DETERMINISTIC_1c7df901b48b1bba
Batch ID: 20250612_164121
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
 * Processes a custom belt order with logo upload and title validation.
 *
 * @param array $orderData The order data containing:
 *               - 'title' (string): The belt title
 *               - 'logo' (array): The uploaded logo file (following $_FILES structure)
 * @return array Result containing 'success' status and 'message' or 'errors'
 */
function processBeltOrder(array $orderData): array
{
    // Initialize result array
    $result = [
        'success' => false,
        'message' => '',
        'errors' => []
    ];

    try {
        // Validate title
        if (empty($orderData['title'])) {
            $result['errors']['title'] = 'Belt title is required.';
        } elseif (strlen($orderData['title']) > 50) {
            $result['errors']['title'] = 'Belt title must be less than 50 characters.';
        }

        // Validate logo
        if (empty($orderData['logo']['tmp_name'])) {
            $result['errors']['logo'] = 'Logo file is required.';
        } else {
            // Check for upload errors
            if ($orderData['logo']['error'] !== UPLOAD_ERR_OK) {
                $result['errors']['logo'] = match ($orderData['logo']['error']) {
                    UPLOAD_ERR_INI_SIZE, UPLOAD_ERR_FORM_SIZE => 'File size too large.',
                    UPLOAD_ERR_PARTIAL => 'File only partially uploaded.',
                    UPLOAD_ERR_NO_FILE => 'No file selected.',
                    UPLOAD_ERR_NO_TMP_DIR => 'Missing temporary folder.',
                    UPLOAD_ERR_CANT_WRITE => 'Failed to write file.',
                    UPLOAD_ERR_EXTENSION => 'File upload blocked by extension.',
                    default => 'Unknown upload error.',
                };
            } else {
                // Validate file type and size
                $allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
                $maxFileSize = 2 * 1024 * 1024; // 2MB

                $finfo = new finfo(FILEINFO_MIME_TYPE);
                $mime = $finfo->file($orderData['logo']['tmp_name']);

                if (!in_array($mime, $allowedTypes)) {
                    $result['errors']['logo'] = 'Invalid file type. Only JPEG, PNG, and GIF are allowed.';
                } elseif ($orderData['logo']['size'] > $maxFileSize) {
                    $result['errors']['logo'] = 'File size exceeds 2MB limit.';
                }
            }
        }

        // If validation passed, process the order
        if (empty($result['errors'])) {
            // In a real implementation, you would:
            // 1. Move the uploaded file to permanent storage
            // 2. Save order details to database
            // 3. Send confirmation emails, etc.

            $result['success'] = true;
            $result['message'] = 'Order processed successfully!';
        }

    } catch (Exception $e) {
        error_log("Order processing failed: " . $e->getMessage());
        $result['errors']['system'] = 'An error occurred while processing your order. Please try again.';
    }

    return $result;
}

// Example usage:
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $orderResult = processBeltOrder([
        'title' => $_POST['title'] ?? '',
        'logo' => $_FILES['logo'] ?? []
    ]);

    if ($orderResult['success']) {
        echo json_encode(['status' => 'success', 'message' => $orderResult['message']]);
    } else {
        echo json_encode(['status' => 'error', 'errors' => $orderResult['errors']]);
    }
    exit;
}
?>```
