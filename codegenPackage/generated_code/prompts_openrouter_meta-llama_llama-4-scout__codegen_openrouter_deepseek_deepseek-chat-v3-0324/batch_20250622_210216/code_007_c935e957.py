"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-minetrix.web.app
Prompt: Create a ReactJS component to display the Bitcoin Minetrix roadmap, showing the different phases of the project and their corresponding milestones.
Generated: DETERMINISTIC_c935e957c9b451d2
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React from 'react';
import PropTypes from 'prop-types';
import './Roadmap.css';

/**
 * Represents a single phase in the Bitcoin Minetrix roadmap.
 * @param {Object} props - The component props.
 * @param {string} props.title - The title of the phase.
 * @param {string} props.description - The description of the phase.
 * @param {string} props.status - The current status of the phase ('completed', 'in-progress', 'upcoming').
 * @param {Array} props.milestones - Array of milestone objects for this phase.
 * @returns {JSX.Element} The Phase component.
 */
const Phase = ({ title, description, status, milestones }) => {
  const statusClass = `phase-status phase-status--${status}`;

  return (
    <div className="phase">
      <div className="phase-header">
        <h3 className="phase-title">{title}</h3>
        <div className={statusClass}>
          {status === 'completed' && '✓'}
          {status === 'in-progress' && '⏳'}
          {status === 'upcoming' && '🔜'}
        </div>
      </div>
      <p className="phase-description">{description}</p>
      <ul className="milestones-list">
        {milestones.map((milestone, index) => (
          <li key={index} className="milestone">
            <span className="milestone-check">
              {milestone.completed ? '✓' : '○'}
            </span>
            <span className="milestone-text">{milestone.text}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

Phase.propTypes = {
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  status: PropTypes.oneOf(['completed', 'in-progress', 'upcoming']).isRequired,
  milestones: PropTypes.arrayOf(
    PropTypes.shape({
      text: PropTypes.string.isRequired,
      completed: PropTypes.bool.isRequired,
    })
  ).isRequired,
};

/**
 * The main Bitcoin Minetrix Roadmap component.
 * @param {Object} props - The component props.
 * @param {Array} props.phases - Array of phase objects to display.
 * @returns {JSX.Element} The Roadmap component.
 */
const BitcoinMinetrixRoadmap = ({ phases }) => {
  if (!phases || phases.length === 0) {
    return <div className="roadmap-empty">No roadmap data available.</div>;
  }

  return (
    <div className="roadmap-container">
      <h2 className="roadmap-title">Bitcoin Minetrix Roadmap</h2>
      <div className="timeline">
        {phases.map((phase, index) => (
          <Phase
            key={index}
            title={phase.title}
            description={phase.description}
            status={phase.status}
            milestones={phase.milestones}
          />
        ))}
      </div>
    </div>
  );
};

BitcoinMinetrixRoadmap.propTypes = {
  phases: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
      status: PropTypes.oneOf(['completed', 'in-progress', 'upcoming']).isRequired,
      milestones: PropTypes.arrayOf(
        PropTypes.shape({
          text: PropTypes.string.isRequired,
          completed: PropTypes.bool.isRequired,
        })
      ).isRequired,
    })
  ).isRequired,
};

export default BitcoinMinetrixRoadmap;
```

```css
/* Roadmap.css */
.roadmap-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
}

.roadmap-title {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

.timeline {
  position: relative;
}

.timeline::before {
  content: '';
  position: absolute;
  width: 2px;
  background-color: #e0e0e0;
  top: 0;
  bottom: 0;
  left: 20px;
  margin-left: -1px;
}

.phase {
  position: relative;
  margin-bottom: 30px;
  padding-left: 50px;
}

.phase-header {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.phase-title {
  margin: 0;
  color: #2c3e50;
  font-size: 1.2em;
}

.phase-status {
  margin-left: 15px;
  padding: 3px 8px;
  border-radius: 12px;
  font-size: 0.8em;
  font-weight: bold;
}

.phase-status--completed {
  background-color: #4CAF50;
  color: white;
}

.phase-status--in-progress {
  background-color: #FFC107;
  color: black;
}

.phase-status--upcoming {
  background-color: #9E9E9E;
  color: white;
}

.phase-description {
  margin: 10px 0;
  color: #555;
}

.milestones-list {
  list-style-type: none;
  padding: 0;
}

.milestone {
  display: flex;
  align-items: center;
  margin-bottom: 8px;
}

.milestone-check {
  margin-right: 10px;
  font-weight: bold;
}

.milestone-text {
  color: #333;
}

.roadmap-empty {
  text-align: center;
  color: #666;
  padding: 20px;
}
```
