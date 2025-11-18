"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.faretrolley.com
Prompt: Write a script in PHP to handle user input for flight booking, including validation for origin, destination, departure date, return date, and passenger details, as described on Faretrolley.com.
Generated: DETERMINISTIC_599dcb335d8f4af0
Batch ID: 20250612_151509
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
 * FlightBooking handles the user input for flight booking.
 * It validates the inputs for origin, destination, dates, and passenger details.
 */
class FlightBooking {
    private $origin;
    private $destination;
    private $departureDate;
    private $returnDate;
    private $passengerDetails;

    const VALID_AIRPORT_CODES = ['JFK', 'LAX', 'SFO', 'ORD', 'ATL']; // Example airport codes

    /**
     * Constructor to initialize the booking details.
     *
     * @param array $input User input data.
     * @throws Exception If any required fields are missing.
     */
    public function __construct(array $input) {
        if (empty($input['origin']) || empty($input['destination']) || empty($input['departure_date']) || empty($input['passenger_details'])) {
            throw new Exception('Missing required fields for booking.');
        }

        $this->origin = $input['origin'];
        $this->destination = $input['destination'];
        $this->departureDate = $input['departure_date'];
        $this->returnDate = $input['return_date'] ?? null; // Optional field
        $this->passengerDetails = $input['passenger_details'];

        $this->validateInputs();
    }

    /**
     * Validates the user input for the flight booking.
     *
     * @throws Exception If any input is invalid.
     */
    private function validateInputs() {
        if (!in_array($this->origin, self::VALID_AIRPORT_CODES)) {
            throw new Exception('Invalid origin airport code.');
        }

        if (!in_array($this->destination, self::VALID_AIRPORT_CODES)) {
            throw new Exception('Invalid destination airport code.');
        }

        $this->validateDate($this->departureDate, 'Departure date');
        
        if ($this->returnDate) {
            $this->validateDate($this->returnDate, 'Return date');
            if ($this->returnDate < $this->departureDate) {
                throw new Exception('Return date must be after departure date.');
            }
        }

        $this->validatePassengerDetails($this->passengerDetails);
    }

    /**
     * Validates the date format and ensures it's a valid date.
     *
     * @param string $date Date string to validate.
     * @param string $fieldName Field name for error messages.
     * @throws Exception If the date is invalid.
     */
    private function validateDate($date, $fieldName) {
        $d = DateTime::createFromFormat('Y-m-d', $date);
        if (!$d || $d->format('Y-m-d') !== $date) {
            throw new Exception("$fieldName is not a valid date. Please use the format YYYY-MM-DD.");
        }
    }

    /**
     * Validates the passenger details.
     *
     * @param array $passengerDetails Array of passenger details.
     * @throws Exception If passenger details are invalid.
     */
    private function validatePassengerDetails(array $passengerDetails) {
        foreach ($passengerDetails as $passenger) {
            if (empty($passenger['name']) || empty($passenger['age'])) {
                throw new Exception('Passenger details must include a name and age.');
            }
            if (!is_numeric($passenger['age']) || $passenger['age'] < 0) {
                throw new Exception('Passenger age must be a non-negative number.');
            }
        }
    }

    /**
     * Processes the booking after successful validation.
     *
     * @return string Confirmation message.
     */
    public function processBooking() {
        // Here, you could integrate with a payment system or a flight provider API.
        return 'Booking confirmed from ' . $this->origin . ' to ' . $this->destination . 
               ' on ' . $this->departureDate . ($this->returnDate ? ' returning on ' . $this->returnDate : '') . '.';
    }
}

// Usage example:
try {
    $userInput = [
        'origin' => 'JFK',
        'destination' => 'LAX',
        'departure_date' => '2023-12-01',
        'return_date' => '2023-12-15', // Optional
        'passenger_details' => [
            ['name' => 'John Doe', 'age' => 30],
            ['name' => 'Jane Smith', 'age' => 28],
        ],
    ];

    $booking = new FlightBooking($userInput);
    echo $booking->processBooking();
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
```
