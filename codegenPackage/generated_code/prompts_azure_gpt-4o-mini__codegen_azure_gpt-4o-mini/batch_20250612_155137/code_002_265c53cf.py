"""
Generated Code Metadata:
========================
Original URL: https://ydmc.edu.np
Prompt: Create a sample REST API call in PHP to access the course details of the Bachelor of Education program offered by YDMC.
Generated: DETERMINISTIC_265c53cf66f3dc7e
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Set the content type to JSON
header('Content-Type: application/json');

// Define the API response structure
$response = [
    'status' => 'success',
    'data' => null,
    'message' => ''
];

// Function to fetch course details
function getCourseDetails($program) {
    // Sample data for the Bachelor of Education program
    $courses = [
        'Bachelor of Education' => [
            [
                'course_id' => 101,
                'course_name' => 'Introduction to Education',
                'credits' => 3,
                'description' => 'An overview of the education system and teaching methodologies.'
            ],
            [
                'course_id' => 102,
                'course_name' => 'Child Development',
                'credits' => 3,
                'description' => 'Study of the psychological and emotional development of children.'
            ],
            [
                'course_id' => 103,
                'course_name' => 'Curriculum Design',
                'credits' => 3,
                'description' => 'Principles and practices of designing effective curricula.'
            ]
        ]
    ];

    // Check if the program exists in the data
    if (array_key_exists($program, $courses)) {
        return $courses[$program];
    } else {
        throw new Exception('Program not found.');
    }
}

// Main execution block
try {
    // Get the program name from the request (default to Bachelor of Education)
    $program = isset($_GET['program']) ? $_GET['program'] : 'Bachelor of Education';

    // Fetch course details
    $response['data'] = getCourseDetails($program);
    $response['message'] = 'Course details retrieved successfully.';
} catch (Exception $e) {
    // Handle errors and set the response accordingly
    $response['status'] = 'error';
    $response['message'] = $e->getMessage();
}

// Return the JSON response
echo json_encode($response);
?>
```
