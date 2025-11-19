"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamuscklog.godaddysites.com
Prompt: Provide an example of using MetaMask for authentication in a Web3 application.
Generated: DETERMINISTIC_dbdda8355a021caf
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

const App = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Check if MetaMask is installed
        if (window.ethereum) {
            const web3Instance = new Web3(window.ethereum);
            setWeb3(web3Instance);
            // Request account access
            window.ethereum.request({ method: 'eth_requestAccounts' })
                .then(accounts => {
                    setAccount(accounts[0]);
                })
                .catch(err => {
                    setError('Failed to connect to MetaMask: ' + err.message);
                });
        } else {
            setError('MetaMask is not installed. Please install it to use this app.');
        }
    }, []);

    // Function to handle logout
    const handleLogout = () => {
        setAccount(null);
    };

    return (
        <div>
            <h1>MetaMask Authentication</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={handleLogout}>Logout</button>
                </div>
            ) : (
                <p>Please connect your MetaMask wallet.</p>
            )}
        </div>
    );
};

export default App;
```

### Package.json dependencies
Make sure to include the following dependencies in your `package.json` file:
```json
{
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "web3": "^1.5.0"
  }
}
```

### Running the Application
1. Ensure you have Node.js and npm installed.
2. Create a new React app using `create-react-app`.
3. Replace the contents of `src/App.js` with the provided code.
4. Install the required dependencies using `npm install`.
5. Run the application with `npm start`.
