"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lattechocolate.com.ar
Prompt: Create a PHP code snippet that sends a request to the Latte Chocolate API to register a new user and handle the response for successful registration.
Generated: DETERMINISTIC_a9240943e73d866d
Batch ID: 20250612_162710
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lattechocolate.com/register": {
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
/**
 * This PHP script sends a request to the Latte Chocolate API
 * to register a new user and handles the response for successful registration.
 */

// Define the API endpoint for user registration
define('API_ENDPOINT', 'https://api.lattechocolate.com/register');

// Function to register a new user
function registerUser($email, $password) {
    // Prepare the data to be sent in the POST request
    $data = [
        'email' => $email,
        'password' => $password,
    ];

    // Initialize cURL session
    $ch = curl_init(API_ENDPOINT);

    // Set cURL options
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Return response as a string
    curl_setopt($ch, CURLOPT_POST, true); // Set method to POST
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data)); // Set POST fields
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/x-www-form-urlencoded']); // Set headers

    // Execute the cURL request and capture the response
    $response = curl_exec($ch);
    
    // Check for cURL errors
    if ($response === false) {
        $error = curl_error($ch);
        curl_close($ch);
        throw new Exception("cURL Error: $error"); // Throw an exception on error
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the JSON response
    $responseData = json_decode($response, true);

    // Check if the registration was successful
    if (isset($responseData['success']) && $responseData['success']) {
        return "User registered successfully!";
    } else {
        // Handle error response
        $errorMessage = isset($responseData['message']) ? $responseData['message'] : 'Registration failed.';
        throw new Exception("API Error: $errorMessage");
    }
}

// Example usage
try {
    // Replace with user input or predefined values
    $email = 'user@example.com';
    $password = 'securePassword123';

    // Call the registerUser function
    $result = registerUser($email, $password);
    echo $result; // Output success message
} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . $e->getMessage();
}
?>
```
