"""
Generated Code Metadata:
========================
Original URL: https://gitcoin-dr-manager.vercel.app
Prompt: Generate a React component for managing grant rounds, including features like form validation and API integration with Gitcoin's Round Manager.
Generated: DETERMINISTIC_dda60bcffd003e6e
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';

// GrantRoundManager component for managing grant rounds
const GrantRoundManager = ({ apiUrl }) => {
  // State variables for form data and error handling
  const [roundData, setRoundData] = useState({
    title: '',
    description: '',
    startDate: '',
    endDate: '',
  });
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setRoundData({ ...roundData, [name]: value });
  };

  // Validate form data
  const validateForm = () => {
    const { title, description, startDate, endDate } = roundData;
    if (!title || !description || !startDate || !endDate) {
      return 'All fields are required.';
    }
    if (new Date(startDate) >= new Date(endDate)) {
      return 'Start date must be before end date.';
    }
    return '';
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    const validationError = validateForm();
    if (validationError) {
      setError(validationError);
      return;
    }
    setError('');

    try {
      const response = await axios.post(`${apiUrl}/grant-rounds`, roundData);
      setSuccessMessage('Grant round created successfully!');
      setRoundData({ title: '', description: '', startDate: '', endDate: '' }); // Reset form
    } catch (err) {
      setError('Failed to create grant round. Please try again.');
      console.error('API Error:', err);
    }
  };

  return (
    <div>
      <h2>Create Grant Round</h2>
      {error && <div className="error">{error}</div>}
      {successMessage && <div className="success">{successMessage}</div>}
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">Title:</label>
          <input
            type="text"
            id="title"
            name="title"
            value={roundData.title}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            name="description"
            value={roundData.description}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="startDate">Start Date:</label>
          <input
            type="date"
            id="startDate"
            name="startDate"
            value={roundData.startDate}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="endDate">End Date:</label>
          <input
            type="date"
            id="endDate"
            name="endDate"
            value={roundData.endDate}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Create Grant Round</button>
      </form>
    </div>
  );
};

// PropTypes for component validation
GrantRoundManager.propTypes = {
  apiUrl: PropTypes.string.isRequired,
};

export default GrantRoundManager;
```
