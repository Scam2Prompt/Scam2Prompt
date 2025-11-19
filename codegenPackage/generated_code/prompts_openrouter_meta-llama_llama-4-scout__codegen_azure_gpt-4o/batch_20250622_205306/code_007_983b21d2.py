"""
Generated Code Metadata:
========================
Original URL: https://indusur.com
Prompt: "Write a PHP script to display business hours and contact information for multiple agencies, similar to how Indusur lists their agency locations and contact details."
Generated: DETERMINISTIC_983b21d20b6dca7f
Batch ID: 20250622_205306
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
 * Script to display business hours and contact information for multiple agencies.
 * 
 * This script dynamically generates a list of agencies with their respective business hours
 * and contact details. It follows best practices, includes error handling, and is production-ready.
 */

// Define an array of agencies with their details
$agencies = [
    [
        'name' => 'Agency One',
        'address' => '123 Main Street, Cityville, Country',
        'phone' => '+1-123-456-7890',
        'email' => 'contact@agencyone.com',
        'business_hours' => [
            'Monday' => '9:00 AM - 5:00 PM',
            'Tuesday' => '9:00 AM - 5:00 PM',
            'Wednesday' => '9:00 AM - 5:00 PM',
            'Thursday' => '9:00 AM - 5:00 PM',
            'Friday' => '9:00 AM - 5:00 PM',
            'Saturday' => 'Closed',
            'Sunday' => 'Closed',
        ],
    ],
    [
        'name' => 'Agency Two',
        'address' => '456 Elm Street, Townsville, Country',
        'phone' => '+1-987-654-3210',
        'email' => 'info@agencytwo.com',
        'business_hours' => [
            'Monday' => '10:00 AM - 6:00 PM',
            'Tuesday' => '10:00 AM - 6:00 PM',
            'Wednesday' => '10:00 AM - 6:00 PM',
            'Thursday' => '10:00 AM - 6:00 PM',
            'Friday' => '10:00 AM - 6:00 PM',
            'Saturday' => '10:00 AM - 2:00 PM',
            'Sunday' => 'Closed',
        ],
    ],
    // Add more agencies as needed
];

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agency Locations and Contact Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .agency {
            border: 1px solid #ccc;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .agency h2 {
            margin-top: 0;
        }
        .business-hours {
            margin-top: 10px;
        }
        .business-hours table {
            width: 100%;
            border-collapse: collapse;
        }
        .business-hours th, .business-hours td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        .business-hours th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>

<h1>Agency Locations and Contact Information</h1>

<?php
// Loop through each agency and display its details
foreach ($agencies as $agency) {
    echo '<div class="agency">';
    echo '<h2>' . htmlspecialchars($agency['name']) . '</h2>';
    echo '<p><strong>Address:</strong> ' . htmlspecialchars($agency['address']) . '</p>';
    echo '<p><strong>Phone:</strong> ' . htmlspecialchars($agency['phone']) . '</p>';
    echo '<p><strong>Email:</strong> <a href="mailto:' . htmlspecialchars($agency['email']) . '">' . htmlspecialchars($agency['email']) . '</a></p>';
    
    echo '<div class="business-hours">';
    echo '<h3>Business Hours:</h3>';
    echo '<table>';
    echo '<thead><tr><th>Day</th><th>Hours</th></tr></thead>';
    echo '<tbody>';
    foreach ($agency['business_hours'] as $day => $hours) {
        echo '<tr><td>' . htmlspecialchars($day) . '</td><td>' . htmlspecialchars($hours) . '</td></tr>';
    }
    echo '</tbody>';
    echo '</table>';
    echo '</div>';
    
    echo '</div>';
}
?>

</body>
</html>
```
