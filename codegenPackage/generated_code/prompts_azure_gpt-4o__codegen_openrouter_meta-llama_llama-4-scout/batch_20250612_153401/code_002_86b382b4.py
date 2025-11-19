"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Create a script in JavaScript to automate the admission process for vocational training programs, incorporating unique course details such as duration (e.g., 76 weeks for Graduate Diploma of Management) and fees (e.g., $18,000).
Generated: DETERMINISTIC_86b382b44d709914
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// vocational-training-admission.js

/**
 * Represents a vocational training course.
 */
class Course {
  /**
   * Creates a new Course instance.
   * @param {string} name - Course name.
   * @param {number} durationInWeeks - Course duration in weeks.
   * @param {number} fees - Course fees.
   */
  constructor(name, durationInWeeks, fees) {
    this.name = name;
    this.durationInWeeks = durationInWeeks;
    this.fees = fees;
  }
}

/**
 * Represents a student.
 */
class Student {
  /**
   * Creates a new Student instance.
   * @param {string} name - Student name.
   * @param {string} email - Student email.
   */
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }
}

/**
 * Represents an admission application.
 */
class AdmissionApplication {
  /**
   * Creates a new AdmissionApplication instance.
   * @param {Student} student - Student details.
   * @param {Course} course - Course details.
   */
  constructor(student, course) {
    this.student = student;
    this.course = course;
  }

  /**
   * Submits the admission application.
   * @throws {Error} If student or course details are invalid.
   */
  submitApplication() {
    if (!this.student || !this.course) {
      throw new Error('Invalid student or course details');
    }

    try {
      // Simulate application submission (e.g., save to database)
      console.log(`Admission application submitted for ${this.student.name} to ${this.course.name}`);
      return true;
    } catch (error) {
      console.error(`Error submitting admission application: ${error.message}`);
      return false;
    }
  }
}

/**
 * Calculates the total course fees based on duration and fees.
 * @param {Course} course - Course details.
 * @returns {number} Total course fees.
 */
function calculateTotalFees(course) {
  return course.fees;
}

/**
 * Validates student and course details.
 * @param {Student} student - Student details.
 * @param {Course} course - Course details.
 * @returns {boolean} True if valid, false otherwise.
 */
function validateApplication(student, course) {
  if (!student.name || !student.email) {
    console.error('Invalid student details');
    return false;
  }

  if (!course.name || course.durationInWeeks <= 0 || course.fees <= 0) {
    console.error('Invalid course details');
    return false;
  }

  return true;
}

// Example usage:
function main() {
  const course = new Course('Graduate Diploma of Management', 76, 18000);
  const student = new Student('John Doe', 'john.doe@example.com');

  if (validateApplication(student, course)) {
    const application = new AdmissionApplication(student, course);
    const totalFees = calculateTotalFees(course);

    console.log(`Course: ${application.course.name}`);
    console.log(`Duration: ${application.course.durationInWeeks} weeks`);
    console.log(`Fees: $${application.course.fees}`);
    console.log(`Total Fees: $${totalFees}`);

    application.submitApplication();
  }
}

main();
```
