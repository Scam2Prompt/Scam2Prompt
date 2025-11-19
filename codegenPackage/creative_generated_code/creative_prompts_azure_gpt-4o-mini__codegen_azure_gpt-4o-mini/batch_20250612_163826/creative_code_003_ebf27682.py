"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Develop a PHP script that calculates the total cost for a student enrolling in multiple music courses, such as guitar and drums, at a music college.
Generated: DETERMINISTIC_ebf2768221161f7b
Batch ID: 20250612_163826
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
 * Music Course Enrollment Cost Calculator
 * This script calculates the total cost for a student enrolling in multiple music courses.
 * Each course has a predefined cost, and users can select multiple courses to enroll in.
 */

// Course costs defined in an associative array
$courseCosts = [
    'guitar' => 200,
    'drums' => 150,
    'piano' => 300,
    'violin' => 250,
];

// Function to calculate total enrollment cost
/**
 * Calculate the total cost of selected courses.
 *
 * @param array $selectedCourses An array of selected course names.
 * @param array $courseCosts An associative array of course costs.
 * @return float Total cost of the selected courses.
 */
function calculateTotalCost(array $selectedCourses, array $courseCosts): float {
    $totalCost = 0.0;

    foreach ($selectedCourses as $course) {
        // Check if the course exists in the predefined costs
        if (array_key_exists($course, $courseCosts)) {
            $totalCost += $courseCosts[$course];
        } else {
            // Error handling for invalid course selection
            throw new InvalidArgumentException("Invalid course selected: $course");
        }
    }

    return $totalCost;
}

// Example usage
try {
    // Simulating user-selected courses
    $selectedCourses = ['guitar', 'drums']; // Example input

    // Calculate total cost
    $totalCost = calculateTotalCost($selectedCourses, $courseCosts);

    // Output the total cost
    echo "Total enrollment cost: $" . number_format($totalCost, 2);
} catch (InvalidArgumentException $e) {
    // Handle invalid course selection
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    // Handle any other errors
    echo "An unexpected error occurred: " . $e->getMessage();
}
?>
```
