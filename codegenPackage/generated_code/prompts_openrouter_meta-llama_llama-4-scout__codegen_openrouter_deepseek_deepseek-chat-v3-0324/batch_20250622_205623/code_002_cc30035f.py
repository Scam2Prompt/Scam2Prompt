"""
Generated Code Metadata:
========================
Original URL: https://learnercamp.com
Prompt: Generate JavaScript code for a basic learning management system course catalog.
Generated: DETERMINISTIC_cc30035fffd8e4a3
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Basic Learning Management System (LMS) Course Catalog
 * This module provides functionality to manage and display courses in a catalog.
 */

class Course {
  /**
   * Creates a new Course instance
   * @param {string} id - Unique identifier for the course
   * @param {string} title - Course title
   * @param {string} description - Course description
   * @param {string} instructor - Course instructor name
   * @param {number} duration - Course duration in hours
   * @param {string} level - Course difficulty level (Beginner, Intermediate, Advanced)
   */
  constructor(id, title, description, instructor, duration, level) {
    this.id = id;
    this.title = title;
    this.description = description;
    this.instructor = instructor;
    this.duration = duration;
    this.level = level;
  }
}

class CourseCatalog {
  /**
   * Creates a new CourseCatalog instance
   */
  constructor() {
    this.courses = [];
  }

  /**
   * Adds a new course to the catalog
   * @param {Course} course - Course object to add
   * @throws {Error} If course is invalid or already exists
   */
  addCourse(course) {
    if (!(course instanceof Course)) {
      throw new Error('Invalid course object');
    }

    if (this.courses.some(c => c.id === course.id)) {
      throw new Error(`Course with ID ${course.id} already exists`);
    }

    this.courses.push(course);
  }

  /**
   * Removes a course from the catalog
   * @param {string} courseId - ID of the course to remove
   * @returns {boolean} True if course was removed, false if not found
   */
  removeCourse(courseId) {
    const initialLength = this.courses.length;
    this.courses = this.courses.filter(course => course.id !== courseId);
    return this.courses.length !== initialLength;
  }

  /**
   * Gets all courses in the catalog
   * @returns {Course[]} Array of all courses
   */
  getAllCourses() {
    return [...this.courses];
  }

  /**
   * Gets courses filtered by level
   * @param {string} level - Level to filter by (Beginner, Intermediate, Advanced)
   * @returns {Course[]} Array of filtered courses
   */
  getCoursesByLevel(level) {
    const validLevels = ['Beginner', 'Intermediate', 'Advanced'];
    if (!validLevels.includes(level)) {
      throw new Error('Invalid level specified');
    }
    return this.courses.filter(course => course.level === level);
  }

  /**
   * Searches courses by title or description
   * @param {string} searchTerm - Term to search for
   * @returns {Course[]} Array of matching courses
   */
  searchCourses(searchTerm) {
    if (!searchTerm || typeof searchTerm !== 'string') {
      return [];
    }

    const term = searchTerm.toLowerCase();
    return this.courses.filter(
      course =>
        course.title.toLowerCase().includes(term) ||
        course.description.toLowerCase().includes(term)
    );
  }

  /**
   * Gets course by ID
   * @param {string} courseId - ID of the course to find
   * @returns {Course|null} Found course or null if not found
   */
  getCourseById(courseId) {
    return this.courses.find(course => course.id === courseId) || null;
  }
}

// Example usage:
/*
const catalog = new CourseCatalog();

try {
  catalog.addCourse(
    new Course(
      'js101',
      'JavaScript Fundamentals',
      'Learn the basics of JavaScript programming',
      'Jane Doe',
      10,
      'Beginner'
    )
  );

  catalog.addCourse(
    new Course(
      'react202',
      'React Advanced Concepts',
      'Deep dive into React hooks and context API',
      'John Smith',
      15,
      'Advanced'
    )
  );

  console.log('All courses:', catalog.getAllCourses());
  console.log('Beginner courses:', catalog.getCoursesByLevel('Beginner'));
  console.log('Search results:', catalog.searchCourses('JavaScript'));
} catch (error) {
  console.error('Error:', error.message);
}
*/
```
