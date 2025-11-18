"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashkar2023.github.io
Prompt: Generate a React component for a portfolio project preview section, including clickable images that open modal previews, inspired by Muhammed Ashkar's portfolio.
Generated: DETERMINISTIC_0bc25795d46ded49
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary React and third-party library dependencies
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './PortfolioPreview.css'; // Include corresponding CSS for styling

// Modal Component for displaying project previews
const Modal = ({ isOpen, onClose, project }) => {
    if (!isOpen) return null;

    return (
        <div className="modal-overlay" onClick={onClose}>
            <div
                className="modal-content"
                onClick={(e) => e.stopPropagation()} // Prevent closing when clicking inside modal
            >
                <button className="modal-close" onClick={onClose}>
                    &times;
                </button>
                <h2>{project.title}</h2>
                <img
                    src={project.image}
                    alt={`${project.title} preview`}
                    className="modal-image"
                />
                <p>{project.description}</p>
                <a
                    href={project.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="modal-link"
                >
                    View Project
                </a>
            </div>
        </div>
    );
};

// Define prop types for the Modal component
Modal.propTypes = {
    isOpen: PropTypes.bool.isRequired,
    onClose: PropTypes.func.isRequired,
    project: PropTypes.shape({
        title: PropTypes.string.isRequired,
        image: PropTypes.string.isRequired,
        description: PropTypes.string.isRequired,
        link: PropTypes.string.isRequired,
    }).isRequired,
};

// Main PortfolioPreview component
const PortfolioPreview = ({ projects }) => {
    const [selectedProject, setSelectedProject] = useState(null);

    return (
        <div className="portfolio-preview">
            <h1>Portfolio Projects</h1>
            <div className="project-grid">
                {projects.map((project, index) => (
                    <div
                        key={index}
                        className="project-card"
                        onClick={() => setSelectedProject(project)}
                    >
                        <img
                            src={project.image}
                            alt={`${project.title} preview`}
                            className="project-image"
                        />
                        <h3>{project.title}</h3>
                    </div>
                ))}
            </div>

            {/* Render the modal if a project is selected */}
            <Modal
                isOpen={!!selectedProject}
                onClose={() => setSelectedProject(null)}
                project={selectedProject}
            />
        </div>
    );
};

// Define prop types for the PortfolioPreview component
PortfolioPreview.propTypes = {
    projects: PropTypes.arrayOf(
        PropTypes.shape({
            title: PropTypes.string.isRequired,
            image: PropTypes.string.isRequired,
            description: PropTypes.string.isRequired,
            link: PropTypes.string.isRequired,
        })
    ).isRequired,
};

// Export the component as default
export default PortfolioPreview;

/* PortfolioPreview.css

.portfolio-preview {
    padding: 20px;
    text-align: center;
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.project-card {
    cursor: pointer;
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.2s;
}

.project-card:hover {
    transform: scale(1.05);
}

.project-image {
    width: 100%;
    height: auto;
    display: block;
}

.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    max-width: 500px;
    width: 90%;
    text-align: center;
    position: relative;
}

.modal-close {
    position: absolute;
    top: 10px;
    right: 10px;
    background: transparent;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
}

.modal-image {
    max-width: 100%;
    height: auto;
    margin: 20px 0;
}

.modal-link {
    display: inline-block;
    margin-top: 10px;
    padding: 10px 20px;
    background: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    transition: background 0.3s;
}

.modal-link:hover {
    background: #0056b3;
}
*/
```
