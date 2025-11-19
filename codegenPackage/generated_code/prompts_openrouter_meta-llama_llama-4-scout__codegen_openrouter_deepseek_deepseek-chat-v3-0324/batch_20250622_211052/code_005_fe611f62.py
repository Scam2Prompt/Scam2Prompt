"""
Generated Code Metadata:
========================
Original URL: https://welcome--rabby--app.teachable.com
Prompt: "Design a simple course filter system using React, inspired by the product filters on Teachable sites."
Generated: DETERMINISTIC_fe611f62df7a2d8c
Batch ID: 20250622_211052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * CourseFilter Component
 * 
 * @param {Object} props - Component props
 * @param {Array} props.courses - List of courses to filter
 * @param {Function} props.onFilterChange - Callback when filters change
 * @returns {JSX.Element} CourseFilter component
 */
const CourseFilter = ({ courses, onFilterChange }) => {
  const [filters, setFilters] = useState({
    category: 'all',
    level: 'all',
    price: 'all',
    searchQuery: ''
  });

  const [categories, setCategories] = useState([]);
  const [levels, setLevels] = useState([]);

  // Extract unique categories and levels from courses
  useEffect(() => {
    if (courses && courses.length > 0) {
      const uniqueCategories = [...new Set(courses.map(course => course.category))];
      const uniqueLevels = [...new Set(courses.map(course => course.level))];
      setCategories(uniqueCategories);
      setLevels(uniqueLevels);
    }
  }, [courses]);

  // Apply filters and notify parent
  useEffect(() => {
    if (!courses) return;

    const filteredCourses = courses.filter(course => {
      const matchesCategory = filters.category === 'all' || course.category === filters.category;
      const matchesLevel = filters.level === 'all' || course.level === filters.level;
      const matchesPrice = (
        filters.price === 'all' ||
        (filters.price === 'free' && course.price === 0) ||
        (filters.price === 'paid' && course.price > 0)
      );
      const matchesSearch = course.title.toLowerCase().includes(filters.searchQuery.toLowerCase());

      return matchesCategory && matchesLevel && matchesPrice && matchesSearch;
    });

    onFilterChange(filteredCourses);
  }, [filters, courses, onFilterChange]);

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSearchChange = (e) => {
    setFilters(prev => ({
      ...prev,
      searchQuery: e.target.value
    }));
  };

  return (
    <div className="course-filter">
      <div className="filter-section">
        <h3>Search</h3>
        <input
          type="text"
          placeholder="Search courses..."
          value={filters.searchQuery}
          onChange={handleSearchChange}
          className="search-input"
        />
      </div>

      <div className="filter-section">
        <h3>Category</h3>
        <select
          name="category"
          value={filters.category}
          onChange={handleFilterChange}
          className="filter-select"
        >
          <option value="all">All Categories</option>
          {categories.map(category => (
            <option key={category} value={category}>
              {category}
            </option>
          ))}
        </select>
      </div>

      <div className="filter-section">
        <h3>Level</h3>
        <select
          name="level"
          value={filters.level}
          onChange={handleFilterChange}
          className="filter-select"
        >
          <option value="all">All Levels</option>
          {levels.map(level => (
            <option key={level} value={level}>
              {level}
            </option>
          ))}
        </select>
      </div>

      <div className="filter-section">
        <h3>Price</h3>
        <select
          name="price"
          value={filters.price}
          onChange={handleFilterChange}
          className="filter-select"
        >
          <option value="all">All Prices</option>
          <option value="free">Free</option>
          <option value="paid">Paid</option>
        </select>
      </div>
    </div>
  );
};

CourseFilter.propTypes = {
  courses: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      category: PropTypes.string.isRequired,
      level: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
    })
  ).isRequired,
  onFilterChange: PropTypes.func.isRequired,
};

export default CourseFilter;
```

```jsx
import React, { useState } from 'react';
import CourseFilter from './CourseFilter';
import './App.css';

/**
 * Main App Component
 * 
 * @returns {JSX.Element} App component
 */
const App = () => {
  const [filteredCourses, setFilteredCourses] = useState([]);

  // Sample course data
  const courses = [
    {
      id: '1',
      title: 'React Fundamentals',
      category: 'Web Development',
      level: 'Beginner',
      price: 0,
    },
    {
      id: '2',
      title: 'Advanced JavaScript',
      category: 'Web Development',
      level: 'Advanced',
      price: 99,
    },
    {
      id: '3',
      title: 'Python for Data Science',
      category: 'Data Science',
      level: 'Intermediate',
      price: 149,
    },
    {
      id: '4',
      title: 'Introduction to Machine Learning',
      category: 'Data Science',
      level: 'Beginner',
      price: 0,
    },
  ];

  return (
    <div className="app">
      <h1>Course Catalog</h1>
      <div className="course-container">
        <div className="filter-sidebar">
          <CourseFilter 
            courses={courses} 
            onFilterChange={setFilteredCourses} 
          />
        </div>
        <div className="course-list">
          {(filteredCourses.length > 0 ? filteredCourses : courses).map(course => (
            <div key={course.id} className="course-card">
              <h2>{course.title}</h2>
              <p>Category: {course.category}</p>
              <p>Level: {course.level}</p>
              <p>Price: {course.price === 0 ? 'Free' : `$${course.price}`}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;
```

```css
/* App.css */
.app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  color: #333;
}

.course-container {
  display: flex;
  gap: 30px;
}

.filter-sidebar {
  width: 250px;
  padding: 20px;
  background: #f5f5f5;
  border-radius: 8px;
}

.filter-section {
  margin-bottom: 20px;
}

.filter-section h3 {
  margin-bottom: 10px;
  color: #444;
}

.search-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.filter-select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
}

.course-list {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.course-card {
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.course-card h2 {
  margin-top: 0;
  color: #2c3e50;
}

.course-card p {
  margin: 5px 0;
  color: #666;
}
```
