"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-dapps.vercel.app
Prompt: Generate a code example to integrate Sui's zkLogin feature for secure authentication in a decentralized finance platform.
Generated: DETERMINISTIC_4440eb74b8432a0e
Batch ID: 20250612_155006
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://sui.api.url": {
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
// Importing necessary libraries
import { useState, useEffect } from 'react';
import { SuiClient } from '@sui/sui-client';
import { zkLogin } from '@sui/zk-login';

const ZkLoginComponent = () => {
  // State to store user data and loading status
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Initialize Sui Client
  const suiClient = new SuiClient({
    apiUrl: 'https://sui.api.url',
  });

  // Function to handle login process
  const handleZkLogin = async () => {
    setLoading(true);
    setError(null);

    try {
      // Perform zkLogin to get user credentials
      const credentials = await zkLogin();

      // Authenticate with the Sui Client
      const response = await suiClient.authenticate(credentials);

      // Check if authentication is successful
      if (response.success) {
        setUserData(response.userData);
      } else {
        throw new Error('Authentication failed');
      }
    } catch (err) {
      // Handle errors and set error state
      console.error('Error during zkLogin:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Effect to handle user session on component mount
  useEffect(() => {
    const checkUserSession = async () => {
      setLoading(true);
      try {
        const sessionData = await suiClient.getSession();
        if (sessionData) {
          setUserData(sessionData.user);
        }
      } catch (err) {
        console.error('Error fetching session data:', err);
      } finally {
        setLoading(false);
      }
    };

    checkUserSession();
  }, [suiClient]);

  return (
    <div>
      <h1>Secure ZK Login</h1>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {userData ? (
        <div>
          <h2>Welcome, {userData.name}!</h2>
          <p>Your wallet address: {userData.walletAddress}</p>
        </div>
      ) : (
        <button onClick={handleZkLogin}>Login with ZK</button>
      )}
    </div>
  );
};

export default ZkLoginComponent;
```
