"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migrate-refi-tokenapp.pages.dev
Prompt: Create a React component for a token migration app that dynamically updates the "Existing Balance" field based on user input and migration status.
Generated: DETERMINISTIC_ab5a374d3fc5d591
Batch ID: 20250612_151027
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

/**
 * TokenMigration component allows users to migrate tokens and displays existing balance.
 * @component
 * @param {Object} props - Component props.
 * @param {number} props.initialBalance - The initial balance of tokens before migration.
 * @param {function} props.onMigrate - Callback function to handle migration logic.
 */

const TokenMigration = ({ initialBalance, onMigrate }) => {
  // State to hold the current balance and migration status
  const [existingBalance, setExistingBalance] = useState(initialBalance);
  const [migrationStatus, setMigrationStatus] = useState('idle'); // 'idle', 'pending', 'completed', 'error'
  const [errorMessage, setErrorMessage] = useState('');

  // Update existing balance if initial balance changes
  useEffect(() => {
    setExistingBalance(initialBalance);
  }, [initialBalance]);

  // Function to handle migration
  const handleMigration = async () => {
    setMigrationStatus('pending');
    setErrorMessage('');

    try {
      // Simulating migration process
      await onMigrate(existingBalance);
      setExistingBalance(0); // Assuming all tokens are migrated
      setMigrationStatus('completed');
    } catch (error) {
      setErrorMessage(`Migration failed: ${error.message}`);
      setMigrationStatus('error');
    }
  };

  return (
    <div className="token-migration">
      <h2>Token Migration</h2>
      <div>
        <label htmlFor="existing-balance">Existing Balance:</label>
        <input
          id="existing-balance"
          type="number"
          value={existingBalance}
          readOnly
        />
      </div>
      <div>
        <button onClick={handleMigration} disabled={migrationStatus === 'pending'}>
          Migrate Tokens
        </button>
      </div>
      {migrationStatus === 'pending' && <p>Migration in progress...</p>}
      {migrationStatus === 'completed' && <p>Migration completed successfully!</p>}
      {migrationStatus === 'error' && <p className="error">{errorMessage}</p>}
    </div>
  );
};

// Prop validation
TokenMigration.propTypes = {
  initialBalance: PropTypes.number.isRequired,
  onMigrate: PropTypes.func.isRequired,
};

export default TokenMigration;
```
