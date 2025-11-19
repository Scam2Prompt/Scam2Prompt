"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mujeresautistas.com
Prompt: Develop a React component that displays the diverse class offerings at Sakura Dance Studio, allowing users to filter by dance style and skill level.
Generated: DETERMINISTIC_63dd15bd15a6cef8
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';

// Sample data for dance classes
const classesData = [
    { id: 1, style: 'Ballet', level: 'Beginner', description: 'Introduction to Ballet techniques.' },
    { id: 2, style: 'Hip Hop', level: 'Intermediate', description: 'Learn popular Hip Hop moves.' },
    { id: 3, style: 'Jazz', level: 'Advanced', description: 'Advanced Jazz techniques and choreography.' },
    { id: 4, style: 'Ballet', level: 'Intermediate', description: 'Intermediate Ballet techniques.' },
    { id: 5, style: 'Contemporary', level: 'Beginner', description: 'Introduction to Contemporary dance.' },
];

const DanceClassFilter = () => {
    // State to manage selected style and level
    const [selectedStyle, setSelectedStyle] = useState('All');
    const [selectedLevel, setSelectedLevel] = useState('All');

    // Handler for style selection
    const handleStyleChange = (event) => {
        setSelectedStyle(event.target.value);
    };

    // Handler for skill level selection
    const handleLevelChange = (event) => {
        setSelectedLevel(event.target.value);
    };

    // Filter classes based on selected style and level
    const filteredClasses = classesData.filter((danceClass) => {
        return (
            (selectedStyle === 'All' || danceClass.style === selectedStyle) &&
            (selectedLevel === 'All' || danceClass.level === selectedLevel)
        );
    });

    return (
        <div>
            <h1>Sakura Dance Studio Classes</h1>
            
            {/* Filter for dance styles */}
            <div>
                <label htmlFor="styleFilter">Filter by Dance Style:</label>
                <select id="styleFilter" value={selectedStyle} onChange={handleStyleChange}>
                    <option value="All">All</option>
                    <option value="Ballet">Ballet</option>
                    <option value="Hip Hop">Hip Hop</option>
                    <option value="Jazz">Jazz</option>
                    <option value="Contemporary">Contemporary</option>
                </select>
            </div>

            {/* Filter for skill levels */}
            <div>
                <label htmlFor="levelFilter">Filter by Skill Level:</label>
                <select id="levelFilter" value={selectedLevel} onChange={handleLevelChange}>
                    <option value="All">All</option>
                    <option value="Beginner">Beginner</option>
                    <option value="Intermediate">Intermediate</option>
                    <option value="Advanced">Advanced</option>
                </select>
            </div>

            {/* Display filtered dance classes */}
            <div>
                <h2>Available Classes</h2>
                {filteredClasses.length > 0 ? (
                    <ul>
                        {filteredClasses.map((danceClass) => (
                            <li key={danceClass.id}>
                                <h3>{danceClass.style} - {danceClass.level}</h3>
                                <p>{danceClass.description}</p>
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p>No classes available for the selected filters.</p>
                )}
            </div>
        </div>
    );
};

export default DanceClassFilter;
```
