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
 * Music Course Enrollment Cost Calculator
 *
 * This script calculates the total cost for a student enrolling in multiple music courses.
 * It takes into account the course fees and any applicable discounts.
 */

// Define course fees
define('COURSE_FEES', [
    'guitar' => 300,
    'drums' => 250,
    'piano' => 350,
]);

// Define discount thresholds
define('DISCOUNT_THRESHOLD', 2); // Number of courses for discount
define('DISCOUNT_RATE', 0.1); // 10% discount

/**
 * Calculate the total cost for the selected courses.
 *
 * @param array $selectedCourses An array of selected course names.
 * @return float The total cost after applying any discounts.
 * @throws InvalidArgumentException If an invalid course is selected.
 */
function calculateTotalCost(array $selectedCourses): float {
    $totalCost = 0;

    foreach ($selectedCourses as $course) {
        if (!array_key_exists($course, COURSE_FEES)) {
            throw new InvalidArgumentException("Invalid course selected: $course");
        }
        $totalCost += COURSE_FEES[$course];
    }

    // Apply discount if applicable
    if (count($selectedCourses) >= DISCOUNT_THRESHOLD) {
        $totalCost -= $totalCost * DISCOUNT_RATE;
    }

    return $totalCost;
}

// Example usage
try {
    // Sample selected courses
    $selectedCourses = ['guitar', 'drums']; // Change this array to test different courses
    $totalCost = calculateTotalCost($selectedCourses);
    
    // Output the total cost
    echo "Total cost for enrolling in the selected courses: $" . number_format($totalCost, 2) . "\n";
} catch (InvalidArgumentException $e) {
    // Handle invalid course selection
    echo "Error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    // Handle any other unexpected errors
    echo "An unexpected error occurred: " . $e->getMessage() . "\n";
}
?>
```
