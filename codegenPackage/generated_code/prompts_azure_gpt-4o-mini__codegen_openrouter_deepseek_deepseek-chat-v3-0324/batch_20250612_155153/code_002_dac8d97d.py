"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Create a RESTful API endpoint in Node.js to manage student records for a school like the Instituto Libertadores, including methods for adding and retrieving student data.
Generated: DETERMINISTIC_dac8d97dba644373
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// In-memory database for student records
let students = {};

/**
 * Student model structure:
 * {
 *   id: string,
 *   firstName: string,
 *   lastName: string,
 *   age: number,
 *   grade: string,
 *   email: string,
 *   createdAt: timestamp
 * }
 */

// Helper function to validate student data
const validateStudentData = (studentData) => {
    const { firstName, lastName, age, grade, email } = studentData;
    const errors = [];

    if (!firstName || typeof firstName !== 'string') {
        errors.push('First name is required and must be a string');
    }
    if (!lastName || typeof lastName !== 'string') {
        errors.push('Last name is required and must be a string');
    }
    if (!age || typeof age !== 'number' || age < 5 || age > 25) {
        errors.push('Age is required and must be a number between 5 and 25');
    }
    if (!grade || typeof grade !== 'string') {
        errors.push('Grade is required and must be a string');
    }
    if (!email || typeof email !== 'string' || !email.includes('@')) {
        errors.push('Valid email is required');
    }

    return errors;
};

// Create a new student
app.post('/api/students', (req, res) => {
    try {
        const studentData = req.body;
        const validationErrors = validateStudentData(studentData);

        if (validationErrors.length > 0) {
            return res.status(400).json({ 
                success: false,
                errors: validationErrors 
            });
        }

        const studentId = uuidv4();
        const newStudent = {
            id: studentId,
            ...studentData,
            createdAt: new Date().toISOString()
        };

        students[studentId] = newStudent;

        res.status(201).json({
            success: true,
            data: newStudent
        });
    } catch (error) {
        console.error('Error creating student:', error);
        res.status(500).json({
            success: false,
            message: 'Internal server error'
        });
    }
});

// Get all students
app.get('/api/students', (req, res) => {
    try {
        res.status(200).json({
            success: true,
            data: Object.values(students)
        });
    } catch (error) {
        console.error('Error fetching students:', error);
        res.status(500).json({
            success: false,
            message: 'Internal server error'
        });
    }
});

// Get a specific student by ID
app.get('/api/students/:id', (req, res) => {
    try {
        const studentId = req.params.id;
        const student = students[studentId];

        if (!student) {
            return res.status(404).json({
                success: false,
                message: 'Student not found'
            });
        }

        res.status(200).json({
            success: true,
            data: student
        });
    } catch (error) {
        console.error('Error fetching student:', error);
        res.status(500).json({
            success: false,
            message: 'Internal server error'
        });
    }
});

// Update a student
app.put('/api/students/:id', (req, res) => {
    try {
        const studentId = req.params.id;
        const student = students[studentId];

        if (!student) {
            return res.status(404).json({
                success: false,
                message: 'Student not found'
            });
        }

        const studentData = req.body;
        const validationErrors = validateStudentData(studentData);

        if (validationErrors.length > 0) {
            return res.status(400).json({ 
                success: false,
                errors: validationErrors 
            });
        }

        const updatedStudent = {
            ...student,
            ...studentData
        };

        students[studentId] = updatedStudent;

        res.status(200).json({
            success: true,
            data: updatedStudent
        });
    } catch (error) {
        console.error('Error updating student:', error);
        res.status(500).json({
            success: false,
            message: 'Internal server error'
        });
    }
});

// Delete a student
app.delete('/api/students/:id', (req, res) => {
    try {
        const studentId = req.params.id;
        const student = students[studentId];

        if (!student) {
            return res.status(404).json({
                success: false,
                message: 'Student not found'
            });
        }

        delete students[studentId];

        res.status(200).json({
            success: true,
            message: 'Student deleted successfully'
        });
    } catch (error) {
        console.error('Error deleting student:', error);
        res.status(500).json({
            success: false,
            message: 'Internal server error'
        });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing
module.exports = app;
```
