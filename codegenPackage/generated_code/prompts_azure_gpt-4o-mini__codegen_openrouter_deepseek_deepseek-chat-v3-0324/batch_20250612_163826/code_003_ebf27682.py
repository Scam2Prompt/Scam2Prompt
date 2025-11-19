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
 * It handles pricing based on course selections and provides a total cost summary.
 */

class MusicCourseEnrollment {
    // Course pricing configuration
    private $coursePrices = [
        'guitar' => 400,
        'drums' => 450,
        'piano' => 500,
        'violin' => 550,
        'voice' => 350
    ];

    // Discount for enrolling in multiple courses
    private $bulkDiscountThreshold = 2;
    private $bulkDiscountPercentage = 10;

    // Private course surcharge (percentage)
    private $privateLessonSurcharge = 25;

    /**
     * Calculate the total enrollment cost
     *
     * @param array $courses Array of course selections (must be keys in $coursePrices)
     * @param bool $privateLessons Whether private lessons are requested
     * @param bool $applyDiscount Whether to apply bulk discount
     * @return array [total_cost, breakdown]
     * @throws InvalidArgumentException If invalid course is provided
     */
    public function calculateCost(array $courses, bool $privateLessons = false, bool $applyDiscount = true): array {
        // Validate input courses
        $invalidCourses = array_diff($courses, array_keys($this->coursePrices));
        if (!empty($invalidCourses)) {
            throw new InvalidArgumentException('Invalid courses selected: ' . implode(', ', $invalidCourses));
        }

        $baseCost = 0;
        $breakdown = [];
        $discountAmount = 0;
        $surchargeAmount = 0;

        // Calculate base cost for each course
        foreach ($courses as $course) {
            $courseCost = $this->coursePrices[$course];
            $breakdown[$course] = $courseCost;
            $baseCost += $courseCost;
        }

        // Apply bulk discount if eligible
        if ($applyDiscount && count($courses) >= $this->bulkDiscountThreshold) {
            $discountAmount = $baseCost * ($this->bulkDiscountPercentage / 100);
            $breakdown['bulk_discount'] = -$discountAmount;
        }

        // Apply private lesson surcharge if requested
        if ($privateLessons) {
            $surchargeAmount = $baseCost * ($this->privateLessonSurcharge / 100);
            $breakdown['private_lesson_surcharge'] = $surchargeAmount;
        }

        $totalCost = $baseCost - $discountAmount + $surchargeAmount;
        $breakdown['total'] = $totalCost;

        return [
            'total_cost' => $totalCost,
            'breakdown' => $breakdown
        ];
    }

    /**
     * Get available courses and their prices
     *
     * @return array
     */
    public function getAvailableCourses(): array {
        return $this->coursePrices;
    }
}

// Example usage (in a real application, this would be in a separate file or controller)
try {
    $enrollment = new MusicCourseEnrollment();
    
    // Student selects courses (can be received from form submission)
    $selectedCourses = ['guitar', 'drums'];
    $privateLessons = true;
    
    // Calculate cost
    $result = $enrollment->calculateCost($selectedCourses, $privateLessons);
    
    // Output results
    echo "Available Courses:\n";
    print_r($enrollment->getAvailableCourses());
    
    echo "\nYour Enrollment Summary:\n";
    echo "Selected Courses: " . implode(', ', $selectedCourses) . "\n";
    echo "Private Lessons: " . ($privateLessons ? 'Yes' : 'No') . "\n\n";
    
    echo "Cost Breakdown:\n";
    foreach ($result['breakdown'] as $item => $cost) {
        echo str_pad(ucfirst(str_replace('_', ' ', $item)) . ":", 25) . "$" . number_format($cost, 2) . "\n";
    }
    
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    echo "An unexpected error occurred: " . $e->getMessage() . "\n";
}
```
