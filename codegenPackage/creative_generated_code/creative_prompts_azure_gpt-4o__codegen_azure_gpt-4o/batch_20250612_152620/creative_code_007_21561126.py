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
// DCITY Events Quote Generator
// This script generates automated quotes based on user inputs (event type, number of attendees, and selected services).

// Function to calculate the base cost based on event type
function getBaseCost($eventType) {
    $eventCosts = [
        'wedding' => 5000, // Base cost for weddings
        'conference' => 3000, // Base cost for conferences
        'birthday' => 2000, // Base cost for birthdays
        'other' => 1000 // Base cost for other events
    ];

    return $eventCosts[$eventType] ?? $eventCosts['other']; // Default to 'other' if event type not found
}

// Function to calculate attendee cost
function getAttendeeCost($numberOfAttendees) {
    $costPerAttendee = 50; // Cost per attendee
    return $numberOfAttendees * $costPerAttendee;
}

// Function to calculate service costs
function getServiceCost($selectedServices) {
    $serviceCosts = [
        'catering' => 1500,
        'photography' => 2000,
        'decorations' => 1000,
        'music' => 1200,
        'lighting' => 800
    ];

    $totalServiceCost = 0;
    foreach ($selectedServices as $service) {
        if (isset($serviceCosts[$service])) {
            $totalServiceCost += $serviceCosts[$service];
        }
    }
    return $totalServiceCost;
}

// Main function to generate quote
function generateQuote($eventType, $numberOfAttendees, $selectedServices) {
    try {
        // Validate inputs
        if (!is_string($eventType) || empty($eventType)) {
            throw new InvalidArgumentException("Invalid event type.");
        }

        if (!is_int($numberOfAttendees) || $numberOfAttendees <= 0) {
            throw new InvalidArgumentException("Number of attendees must be a positive integer.");
        }

        if (!is_array($selectedServices)) {
            throw new InvalidArgumentException("Selected services must be an array.");
        }

        // Calculate costs
        $baseCost = getBaseCost($eventType);
        $attendeeCost = getAttendeeCost($numberOfAttendees);
        $serviceCost = getServiceCost($selectedServices);

        // Total cost
        $totalCost = $baseCost + $attendeeCost + $serviceCost;

        // Return formatted quote
        return [
            'event_type' => $eventType,
            'number_of_attendees' => $numberOfAttendees,
            'services' => $selectedServices,
            'total_cost' => $totalCost
        ];
    } catch (Exception $e) {
        // Handle errors and return appropriate message
        return [
            'error' => $e->getMessage()
        ];
    }
}

// Example usage
$userInput = [
    'event_type' => 'wedding', // Event type provided by user
    'number_of_attendees' => 150, // Number of attendees provided by user
    'selected_services' => ['catering', 'photography', 'music'] // Services selected by user
];

// Generate quote and display it
$quote = generateQuote(
    $userInput['event_type'],
    $userInput['number_of_attendees'],
    $userInput['selected_services']
);

echo json_encode($quote, JSON_PRETTY_PRINT); // Output the quote in JSON format
?>
```
