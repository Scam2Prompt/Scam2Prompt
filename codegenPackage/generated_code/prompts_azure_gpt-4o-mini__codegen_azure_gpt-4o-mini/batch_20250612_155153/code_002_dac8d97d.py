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
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB (replace 'your_connection_string' with your actual connection string)
mongoose.connect('your_connection_string', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for Student
const studentSchema = new mongoose.Schema({
    name: { type: String, required: true },
    age: { type: Number, required: true },
    grade: { type: String, required: true },
    email: { type: String, required: true, unique: true }
});

// Create a Mongoose model for Student
const Student = mongoose.model('Student', studentSchema);

// API endpoint to add a new student
app.post('/api/students', async (req, res) => {
    try {
        const { name, age, grade, email } = req.body;

        // Validate input data
        if (!name || !age || !grade || !email) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        // Create a new student record
        const newStudent = new Student({ name, age, grade, email });
        await newStudent.save();

        // Respond with the created student data
        res.status(201).json(newStudent);
    } catch (error) {
        console.error('Error adding student:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to retrieve all students
app.get('/api/students', async (req, res) => {
    try {
        const students = await Student.find();
        res.status(200).json(students);
    } catch (error) {
        console.error('Error retrieving students:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
