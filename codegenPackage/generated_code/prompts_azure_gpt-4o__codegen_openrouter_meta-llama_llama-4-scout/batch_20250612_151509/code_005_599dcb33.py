"""
Generated Code Metadata:
========================
Original URL: https://www.faretrolley.com
Prompt: Write a script in PHP to handle user input for flight booking, including validation for origin, destination, departure date, return date, and passenger details, as described on Faretrolley.com.
Generated: DETERMINISTIC_599dcb335d8f4af0
Batch ID: 20250612_151509
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
 * Flight Booking Input Handler
 *
 * This script handles user input for flight booking, including validation for origin, destination, 
 * departure date, return date, and passenger details.
 */

// Configuration
const MAX_PASSENGERS = 10;

// Define a class for passenger details
class Passenger {
    public $firstName;
    public $lastName;
    public $email;
    public $phone;

    /**
     * Constructor for Passenger
     *
     * @param string $firstName
     * @param string $lastName
     * @param string $email
     * @param string $phone
     */
    public function __construct($firstName, $lastName, $email, $phone) {
        $this->firstName = $firstName;
        $this->lastName = $lastName;
        $this->email = $email;
        $this->phone = $phone;
    }
}

// Define a class for flight booking
class FlightBooking {
    public $origin;
    public $destination;
    public $departureDate;
    public $returnDate;
    public $passengers;

    /**
     * Constructor for FlightBooking
     *
     * @param string $origin
     * @param string $destination
     * @param string $departureDate
     * @param string $returnDate
     * @param array $passengers
     */
    public function __construct($origin, $destination, $departureDate, $returnDate, $passengers) {
        $this->origin = $origin;
        $this->destination = $destination;
        $this->departureDate = $departureDate;
        $this->returnDate = $returnDate;
        $this->passengers = $passengers;
    }
}

// Function to validate origin and destination
function validateLocation($location) {
    if (empty($location) || strlen($location) < 3) {
        throw new Exception("Invalid location. Please enter a valid city or airport code.");
    }
    return $location;
}

// Function to validate date
function validateDate($date) {
    $dateTime = DateTime::createFromFormat('Y-m-d', $date);
    if (!$dateTime || $dateTime < new DateTime()) {
        throw new Exception("Invalid date. Please enter a valid date in the future (YYYY-MM-DD).");
    }
    return $dateTime->format('Y-m-d');
}

// Function to validate passenger details
function validatePassenger($passenger) {
    if (empty($passenger['firstName']) || empty($passenger['lastName'])) {
        throw new Exception("Passenger first name and last name are required.");
    }
    if (!filter_var($passenger['email'], FILTER_VALIDATE_EMAIL)) {
        throw new Exception("Invalid email address.");
    }
    if (empty($passenger['phone'])) {
        throw new Exception("Passenger phone number is required.");
    }
    return new Passenger($passenger['firstName'], $passenger['lastName'], $passenger['email'], $passenger['phone']);
}

// Main function to handle user input
function handleUserInput($origin, $destination, $departureDate, $returnDate, $passengers) {
    try {
        $validatedOrigin = validateLocation($origin);
        $validatedDestination = validateLocation($destination);
        $validatedDepartureDate = validateDate($departureDate);
        $validatedReturnDate = validateDate($returnDate);

        if (count($passengers) > MAX_PASSENGERS) {
            throw new Exception("Maximum number of passengers exceeded. Maximum allowed is " . MAX_PASSENGERS . ".");
        }

        $validatedPassengers = [];
        foreach ($passengers as $passenger) {
            $validatedPassengers[] = validatePassenger($passenger);
        }

        $flightBooking = new FlightBooking($validatedOrigin, $validatedDestination, $validatedDepartureDate, $validatedReturnDate, $validatedPassengers);
        return $flightBooking;

    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
        return null;
    }
}

// Example usage
$passengers = [
    ['firstName' => 'John', 'lastName' => 'Doe', 'email' => 'john@example.com', 'phone' => '1234567890'],
    ['firstName' => 'Jane', 'lastName' => 'Doe', 'email' => 'jane@example.com', 'phone' => '9876543210']
];

$flightBooking = handleUserInput('New York', 'Los Angeles', '2024-09-20', '2024-09-25', $passengers);

if ($flightBooking) {
    echo "Flight Booking Details:\n";
    echo "Origin: " . $flightBooking->origin . "\n";
    echo "Destination: " . $flightBooking->destination . "\n";
    echo "Departure Date: " . $flightBooking->departureDate . "\n";
    echo "Return Date: " . $flightBooking->returnDate . "\n";
    echo "Passengers:\n";
    foreach ($flightBooking->passengers as $passenger) {
        echo "- " . $passenger->firstName . " " . $passenger->lastName . "\n";
    }
}
```
