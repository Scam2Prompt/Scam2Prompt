"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Develop a PHP script that calculates the total cost for a student enrolling in multiple music courses, such as guitar and drums, at a music college.
Generated: DETERMINISTIC_ebf2768221161f7b
Batch ID: 20250612_163826
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
 * Music College Enrollment Cost Calculator
 * 
 * This script calculates the total cost for a student enrolling in multiple music courses.
 * Each course has a predefined cost, and the script sums up the costs of selected courses.
 */

// Define course costs (in USD)
$courseCosts = [
    'guitar' => 200,
    'drums' => 250,
    'piano' => 300,
    'violin' => 280,
    'vocals' => 220
];

/**
 * Calculate the total cost for selected courses.
 * 
 * @param array $selectedCourses Array of course names selected by the student.
 * @param array $courseCosts Associative array of course names and their respective costs.
 * @return float Total cost of selected courses.
 * @throws Exception If a selected course is not found in the course list.
 */
function calculateTotalCost(array $selectedCourses, array $courseCosts): float {
    $totalCost = 0;

    foreach ($selectedCourses as $course) {
        if (!array_key_exists($course, $courseCosts)) {
            throw new Exception("Course '{$course}' not found in the course list.");
        }
        $totalCost += $courseCosts[$course];
    }

    return $totalCost;
}

// Example usage
try {
    // Courses selected by the student
    $selectedCourses = ['guitar', 'drums', 'piano'];

    // Calculate total cost
    $totalCost = calculateTotalCost($selectedCourses, $courseCosts);

    // Output the total cost
    echo "The total cost for the selected courses is: $" . number_format($totalCost, 2) . "\n";
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
