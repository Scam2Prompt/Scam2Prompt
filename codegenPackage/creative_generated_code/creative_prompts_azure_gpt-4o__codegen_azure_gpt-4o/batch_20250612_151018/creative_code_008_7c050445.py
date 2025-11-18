"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2614--docusaurus-2.netlify.app
Prompt: How can I use Docusaurus to create a showcase page for open-source projects? Provide relevant code snippets.
Generated: DETERMINISTIC_7c0504451abc092d
Batch ID: 20250612_151018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/org/beta-framework": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/org/gamma-library": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/org/project-alpha": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Docusaurus showcase page example
// This can be added to your Docusaurus project under the appropriate route
// Ensure Docusaurus is installed and properly set up.
// Install dependencies using `npm install @docusaurus/core @docusaurus/theme-classic`

// src/pages/Showcase.js
import React from 'react';
import Layout from '@theme/Layout'; // Layout component from Docusaurus
import clsx from 'clsx'; // Utility for conditional class names
import styles from './showcase.module.css'; // Custom CSS for styling

// Data for open-source projects
const projects = [
  {
    name: 'Project Alpha',
    description: 'An open-source tool for managing workflows efficiently.',
    url: 'https://github.com/org/project-alpha',
    stars: 1500,
  },
  {
    name: 'Beta Framework',
    description: 'A lightweight framework for building web applications.',
    url: 'https://github.com/org/beta-framework',
    stars: 2300,
  },
  {
    name: 'Gamma Library',
    description: 'A library for handling asynchronous tasks in JavaScript.',
    url: 'https://github.com/org/gamma-library',
    stars: 450,
  },
];

// Functional component for displaying project cards
function ProjectCard({ name, description, url, stars }) {
  return (
    <div className={clsx(styles.card)}>
      <h3>{name}</h3>
      <p>{description}</p>
      <a href={url} target="_blank" rel="noopener noreferrer">
        View on GitHub
      </a>
      <p className={clsx(styles.stars)}>⭐ Stars: {stars}</p>
    </div>
  );
}

// Main showcase page component
export default function Showcase() {
  return (
    <Layout title="Open-Source Showcase" description="Discover amazing open-source projects.">
      <div className={clsx(styles.container)}>
        <h1>Open-Source Showcase</h1>
        <p>Explore some of the most popular open-source projects.</p>
        <div className={clsx(styles.grid)}>
          {projects.map((project) => (
            <ProjectCard key={project.name} {...project} />
          ))}
        </div>
      </div>
    </Layout>
  );
}

// CSS module for styling (src/pages/showcase.module.css)
/*
.container {
  padding: 2rem;
  text-align: center;
}

.grid {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

.card {
  border: 1px solid #ddd;
  padding: 1.5rem;
  border-radius: 8px;
  width: 300px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card h3 {
  margin-bottom: 1rem;
  color: #333;
}

.card p {
  color: #555;
  margin-bottom: 1rem;
}

.card a {
  text-decoration: none;
  color: #0066cc;
}

.card a:hover {
  text-decoration: underline;
}

.stars {
  margin-top: 1rem;
  font-weight: bold;
}
*/

// Notes:
// 1. This page uses React components provided by Docusaurus.
// 2. Customize the `projects` array to include your own open-source projects.
// 3. To add this page to your site, simply place `Showcase.js` and `showcase.module.css` in the appropriate directories and test it by running your Docusaurus development server.
```
