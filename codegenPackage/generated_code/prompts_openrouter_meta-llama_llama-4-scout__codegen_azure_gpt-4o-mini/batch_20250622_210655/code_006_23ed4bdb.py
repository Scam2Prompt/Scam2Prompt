"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: "Create a scheduling system in PHP for managing appointments and emergency roof services, ensuring efficient allocation of resources."
Generated: DETERMINISTIC_23ed4bdb4e77f07b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// AppointmentScheduler.php

class AppointmentScheduler {
    private $appointments = [];
    private $resources = [];

    // Constructor to initialize resources
    public function __construct(array $resources) {
        $this->resources = $resources;
    }

    // Method to schedule an appointment
    public function scheduleAppointment($dateTime, $serviceType) {
        // Validate dateTime and serviceType
        if (!$this->isValidDateTime($dateTime)) {
            throw new InvalidArgumentException("Invalid date and time provided.");
        }

        if (!in_array($serviceType, $this->resources)) {
            throw new InvalidArgumentException("Invalid service type provided.");
        }

        // Check for conflicts
        if ($this->isTimeSlotAvailable($dateTime)) {
            $this->appointments[] = [
                'dateTime' => $dateTime,
                'serviceType' => $serviceType
            ];
            return "Appointment scheduled successfully.";
        } else {
            throw new RuntimeException("The selected time slot is already booked.");
        }
    }

    // Method to check if a time slot is available
    private function isTimeSlotAvailable($dateTime) {
        foreach ($this->appointments as $appointment) {
            if ($appointment['dateTime'] === $dateTime) {
                return false; // Time slot is not available
            }
        }
        return true; // Time slot is available
    }

    // Method to validate date and time format
    private function isValidDateTime($dateTime) {
        $d = DateTime::createFromFormat('Y-m-d H:i:s', $dateTime);
        return $d && $d->format('Y-m-d H:i:s') === $dateTime;
    }

    // Method to list all appointments
    public function listAppointments() {
        return $this->appointments;
    }
}

// Example usage
try {
    // Define available resources
    $resources = ['Roof Inspection', 'Roof Repair', 'Emergency Service'];

    // Create an instance of AppointmentScheduler
    $scheduler = new AppointmentScheduler($resources);

    // Schedule appointments
    echo $scheduler->scheduleAppointment('2023-10-15 10:00:00', 'Roof Inspection') . PHP_EOL;
    echo $scheduler->scheduleAppointment('2023-10-15 11:00:00', 'Emergency Service') . PHP_EOL;

    // List all scheduled appointments
    print_r($scheduler->listAppointments());

} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```
