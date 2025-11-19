"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://934ummfm.com
Prompt: Develop a simple web application using React that showcases a weekly podcast schedule, incorporating elements from UMM FM's programming details.
Generated: DETERMINISTIC_684913bbb27095e1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/App.js

import React from 'react';
import PodcastSchedule from './components/PodcastSchedule';
import './App.css';

/**
 * Main App component for the podcast schedule application.
 */
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>UMM FM Weekly Podcast Schedule</h1>
      </header>
      <main>
        <PodcastSchedule />
      </main>
    </div>
  );
}

export default App;
```

```javascript
// src/components/PodcastSchedule.js

import React from 'react';
import ScheduleCard from './ScheduleCard';

// Sample data representing the podcast schedule
const podcastData = [
  {
    day: 'Monday',
    title: 'Morning Motivation',
    time: '9:00 AM - 10:00 AM',
    host: 'Alex Smith',
  },
  {
    day: 'Wednesday',
    title: 'Tech Talk',
    time: '3:00 PM - 4:00 PM',
    host: 'Jordan Lee',
  },
  {
    day: 'Friday',
    title: 'Music Mix',
    time: '5:00 PM - 6:00 PM',
    host: 'Taylor Johnson',
  },
];

/**
 * PodcastSchedule component to display a list of scheduled podcasts.
 */
const PodcastSchedule = () => {
  return (
    <div className="podcast-schedule">
      {podcastData.map((podcast, index) => (
        <ScheduleCard key={index} {...podcast} />
      ))}
    </div>
  );
};

export default PodcastSchedule;
```

```javascript
// src/components/ScheduleCard.js

import React from 'react';
import PropTypes from 'prop-types';

/**
 * ScheduleCard component to display individual podcast details.
 * 
 * @param {Object} props - Properties passed to the component.
 * @param {string} props.day - Day of the week.
 * @param {string} props.title - Title of the podcast.
 * @param {string} props.time - Time of the podcast.
 * @param {string} props.host - Host of the podcast.
 */
const ScheduleCard = ({ day, title, time, host }) => {
  return (
    <div className="schedule-card">
      <h3>{day}</h3>
      <p><strong>Title:</strong> {title}</p>
      <p><strong>Time:</strong> {time}</p>
      <p><strong>Host:</strong> {host}</p>
    </div>
  );
};

ScheduleCard.propTypes = {
  day: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  time: PropTypes.string.isRequired,
  host: PropTypes.string.isRequired,
};

export default ScheduleCard;
```

```css
/* src/App.css */

.App {
  text-align: center;
  font-family: Arial, sans-serif;
}

.App-header {
  background-color: #282c34;
  padding: 20px;
  color: white;
}

.podcast-schedule {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.schedule-card {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin: 10px;
  width: 300px;
  background-color: #f9f9f9;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}
```

```bash
# package.json scripts section (for running the app)

{
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

To run the application, ensure you have Node.js and npm installed. Create a new React app using `create-react-app`, replace the generated files with the code provided, and run `npm start` in your terminal to see the application in action.
