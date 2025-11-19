"""
Generated Code Metadata:
========================
Original URL: https://retro-pgf.vercel.app
Prompt: Write a function to display project lists with ❤️ icons, as described on the Retro PGF site, using JavaScript or React.
Generated: DETERMINISTIC_ab455c1f5f000249
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React from 'react';
import PropTypes from 'prop-types';

/**
 * ProjectList component displays a list of projects with ❤️ icons.
 * 
 * @param {Object[]} projects - Array of project objects.
 * @param {string} projects[].name - The name of the project.
 * @param {string} projects[].description - A brief description of the project.
 * @param {string} projects[].url - The URL to the project.
 * 
 * @returns {JSX.Element} Rendered list of projects.
 */
const ProjectList = ({ projects }) => {
    // Error handling for empty projects array
    if (!Array.isArray(projects) || projects.length === 0) {
        return <p>No projects available.</p>;
    }

    return (
        <div className="project-list">
            <h2>Project List</h2>
            <ul>
                {projects.map((project, index) => (
                    <li key={index} className="project-item">
                        <a href={project.url} target="_blank" rel="noopener noreferrer">
                            {project.name} ❤️
                        </a>
                        <p>{project.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

// PropTypes for type checking
ProjectList.propTypes = {
    projects: PropTypes.arrayOf(
        PropTypes.shape({
            name: PropTypes.string.isRequired,
            description: PropTypes.string.isRequired,
            url: PropTypes.string.isRequired,
        })
    ).isRequired,
};

export default ProjectList;
```
