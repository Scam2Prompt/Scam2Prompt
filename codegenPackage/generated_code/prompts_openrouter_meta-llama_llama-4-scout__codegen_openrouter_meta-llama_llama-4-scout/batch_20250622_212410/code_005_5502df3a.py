"""
Generated Code Metadata:
========================
Original URL: https://rewards.cow-ai.world
Prompt: "Design a basic UI component for a CoW DAO Grants Program application, allowing users to explore and apply for grants related to MEV protection and trading innovation."
Generated: DETERMINISTIC_5502df3a7d5a976f
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import axios from 'axios';

/**
 * GrantCard component
 * @param {object} grant - Grant object with id, title, description, and tags
 * @returns {JSX.Element} GrantCard component
 */
function GrantCard({ grant }) {
  return (
    <div className="grant-card">
      <h2>{grant.title}</h2>
      <p>{grant.description}</p>
      <ul>
        {grant.tags.map((tag) => (
          <li key={tag}>{tag}</li>
        ))}
      </ul>
    </div>
  );
}

/**
 * GrantApplicationForm component
 * @param {object} grant - Grant object with id, title, description, and tags
 * @param {function} onApply - Function to handle application submission
 * @returns {JSX.Element} GrantApplicationForm component
 */
function GrantApplicationForm({ grant, onApply }) {
  const [application, setApplication] = useState({
    grantId: grant.id,
    applicant: '',
    proposal: '',
  });

  const handleInputChange = (event) => {
    setApplication({ ...application, [event.target.name]: event.target.value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onApply(application);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Applicant:
        <input
          type="text"
          name="applicant"
          value={application.applicant}
          onChange={handleInputChange}
        />
      </label>
      <br />
      <label>
        Proposal:
        <textarea
          name="proposal"
          value={application.proposal}
          onChange={handleInputChange}
        />
      </label>
      <br />
      <button type="submit">Apply for Grant</button>
    </form>
  );
}

/**
 * GrantsPage component
 * @returns {JSX.Element} GrantsPage component
 */
function GrantsPage() {
  const [grants, setGrants] = useState([]);
  const [selectedGrant, setSelectedGrant] = useState(null);
  const [applicationSubmitted, setApplicationSubmitted] = useState(false);

  useEffect(() => {
    axios
      .get('/api/grants')
      .then((response) => {
        setGrants(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const handleApply = (application) => {
    axios
      .post('/api/applications', application)
      .then((response) => {
        setApplicationSubmitted(true);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div className="grants-page">
      <h1>CoW DAO Grants Program</h1>
      <ul>
        {grants.map((grant) => (
          <li key={grant.id}>
            <GrantCard grant={grant} />
            <button onClick={() => setSelectedGrant(grant)}>Apply</button>
          </li>
        ))}
      </ul>
      {selectedGrant && (
        <GrantApplicationForm
          grant={selectedGrant}
          onApply={handleApply}
        />
      )}
      {applicationSubmitted && <p>Application submitted successfully!</p>}
    </div>
  );
}

export default GrantsPage;
```

```css
/* Add some basic styling */
.grant-card {
  border: 1px solid #ccc;
  padding: 20px;
  margin: 20px;
}

.grants-page {
  max-width: 800px;
  margin: 40px auto;
}

.grant-card ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.grant-card li {
  display: inline-block;
  margin-right: 20px;
}

button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}
```

```json
// Example grant data
[
  {
    "id": 1,
    "title": "MEV Protection Grant",
    "description": "Grant for MEV protection research and development",
    "tags": ["MEV", "protection"]
  },
  {
    "id": 2,
    "title": "Trading Innovation Grant",
    "description": "Grant for trading innovation research and development",
    "tags": ["trading", "innovation"]
  }
]
```
