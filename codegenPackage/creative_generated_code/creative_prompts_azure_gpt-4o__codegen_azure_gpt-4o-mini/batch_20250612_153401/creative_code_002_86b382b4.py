"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Create a script in JavaScript to automate the admission process for vocational training programs, incorporating unique course details such as duration (e.g., 76 weeks for Graduate Diploma of Management) and fees (e.g., $18,000).
Generated: DETERMINISTIC_86b382b44d709914
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file admissionAutomation.js
 * @description A script to automate the admission process for vocational training programs.
 * This script includes course details such as duration and fees.
 * It also handles user input and provides error handling for a smooth experience.
 */

// Course class to define the properties of a vocational training program
class Course {
    constructor(name, duration, fees) {
        this.name = name;                // Name of the course
        this.duration = duration;        // Duration in weeks
        this.fees = fees;                // Fees in dollars
    }

    // Method to display course details
    displayDetails() {
        console.log(`Course Name: ${this.name}`);
        console.log(`Duration: ${this.duration} weeks`);
        console.log(`Fees: $${this.fees}`);
    }
}

// Admission class to handle the admission process
class Admission {
    constructor() {
        this.courses = [];               // Array to hold available courses
    }

    // Method to add a new course
    addCourse(course) {
        if (course instanceof Course) {
            this.courses.push(course);
        } else {
            console.error("Invalid course object. Please provide a valid Course instance.");
        }
    }

    // Method to display all available courses
    displayCourses() {
        if (this.courses.length === 0) {
            console.log("No courses available for admission.");
            return;
        }
        console.log("Available Courses for Admission:");
        this.courses.forEach(course => course.displayDetails());
    }

    // Method to apply for a course
    applyForCourse(courseName) {
        const course = this.courses.find(c => c.name === courseName);
        if (!course) {
            console.error(`Course "${courseName}" not found. Please choose a valid course.`);
            return;
        }
        console.log(`Successfully applied for the course: ${course.name}`);
        // Here we could add additional steps to finalize the admission, such as payment processing
    }
}

// Creating an instance of the Admission system
const admissionSystem = new Admission();

// Adding courses to the system
admissionSystem.addCourse(new Course("Graduate Diploma of Management", 76, 18000));
admissionSystem.addCourse(new Course("Certificate IV in Project Management", 52, 12000));

// Displaying available courses
admissionSystem.displayCourses();

// Applying for a specific course (this can be changed as needed)
admissionSystem.applyForCourse("Graduate Diploma of Management");

// Error handling for course application with invalid course name
admissionSystem.applyForCourse("Non-Existent Course");
```

This JavaScript code provides a structured approach to automating the admission process, ensuring that all the requirements specified are met with proper handling and documentation throughout.
