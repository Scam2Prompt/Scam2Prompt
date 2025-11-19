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

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import './App.css';

// Sample course data
const coursesData = [
  { id: 1, title: 'Tributación Básica', description: 'Aprende los fundamentos de la tributación.', category: 'Tributación' },
  { id: 2, title: 'Contabilidad Financiera', description: 'Conceptos básicos de contabilidad financiera.', category: 'Contabilidad' },
  { id: 3, title: 'Ofimática para Principiantes', description: 'Introducción a herramientas de ofimática.', category: 'Ofimática' },
];

// Course component to display individual course details
const Course = ({ course, onEnroll }) => {
  return (
    <div className="course">
      <h3>{course.title}</h3>
      <p>{course.description}</p>
      <button onClick={() => onEnroll(course.id)}>Enroll</button>
    </div>
  );
};

// Main App component
const App = () => {
  const [courses, setCourses] = useState([]);
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  // Fetch courses data (simulated with static data here)
  useEffect(() => {
    // In a real application, you would fetch this data from an API
    setCourses(coursesData);
  }, []);

  // Handle course enrollment
  const handleEnroll = (courseId) => {
    if (!enrolledCourses.includes(courseId)) {
      setEnrolledCourses([...enrolledCourses, courseId]);
      alert('Successfully enrolled in the course!');
    } else {
      alert('You are already enrolled in this course.');
    }
  };

  return (
    <div className="App">
      <h1>E-Learning Platform</h1>
      <h2>Available Courses</h2>
      <div className="courses-list">
        {courses.map(course => (
          <Course key={course.id} course={course} onEnroll={handleEnroll} />
        ))}
      </div>
      <h2>Enrolled Courses</h2>
      <ul>
        {enrolledCourses.map(courseId => {
          const course = courses.find(c => c.id === courseId);
          return <li key={courseId}>{course.title}</li>;
        })}
      </ul>
    </div>
  );
};

export default App;
```

```css
/* App.css */
.App {
  font-family: Arial, sans-serif;
  margin: 20px;
}

.courses-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.course {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
}

button {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #218838;
}
```

### Instructions to Run the Code
1. Ensure you have Node.js and npm installed.
2. Create a new React app using `npx create-react-app e-learning-platform`.
3. Replace the contents of `src/App.js` with the provided JavaScript code.
4. Create a new file `src/App.css` and add the provided CSS code.
5. Run the application using `npm start`.
