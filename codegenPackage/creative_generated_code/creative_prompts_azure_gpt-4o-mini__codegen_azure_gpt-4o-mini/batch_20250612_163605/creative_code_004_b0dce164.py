"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aamctg.edu.bd
Prompt: Construct a REST API endpoint in Node.js to manage student registration for the Alim examination at Ashekane Aulia Fazil Madrasah.
Generated: DETERMINISTIC_b0dce16418e3c7c8
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initializing the Express application
const app = express();

// Middleware
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/alim_exams', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => {
    console.error('MongoDB connection error:', err);
    process.exit(1);
});

// Student Schema
const studentSchema = new mongoose.Schema({
    name: { type: String, required: true },
    rollNumber: { type: String, required: true, unique: true },
    madrasah: { type: String, required: true },
    registrationDate: { type: Date, default: Date.now },
});

// Student Model
const Student = mongoose.model('Student', studentSchema);

// Endpoint to register a new student
app.post('/api/students/register', async (req, res) => {
    try {
        const { name, rollNumber, madrasah } = req.body;

        // Creating a new student instance
        const newStudent = new Student({ name, rollNumber, madrasah });
        
        // Saving the student to the database
        await newStudent.save();
        
        // Sending a success response
        res.status(201).json({
            message: 'Student registered successfully',
            student: newStudent,
        });
    } catch (error) {
        // Handling errors
        console.error('Error during student registration:', error);
        res.status(400).json({
            message: 'Error registering student',
            error: error.message,
        });
    }
});

// Endpoint to get all registered students
app.get('/api/students', async (req, res) => {
    try {
        const students = await Student.find();
        res.status(200).json(students);
    } catch (error) {
        console.error('Error fetching students:', error);
        res.status(500).json({
            message: 'Error fetching students',
            error: error.message,
        });
    }
});

// Starting the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
