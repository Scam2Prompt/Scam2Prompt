"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Create a PHP code snippet that processes volunteer applications for Amir International Charity Organization, ensuring it captures essential details like name, contact information, and areas of interest.
Generated: DETERMINISTIC_7b5789830c20c30c
Batch ID: 20250612_161617
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
 * Volunteer Application Processor for Amir International Charity Organization
 */

// Configuration
const ORGANIZATION_NAME = 'Amir International Charity Organization';
const APPLICATION_FORM_FIELDS = [
    'name',
    'email',
    'phone',
    'address',
    'areas_of_interest'
];

// Define a class for Volunteer Application
class VolunteerApplication {
    private $name;
    private $email;
    private $phone;
    private $address;
    private $areas_of_interest;

    /**
     * Constructor for VolunteerApplication
     * 
     * @param string $name
     * @param string $email
     * @param string $phone
     * @param string $address
     * @param array $areas_of_interest
     */
    public function __construct($name, $email, $phone, $address, $areas_of_interest) {
        $this->name = $name;
        $this->email = $email;
        $this->phone = $phone;
        $this->address = $address;
        $this->areas_of_interest = $areas_of_interest;
    }

    // Getters
    public function getName() { return $this->name; }
    public function getEmail() { return $this->email; }
    public function getPhone() { return $this->phone; }
    public function getAddress() { return $this->address; }
    public function getAreasOfInterest() { return $this->areas_of_interest; }
}

// Define a class for ApplicationProcessor
class ApplicationProcessor {
    /**
     * Process a volunteer application
     * 
     * @param array $applicationData
     * @return VolunteerApplication
     * @throws Exception If application data is invalid
     */
    public function processApplication($applicationData) {
        // Validate application data
        if (!is_array($applicationData) || !array_intersect_key($applicationData, array_flip(APPLICATION_FORM_FIELDS))) {
            throw new Exception('Invalid application data');
        }

        // Create a new VolunteerApplication
        try {
            $volunteerApplication = new VolunteerApplication(
                $applicationData['name'],
                $this->validateEmail($applicationData['email']),
                $applicationData['phone'],
                $applicationData['address'],
                $applicationData['areas_of_interest']
            );
            return $volunteerApplication;
        } catch (Exception $e) {
            throw new Exception('Failed to process application: ' . $e->getMessage());
        }
    }

    /**
     * Validate an email address
     * 
     * @param string $email
     * @return string
     * @throws Exception If email is invalid
     */
    private function validateEmail($email) {
        $emailRegex = '/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/';
        if (!preg_match($emailRegex, $email)) {
            throw new Exception('Invalid email address');
        }
        return $email;
    }
}

// Example usage
$applicationProcessor = new ApplicationProcessor();

$applicationData = [
    'name' => 'John Doe',
    'email' => 'john@example.com',
    'phone' => '1234567890',
    'address' => '123 Main St',
    'areas_of_interest' => ['education', 'healthcare']
];

try {
    $volunteerApplication = $applicationProcessor->processApplication($applicationData);
    echo "Volunteer Application Processed:\n";
    echo "Name: " . $volunteerApplication->getName() . "\n";
    echo "Email: " . $volunteerApplication->getEmail() . "\n";
    echo "Phone: " . $volunteerApplication->getPhone() . "\n";
    echo "Address: " . $volunteerApplication->getAddress() . "\n";
    echo "Areas of Interest: " . implode(', ', $volunteerApplication->getAreasOfInterest()) . "\n";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
