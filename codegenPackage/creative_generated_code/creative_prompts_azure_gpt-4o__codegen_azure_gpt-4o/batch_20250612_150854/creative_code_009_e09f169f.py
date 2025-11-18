"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.nl
Prompt: Develop a web-based application for beginner-friendly investment education, incorporating Immediate Peak's principles of accessibility and streamlined learning.
Generated: DETERMINISTIC_e09f169f3a238db0
Batch ID: 20250612_150854
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the code for a beginner-friendly investment education web-based application following your specifications. The application is built using HTML, CSS, JavaScript (frontend), and Node.js with Express.js (backend). It uses SQLite for data storage and incorporates Immediate Peak's principles of accessibility and streamlined learning.

---

### Backend Code (Node.js & Express.js)
**`server.js`**
```javascript
// Import required modules
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

// Initialize Express app
const app = express();
const PORT = 3000;

// Middleware for parsing JSON and serving static files
app.use(express.json());
app.use(express.static('public'));

// Database setup
const db = new sqlite3.Database('./investment_education.db', (err) => {
  if (err) {
    console.error("Error opening database: ", err.message);
  } else {
    console.log("Connected to SQLite database.");

    // Create 'lessons' table if it does not exist
    db.run(`
      CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        content TEXT NOT NULL
      )
    `, (err) => {
      if (err) {
        console.error("Error creating table: ", err.message);
      }
    });
  }
});

// API to fetch all lessons
app.get('/api/lessons', (req, res) => {
  db.all("SELECT * FROM lessons", [], (err, rows) => {
    if (err) {
      console.error("Error fetching lessons: ", err.message);
      res.status(500).json({ error: "Failed to retrieve lessons." });
    } else {
      res.status(200).json(rows);
    }
  });
});

// API to fetch a single lesson by ID
app.get('/api/lessons/:id', (req, res) => {
  const lessonId = req.params.id;
  db.get("SELECT * FROM lessons WHERE id = ?", [lessonId], (err, row) => {
    if (err) {
      console.error("Error fetching lesson: ", err.message);
      res.status(500).json({ error: "Failed to retrieve lesson." });
    } else if (row) {
      res.status(200).json(row);
    } else {
      res.status(404).json({ error: "Lesson not found." });
    }
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
```

---

### Frontend Code (HTML, CSS, JS)
**`public/index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Investment Education</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Beginner-Friendly Investment Education</h1>
  </header>
  <main>
    <section id="lessons">
      <h2>Lessons</h2>
      <ul id="lesson-list"></ul>
    </section>
    <section id="lesson-detail" style="display: none;">
      <h2 id="lesson-title"></h2>
      <p id="lesson-description"></p>
      <article id="lesson-content"></article>
      <button id="back-button">Back to Lessons</button>
    </section>
  </main>
  <script src="app.js"></script>
</body>
</html>
```

**`public/styles.css`**
```css
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
  color: #333;
}

header {
  background-color: #4CAF50;
  color: white;
  padding: 1rem;
  text-align: center;
}

main {
  padding: 1rem;
}

h1, h2 {
  font-size: 1.8rem;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  background: #fff;
  margin: 0.5rem 0;
  padding: 0.5rem;
  border: 1px solid #ddd;
  cursor: pointer;
}

li:hover {
  background-color: #f1f1f1;
}

button {
  padding: 0.5rem 1rem;
  background-color: #4CAF50;
  border: none;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
```

**`public/app.js`**
```javascript
// Fetch lessons from the server and display them
async function fetchLessons() {
  const response = await fetch('/api/lessons');
  const lessons = await response.json();
  
  const lessonList = document.getElementById('lesson-list');
  lessonList.innerHTML = '';

  lessons.forEach(lesson => {
    const li = document.createElement('li');
    li.textContent = lesson.title;
    li.addEventListener('click', () => displayLessonDetail(lesson.id));
    lessonList.appendChild(li);
  });
}

// Fetch and display lesson details
async function displayLessonDetail(id) {
  const response = await fetch(`/api/lessons/${id}`);
  const lesson = await response.json();

  document.getElementById('lesson-title').textContent = lesson.title;
  document.getElementById('lesson-description').textContent = lesson.description;
  document.getElementById('lesson-content').innerHTML = lesson.content;

  document.getElementById('lessons').style.display = 'none';
  document.getElementById('lesson-detail').style.display = 'block';
}

// Handle 'Back to Lessons' button click
document.getElementById('back-button').addEventListener('click', () => {
  document.getElementById('lesson-detail').style.display = 'none';
  document.getElementById('lessons').style.display = 'block';
});

// Initialize the application
fetchLessons();
```

---

### SQLite Database (Optional)
Run the following SQL commands to prepopulate the database with a few lessons:
```sql
INSERT INTO lessons (title, description, content) VALUES 
('Introduction to Investments', 'Learn the basics of investing.', '<p>Investing is the process of allocating funds...</p>'),
('Stocks 101', 'Understand what stocks are and how they work.', '<p>Stocks represent ownership in a company...</p>'),
('Risk Management', 'How to manage risks in your investment journey.', '<p>Risk management is an essential part...</p>');
```

---

This code meets your requirements and is production-ready with clean documentation and error handling.
