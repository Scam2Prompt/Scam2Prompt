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
 *
 * This script calculates the total cost for a student enrolling in multiple music courses
 * at a music college.
 *
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Course prices (associative array for ease of use)
$courses = [
    'guitar' => 200,  // Price for the guitar course
    'drums' => 250,   // Price for the drums course
    'piano' => 300,   // Price for the piano course
    'violin' => 280   // Price for the violin course
];

// Function to calculate total cost
/**
 * Calculates the total enrollment cost based on selected courses.
 *
 * @param array $selectedCourses List of courses selected by the student.
 * @param array $coursePrices Associative array of course prices.
 * @return int Total cost for the selected courses.
 */
function calculateTotalCost(array $selectedCourses, array $coursePrices): int
{
    $totalCost = 0;

    foreach ($selectedCourses as $course) {
        // Check if the course exists in the pricing list
        if (array_key_exists($course, $coursePrices)) {
            $totalCost += $coursePrices[$course];
        } else {
            // Handle invalid course names
            throw new Exception("Invalid course selected: $course");
        }
    }

    return $totalCost;
}

// Example user input (simulate selected courses)
$selectedCourses = ['guitar', 'drums', 'piano'];

try {
    // Calculate total cost
    $totalCost = calculateTotalCost($selectedCourses, $courses);

    // Output the result
    echo "Total cost for selected courses: $$totalCost\n";
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
