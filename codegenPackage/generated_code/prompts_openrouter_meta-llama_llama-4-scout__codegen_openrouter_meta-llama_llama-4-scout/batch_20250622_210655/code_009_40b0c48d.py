"""
Generated Code Metadata:
========================
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Create a RESTful API using Node.js and Express.js to manage student data and academic records for Escuela Preparatoria Oficial N.73.
Generated: DETERMINISTIC_40b0c48d7e4023c3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Student API**
===============

**dependencies**
---------------

*   express: ^4.18.2
*   mongoose: ^6.7.2
*   body-parser: ^1.20.2

**student.model.js**
--------------------

```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define student schema
const studentSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    lastName: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    grade: {
        type: Number,
        required: true
    },
    academicRecords: [
        {
            subject: {
                type: String,
                required: true
            },
            grade: {
                type: Number,
                required: true
            }
        }
    ]
});

// Export student model
module.exports = mongoose.model('Student', studentSchema);
```

**student.controller.js**
-------------------------

```javascript
// Import student model
const Student = require('./student.model');

// Get all students
exports.getStudents = async (req, res) => {
    try {
        const students = await Student.find().exec();
        res.json(students);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};

// Get student by ID
exports.getStudent = async (req, res) => {
    try {
        const student = await Student.findById(req.params.id).exec();
        if (!student) {
            return res.status(404).json({ message: 'Student not found' });
        }
        res.json(student);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};

// Create new student
exports.createStudent = async (req, res) => {
    try {
        const student = new Student(req.body);
        await student.save();
        res.status(201).json(student);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
};

// Update student
exports.updateStudent = async (req, res) => {
    try {
        const student = await Student.findByIdAndUpdate(req.params.id, req.body, { new: true }).exec();
        if (!student) {
            return res.status(404).json({ message: 'Student not found' });
        }
        res.json(student);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
};

// Delete student
exports.deleteStudent = async (req, res) => {
    try {
        await Student.findByIdAndRemove(req.params.id).exec();
        res.status(204).json({ message: 'Student deleted successfully' });
    } catch (err) {
        res.status(404).json({ message: err.message });
    }
};

// Add academic record
exports.addAcademicRecord = async (req, res) => {
    try {
        const student = await Student.findById(req.params.id).exec();
        if (!student) {
            return res.status(404).json({ message: 'Student not found' });
        }
        student.academicRecords.push(req.body);
        await student.save();
        res.json(student);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
};

// Update academic record
exports.updateAcademicRecord = async (req, res) => {
    try {
        const student = await Student.findById(req.params.id).exec();
        if (!student) {
            return res.status(404).json({ message: 'Student not found' });
        }
        const recordIndex = student.academicRecords.findIndex(record => record._id.toString() === req.params.recordId);
        if (recordIndex === -1) {
            return res.status(404).json({ message: 'Academic record not found' });
        }
        student.academicRecords[recordIndex] = req.body;
        await student.save();
        res.json(student);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
};

// Delete academic record
exports.deleteAcademicRecord = async (req, res) => {
    try {
        const student = await Student.findById(req.params.id).exec();
        if (!student) {
            return res.status(404).json({ message: 'Student not found' });
        }
        student.academicRecords = student.academicRecords.filter(record => record._id.toString() !== req.params.recordId);
        await student.save();
        res.status(204).json({ message: 'Academic record deleted successfully' });
    } catch (err) {
        res.status(404).json({ message: err.message });
    }
};
```

**student.route.js**
--------------------

```javascript
// Import express
const express = require('express');

// Import student controller
const studentController = require('./student.controller');

// Create router
const router = express.Router();

// Get all students
router.get('/students', studentController.getStudents);

// Get student by ID
router.get('/students/:id', studentController.getStudent);

// Create new student
router.post('/students', studentController.createStudent);

// Update student
router.put('/students/:id', studentController.updateStudent);

// Delete student
router.delete('/students/:id', studentController.deleteStudent);

// Add academic record
router.post('/students/:id/academic-records', studentController.addAcademicRecord);

// Update academic record
router.put('/students/:id/academic-records/:recordId', studentController.updateAcademicRecord);

// Delete academic record
router.delete('/students/:id/academic-records/:recordId', studentController.deleteAcademicRecord);

// Export router
module.exports = router;
```

**app.js**
------------

```javascript
// Import express
const express = require('express');

// Import mongoose
const mongoose = require('mongoose');

// Import student route
const studentRoute = require('./student.route');

// Create app
const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/escuela-preparatoria')
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.error('Error connecting to MongoDB:', err));

// Use body-parser middleware
app.use(express.json());

// Use student route
app.use('/api', studentRoute);

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```

**package.json**
-----------------

```json
{
  "name": "escuela-preparatoria-api",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^6.7.2",
    "body-parser": "^1.20.2"
  }
}
```
