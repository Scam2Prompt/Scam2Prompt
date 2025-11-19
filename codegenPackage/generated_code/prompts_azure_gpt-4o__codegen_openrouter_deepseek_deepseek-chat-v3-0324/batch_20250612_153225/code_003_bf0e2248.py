"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Write a script in PHP to calculate service costs based on selected options, such as foot reflexology ($28), ear candling ($28), and body massage ($35), and display the total price.
Generated: DETERMINISTIC_bf0e2248d20695cb
Batch ID: 20250612_153225
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
 * Service Cost Calculator
 * 
 * Calculates the total cost based on selected services and displays the result.
 */

// Define service prices
$servicePrices = [
    'foot_reflexology' => 28,
    'ear_candling' => 28,
    'body_massage' => 35
];

// Initialize variables
$totalCost = 0;
$selectedServices = [];

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and process selected services
    if (isset($_POST['services']) && is_array($_POST['services'])) {
        foreach ($_POST['services'] as $service) {
            if (array_key_exists($service, $servicePrices)) {
                $selectedServices[] = $service;
                $totalCost += $servicePrices[$service];
            }
        }
    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Cost Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .service-list { margin-bottom: 20px; }
        .result { margin-top: 20px; padding: 15px; background-color: #f5f5f5; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Service Cost Calculator</h1>
    <form method="post">
        <div class="service-list">
            <h3>Select Services:</h3>
            <label>
                <input type="checkbox" name="services[]" value="foot_reflexology">
                Foot Reflexology ($<?php echo $servicePrices['foot_reflexology']; ?>)
            </label><br>
            <label>
                <input type="checkbox" name="services[]" value="ear_candling">
                Ear Candling ($<?php echo $servicePrices['ear_candling']; ?>)
            </label><br>
            <label>
                <input type="checkbox" name="services[]" value="body_massage">
                Body Massage ($<?php echo $servicePrices['body_massage']; ?>)
            </label><br>
        </div>
        <button type="submit">Calculate Total</button>
    </form>

    <?php if ($_SERVER['REQUEST_METHOD'] === 'POST'): ?>
        <div class="result">
            <h3>Order Summary</h3>
            <?php if (!empty($selectedServices)): ?>
                <p>Selected Services:</p>
                <ul>
                    <?php foreach ($selectedServices as $service): ?>
                        <li><?php echo ucwords(str_replace('_', ' ', $service)); ?>: $<?php echo $servicePrices[$service]; ?></li>
                    <?php endforeach; ?>
                </ul>
                <p><strong>Total Cost: $<?php echo $totalCost; ?></strong></p>
            <?php else: ?>
                <p>No services selected.</p>
            <?php endif; ?>
        </div>
    <?php endif; ?>
</body>
</html>
```
