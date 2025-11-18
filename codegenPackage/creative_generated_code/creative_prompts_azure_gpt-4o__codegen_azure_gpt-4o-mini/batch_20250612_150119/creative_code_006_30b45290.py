"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retro-pgf.vercel.app
Prompt: Write a React component to implement a "Run your own RPGF Round" feature, using the EasyRetroPGF framework for backend integration.
Generated: DETERMINISTIC_30b452902d448204
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

/**
 * RPGFRound Component
 * This component allows users to run their own RPGF round using the EasyRetroPGF framework.
 */
const RPGFRound = ({ apiUrl }) => {
  const [participants, setParticipants] = useState([]);
  const [roundResults, setRoundResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch participants from the EasyRetroPGF backend
  const fetchParticipants = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${apiUrl}/participants`);
      setParticipants(response.data);
    } catch (err) {
      setError('Failed to fetch participants.');
      console.error('Error fetching participants:', err);
    } finally {
      setLoading(false);
    }
  };

  // Trigger the RPGF round
  const runRound = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post(`${apiUrl}/runRound`, { participants });
      setRoundResults(response.data);
    } catch (err) {
      setError('Failed to run the RPGF round.');
      console.error('Error running RPGF round:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchParticipants();
  }, [apiUrl]);

  return (
    <div className="rpgf-round">
      <h2>Run Your Own RPGF Round</h2>
      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}
      <div>
        <button onClick={runRound} disabled={loading || participants.length === 0}>
          Start Round
        </button>
      </div>
      {roundResults && (
        <div className="results">
          <h3>Round Results:</h3>
          <pre>{JSON.stringify(roundResults, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

RPGFRound.propTypes = {
  apiUrl: PropTypes.string.isRequired,
};

export default RPGFRound;

```
