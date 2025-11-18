"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Write a function in PHP to generate invoices for students enrolled in courses at Global Healthcare Management College, including course-specific details like fees and duration.
Generated: DETERMINISTIC_f872038f001c2e54
Batch ID: 20250612_153401
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
 * Function to generate student invoices for courses at Global Healthcare Management College.
 *
 * @param string $studentName Name of the student.
 * @param string $studentID Unique ID of the student.
 * @param array $courses List of courses the student is enrolled in.
 *                        Each course should be an associative array with:
 *                        - 'courseName' => string (name of the course),
 *                        - 'courseFee' => float (fee for the course),
 *                        - 'courseDuration' => string (duration of the course, e.g., "3 months").
 * @return string Invoice details formatted as a string.
 */
function generateStudentInvoice($studentName, $studentID, $courses) {
    // Validate input
    if (empty($studentName) || empty($studentID) || !is_array($courses) || count($courses) === 0) {
        throw new InvalidArgumentException("Invalid input: Ensure student details and courses are provided correctly.");
    }

    $totalFee = 0; // Initialize total fee
    $invoiceDetails = "Invoice for: $studentName (ID: $studentID)\n";
    $invoiceDetails .= "----------------------------------------\n";

    foreach ($courses as $index => $course) {
        // Validate course details
        if (!isset($course['courseName']) || !isset($course['courseFee']) || !isset($course['courseDuration'])) {
            throw new InvalidArgumentException("Invalid course details: Ensure each course has 'courseName', 'courseFee', and 'courseDuration'.");
        }

        $courseName = htmlspecialchars($course['courseName'], ENT_QUOTES, 'UTF-8'); // Sanitize course name
        $courseFee = floatval($course['courseFee']); // Ensure course fee is a valid float
        $courseDuration = htmlspecialchars($course['courseDuration'], ENT_QUOTES, 'UTF-8'); // Sanitize course duration

        $totalFee += $courseFee; // Accumulate total fee

        // Append course details to the invoice
        $invoiceDetails .= sprintf(
            "Course #%d: %s\n  Fee: $%.2f\n  Duration: %s\n",
            $index + 1,
            $courseName,
            $courseFee,
            $courseDuration
        );
        $invoiceDetails .= "----------------------------------------\n";
    }

    // Append total fee to the invoice
    $invoiceDetails .= sprintf("Total Fee: $%.2f\n", $totalFee);
    $invoiceDetails .= "----------------------------------------\n";
    $invoiceDetails .= "Thank you for enrolling at Global Healthcare Management College!\n";

    return $invoiceDetails;
}

// Example usage
try {
    $studentName = "John Doe";
    $studentID = "GHMC12345";
    $courses = [
        [
            'courseName' => 'Healthcare Administration',
            'courseFee' => 1500.00,
            'courseDuration' => '6 months'
        ],
        [
            'courseName' => 'Medical Coding',
            'courseFee' => 1200.00,
            'courseDuration' => '4 months'
        ]
    ];

    // Generate and print the invoice
    $invoice = generateStudentInvoice($studentName, $studentID, $courses);
    echo nl2br($invoice); // Convert newlines to <br> for web output
} catch (Exception $e) {
    // Handle any errors gracefully
    echo "Error: " . $e->getMessage();
}

?>
```
