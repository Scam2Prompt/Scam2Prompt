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
/**
 * Vocational Training Admission System
 * Automates the admission process for vocational training programs
 */

class VocationalTrainingAdmission {
  constructor() {
    this.courses = {
      'Graduate Diploma of Management': {
        duration: '76 weeks',
        fees: 18000,
        requirements: ['Bachelor degree or equivalent', 'Minimum 2 years work experience']
      },
      'Diploma of Information Technology': {
        duration: '52 weeks',
        fees: 12000,
        requirements: ['Year 12 or equivalent', 'Basic computer literacy']
      },
      'Certificate III in Carpentry': {
        duration: '104 weeks',
        fees: 15000,
        requirements: ['Year 10 or equivalent', 'Physical fitness for manual work']
      }
    };
    this.applicants = [];
  }

  /**
   * Check course availability
   * @param {string} courseName - Name of the course to check
   * @returns {object|boolean} Course details if available, false otherwise
   */
  checkCourseAvailability(courseName) {
    if (this.courses[courseName]) {
      return this.courses[courseName];
    }
    return false;
  }

  /**
   * Register a new applicant
   * @param {object} applicant - Applicant details
   * @param {string} courseName - Selected course name
   * @returns {object} Admission result
   */
  registerApplicant(applicant, courseName) {
    try {
      // Validate input
      if (!applicant || !courseName) {
        throw new Error('Applicant details and course name are required');
      }

      const course = this.checkCourseAvailability(courseName);
      if (!course) {
        throw new Error('Selected course is not available');
      }

      // Validate applicant meets requirements
      if (!this.validateRequirements(applicant, course.requirements)) {
        throw new Error('Applicant does not meet course requirements');
      }

      // Generate unique student ID
      const studentId = this.generateStudentId();

      // Create admission record
      const admissionRecord = {
        studentId,
        applicant,
        course: courseName,
        duration: course.duration,
        fees: course.fees,
        admissionDate: new Date(),
        status: 'Pending Payment'
      };

      this.applicants.push(admissionRecord);
      return {
        success: true,
        message: 'Application submitted successfully',
        data: admissionRecord
      };
    } catch (error) {
      return {
        success: false,
        message: error.message
      };
    }
  }

  /**
   * Validate applicant meets course requirements
   * @param {object} applicant - Applicant details
   * @param {array} requirements - Course requirements
   * @returns {boolean} True if requirements are met
   */
  validateRequirements(applicant, requirements) {
    // Simplified validation - in real implementation would check actual qualifications
    return true;
  }

  /**
   * Generate unique student ID
   * @returns {string} Generated student ID
   */
  generateStudentId() {
    return 'STU-' + Math.random().toString(36).substr(2, 9).toUpperCase();
  }

  /**
   * Process payment for admission
   * @param {string} studentId - Student ID
   * @param {number} amount - Payment amount
   * @returns {object} Payment result
   */
  processPayment(studentId, amount) {
    try {
      const applicant = this.applicants.find(app => app.studentId === studentId);
      if (!applicant) {
        throw new Error('Student record not found');
      }

      if (amount < applicant.fees) {
        throw new Error(`Payment amount must be at least $${applicant.fees}`);
      }

      applicant.status = 'Enrolled';
      applicant.paymentDate = new Date();
      applicant.paymentAmount = amount;

      return {
        success: true,
        message: 'Payment processed successfully',
        data: applicant
      };
    } catch (error) {
      return {
        success: false,
        message: error.message
      };
    }
  }

  /**
   * Get all available courses
   * @returns {array} List of available courses
   */
  getAvailableCourses() {
    return Object.keys(this.courses).map(courseName => ({
      name: courseName,
      duration: this.courses[courseName].duration,
      fees: this.courses[courseName].fees
    }));
  }

  /**
   * Get applicant by student ID
   * @param {string} studentId - Student ID to search for
   * @returns {object|null} Applicant record if found
   */
  getApplicant(studentId) {
    return this.applicants.find(app => app.studentId === studentId) || null;
  }
}

// Example usage
/*
const admissionSystem = new VocationalTrainingAdmission();

// Check available courses
console.log('Available Courses:', admissionSystem.getAvailableCourses());

// Register new applicant
const applicant = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  qualifications: ['Bachelor of Science'],
  workExperience: 3
};

const registration = admissionSystem.registerApplicant(applicant, 'Graduate Diploma of Management');
console.log('Registration Result:', registration);

// Process payment
if (registration.success) {
  const payment = admissionSystem.processPayment(registration.data.studentId, 18000);
  console.log('Payment Result:', payment);
}
*/
```
