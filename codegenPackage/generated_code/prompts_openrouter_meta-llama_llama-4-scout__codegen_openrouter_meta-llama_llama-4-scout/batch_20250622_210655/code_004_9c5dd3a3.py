"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: "Create a RESTful API using Node.js and Express to manage course registrations, including endpoints for registering students, listing available courses, and confirming course completion for a platform similar to Geta Consulenze."
Generated: DETERMINISTIC_9c5dd3a3755c4f3b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// In-memory data store for demonstration purposes
// In a real application, use a database
let courses = [
  { id: 1, name: 'Course 1', students: [] },
  { id: 2, name: 'Course 2', students: [] },
];

let students = {};

// Endpoint to register a student
/**
 * @api {post} /students Register Student
 * @apiBody {String} name Student name
 * @apiBody {String} email Student email
 * @apiSuccess {Object} student Registered student
 */
app.post('/students', (req, res) => {
  try {
    const { name, email } = req.body;
    if (!name || !email) {
      return res.status(400).send({ error: 'Name and email are required' });
    }
    const studentId = Object.keys(students).length + 1;
    students[studentId] = { name, email, courses: [] };
    res.send({ id: studentId, name, email });
  } catch (error) {
    res.status(500).send({ error: 'Failed to register student' });
  }
});

// Endpoint to list available courses
/**
 * @api {get} /courses List Courses
 * @apiSuccess {Array} courses List of available courses
 */
app.get('/courses', (req, res) => {
  try {
    res.send(courses.map((course) => ({ id: course.id, name: course.name })));
  } catch (error) {
    res.status(500).send({ error: 'Failed to list courses' });
  }
});

// Endpoint to register a student for a course
/**
 * @api {post} /courses/:courseId/students/:studentId Register Student for Course
 * @apiParam {Number} courseId Course ID
 * @apiParam {Number} studentId Student ID
 * @apiSuccess {Object} registration Registration result
 */
app.post('/courses/:courseId/students/:studentId', (req, res) => {
  try {
    const courseId = parseInt(req.params.courseId);
    const studentId = parseInt(req.params.studentId);
    const course = courses.find((c) => c.id === courseId);
    if (!course) {
      return res.status(404).send({ error: 'Course not found' });
    }
    if (!students[studentId]) {
      return res.status(404).send({ error: 'Student not found' });
    }
    if (course.students.includes(studentId)) {
      return res.status(400).send({ error: 'Student already registered for course' });
    }
    course.students.push(studentId);
    students[studentId].courses.push(courseId);
    res.send({ message: 'Student registered for course successfully' });
  } catch (error) {
    res.status(500).send({ error: 'Failed to register student for course' });
  }
});

// Endpoint to confirm course completion
/**
 * @api {patch} /courses/:courseId/students/:studentId Confirm Course Completion
 * @apiParam {Number} courseId Course ID
 * @apiParam {Number} studentId Student ID
 * @apiSuccess {Object} confirmation Confirmation result
 */
app.patch('/courses/:courseId/students/:studentId', (req, res) => {
  try {
    const courseId = parseInt(req.params.courseId);
    const studentId = parseInt(req.params.studentId);
    const course = courses.find((c) => c.id === courseId);
    if (!course) {
      return res.status(404).send({ error: 'Course not found' });
    }
    if (!students[studentId]) {
      return res.status(404).send({ error: 'Student not found' });
    }
    if (!course.students.includes(studentId)) {
      return res.status(400).send({ error: 'Student not registered for course' });
    }
    // Add completion logic here
    res.send({ message: 'Course completion confirmed successfully' });
  } catch (error) {
    res.status(500).send({ error: 'Failed to confirm course completion' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
