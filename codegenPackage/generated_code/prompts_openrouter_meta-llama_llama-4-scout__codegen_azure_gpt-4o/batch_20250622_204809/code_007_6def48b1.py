"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: "Implement a simple e-learning platform using a framework like React or Angular that allows users to browse and enroll in courses related to tributación, contabilidad, and ofimática."
Generated: DETERMINISTIC_6def48b1135ae3a9
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is a simple implementation of an e-learning platform using React. This code includes components for browsing and enrolling in courses related to "tributación," "contabilidad," and "ofimática."

```javascript
// File: App.js
import React from "react";
import CourseList from "./components/CourseList";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>E-Learning Platform</h1>
        <p>Browse and enroll in courses related to Tributación, Contabilidad, and Ofimática.</p>
      </header>
      <main>
        <CourseList />
      </main>
    </div>
  );
}

export default App;
```

```javascript
// File: components/CourseList.js
import React, { useState } from "react";
import CourseCard from "./CourseCard";

// Sample course data
const courses = [
  { id: 1, title: "Introduction to Tributación", category: "Tributación" },
  { id: 2, title: "Advanced Contabilidad", category: "Contabilidad" },
  { id: 3, title: "Mastering Ofimática Tools", category: "Ofimática" },
  { id: 4, title: "Tributación for Small Businesses", category: "Tributación" },
  { id: 5, title: "Contabilidad Basics", category: "Contabilidad" },
];

function CourseList() {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  // Handle course enrollment
  const handleEnroll = (course) => {
    if (!enrolledCourses.find((c) => c.id === course.id)) {
      setEnrolledCourses([...enrolledCourses, course]);
      alert(`You have enrolled in "${course.title}"`);
    } else {
      alert(`You are already enrolled in "${course.title}"`);
    }
  };

  return (
    <div>
      <h2>Available Courses</h2>
      <div className="course-list">
        {courses.map((course) => (
          <CourseCard key={course.id} course={course} onEnroll={handleEnroll} />
        ))}
      </div>
      <h2>Enrolled Courses</h2>
      <ul>
        {enrolledCourses.map((course) => (
          <li key={course.id}>{course.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default CourseList;
```

```javascript
// File: components/CourseCard.js
import React from "react";
import PropTypes from "prop-types";

function CourseCard({ course, onEnroll }) {
  return (
    <div className="course-card">
      <h3>{course.title}</h3>
      <p>Category: {course.category}</p>
      <button onClick={() => onEnroll(course)}>Enroll</button>
    </div>
  );
}

CourseCard.propTypes = {
  course: PropTypes.shape({
    id: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    category: PropTypes.string.isRequired,
  }).isRequired,
  onEnroll: PropTypes.func.isRequired,
};

export default CourseCard;
```

```css
/* File: App.css */
.App {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 0 auto;
  padding: 20px;
  max-width: 800px;
}

.App-header {
  background-color: #282c34;
  color: white;
  padding: 20px;
  border-radius: 8px;
}

.course-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
  margin: 20px 0;
}

.course-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 15px;
  width: 250px;
  text-align: left;
}

.course-card h3 {
  margin: 0 0 10px;
}

.course-card button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 4px;
  cursor: pointer;
}

.course-card button:hover {
  background-color: #0056b3;
}
```

```javascript
// File: index.js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import "./index.css";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
```

```css
/* File: index.css */
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 5px 0;
}
```

### Notes:
- This implementation uses React functional components and hooks (`useState`) for state management.
- The app is styled with basic CSS for simplicity.
- Error handling is minimal (e.g., preventing duplicate enrollments).
- To run this code, ensure you have a React environment set up (e.g., using `create-react-app`).
