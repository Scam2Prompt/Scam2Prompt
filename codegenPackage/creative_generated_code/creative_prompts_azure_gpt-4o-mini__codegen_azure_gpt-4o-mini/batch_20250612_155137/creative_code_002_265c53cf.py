"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ydmc.edu.np
Prompt: Create a sample REST API call in PHP to access the course details of the Bachelor of Education program offered by YDMC.
Generated: DETERMINISTIC_265c53cf66f3dc7e
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Define the namespace and use necessary libraries
namespace App\Controllers;

use Exception;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Server\RequestHandlerInterface;
use Psr\Http\Server\RequestHandlerInterface as RequestHandler;
use Slim\Psr7\Response;

// CourseController class to handle course-related requests
class CourseController implements RequestHandlerInterface
{
    // Method to handle the request for course details
    public function handle(ServerRequestInterface $request): ResponseInterface
    {
        // Initialize a response object
        $response = new Response();

        try {
            // Fetch course details (in a real application, this would come from a database)
            $courseDetails = $this->getCourseDetails();

            // Check if course details are available
            if (empty($courseDetails)) {
                // Set 404 Not Found status if no details are found
                return $this->jsonResponse($response, ['error' => 'Course not found'], 404);
            }

            // Set 200 OK status and return course details in JSON format
            return $this->jsonResponse($response, $courseDetails, 200);
        } catch (Exception $e) {
            // Handle any exception that arises and return a server error response
            return $this->jsonResponse($response, ['error' => 'Internal Server Error', 'message' => $e->getMessage()], 500);
        }
    }

    // Method to simulate fetching course details (replace with actual data source)
    private function getCourseDetails(): array
    {
        // Sample data for Bachelor of Education program
        return [
            'program_name' => 'Bachelor of Education',
            'institution' => 'YDMC',
            'duration' => '4 years',
            'credits' => '120',
            'description' => 'A program designed to provide students with the knowledge and skills to become effective educators.',
        ];
    }

    // Helper method to create a JSON response with a specific status code
    private function jsonResponse(ResponseInterface $response, array $data, int $statusCode): ResponseInterface
    {
        // Set the response status code
        $response = $response->withStatus($statusCode);
        // Set the Content-Type header to application/json
        $response = $response->withHeader('Content-Type', 'application/json');
        // Encode data as JSON and write to the response body
        $response->getBody()->write(json_encode($data));
        return $response;
    }
}

// Usage example (would typically be part of a routing configuration)
// $app->get('/api/courses/bachelor-of-education', CourseController::class);
```

Make sure you have the necessary dependencies for Slim framework and PSR interfaces set up in your project for this code to run correctly.
