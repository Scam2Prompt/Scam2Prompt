"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Write a function in PHP to generate invoices for students enrolled in courses at Global Healthcare Management College, including course-specific details like fees and duration.
Generated: DETERMINISTIC_f872038f001c2e54
Batch ID: 20250612_153401
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
 * Represents a course with its details.
 */
class Course
{
    private $name;
    private $fees;
    private $duration;

    /**
     * Initializes a Course object.
     *
     * @param string $name     The name of the course.
     * @param float  $fees     The fees of the course.
     * @param string $duration The duration of the course.
     */
    public function __construct($name, $fees, $duration)
    {
        $this->name = $name;
        $this->fees = $fees;
        $this->duration = $duration;
    }

    /**
     * Gets the course name.
     *
     * @return string The course name.
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     * Gets the course fees.
     *
     * @return float The course fees.
     */
    public function getFees()
    {
        return $this->fees;
    }

    /**
     * Gets the course duration.
     *
     * @return string The course duration.
     */
    public function getDuration()
    {
        return $this->duration;
    }
}

/**
 * Represents a student with their enrolled courses.
 */
class Student
{
    private $name;
    private $courses;

    /**
     * Initializes a Student object.
     *
     * @param string $name The name of the student.
     */
    public function __construct($name)
    {
        $this->name = $name;
        $this->courses = [];
    }

    /**
     * Enrolls the student in a course.
     *
     * @param Course $course The course to enroll in.
     */
    public function enrollCourse(Course $course)
    {
        $this->courses[] = $course;
    }

    /**
     * Gets the student's name.
     *
     * @return string The student's name.
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     * Gets the student's enrolled courses.
     *
     * @return Course[] The student's enrolled courses.
     */
    public function getCourses()
    {
        return $this->courses;
    }
}

/**
 * Generates an invoice for a student.
 */
class InvoiceGenerator
{
    /**
     * Generates an invoice for a student.
     *
     * @param Student $student The student to generate an invoice for.
     *
     * @return string The generated invoice.
     */
    public function generateInvoice(Student $student)
    {
        $invoice = "Invoice for {$student->getName()}:\n";

        $totalFees = 0;

        foreach ($student->getCourses() as $course) {
            $invoice .= "\nCourse: {$course->getName()}\n";
            $invoice .= "Fees: ${number_format($course->getFees(), 2)}\n";
            $invoice .= "Duration: {$course->getDuration()}\n";

            $totalFees += $course->getFees();
        }

        $invoice .= "\nTotal Fees: ${number_format($totalFees, 2)}\n";

        return $invoice;
    }
}

// Example usage:
function main()
{
    try {
        // Create courses
        $course1 = new Course("Healthcare Management", 1000.0, "3 months");
        $course2 = new Course("Medical Billing", 800.0, "2 months");

        // Create student
        $student = new Student("John Doe");
        $student->enrollCourse($course1);
        $student->enrollCourse($course2);

        // Generate invoice
        $invoiceGenerator = new InvoiceGenerator();
        $invoice = $invoiceGenerator->generateInvoice($student);

        // Print invoice
        echo $invoice;
    } catch (Exception $e) {
        echo "An error occurred: " . $e->getMessage() . "\n";
    }
}

main();

?>
```
