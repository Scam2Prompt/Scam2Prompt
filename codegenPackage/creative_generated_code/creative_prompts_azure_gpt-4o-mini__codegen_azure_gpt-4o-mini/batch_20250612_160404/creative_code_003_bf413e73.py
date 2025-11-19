"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Develop a front-end component using React that displays upcoming events for a business association, inspired by the event listings on the IACI website.
Generated: DETERMINISTIC_bf413e7373fb6cbd
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './EventList.css'; // Import CSS for styling

// Functional component to display upcoming events
const EventList = ({ apiUrl }) => {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Function to fetch events from the API
    const fetchEvents = async () => {
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`Error fetching events: ${response.statusText}`);
        }
        const data = await response.json();
        setEvents(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchEvents();
  }, [apiUrl]); // Dependency array - re-fetch if apiUrl changes

  // Render loading state
  if (loading) {
    return <div className="loading">Loading events...</div>;
  }

  // Render error state
  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  // Render the list of events
  return (
    <div className="event-list">
      <h2>Upcoming Events</h2>
      {events.length === 0 ? (
        <div>No upcoming events found.</div>
      ) : (
        <ul>
          {events.map(event => (
            <li key={event.id} className="event-item">
              <h3>{event.title}</h3>
              <p>{event.date}</p>
              <p>{event.location}</p>
              <p>{event.description}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

// Prop Types validation
EventList.propTypes = {
  apiUrl: PropTypes.string.isRequired,
};

// Default export of the component
export default EventList;
```

```css
/* EventList.css */

/* Basic styling for the event list */
.event-list {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.loading {
  text-align: center;
  font-size: 18px;
}

.error {
  color: red;
  text-align: center;
}

.event-item {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 3px;
  background-color: #fff;
}

.event-item h3 {
  margin: 0;
  font-size: 20px;
}

.event-item p {
  margin: 5px 0;
}
```
