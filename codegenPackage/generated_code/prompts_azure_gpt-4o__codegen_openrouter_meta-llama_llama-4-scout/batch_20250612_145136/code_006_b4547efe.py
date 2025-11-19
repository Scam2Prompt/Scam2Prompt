"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: Create a REST API endpoint in Node.js for INESO that allows users to fetch details about available courses, including their duration, modality, and accreditation status.
Generated: DETERMINISTIC_b4547efe5eedb565
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// courses.controller.js
const express = require('express');
const router = express.Router();
const courseService = require('./courses.service');

/**
 * GET /courses
 * @description Fetch all available courses
 * @returns {Object[]} An array of course objects
 */
router.get('/', async (req, res) => {
  try {
    const courses = await courseService.getAllCourses();
    res.json(courses);
  } catch (error) {
    res.status(500).json({ message: 'Failed to fetch courses' });
  }
});

/**
 * GET /courses/:id
 * @description Fetch a course by ID
 * @param {string} id - The ID of the course
 * @returns {Object} A course object
 */
router.get('/:id', async (req, res) => {
  try {
    const id = req.params.id;
    if (!id) {
      res.status(400).json({ message: 'Course ID is required' });
      return;
    }
    const course = await courseService.getCourseById(id);
    if (!course) {
      res.status(404).json({ message: 'Course not found' });
      return;
    }
    res.json(course);
  } catch (error) {
    res.status(500).json({ message: 'Failed to fetch course' });
  }
});

module.exports = router;
```

```javascript
// courses.service.js
const courseRepository = require('./courses.repository');

/**
 * Fetch all available courses
 * @returns {Object[]} An array of course objects
 */
async function getAllCourses() {
  try {
    return await courseRepository.getAllCourses();
  } catch (error) {
    throw new Error('Failed to fetch courses');
  }
}

/**
 * Fetch a course by ID
 * @param {string} id - The ID of the course
 * @returns {Object} A course object
 */
async function getCourseById(id) {
  try {
    return await courseRepository.getCourseById(id);
  } catch (error) {
    throw new Error('Failed to fetch course');
  }
}

module.exports = { getAllCourses, getCourseById };
```

```javascript
// courses.repository.js
const Course = require('./courses.model');

/**
 * Fetch all available courses
 * @returns {Object[]} An array of course objects
 */
async function getAllCourses() {
  try {
    return await Course.find().exec();
  } catch (error) {
    throw new Error('Failed to fetch courses');
  }
}

/**
 * Fetch a course by ID
 * @param {string} id - The ID of the course
 * @returns {Object} A course object
 */
async function getCourseById(id) {
  try {
    return await Course.findById(id).exec();
  } catch (error) {
    throw new Error('Failed to fetch course');
  }
}

module.exports = { getAllCourses, getCourseById };
```

```javascript
// courses.model.js
const mongoose = require('mongoose');

const courseSchema = new mongoose.Schema({
  name: { type: String, required: true },
  duration: { type: String, required: true },
  modality: { type: String, required: true },
  accreditationStatus: { type: String, required: true },
});

const Course = mongoose.model('Course', courseSchema);

module.exports = Course;
```

```javascript
// app.js
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const coursesController = require('./courses.controller');

app.use(express.json());

mongoose.connect('mongodb://localhost/ineso', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((error) => console.error('Failed to connect to MongoDB', error));

app.use('/api/courses', coursesController);

const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
