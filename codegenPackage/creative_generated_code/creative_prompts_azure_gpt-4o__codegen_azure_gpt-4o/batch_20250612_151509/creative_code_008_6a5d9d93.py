"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govssc.edu.bd
Prompt: Develop a React-based frontend for displaying the Govt. Shah Sultan College's academic routine and syllabus, fetched dynamically from the website.
Generated: DETERMINISTIC_6a5d9d930149d624
Batch ID: 20250612_151509
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api": {
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
// Import necessary modules and libraries
import React, { useState, useEffect } from 'react';
import axios from 'axios'; // Axios for HTTP requests

// Define the main component
const AcademicInfo = () => {
  // Use state to hold routine and syllabus data
  const [routine, setRoutine] = useState([]);
  const [syllabus, setSyllabus] = useState([]);
  const [loading, setLoading] = useState(true); // Loading state
  const [error, setError] = useState(null); // Error state

  // Base URL for fetching data
  const BASE_URL = 'https://example.com/api'; // Replace with the actual URL of the college's API

  // Fetch academic data (routine and syllabus) when the component is mounted
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true); // Start loading
        const routineResponse = await axios.get(`${BASE_URL}/academic-routine`);
        const syllabusResponse = await axios.get(`${BASE_URL}/academic-syllabus`);
        setRoutine(routineResponse.data); // Update state with routine data
        setSyllabus(syllabusResponse.data); // Update state with syllabus data
      } catch (err) {
        setError('Failed to fetch academic information. Please try again later.'); // Set error state
      } finally {
        setLoading(false); // Stop loading
      }
    };

    fetchData();
  }, [BASE_URL]); // Dependency array ensures this runs only once

  // Render the component
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Govt. Shah Sultan College Academic Info</h1>
      {loading && <p>Loading data...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {!loading && !error && (
        <>
          <section>
            <h2>Academic Routine</h2>
            {routine.length > 0 ? (
              <ul>
                {routine.map((item, index) => (
                  <li key={index}>
                    <strong>{item.subject}</strong>: {item.time}
                  </li>
                ))}
              </ul>
            ) : (
              <p>No routine data available.</p>
            )}
          </section>
          <section>
            <h2>Academic Syllabus</h2>
            {syllabus.length > 0 ? (
              <ul>
                {syllabus.map((item, index) => (
                  <li key={index}>
                    <strong>{item.course}</strong>: {item.description}
                  </li>
                ))}
              </ul>
            ) : (
              <p>No syllabus data available.</p>
            )}
          </section>
        </>
      )}
    </div>
  );
};

export default AcademicInfo;
```

### Notes:

1. Replace `BASE_URL` with the actual endpoint URL for fetching the academic routine and syllabus.
2. Ensure the API response structure matches the rendering logic (e.g., `subject`, `time`, `course`, `description`).
3. Install dependencies (`react` and `axios`) before running the code:
   ```bash
   npm install react axios
   ```
4. Best practices like separation of concerns, modularity, and error handling are followed.
