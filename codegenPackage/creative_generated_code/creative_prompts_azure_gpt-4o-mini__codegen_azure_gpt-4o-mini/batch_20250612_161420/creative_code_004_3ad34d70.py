"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marqador.com
Prompt: Design a user interface component that allows users to select stamp types and add QR codes for contact information, based on the marQadoR product features.
Generated: DETERMINISTIC_3ad34d7072846b7d
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * StampSelector component allows users to select stamp types
 * and add QR codes for contact information.
 *
 * @param {Object} props - The component props
 * @param {Array} props.stampTypes - Available stamp types
 * @param {function} props.onSubmit - Callback function when submitting the contact information
 */
const StampSelector = ({ stampTypes, onSubmit }) => {
  const [selectedStamp, setSelectedStamp] = useState('');
  const [contactInfo, setContactInfo] = useState('');
  const [error, setError] = useState('');

  /**
   * Handles the change of stamp type selection.
   *
   * @param {Event} event - The event triggered by selecting a stamp type
   */
  const handleStampChange = (event) => {
    setSelectedStamp(event.target.value);
    setError('');
  };

  /**
   * Handles the change of contact information input.
   *
   * @param {Event} event - The event triggered by input change
   */
  const handleContactChange = (event) => {
    setContactInfo(event.target.value);
    setError('');
  };

  /**
   * Validates the form and calls the onSubmit callback if valid.
   */
  const handleSubmit = (event) => {
    event.preventDefault();
    if (!selectedStamp || !contactInfo) {
      setError('Please select a stamp type and enter contact information.');
      return;
    }
    
    try {
      onSubmit({ selectedStamp, contactInfo });
      // Clear inputs after submission
      setSelectedStamp('');
      setContactInfo('');
    } catch (err) {
      console.error('Error submitting form:', err);
      setError('An error occurred while submitting the information. Please try again.');
    }
  };

  return (
    <div className="stamp-selector">
      <h2>Select Stamp Type and Add QR Code</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="stampType">Select Stamp Type:</label>
          <select id="stampType" value={selectedStamp} onChange={handleStampChange}>
            <option value="">--Choose a stamp type--</option>
            {stampTypes.map((type) => (
              <option key={type} value={type}>{type}</option>
            ))}
          </select>
        </div>
        
        <div>
          <label htmlFor="contactInfo">Contact Information:</label>
          <input
            type="text"
            id="contactInfo"
            value={contactInfo}
            onChange={handleContactChange}
            placeholder="Enter your contact info"
          />
        </div>

        {error && <p className="error">{error}</p>}

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

StampSelector.propTypes = {
  stampTypes: PropTypes.arrayOf(PropTypes.string).isRequired,
  onSubmit: PropTypes.func.isRequired,
};

export default StampSelector;
```
