"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Recommend APIs or libraries for creating a web-based personal branding portfolio, including tools for integrating client testimonials and project showcases, as outlined in the КарьераОнлайн module on building a personal brand.
Generated: DETERMINISTIC_66f2a5f4a0b39df2
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: portfolio.js
// This script manages the web-based personal branding portfolio features

// Importing required libraries
import express from 'express'; // Web framework for Node.js
import mongoose from 'mongoose'; // MongoDB object modeling tool
import bodyParser from 'body-parser'; // Middleware for parsing request bodies
import dotenv from 'dotenv'; // Loads environment variables from .env file
import cors from 'cors'; // Middleware for enabling CORS

// Load environment variables
dotenv.config();

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all requests
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log("Connected to MongoDB");
}).catch((error) => {
    console.error("Error connecting to MongoDB:", error);
});

// Define a schema for testimonials
const testimonialSchema = new mongoose.Schema({
    name: { type: String, required: true },
    content: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
});

// Create a model for testimonials
const Testimonial = mongoose.model('Testimonial', testimonialSchema);

// API route to add a new testimonial
app.post('/api/testimonials', async (req, res) => {
    try {
        const { name, content } = req.body;
        const newTestimonial = new Testimonial({ name, content });
        await newTestimonial.save();
        res.status(201).json(newTestimonial);
    } catch (error) {
        console.error("Error adding testimonial:", error);
        res.status(500).json({ message: "Internal Server Error" });
    }
});

// API route to get all testimonials
app.get('/api/testimonials', async (req, res) => {
    try {
        const testimonials = await Testimonial.find();
        res.status(200).json(testimonials);
    } catch (error) {
        console.error("Error fetching testimonials:", error);
        res.status(500).json({ message: "Internal Server Error" });
    }
});

// Define a schema for projects
const projectSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    url: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
});

// Create a model for projects
const Project = mongoose.model('Project', projectSchema);

// API route to add a new project
app.post('/api/projects', async (req, res) => {
    try {
        const { title, description, url } = req.body;
        const newProject = new Project({ title, description, url });
        await newProject.save();
        res.status(201).json(newProject);
    } catch (error) {
        console.error("Error adding project:", error);
        res.status(500).json({ message: "Internal Server Error" });
    }
});

// API route to get all projects
app.get('/api/projects', async (req, res) => {
    try {
        const projects = await Project.find();
        res.status(200).json(projects);
    } catch (error) {
        console.error("Error fetching projects:", error);
        res.status(500).json({ message: "Internal Server Error" });
    }
});

// Start the server
const PORT = process.env.PORT || 5000; // Default to port 5000
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Environment Setup
```dotenv
// File: .env
MONGODB_URI=mongodb://localhost:27017/portfolio
PORT=5000
```

### Usage
- Install necessary packages: 
```bash
npm install express mongoose body-parser dotenv cors
```
- Run the server:
```bash
node portfolio.js
``` 

This code creates a simple web-based personal branding portfolio API using Express and MongoDB, allowing for the addition and retrieval of client testimonials and project showcases.
