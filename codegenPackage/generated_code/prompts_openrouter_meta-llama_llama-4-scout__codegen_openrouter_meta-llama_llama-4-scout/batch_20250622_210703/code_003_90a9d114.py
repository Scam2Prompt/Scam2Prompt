"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Write a JavaScript code to create a simple webpage for Nzotho FET College's Student Portal, including features for student registration and course selection.
Generated: DETERMINISTIC_90a9d114bfda5ed0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html and script.js are assumed to be in the same directory

// script.js
class StudentPortal {
  /**
   * Initialize the student portal with an empty list of students and courses.
   */
  constructor() {
    this.students = {};
    this.courses = [
      { id: 1, name: "Mathematics" },
      { id: 2, name: "Science" },
      { id: 3, name: "History" },
      { id: 4, name: "English" },
    ];
  }

  /**
   * Register a new student.
   * @param {string} studentId - The student's ID.
   * @param {string} name - The student's name.
   * @param {string} email - The student's email.
   */
  registerStudent(studentId, name, email) {
    if (this.students[studentId]) {
      throw new Error(`Student with ID ${studentId} already exists.`);
    }
    this.students[studentId] = { name, email, courses: [] };
  }

  /**
   * Select courses for a student.
   * @param {string} studentId - The student's ID.
   * @param {number[]} courseIds - The IDs of the courses to select.
   */
  selectCourses(studentId, courseIds) {
    if (!this.students[studentId]) {
      throw new Error(`Student with ID ${studentId} does not exist.`);
    }
    const student = this.students[studentId];
    courseIds.forEach((courseId) => {
      const course = this.courses.find((c) => c.id === courseId);
      if (course && !student.courses.includes(course)) {
        student.courses.push(course);
      }
    });
  }

  /**
   * Get a student's details.
   * @param {string} studentId - The student's ID.
   * @returns {{ name: string, email: string, courses: { id: number, name: string }[] }} The student's details.
   */
  getStudentDetails(studentId) {
    if (!this.students[studentId]) {
      throw new Error(`Student with ID ${studentId} does not exist.`);
    }
    return this.students[studentId];
  }
}

// Create a new student portal
const portal = new StudentPortal();

// Get elements from the DOM
const registerForm = document.getElementById("register-form");
const courseForm = document.getElementById("course-form");
const studentDetailsElement = document.getElementById("student-details");

// Add event listener to the register form
registerForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const studentId = document.getElementById("student-id").value;
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  try {
    portal.registerStudent(studentId, name, email);
    alert(`Student ${name} registered successfully.`);
  } catch (error) {
    alert(error.message);
  }
});

// Add event listener to the course form
courseForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const studentId = document.getElementById("student-id-course").value;
  const courseIds = Array.from(document.querySelectorAll("#courses input[type='checkbox']:checked")).map((checkbox) => parseInt(checkbox.value));
  try {
    portal.selectCourses(studentId, courseIds);
    alert(`Courses selected successfully for student ${studentId}.`);
  } catch (error) {
    alert(error.message);
  }
});

// Add event listener to the student details button
document.getElementById("get-student-details").addEventListener("click", () => {
  const studentId = document.getElementById("student-id-details").value;
  try {
    const studentDetails = portal.getStudentDetails(studentId);
    studentDetailsElement.innerHTML = `
      <h2>Student Details</h2>
      <p>Name: ${studentDetails.name}</p>
      <p>Email: ${studentDetails.email}</p>
      <h3>Courses:</h3>
      <ul>
        ${studentDetails.courses.map((course) => `<li>${course.name}</li>`).join("")}
      </ul>
    `;
  } catch (error) {
    studentDetailsElement.innerHTML = `<p>${error.message}</p>`;
  }
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nzotho FET College Student Portal</title>
  <style>
    /* Basic styling for the portal */
    body {
      font-family: Arial, sans-serif;
    }
    form {
      margin-bottom: 20px;
    }
    label {
      display: block;
      margin-bottom: 10px;
    }
    input[type="text"], input[type="email"] {
      width: 100%;
      height: 30px;
      margin-bottom: 20px;
      padding: 10px;
      border: 1px solid #ccc;
    }
    input[type="checkbox"] {
      margin-right: 10px;
    }
  </style>
</head>
<body>
  <h1>Nzotho FET College Student Portal</h1>
  
  <h2>Register Student</h2>
  <form id="register-form">
    <label for="student-id">Student ID:</label>
    <input type="text" id="student-id" required>
    <label for="name">Name:</label>
    <input type="text" id="name" required>
    <label for="email">Email:</label>
    <input type="email" id="email" required>
    <button type="submit">Register</button>
  </form>
  
  <h2>Select Courses</h2>
  <form id="course-form">
    <label for="student-id-course">Student ID:</label>
    <input type="text" id="student-id-course" required>
    <label for="courses">Courses:</label>
    <ul id="courses">
      <li><input type="checkbox" id="course-1" value="1"><label for="course-1">Mathematics</label></li>
      <li><input type="checkbox" id="course-2" value="2"><label for="course-2">Science</label></li>
      <li><input type="checkbox" id="course-3" value="3"><label for="course-3">History</label></li>
      <li><input type="checkbox" id="course-4" value="4"><label for="course-4">English</label></li>
    </ul>
    <button type="submit">Select Courses</button>
  </form>
  
  <h2>Get Student Details</h2>
  <label for="student-id-details">Student ID:</label>
  <input type="text" id="student-id-details" required>
  <button id="get-student-details">Get Details</button>
  <div id="student-details"></div>

  <script src="script.js"></script>
</body>
</html>
```
