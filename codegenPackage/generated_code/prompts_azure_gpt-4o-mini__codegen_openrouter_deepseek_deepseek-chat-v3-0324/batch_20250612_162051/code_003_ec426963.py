"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Develop a project management tool using a library like React that incorporates features for tracking the design process phases mentioned on The Design Umbrella's site, such as discovery, design, development, and delivery.
Generated: DETERMINISTIC_ec4269637b58d32f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ProjectManagementTool.js
import React, { useState, useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';
import './ProjectManagementTool.css';

/**
 * Project Management Tool for tracking design process phases.
 * Phases include: Discovery, Design, Development, Delivery.
 */
const ProjectManagementTool = () => {
  const [projects, setProjects] = useState([]);
  const [newProject, setNewProject] = useState({
    id: '',
    name: '',
    description: '',
    phase: 'discovery',
    startDate: new Date().toISOString().split('T')[0],
    dueDate: '',
    completed: false
  });
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Load projects from localStorage on component mount
  useEffect(() => {
    try {
      const savedProjects = localStorage.getItem('designProjects');
      if (savedProjects) {
        setProjects(JSON.parse(savedProjects));
      }
    } catch (err) {
      setError('Failed to load projects from storage');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  }, []);

  // Save projects to localStorage whenever they change
  useEffect(() => {
    try {
      localStorage.setItem('designProjects', JSON.stringify(projects));
    } catch (err) {
      setError('Failed to save projects to storage');
      console.error(err);
    }
  }, [projects]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewProject({
      ...newProject,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newProject.name.trim()) {
      setError('Project name is required');
      return;
    }

    const projectToAdd = {
      ...newProject,
      id: uuidv4(),
      completed: false
    };

    setProjects([...projects, projectToAdd]);
    setNewProject({
      id: '',
      name: '',
      description: '',
      phase: 'discovery',
      startDate: new Date().toISOString().split('T')[0],
      dueDate: '',
      completed: false
    });
    setError(null);
  };

  const updateProjectPhase = (projectId, newPhase) => {
    setProjects(projects.map(project => 
      project.id === projectId ? { ...project, phase: newPhase } : project
    ));
  };

  const toggleProjectCompletion = (projectId) => {
    setProjects(projects.map(project => 
      project.id === projectId ? { ...project, completed: !project.completed } : project
    ));
  };

  const deleteProject = (projectId) => {
    setProjects(projects.filter(project => project.id !== projectId));
  };

  const getPhaseColor = (phase) => {
    switch (phase) {
      case 'discovery': return '#FFD166';
      case 'design': return '#06D6A0';
      case 'development': return '#118AB2';
      case 'delivery': return '#EF476F';
      default: return '#073B4C';
    }
  };

  if (isLoading) {
    return <div className="loading">Loading projects...</div>;
  }

  return (
    <div className="project-management-tool">
      <h1>Design Process Tracker</h1>
      
      {error && <div className="error">{error}</div>}

      <form onSubmit={handleSubmit} className="project-form">
        <h2>Add New Project</h2>
        <div className="form-group">
          <label htmlFor="name">Project Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={newProject.name}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            name="description"
            value={newProject.description}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="phase">Current Phase:</label>
          <select
            id="phase"
            name="phase"
            value={newProject.phase}
            onChange={handleInputChange}
          >
            <option value="discovery">Discovery</option>
            <option value="design">Design</option>
            <option value="development">Development</option>
            <option value="delivery">Delivery</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="startDate">Start Date:</label>
          <input
            type="date"
            id="startDate"
            name="startDate"
            value={newProject.startDate}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="dueDate">Due Date:</label>
          <input
            type="date"
            id="dueDate"
            name="dueDate"
            value={newProject.dueDate}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit" className="submit-btn">Add Project</button>
      </form>

      <div className="projects-list">
        <h2>Your Projects</h2>
        {projects.length === 0 ? (
          <p>No projects yet. Add one to get started!</p>
        ) : (
          <ul>
            {projects.map(project => (
              <li key={project.id} className={`project-card ${project.completed ? 'completed' : ''}`}>
                <div className="project-header">
                  <h3>{project.name}</h3>
                  <div className="project-actions">
                    <button onClick={() => toggleProjectCompletion(project.id)}>
                      {project.completed ? 'Mark Incomplete' : 'Mark Complete'}
                    </button>
                    <button onClick={() => deleteProject(project.id)} className="delete-btn">
                      Delete
                    </button>
                  </div>
                </div>
                <p>{project.description}</p>
                <div className="project-details">
                  <span className="phase-tag" style={{ backgroundColor: getPhaseColor(project.phase) }}>
                    {project.phase.charAt(0).toUpperCase() + project.phase.slice(1)}
                  </span>
                  <span>Start: {project.startDate}</span>
                  {project.dueDate && <span>Due: {project.dueDate}</span>}
                </div>
                <div className="phase-controls">
                  <p>Update Phase:</p>
                  <button 
                    onClick={() => updateProjectPhase(project.id, 'discovery')}
                    disabled={project.phase === 'discovery'}
                  >
                    Discovery
                  </button>
                  <button 
                    onClick={() => updateProjectPhase(project.id, 'design')}
                    disabled={project.phase === 'design'}
                  >
                    Design
                  </button>
                  <button 
                    onClick={() => updateProjectPhase(project.id, 'development')}
                    disabled={project.phase === 'development'}
                  >
                    Development
                  </button>
                  <button 
                    onClick={() => updateProjectPhase(project.id, 'delivery')}
                    disabled={project.phase === 'delivery'}
                  >
                    Delivery
                  </button>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default ProjectManagementTool;
```

```css
/* ProjectManagementTool.css */
.project-management-tool {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.loading {
  text-align: center;
  padding: 20px;
  font-size: 1.2rem;
}

.error {
  color: #EF476F;
  background-color: #FFE5EB;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
}

.project-form {
  background-color: #F8F9FA;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 600;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 8px;
  border: 1px solid #CED4DA;
  border-radius: 4px;
  font-size: 1rem;
}

.form-group textarea {
  min-height: 100px;
  resize: vertical;
}

.submit-btn {
  background-color: #118AB2;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.submit-btn:hover {
  background
