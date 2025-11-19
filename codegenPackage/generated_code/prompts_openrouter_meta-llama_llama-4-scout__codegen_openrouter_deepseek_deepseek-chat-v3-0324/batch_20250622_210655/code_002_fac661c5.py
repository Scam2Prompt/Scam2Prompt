"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: "Write a code snippet in JavaScript to implement a simple e-learning platform that provides courses and training programs similar to those offered by Geta Consulenze."
Generated: DETERMINISTIC_fac661c5968a337e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple E-Learning Platform Implementation
 * 
 * Features:
 * - Course management
 * - User enrollment
 * - Progress tracking
 */

class ELearningPlatform {
  constructor() {
    this.courses = [];
    this.users = [];
    this.enrollments = [];
  }

  /**
   * Add a new course to the platform
   * @param {string} id - Unique course identifier
   * @param {string} title - Course title
   * @param {string} description - Course description
   * @param {string} instructor - Course instructor
   * @param {number} duration - Course duration in hours
   * @param {string[]} modules - Array of module names
   * @returns {boolean} True if course was added successfully
   */
  addCourse(id, title, description, instructor, duration, modules) {
    if (!id || !title || !description || !instructor || !duration || !modules) {
      throw new Error('All course fields are required');
    }

    if (this.courses.some(course => course.id === id)) {
      throw new Error('Course with this ID already exists');
    }

    this.courses.push({
      id,
      title,
      description,
      instructor,
      duration,
      modules,
      createdAt: new Date()
    });
    return true;
  }

  /**
   * Register a new user
   * @param {string} id - Unique user identifier
   * @param {string} name - User's full name
   * @param {string} email - User's email address
   * @param {string} role - User role (student/instructor/admin)
   * @returns {boolean} True if user was registered successfully
   */
  registerUser(id, name, email, role = 'student') {
    if (!id || !name || !email) {
      throw new Error('ID, name, and email are required');
    }

    if (!['student', 'instructor', 'admin'].includes(role)) {
      throw new Error('Invalid user role');
    }

    if (this.users.some(user => user.id === id)) {
      throw new Error('User with this ID already exists');
    }

    if (this.users.some(user => user.email === email)) {
      throw new Error('Email already registered');
    }

    this.users.push({
      id,
      name,
      email,
      role,
      registeredAt: new Date()
    });
    return true;
  }

  /**
   * Enroll a user in a course
   * @param {string} userId - User ID
   * @param {string} courseId - Course ID
   * @returns {boolean} True if enrollment was successful
   */
  enrollUser(userId, courseId) {
    const user = this.users.find(u => u.id === userId);
    if (!user) {
      throw new Error('User not found');
    }

    const course = this.courses.find(c => c.id === courseId);
    if (!course) {
      throw new Error('Course not found');
    }

    if (this.enrollments.some(e => e.userId === userId && e.courseId === courseId)) {
      throw new Error('User is already enrolled in this course');
    }

    this.enrollments.push({
      userId,
      courseId,
      enrolledAt: new Date(),
      progress: 0,
      completedModules: []
    });
    return true;
  }

  /**
   * Update user progress in a course
   * @param {string} userId - User ID
   * @param {string} courseId - Course ID
   * @param {string} module - Module name
   * @returns {boolean} True if progress was updated successfully
   */
  updateProgress(userId, courseId, module) {
    const enrollment = this.enrollments.find(e => 
      e.userId === userId && e.courseId === courseId
    );

    if (!enrollment) {
      throw new Error('Enrollment not found');
    }

    const course = this.courses.find(c => c.id === courseId);
    if (!course.modules.includes(module)) {
      throw new Error('Module not found in course');
    }

    if (enrollment.completedModules.includes(module)) {
      throw new Error('Module already completed');
    }

    enrollment.completedModules.push(module);
    enrollment.progress = Math.round(
      (enrollment.completedModules.length / course.modules.length) * 100
    );
    return true;
  }

  /**
   * Get all courses
   * @returns {Array} List of all courses
   */
  getAllCourses() {
    return this.courses;
  }

  /**
   * Get courses a user is enrolled in
   * @param {string} userId - User ID
   * @returns {Array} List of enrolled courses with progress
   */
  getUserCourses(userId) {
    if (!this.users.some(u => u.id === userId)) {
      throw new Error('User not found');
    }

    return this.enrollments
      .filter(e => e.userId === userId)
      .map(enrollment => {
        const course = this.courses.find(c => c.id === enrollment.courseId);
        return {
          ...course,
          progress: enrollment.progress,
          completedModules: enrollment.completedModules
        };
      });
  }
}

// Example usage:
/*
const platform = new ELearningPlatform();

// Add courses
platform.addCourse(
  'js101',
  'JavaScript Fundamentals',
  'Learn the basics of JavaScript programming',
  'John Doe',
  20,
  ['Variables', 'Functions', 'Objects', 'DOM']
);

platform.addCourse(
  'react-advanced',
  'Advanced React',
  'Master React with advanced patterns',
  'Jane Smith',
  30,
  ['Hooks', 'Context', 'Performance', 'Testing']
);

// Register users
platform.registerUser('user1', 'Alice Johnson', 'alice@example.com');
platform.registerUser('user2', 'Bob Williams', 'bob@example.com');

// Enroll users
platform.enrollUser('user1', 'js101');
platform.enrollUser('user1', 'react-advanced');
platform.enrollUser('user2', 'js101');

// Update progress
platform.updateProgress('user1', 'js101', 'Variables');
platform.updateProgress('user1', 'js101', 'Functions');

// Get user courses
console.log(platform.getUserCourses('user1'));
*/
```
