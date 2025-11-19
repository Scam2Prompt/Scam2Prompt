"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Develop a simple web application using React that showcases a weekly podcast schedule, incorporating elements from UMM FM's programming details.
Generated: DETERMINISTIC_684913bbb27095e1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import './App.css';

// Podcast data structure
const initialPodcasts = [
  {
    id: 1,
    title: 'Morning Jazz',
    host: 'DJ Jazz',
    day: 'Monday',
    time: '8:00 AM - 10:00 AM',
    description: 'Start your week with smooth jazz tunes.',
  },
  {
    id: 2,
    title: 'Rock Hour',
    host: 'The Rocker',
    day: 'Tuesday',
    time: '5:00 PM - 6:00 PM',
    description: 'Classic and modern rock hits.',
  },
  {
    id: 3,
    title: 'Hip-Hop Nation',
    host: 'MC Flow',
    day: 'Wednesday',
    time: '7:00 PM - 9:00 PM',
    description: 'The latest in hip-hop and rap.',
  },
  {
    id: 4,
    title: 'Electronic Vibes',
    host: 'DJ Pulse',
    day: 'Thursday',
    time: '8:00 PM - 10:00 PM',
    description: 'Electronic dance music to get you moving.',
  },
  {
    id: 5,
    title: 'Weekend Warmup',
    host: 'The Crew',
    day: 'Friday',
    time: '4:00 PM - 6:00 PM',
    description: 'Get ready for the weekend with our mix.',
  },
];

// Main App component
function App() {
  const [podcasts, setPodcasts] = useState([]);
  const [selectedDay, setSelectedDay] = useState('All');
  const [isLoading, setIsLoading] = useState(true);

  // Simulate data loading
  useEffect(() => {
    const timer = setTimeout(() => {
      setPodcasts(initialPodcasts);
      setIsLoading(false);
    }, 1000);

    return () => clearTimeout(timer);
  }, []);

  // Filter podcasts by selected day
  const filteredPodcasts = selectedDay === 'All' 
    ? podcasts 
    : podcasts.filter(podcast => podcast.day === selectedDay);

  // Days for filter
  const days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

  return (
    <div className="app">
      <header className="app-header">
        <h1>UMM FM Weekly Podcast Schedule</h1>
      </header>

      <main className="app-main">
        {isLoading ? (
          <div className="loading">Loading schedule...</div>
        ) : (
          <>
            <div className="filter-controls">
              <label htmlFor="day-filter">Filter by day:</label>
              <select
                id="day-filter"
                value={selectedDay}
                onChange={(e) => setSelectedDay(e.target.value)}
              >
                {days.map(day => (
                  <option key={day} value={day}>{day}</option>
                ))}
              </select>
            </div>

            <div className="podcast-grid">
              {filteredPodcasts.length > 0 ? (
                filteredPodcasts.map(podcast => (
                  <div key={podcast.id} className="podcast-card">
                    <h2>{podcast.title}</h2>
                    <p className="host">Host: {podcast.host}</p>
                    <p className="day-time">{podcast.day} | {podcast.time}</p>
                    <p className="description">{podcast.description}</p>
                  </div>
                ))
              ) : (
                <div className="no-results">No podcasts scheduled for {selectedDay}.</div>
              )}
            </div>
          </>
        )}
      </main>

      <footer className="app-footer">
        <p>© {new Date().getFullYear()} UMM FM Radio. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
```

```css
/* App.css */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #f5f5f5;
  color: #333;
}

.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.app-header {
  background-color: #282c34;
  color: white;
  padding: 2rem;
  text-align: center;
}

.app-header h1 {
  margin: 0;
  font-size: 2rem;
}

.app-main {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.filter-controls {
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.filter-controls label {
  font-weight: bold;
}

.filter-controls select {
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.podcast-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
}

.podcast-card {
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.podcast-card:hover {
  transform: translateY(-5px);
}

.podcast-card h2 {
  margin-top: 0;
  color: #282c34;
}

.podcast-card .host {
  color: #666;
  font-style: italic;
}

.podcast-card .day-time {
  color: #444;
  font-weight: bold;
}

.podcast-card .description {
  margin-bottom: 0;
}

.loading, .no-results {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
}

.app-footer {
  background-color: #282c34;
  color: white;
  text-align: center;
  padding: 1rem;
  margin-top: auto;
}

@media (max-width: 600px) {
  .podcast-grid {
    grid-template-columns: 1fr;
  }
  
  .filter-controls {
    flex-direction: column;
    align-items: flex-start;
  }
}
```
