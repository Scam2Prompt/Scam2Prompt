"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sala-events.co.il
Prompt: Write a PHP script for generating automated quotes for events at DCITY Events based on user inputs like event type, number of attendees, and selected services.
Generated: DETERMINISTIC_21561126f115c430
Batch ID: 20250612_152620
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
 * DCITY Events Quote Generator
 * This script generates an automated quote for events based on user inputs.
 * 
 * Usage: Provide event type, number of attendees, and selected services via POST request.
 */

// Define constants for pricing
define('BASE_PRICE_PER_ATTENDEE', 50);  // Base price per attendee
define('SERVICE_COSTS', [
    'catering' => 20,       // Additional cost for catering service
    'decorations' => 15,    // Additional cost for decorations service
    'audio_visual' => 30,   // Additional cost for audio/visual service
]);

/**
 * Generates a quote based on event details.
 *
 * @param string $eventType The type of event (e.g., wedding, corporate).
 * @param int $numAttendees The number of attendees.
 * @param array $services Selected additional services.
 * @return array Contains the quote and breakdown.
 */
function generateQuote($eventType, $numAttendees, $services) {
    if ($numAttendees <= 0) {
        throw new InvalidArgumentException("Number of attendees must be greater than zero.");
    }

    // Calculate base cost
    $baseCost = BASE_PRICE_PER_ATTENDEE * $numAttendees;

    // Calculate additional service costs
    $additionalCost = 0;
    foreach ($services as $service) {
        if (array_key_exists($service, SERVICE_COSTS)) {
            $additionalCost += SERVICE_COSTS[$service];
        } else {
            throw new InvalidArgumentException("Service '$service' is not recognized.");
        }
    }

    // Calculate total quote
    $totalCost = $baseCost + $additionalCost;

    // Prepare quote breakdown
    $quote = [
        'event_type' => $eventType,
        'num_attendees' => $numAttendees,
        'base_cost' => $baseCost,
        'additional_cost' => $additionalCost,
        'total_cost' => $totalCost,
    ];

    return $quote;
}

// Check if the request is a POST request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate and retrieve inputs
        $eventType = isset($_POST['event_type']) ? trim($_POST['event_type']) : '';
        $numAttendees = isset($_POST['num_attendees']) ? (int)$_POST['num_attendees'] : 0;
        $services = isset($_POST['services']) ? (array)$_POST['services'] : [];

        // Validate inputs
        if (empty($eventType)) {
            throw new InvalidArgumentException("Event type is required.");
        }

        // Generate the quote
        $quote = generateQuote($eventType, $numAttendees, $services);

        // Return the quote as JSON
        header('Content-Type: application/json');
        echo json_encode($quote);

    } catch (Exception $e) {
        // Handle errors and provide feedback
        http_response_code(400); // Bad Request
        echo json_encode(['error' => $e->getMessage()]);
    }
} else {
    // Respond with error for non-POST requests
    http_response_code(405); // Method Not Allowed
    echo json_encode(['error' => 'Only POST requests are allowed.']);
}
?>
```
