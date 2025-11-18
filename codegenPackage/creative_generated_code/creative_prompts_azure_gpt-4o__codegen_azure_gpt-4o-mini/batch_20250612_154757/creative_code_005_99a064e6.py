"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-solution.web.app
Prompt: Write JavaScript code to create a user interface for verifying wallet recovery phrases on a cryptocurrency platform like Coinbase.
Generated: DETERMINISTIC_99a064e608a5010d
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// RecoveryPhraseVerifier component
const RecoveryPhraseVerifier = ({ expectedPhrase }) => {
  // State to manage user input and validation result
  const [userInput, setUserInput] = useState('');
  const [isValid, setIsValid] = useState(null);
  const [error, setError] = useState('');

  // Handle input change
  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  // Validate recovery phrase
  const validatePhrase = (event) => {
    event.preventDefault(); // Prevent form submission

    // Split the user input and expected phrase into arrays for comparison
    const userPhraseArray = userInput.trim().split(/\s+/);
    const expectedPhraseArray = expectedPhrase.trim().split(/\s+/);

    // Basic validation: check if lengths match
    if (userPhraseArray.length !== expectedPhraseArray.length) {
      setError('The number of words does not match. Please try again.');
      setIsValid(false);
      return;
    }

    // Check if all words match
    const isMatch = userPhraseArray.every((word, index) => word === expectedPhraseArray[index]);

    // Update validation result state
    setIsValid(isMatch);
    setError(isMatch ? '' : 'The recovery phrase is incorrect.');
  };

  return (
    <div className="recovery-phrase-verifier">
      <h2>Verify Your Recovery Phrase</h2>
      <form onSubmit={validatePhrase}>
        <textarea
          value={userInput}
          onChange={handleInputChange}
          placeholder="Enter your recovery phrase here..."
          rows="4"
          cols="50"
          required
        />
        <button type="submit">Verify</button>
      </form>
      {isValid !== null && (
        <div className={`result ${isValid ? 'valid' : 'invalid'}`}>
          {isValid ? 'Recovery phrase is valid!' : error}
        </div>
      )}
    </div>
  );
};

// PropTypes for type-checking props
RecoveryPhraseVerifier.propTypes = {
  expectedPhrase: PropTypes.string.isRequired,
};

// Export the component for use in other parts of the application
export default RecoveryPhraseVerifier;
```
