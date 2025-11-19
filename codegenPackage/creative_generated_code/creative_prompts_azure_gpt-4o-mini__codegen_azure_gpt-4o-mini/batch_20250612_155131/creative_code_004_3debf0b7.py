"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abelltodoit.com.au
Prompt: Illustrate how to structure a web application using the file organization seen in the abelltodoit.com.au index.
Generated: DETERMINISTIC_3debf0b79369a676
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```plaintext
my_web_app/
├── app/
│   ├── controllers/
│   │   ├── todoController.js
│   ├── models/
│   │   ├── todoModel.js
│   ├── views/
│   │   ├── index.ejs
│   │   ├── layout.ejs
│   └── routes/
│       ├── todoRoutes.js
├── config/
│   ├── db.js
│   └── appConfig.js
├── public/
│   ├── css/
│   │   ├── styles.css
│   ├── js/
│   │   ├── scripts.js
│   └── images/
├── tests/
│   ├── todo.test.js
├── .env
├── .gitignore
├── package.json
├── server.js
└── README.md
```

```javascript
// server.js
const express = require('express');
const mongoose = require('mongoose');
const todoRoutes = require('./app/routes/todoRoutes');
const appConfig = require('./config/appConfig');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Create an Express application
const app = express();

// Middleware to parse JSON requests
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Set view engine to EJS
app.set('view engine', 'ejs');

// Serve static files from the public directory
app.use(express.static('public'));

// Connect to MongoDB database
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('Database connection error:', err));

// Define routes
app.use('/api/todos', todoRoutes);

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

```javascript
// config/db.js
const mongoose = require('mongoose');

const connectDB = async () => {
    try {
        await mongoose.connect(process.env.MONGODB_URI, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        });
        console.log('MongoDB connected');
    } catch (error) {
        console.error('Database connection error:', error);
        process.exit(1); // Exit process with failure
    }
};

module.exports = connectDB;
```

```javascript
// config/appConfig.js
module.exports = {
    appName: 'My Todo App',
    version: '1.0.0',
};
```

```javascript
// app/models/todoModel.js
const mongoose = require('mongoose');

// Define a schema for todos
const TodoSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
    },
    completed: {
        type: Boolean,
        default: false,
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

// Create a model for todos
const Todo = mongoose.model('Todo', TodoSchema);

module.exports = Todo;
```

```javascript
// app/controllers/todoController.js
const Todo = require('../models/todoModel');

/**
 * Get all todos
 */
const getAllTodos = async (req, res) => {
    try {
        const todos = await Todo.find();
        res.status(200).json(todos);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching todos', error });
    }
};

/**
 * Create a new todo
 */
const createTodo = async (req, res) => {
    const { title } = req.body;

    if (!title) {
        return res.status(400).json({ message: 'Title is required' });
    }

    const todo = new Todo({
        title,
    });

    try {
        const savedTodo = await todo.save();
        res.status(201).json(savedTodo);
    } catch (error) {
        res.status(500).json({ message: 'Error creating todo', error });
    }
};

module.exports = {
    getAllTodos,
    createTodo,
};
```

```javascript
// app/routes/todoRoutes.js
const express = require('express');
const { getAllTodos, createTodo } = require('../controllers/todoController');

const router = express.Router();

// Route to get all todos
router.get('/', getAllTodos);

// Route to create a new todo
router.post('/', createTodo);

module.exports = router;
```

```html
<!-- app/views/layout.ejs -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><%= appName %></title>
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
    <div class="container">
        <%- body %>
    </div>
    <script src="/js/scripts.js"></script>
</body>
</html>
```

```html
<!-- app/views/index.ejs -->
<% layout('layout') -%>
<h1>Welcome to <%= appName %></h1>
<!-- Add your HTML content here -->
```

```javascript
// public/js/scripts.js
// This file can include client-side JavaScript for your web application

console.log('Client-side JavaScript loaded');
```

```css
/* public/css/styles.css */
/* Add your CSS styles here */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}
```

```plaintext
// tests/todo.test.js
const request = require('supertest');
const app = require('../server');

describe('Todo API', () => {
    it('should get all todos', async () => {
        const res = await request(app).get('/api/todos');
        expect(res.statusCode).toEqual(200);
    });

    it('should create a new todo', async () => {
        const res = await request(app).post('/api/todos').send({ title: 'Test Todo' });
        expect(res.statusCode).toEqual(201);
        expect(res.body).toHaveProperty('title', 'Test Todo');
    });
});
```

```plaintext
// .env
MONGODB_URI=mongodb://localhost:27017/my_todo_app
PORT=3000
```

```plaintext
// .gitignore
node_modules
.env
```

```json
// package.json
{
  "name": "my_web_app",
  "version": "1.0.0",
  "description": "A simple todo web application",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongoose": "^5.10.9",
    "dotenv": "^8.2.0",
    "ejs": "^3.1.6",
    "supertest": "^6.1.0"
  },
  "devDependencies": {
    "jest": "^26.6.3"
  }
}
```

```plaintext
// README.md
# My Todo App

A simple web application for managing todos.

## Installation

1. Clone the repository.
2. Run `npm install` to install the dependencies.
3. Create a `.env` file based on the provided `.env` template.
4. Run `npm start` to start the server.

## Running Tests

Run `npm test` to execute the tests.
```
