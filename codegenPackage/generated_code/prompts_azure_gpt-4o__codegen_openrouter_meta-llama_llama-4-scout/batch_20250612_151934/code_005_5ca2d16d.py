"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: Develop a web application for SMA Rizvi Textile Institute that displays their featured courses and allows students to register online securely.
Generated: DETERMINISTIC_5ca2d16d2b688536
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**SMA Rizvi Textile Institute Web Application**
=====================================================

**Database Schema**
------------------

```sql
CREATE TABLE courses (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  featured BOOLEAN DEFAULT FALSE
);

CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE registrations (
  id INT PRIMARY KEY,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

**Backend API (Node.js and Express)**
--------------------------------------

```javascript
// server.js
const express = require('express');
const app = express();
const mysql = require('mysql');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Database connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'sma_rizvi_textile_institute'
});

db.connect((err) => {
  if (err) {
    console.error('error connecting:', err);
    return;
  }
  console.log('connected as id ' + db.threadId);
});

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Get featured courses
app.get('/api/courses', (req, res) => {
  const query = 'SELECT * FROM courses WHERE featured = TRUE';
  db.query(query, (err, results) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error fetching courses' });
    } else {
      res.send(results);
    }
  });
});

// Register student
app.post('/api/register', (req, res) => {
  const { name, email, password } = req.body;
  const hashedPassword = bcrypt.hashSync(password, 10);
  const query = 'INSERT INTO students SET ?';
  db.query(query, { name, email, password: hashedPassword }, (err, results) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error registering student' });
    } else {
      res.send({ message: 'Student registered successfully' });
    }
  });
});

// Login student
app.post('/api/login', (req, res) => {
  const { email, password } = req.body;
  const query = 'SELECT * FROM students WHERE email = ?';
  db.query(query, [email], (err, results) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error logging in' });
    } else if (results.length === 0) {
      res.status(401).send({ message: 'Invalid email or password' });
    } else {
      const student = results[0];
      if (bcrypt.compareSync(password, student.password)) {
        const token = jwt.sign({ studentId: student.id }, 'secret_key', {
          expiresIn: '1h'
        });
        res.send({ token });
      } else {
        res.status(401).send({ message: 'Invalid email or password' });
      }
    }
  });
});

// Register for course
app.post('/api/register-course', authenticateToken, (req, res) => {
  const { courseId } = req.body;
  const studentId = req.studentId;
  const query = 'INSERT INTO registrations SET ?';
  db.query(query, { studentId, courseId }, (err, results) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error registering for course' });
    } else {
      res.send({ message: 'Registered for course successfully' });
    }
  });
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (token) {
    jwt.verify(token, 'secret_key', (err, decoded) => {
      if (err) {
        res.status(401).send({ message: 'Invalid token' });
      } else {
        req.studentId = decoded.studentId;
        next();
      }
    });
  } else {
    res.status(401).send({ message: 'No token provided' });
  }
}

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
```

**Frontend (React)**
--------------------

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [courses, setCourses] = useState([]);
  const [registeredCourses, setRegisteredCourses] = useState([]);
  const [student, setStudent] = useState({});

  useEffect(() => {
    axios.get('/api/courses')
      .then(response => {
        setCourses(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleRegister = (courseId) => {
    axios.post('/api/register-course', { courseId }, {
      headers: {
        Authorization: localStorage.getItem('token')
      }
    })
      .then(response => {
        setRegisteredCourses([...registeredCourses, courseId]);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleLogin = (email, password) => {
    axios.post('/api/login', { email, password })
      .then(response => {
        localStorage.setItem('token', response.data.token);
        setStudent({ email });
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleRegisterStudent = (name, email, password) => {
    axios.post('/api/register', { name, email, password })
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Courses</h1>
      <ul>
        {courses.map(course => (
          <li key={course.id}>
            {course.name}
            <button onClick={() => handleRegister(course.id)}>Register</button>
          </li>
        ))}
      </ul>
      <h1>Login</h1>
      <form onSubmit={(e) => {
        e.preventDefault();
        handleLogin(e.target.email.value, e.target.password.value);
      }}>
        <input type="email" name="email" placeholder="Email" />
        <input type="password" name="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
      <h1>Register</h1>
      <form onSubmit={(e) => {
        e.preventDefault();
        handleRegisterStudent(e.target.name.value, e.target.email.value, e.target.password.value);
      }}>
        <input type="text" name="name" placeholder="Name" />
        <input type="email" name="email" placeholder="Email" />
        <input type="password" name="password" placeholder="Password" />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default App;
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SMA Rizvi Textile Institute</title>
</head>
<body>
  <div id="root"></div>
  <script src="index.js"></script>
</body>
</html>
```
