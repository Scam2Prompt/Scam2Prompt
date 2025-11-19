"""
Generated Code Metadata:
========================
Original URL: https://mantadev.pages.dev
Prompt: Create a web application using React to display user rankings, quests, and KARMA rewards on MANTRA Zone.
Generated: DETERMINISTIC_96110d94d1b04c1d
Batch ID: 20250622_204726
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.mantrazone.com/users": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mantrazone.com/quests": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
  const [users, setUsers] = useState([]);
  const [quests, setQuests] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [usersResponse, questsResponse] = await Promise.all([
          axios.get('https://api.mantrazone.com/users'),
          axios.get('https://api.mantrazone.com/quests')
        ]);
        
        setUsers(usersResponse.data.sort((a, b) => b.karma - a.karma));
        setQuests(questsResponse.data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div className="loading">Loading...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="app">
      <header className="header">
        <h1>MANTRA Zone</h1>
        <p>User Rankings, Quests & KARMA Rewards</p>
      </header>

      <main className="main-content">
        <section className="rankings-section">
          <h2>User Rankings</h2>
          <div className="rankings-table">
            <table>
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>Username</th>
                  <th>KARMA</th>
                </tr>
              </thead>
              <tbody>
                {users.map((user, index) => (
                  <tr key={user.id}>
                    <td>{index + 1}</td>
                    <td>{user.username}</td>
                    <td>{user.karma}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <section className="quests-section">
          <h2>Available Quests</h2>
          <div className="quests-grid">
            {quests.map(quest => (
              <div key={quest.id} className="quest-card">
                <h3>{quest.title}</h3>
                <p>{quest.description}</p>
                <div className="quest-reward">
                  <span>Reward: {quest.reward} KARMA</span>
                </div>
              </div>
            ))}
          </div>
        </section>
      </main>

      <footer className="footer">
        <p>© 2023 MANTRA Zone. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default App;

// App.css
body {
  margin: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f5f5f5;
  color: #333;
}

.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header {
  background-color: #2c3e50;
  color: white;
  padding: 2rem;
  text-align: center;
}

.header h1 {
  margin: 0;
  font-size: 2.5rem;
}

.header p {
  margin: 0.5rem 0 0;
  font-size: 1.2rem;
}

.main-content {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.rankings-section, .quests-section {
  margin-bottom: 3rem;
}

.rankings-section h2, .quests-section h2 {
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 0.5rem;
}

.rankings-table {
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

th, td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #3498db;
  color: white;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

.quests-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}

.quest-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  transition: transform 0.2s;
}

.quest-card:hover {
  transform: translateY(-5px);
}

.quest-card h3 {
  margin-top: 0;
  color: #2c3e50;
}

.quest-reward {
  margin-top: 1rem;
  font-weight: bold;
  color: #27ae60;
}

.loading, .error {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
}

.loading {
  color: #3498db;
}

.error {
  color: #e74c3c;
}

.footer {
  background-color: #2c3e50;
  color: white;
  text-align: center;
  padding: 1rem;
  margin-top: auto;
}

@media (max-width: 768px) {
  .main-content {
    padding: 1rem;
  }
  
  .quests-grid {
    grid-template-columns: 1fr;
  }
}

// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();

// reportWebVitals.js
const reportWebVitals = onPerfEntry => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;
```
