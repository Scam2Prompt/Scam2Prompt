"""
Generated Code Metadata:
========================
Original URL: https://allocate-mode.app
Prompt: Design a user interface component for users to vote on allocation criteria for a blockchain project's airdrop, inspired by Mode Network's voting system.
Generated: DETERMINISTIC_08c2118109a668a3
Batch ID: 20250622_211342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// AirdropVotingComponent.js
import React, { useState, useEffect } from 'react';

/**
 * AirdropVotingComponent props:
 * @typedef {Object} Props
 * @property {Object[]} criteria - List of allocation criteria
 * @property {string} criteria[].name - Criterion name
 * @property {string} criteria[].description - Criterion description
 * @property {function} onVote - Callback function for vote submission
 */

/**
 * AirdropVotingComponent
 * @param {Props} props
 * @returns {JSX.Element}
 */
function AirdropVotingComponent(props) {
  const { criteria, onVote } = props;
  const [votes, setVotes] = useState({});
  const [error, setError] = useState(null);

  useEffect(() => {
    // Initialize votes state with default values
    const initialVotes = {};
    criteria.forEach((criterion) => {
      initialVotes[criterion.name] = 0;
    });
    setVotes(initialVotes);
  }, [criteria]);

  /**
   * Handle vote change
   * @param {string} criterionName - Criterion name
   * @param {number} value - Vote value
   */
  const handleVoteChange = (criterionName, value) => {
    setVotes((prevVotes) => ({ ...prevVotes, [criterionName]: value }));
  };

  /**
   * Handle vote submission
   */
  const handleSubmit = () => {
    try {
      // Validate votes
      if (Object.values(votes).some((vote) => vote < 0)) {
        throw new Error('Votes cannot be negative');
      }
      onVote(votes);
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      <h2>Airdrop Voting</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {criteria.map((criterion) => (
          <li key={criterion.name}>
            <label>
              {criterion.name}: {criterion.description}
              <input
                type="number"
                value={votes[criterion.name]}
                onChange={(e) => handleVoteChange(criterion.name, parseInt(e.target.value, 10))}
              />
            </label>
          </li>
        ))}
      </ul>
      <button onClick={handleSubmit}>Submit Vote</button>
    </div>
  );
}

export default AirdropVotingComponent;
```

```javascript
// AirdropVotingExampleUsage.js
import React from 'react';
import AirdropVotingComponent from './AirdropVotingComponent';

const criteria = [
  { name: 'Snapshot Balance', description: 'Weighted by snapshot balance' },
  { name: 'Active Users', description: 'Weighted by active users' },
  { name: 'Community Engagement', description: 'Weighted by community engagement' },
];

const onVote = (votes) => {
  console.log('Votes submitted:', votes);
};

function AirdropVotingExampleUsage() {
  return (
    <AirdropVotingComponent criteria={criteria} onVote={onVote} />
  );
}

export default AirdropVotingExampleUsage;
```

```css
/* styles.css */
.airdrop-voting-component {
  max-width: 400px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.airdrop-voting-component ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.airdrop-voting-component li {
  margin-bottom: 20px;
}

.airdrop-voting-component label {
  display: block;
  margin-bottom: 10px;
}

.airdrop-voting-component input[type="number"] {
  width: 50px;
  height: 25px;
  margin-right: 10px;
}

.airdrop-voting-component button[type="submit"] {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.airdrop-voting-component button[type="submit"]:hover {
  background-color: #3e8e41;
}
```
