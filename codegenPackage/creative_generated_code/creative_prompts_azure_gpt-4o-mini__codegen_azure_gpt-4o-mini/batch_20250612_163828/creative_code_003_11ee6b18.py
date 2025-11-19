"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Develop a PHP application that integrates with ENACIP's virtual classroom system, allowing users to log in and access their enrolled courses.
Generated: DETERMINISTIC_11ee6b18ce2abb10
Batch ID: 20250612_163828
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.enacip.com/v1": {
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
 * ENACIP Virtual Classroom Integration
 *
 * This PHP application integrates with ENACIP's virtual classroom system,
 * allowing users to log in and access their enrolled courses.
 */

// Configuration settings
define('ENACIP_API_URL', 'https://api.enacip.com/v1'); // Replace with actual API URL
define('ENACIP_API_KEY', 'your_api_key_here'); // Replace with your actual API key

/**
 * Function to perform a login request to ENACIP's API
 *
 * @param string $username The username of the user
 * @param string $password The password of the user
 * @return array|bool Returns user data if successful, false otherwise
 */
function loginToEnacip($username, $password) {
    $url = ENACIP_API_URL . '/login';
    
    // Prepare the data for the API request
    $data = [
        'username' => $username,
        'password' => $password,
    ];

    // Initialize CURL
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . ENACIP_API_KEY,
    ]);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

    // Execute the CURL request and handle errors
    $response = curl_exec($ch);
    if (curl_errno($ch)) {
        error_log('CURL error: ' . curl_error($ch));
        curl_close($ch);
        return false;
    }
    
    curl_close($ch);

    // Decode the JSON response
    $responseData = json_decode($response, true);
    if (isset($responseData['error'])) {
        error_log('API error: ' . $responseData['error']);
        return false;
    }

    return $responseData;
}

/**
 * Function to get the enrolled courses for the authenticated user
 *
 * @param string $token The authentication token of the user
 * @return array|bool Returns an array of courses if successful, false otherwise
 */
function getEnrolledCourses($token) {
    $url = ENACIP_API_URL . '/courses/enrolled';
    
    // Initialize CURL
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . $token,
    ]);
    
    // Execute the CURL request and handle errors
    $response = curl_exec($ch);
    if (curl_errno($ch)) {
        error_log('CURL error: ' . curl_error($ch));
        curl_close($ch);
        return false;
    }
    
    curl_close($ch);

    // Decode the JSON response
    $responseData = json_decode($response, true);
    if (isset($responseData['error'])) {
        error_log('API error: ' . $responseData['error']);
        return false;
    }

    return $responseData;
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Capture user credentials from the login form
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    // Attempt to log in to ENACIP
    $userData = loginToEnacip($username, $password);
    if ($userData) {
        // Successful login, get courses
        $courses = getEnrolledCourses($userData['token']);
        
        if ($courses) {
            echo 'Enrolled Courses:';
            foreach ($courses as $course) {
                echo '<p>' . htmlspecialchars($course['name']) . '</p>';
            }
        } else {
            echo 'Failed to retrieve courses.';
        }
    } else {
        echo 'Login failed. Please check your credentials.';
    }
}
?>

<!-- Simple HTML form for user login -->
<!DOCTYPE html>
<html>
<head>
    <title>ENACIP Virtual Classroom Login</title>
</head>
<body>
    <h1>Login to ENACIP Virtual Classroom</h1>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```
