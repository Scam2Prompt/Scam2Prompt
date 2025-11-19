"""
Generated Code Metadata:
========================
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Generate JavaScript code for implementing a "Sort by" dropdown menu for an online course platform, as seen in the rabbie-wall--extension-docs interface.
Generated: DETERMINISTIC_61113d3f13992763
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SortByDropdown.js

/**
 * SortByDropdown component for sorting courses.
 * 
 * @param {Object} props 
 * @param {Array} props.courses - List of courses to be sorted.
 * @param {String} props.defaultSort - Default sort option.
 * @param {Function} props.onSortChange - Callback function for sort change.
 */

function SortByDropdown({ courses, defaultSort, onSortChange }) {
    // Define sort options
    const sortOptions = [
        { value: 'title-asc', label: 'Title (A-Z)' },
        { value: 'title-desc', label: 'Title (Z-A)' },
        { value: 'price-asc', label: 'Price (Low-High)' },
        { value: 'price-desc', label: 'Price (High-Low)' },
        { value: 'rating-desc', label: 'Rating (High-Low)' },
    ];

    // State to store selected sort option
    const [selectedSort, setSelectedSort] = React.useState(defaultSort);

    // Handle sort change
    const handleSortChange = (event) => {
        const newSort = event.target.value;
        setSelectedSort(newSort);
        onSortChange(newSort);
    };

    // Sort courses based on selected sort option
    const sortedCourses = React.useMemo(() => {
        if (!courses) return [];

        switch (selectedSort) {
            case 'title-asc':
                return courses.sort((a, b) => a.title.localeCompare(b.title));
            case 'title-desc':
                return courses.sort((a, b) => b.title.localeCompare(a.title));
            case 'price-asc':
                return courses.sort((a, b) => a.price - b.price);
            case 'price-desc':
                return courses.sort((a, b) => b.price - a.price);
            case 'rating-desc':
                return courses.sort((a, b) => b.rating - a.rating);
            default:
                return courses;
        }
    }, [courses, selectedSort]);

    return (
        <div className="sort-by-dropdown">
            <label>Sort by:</label>
            <select value={selectedSort} onChange={handleSortChange}>
                {sortOptions.map((option) => (
                    <option key={option.value} value={option.value}>
                        {option.label}
                    </option>
                ))}
            </select>
        </div>
    );
}

export default SortByDropdown;
```

```javascript
// App.js

import React, { useState } from 'react';
import SortByDropdown from './SortByDropdown';

function App() {
    // Sample courses data
    const [courses, setCourses] = useState([
        { title: 'Course 1', price: 100, rating: 4.5 },
        { title: 'Course 2', price: 200, rating: 4.8 },
        { title: 'Course 3', price: 50, rating: 4.2 },
    ]);

    // Default sort option
    const [defaultSort, setDefaultSort] = useState('title-asc');

    // Callback function for sort change
    const handleSortChange = (newSort) => {
        setDefaultSort(newSort);
    };

    return (
        <div className="app">
            <SortByDropdown
                courses={courses}
                defaultSort={defaultSort}
                onSortChange={handleSortChange}
            />
            <ul>
                {courses.map((course) => (
                    <li key={course.title}>
                        {course.title} - ${course.price} - {course.rating}/5
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
```
