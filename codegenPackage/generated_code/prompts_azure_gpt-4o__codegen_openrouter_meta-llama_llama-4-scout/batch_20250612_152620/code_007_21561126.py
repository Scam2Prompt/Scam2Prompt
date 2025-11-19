"""
Generated Code Metadata:
========================
Original URL: https://sala-events.co.il
Prompt: Write a PHP script for generating automated quotes for events at DCITY Events based on user inputs like event type, number of attendees, and selected services.
Generated: DETERMINISTIC_21561126f115c430
Batch ID: 20250612_152620
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
 * DCITY Events Automated Quote Generator
 */

// Configuration
$config = [
    'event_types' => [
        'wedding' => 1000,
        'corporate' => 500,
        'birthday' => 800,
    ],
    'services' => [
        'catering' => 50,
        'photography' => 1000,
        'music' => 500,
        'venue' => 2000,
    ],
];

// Event Quote class
class EventQuote
{
    private $eventType;
    private $numAttendees;
    private $selectedServices;

    public function __construct($eventType, $numAttendees, $selectedServices)
    {
        $this->eventType = $eventType;
        $this->numAttendees = $numAttendees;
        $this->selectedServices = $selectedServices;
    }

    public function calculateBasePrice()
    {
        global $config;
        return $config['event_types'][$this->eventType] ?? 0;
    }

    public function calculateServicePrice()
    {
        global $config;
        $servicePrice = 0;
        foreach ($this->selectedServices as $service) {
            $servicePrice += $config['services'][$service] ?? 0;
        }
        return $servicePrice;
    }

    public function calculateAttendeePrice()
    {
        return $this->numAttendees * 10; // $10 per attendee
    }

    public function generateQuote()
    {
        $basePrice = $this->calculateBasePrice();
        $servicePrice = $this->calculateServicePrice();
        $attendeePrice = $this->calculateAttendeePrice();
        $totalPrice = $basePrice + $servicePrice + $attendeePrice;

        return [
            'base_price' => $basePrice,
            'service_price' => $servicePrice,
            'attendee_price' => $attendeePrice,
            'total_price' => $totalPrice,
        ];
    }
}

// User input handling
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $eventType = filter_input(INPUT_POST, 'event_type', FILTER_SANITIZE_STRING);
        $numAttendees = filter_input(INPUT_POST, 'num_attendees', FILTER_VALIDATE_INT);
        $selectedServices = filter_input(INPUT_POST, 'selected_services', FILTER_SANITIZE_STRING, FILTER_REQUIRE_ARRAY);

        if (!$eventType || !$numAttendees || empty($selectedServices)) {
            throw new Exception('Invalid input');
        }

        $eventQuote = new EventQuote($eventType, $numAttendees, $selectedServices);
        $quote = $eventQuote->generateQuote();

        // Output quote
        header('Content-Type: application/json');
        echo json_encode($quote, JSON_PRETTY_PRINT);
    } catch (Exception $e) {
        http_response_code(400);
        echo json_encode(['error' => $e->getMessage()], JSON_PRETTY_PRINT);
    }
} else {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed'], JSON_PRETTY_PRINT);
}
```
