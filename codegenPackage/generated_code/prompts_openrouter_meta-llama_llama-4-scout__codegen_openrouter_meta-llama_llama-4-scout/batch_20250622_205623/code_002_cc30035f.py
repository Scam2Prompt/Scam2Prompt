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
// course.js

/**
 * Represents a Course in the Learning Management System.
 */
class Course {
  /**
   * Creates a new Course.
   * @param {string} id - Unique identifier for the course.
   * @param {string} name - Name of the course.
   * @param {string} description - Brief description of the course.
   * @param {number} credits - Number of credits the course is worth.
   */
  constructor(id, name, description, credits) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.credits = credits;
  }

  /**
   * Returns a string representation of the Course.
   * @returns {string}
   */
  toString() {
    return `${this.name} (${this.id}) - ${this.description} (${this.credits} credits)`;
  }
}

/**
 * Represents the Course Catalog in the Learning Management System.
 */
class CourseCatalog {
  /**
   * Creates a new CourseCatalog.
   */
  constructor() {
    this.courses = {};
  }

  /**
   * Adds a course to the catalog.
   * @param {Course} course - Course to add.
   * @throws {Error} If a course with the same ID already exists.
   */
  addCourse(course) {
    if (this.courses[course.id]) {
      throw new Error(`Course with ID ${course.id} already exists.`);
    }
    this.courses[course.id] = course;
  }

  /**
   * Removes a course from the catalog.
   * @param {string} id - ID of the course to remove.
   * @throws {Error} If the course does not exist.
   */
  removeCourse(id) {
    if (!this.courses[id]) {
      throw new Error(`Course with ID ${id} does not exist.`);
    }
    delete this.courses[id];
  }

  /**
   * Gets a course from the catalog.
   * @param {string} id - ID of the course to get.
   * @returns {Course|null} The course, or null if not found.
   */
  getCourse(id) {
    return this.courses[id] || null;
  }

  /**
   * Lists all courses in the catalog.
   * @returns {Course[]} Array of all courses.
   */
  listCourses() {
    return Object.values(this.courses);
  }
}

// Example usage:
function main() {
  const catalog = new CourseCatalog();

  try {
    const course1 = new Course("CS101", "Introduction to Computer Science", "Basic programming concepts.", 3);
    const course2 = new Course("CS202", "Data Structures", "Advanced data structures and algorithms.", 4);

    catalog.addCourse(course1);
    catalog.addCourse(course2);

    console.log("Courses:");
    catalog.listCourses().forEach((course) => console.log(course.toString()));

    console.log("\nGet Course:");
    const retrievedCourse = catalog.getCourse("CS101");
    if (retrievedCourse) {
      console.log(retrievedCourse.toString());
    } else {
      console.log("Course not found.");
    }

    catalog.removeCourse("CS101");

    console.log("\nCourses after removal:");
    catalog.listCourses().forEach((course) => console.log(course.toString()));
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
