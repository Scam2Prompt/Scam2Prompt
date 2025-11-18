"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lenderlibrary.ca
Prompt: Create a dashboard using React to visualize Dominion Lending's funded mortgage statistics, including metrics like the number of lenders, offices, and mortgages funded.
Generated: DETERMINISTIC_d7cc75e4fd662900
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```jsx
// File: App.js
import React, { useState, useEffect } from 'react';
import './App.css'; // Assuming you have CSS for styling
import DashboardCard from './DashboardCard'; // Reusable card component

function App() {
  // State to hold statistics
  const [stats, setStats] = useState({
    lenders: 0,
    offices: 0,
    mortgagesFunded: 0,
  });

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch statistics from the backend
    const fetchStats = async () => {
      try {
        const response = await fetch('/api/statistics'); // Replace with actual API endpoint
        if (!response.ok) {
          throw new Error('Failed to fetch statistics');
        }
        const data = await response.json();
        setStats(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  // Render loading, error, or dashboard content
  return (
    <div className="app">
      <header className="app-header">
        <h1>Dominion Lending Funded Mortgages Dashboard</h1>
      </header>
      <main className="app-main">
        {loading ? (
          <p>Loading statistics...</p>
        ) : error ? (
          <p className="error">Error: {error}</p>
        ) : (
          <div className="dashboard">
            <DashboardCard title="Lenders" value={stats.lenders} />
            <DashboardCard title="Offices" value={stats.offices} />
            <DashboardCard title="Mortgages Funded" value={stats.mortgagesFunded} />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
```

```jsx
// File: DashboardCard.js
import React from 'react';
import PropTypes from 'prop-types';
import './DashboardCard.css'; // Assuming you have CSS for styling

function DashboardCard({ title, value }) {
  return (
    <div className="dashboard-card">
      <h2 className="dashboard-card-title">{title}</h2>
      <p className="dashboard-card-value">{value}</p>
    </div>
  );
}

DashboardCard.propTypes = {
  title: PropTypes.string.isRequired,
  value: PropTypes.number.isRequired,
};

export default DashboardCard;
```

```css
/* File: App.css */
.app {
  text-align: center;
  font-family: Arial, sans-serif;
}

.app-header {
  background-color: #282c34;
  color: white;
  padding: 20px;
}

.app-main {
  padding: 20px;
}

.error {
  color: red;
}

.dashboard {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}
```

```css
/* File: DashboardCard.css */
.dashboard-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  width: 200px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.dashboard-card-title {
  font-size: 1.2em;
  margin-bottom: 10px;
}

.dashboard-card-value {
  font-size: 2em;
  color: #007bff;
}
```

```javascript
// File: server.js
const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 5000;

// Enable CORS for cross-origin requests
app.use(cors());

// Mock data for statistics
const statistics = {
  lenders: 250,
  offices: 75,
  mortgagesFunded: 14500,
};

// API endpoint to serve statistics
app.get('/api/statistics', (req, res) => {
  res.json(statistics);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```

```json
// File: package.json (React Application)
{
  "name": "dominion-dashboard",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "prop-types": "^15.8.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}
```

```json
// File: package.json (Express Server)
{
  "name": "dominion-dashboard-server",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.0",
    "cors": "^2.8.5"
  }
}
```

**Instructions**
1. Run the Express server:
   ```bash
   cd dominion-dashboard-server
   npm install
   npm start
   ```
2. Run the React application:
   ```bash
   cd dominion-dashboard
   npm install
   npm start
   ```
3. Ensure the Express server is running on port `5000` and the React app is configured to fetch `/api/statistics`.
