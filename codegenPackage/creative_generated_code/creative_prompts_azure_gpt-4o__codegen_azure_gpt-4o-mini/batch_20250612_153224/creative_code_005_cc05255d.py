"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Write code in PHP to implement an order form for custom metallic stickers, allowing users to select from Nickel Metal Stickers, 3D Metal Nickel Stickers, and Packing Box Metal Stickers.
Generated: DETERMINISTIC_cc05255d19c02ebd
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define an array of available sticker types with their prices
$stickerTypes = [
    'nickel' => ['name' => 'Nickel Metal Stickers', 'price' => 1.50],
    '3d_nickel' => ['name' => '3D Metal Nickel Stickers', 'price' => 2.00],
    'packing_box' => ['name' => 'Packing Box Metal Stickers', 'price' => 1.75],
];

// Initialize variables for form handling
$error = '';
$successMessage = '';
$orderTotal = 0;

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    if (isset($_POST['sticker_type']) && array_key_exists($_POST['sticker_type'], $stickerTypes)) {
        // Capture selected sticker type
        $selectedSticker = $stickerTypes[$_POST['sticker_type']];
        $orderTotal = $selectedSticker['price'];
        $successMessage = 'Order placed successfully for ' . $selectedSticker['name'] . ' at $' . number_format($orderTotal, 2);
    } else {
        $error = 'Please select a valid sticker type.';
    }
}

// Function to display the order form
function displayOrderForm($stickerTypes, $error, $successMessage) {
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Metal Stickers Order Form</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <h1>Custom Metallic Stickers Order Form</h1>
            <?php if ($error): ?>
                <div class="alert alert-danger" role="alert">
                    <?= htmlspecialchars($error) ?>
                </div>
            <?php endif; ?>
            <?php if ($successMessage): ?>
                <div class="alert alert-success" role="alert">
                    <?= htmlspecialchars($successMessage) ?>
                </div>
            <?php endif; ?>
            <form method="POST" action="">
                <div class="form-group">
                    <label for="sticker_type">Select Sticker Type:</label>
                    <select class="form-control" id="sticker_type" name="sticker_type" required>
                        <option value="">-- Select a Sticker Type --</option>
                        <?php foreach ($stickerTypes as $key => $sticker): ?>
                            <option value="<?= htmlspecialchars($key) ?>"><?= htmlspecialchars($sticker['name']) ?> - $<?= number_format($sticker['price'], 2) ?></option>
                        <?php endforeach; ?>
                    </select>
                </div>
                <button type="submit" class="btn btn-primary">Submit Order</button>
            </form>
        </div>
    </body>
    </html>
    <?php
}

// Display the order form
displayOrderForm($stickerTypes, $error, $successMessage);
?>
```
