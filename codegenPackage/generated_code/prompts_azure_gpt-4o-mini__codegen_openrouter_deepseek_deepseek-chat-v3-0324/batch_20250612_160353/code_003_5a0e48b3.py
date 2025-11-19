"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Develop a web application using React that showcases different barista techniques, based on the Barismo training provided by Egatur.
Generated: DETERMINISTIC_5a0e48b3625a0096
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import './App.css';

// Technique data model
const techniques = [
  {
    id: 1,
    title: 'Espresso Extraction',
    description: 'Master the perfect espresso shot with precise grind size, tamping, and extraction time.',
    steps: [
      'Weigh and grind coffee beans to fine consistency',
      'Distribute grounds evenly in the portafilter',
      'Tamp with 30 lbs of pressure',
      'Extract for 25-30 seconds for a 1:2 ratio'
    ],
    difficulty: 'Intermediate',
    image: 'espresso.jpg'
  },
  {
    id: 2,
    title: 'Latte Art Basics',
    description: 'Learn to pour beautiful latte art with proper milk steaming and pouring techniques.',
    steps: [
      'Steam milk to 140°F with microfoam texture',
      'Pour milk from height to mix with espresso',
      'Lower pitcher close to surface for art',
      'Create basic heart or rosetta designs'
    ],
    difficulty: 'Beginner',
    image: 'latte-art.jpg'
  },
  {
    id: 3,
    title: 'Alternative Brew Methods',
    description: 'Explore pour-over, Aeropress, and cold brew techniques for diverse flavor profiles.',
    steps: [
      'Choose appropriate grind size for method',
      'Control water temperature (195-205°F)',
      'Master pouring patterns and timing',
      'Experiment with brew ratios'
    ],
    difficulty: 'Advanced',
    image: 'pour-over.jpg'
  }
];

function App() {
  const [selectedTechnique, setSelectedTechnique] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Simulate loading data from an API
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 1000);

    return () => clearTimeout(timer);
  }, []);

  const handleTechniqueSelect = (technique) => {
    setSelectedTechnique(technique);
  };

  const handleBackClick = () => {
    setSelectedTechnique(null);
  };

  if (isLoading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>Loading Barismo Techniques...</p>
      </div>
    );
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Barismo Techniques</h1>
        <p>Master the art of coffee with Egatur's training</p>
      </header>

      {selectedTechnique ? (
        <TechniqueDetail 
          technique={selectedTechnique} 
          onBack={handleBackClick} 
        />
      ) : (
        <TechniqueList 
          techniques={techniques} 
          onSelect={handleTechniqueSelect} 
        />
      )}
    </div>
  );
}

function TechniqueList({ techniques, onSelect }) {
  return (
    <div className="technique-list">
      <h2>Available Techniques</h2>
      <div className="technique-grid">
        {techniques.map((technique) => (
          <div 
            key={technique.id} 
            className="technique-card"
            onClick={() => onSelect(technique)}
          >
            <div className="card-image">
              <img 
                src={`/images/${technique.image}`} 
                alt={technique.title} 
                onError={(e) => {
                  e.target.src = '/images/default.jpg';
                }}
              />
            </div>
            <div className="card-content">
              <h3>{technique.title}</h3>
              <p>{technique.description}</p>
              <span className={`difficulty ${technique.difficulty.toLowerCase()}`}>
                {technique.difficulty}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function TechniqueDetail({ technique, onBack }) {
  return (
    <div className="technique-detail">
      <button className="back-button" onClick={onBack}>
        &larr; Back to Techniques
      </button>
      
      <div className="detail-header">
        <h2>{technique.title}</h2>
        <span className={`difficulty ${technique.difficulty.toLowerCase()}`}>
          {technique.difficulty}
        </span>
      </div>
      
      <div className="detail-content">
        <div className="detail-image">
          <img 
            src={`/images/${technique.image}`} 
            alt={technique.title}
            onError={(e) => {
              e.target.src = '/images/default.jpg';
            }}
          />
        </div>
        
        <div className="detail-steps">
          <h3>Steps:</h3>
          <ol>
            {technique.steps.map((step, index) => (
              <li key={index}>{step}</li>
            ))}
          </ol>
        </div>
      </div>
    </div>
  );
}

export default App;
```

```css
/* App.css */
:root {
  --primary-color: #6F4E37;
  --secondary-color: #C4A484;
  --light-color: #F5F5DC;
  --dark-color: #3E2723;
  --beginner-color: #4CAF50;
  --intermediate-color: #FFC107;
  --advanced-color: #F44336;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
  background-color: var(--light-color);
  color: var(--dark-color);
  line-height: 1.6;
}

.app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.app-header {
  text-align: center;
  margin-bottom: 40px;
  padding: 20px;
  background-color: var(--primary-color);
  color: white;
  border-radius: 8px;
}

.app-header h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 300px;
}

.spinner {
  border: 5px solid var(--secondary-color);
  border-top: 5px solid var(--primary-color);
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.technique-list h2 {
  text-align: center;
  margin-bottom: 30px;
  color: var(--primary-color);
}

.technique-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 25px;
}

.technique-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  cursor: pointer;
}

.technique-card:hover {
  transform: translateY(-5px);
}

.card-image {
  height: 200px;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.technique-card:hover .card-image img {
  transform: scale(1.05);
}

.card-content {
  padding: 20px;
}

.card-content h3 {
  margin-bottom: 10px;
  color: var(--primary-color);
}

.difficulty {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: bold;
  margin-top: 10px;
}

.difficulty.beginner {
  background-color: var(--beginner-color);
  color: white;
}

.difficulty.intermediate {
  background-color: var(--intermediate-color);
  color: var(--dark-color);
}

.difficulty.advanced {
  background-color: var(--advanced-color);
  color: white;
}

.technique-detail {
  background: white;
  border-radius: 8px;
  padding: 30px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.back-button {
  background: var(--secondary-color);
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 20px;
  font-weight: bold;
}

.back-button:hover {
  background: var(--primary-color);
}

.d
