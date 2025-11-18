"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-three.vercel.app
Prompt: Create a React app with a button that triggers MetaMask to request wallet connection and logs the connected account to the console.
Generated: DETERMINISTIC_bf8a05066711d74f
Batch ID: 20250612_150052
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
import ReactDOM from 'react-dom';

// Main App component
const App = () => {
    // State to hold the connected account
    const [account, setAccount] = useState(null);

    // Function to connect to MetaMask
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

                // Set the first account as the connected account
                setAccount(accounts[0]);
                console.log('Connected account:', accounts[0]);
            } catch (error) {
                // Handle error cases
                if (error.code === 4001) {
                    console.error('User rejected the request.');
                } else {
                    console.error('Error connecting to MetaMask:', error);
                }
            }
        } else {
            console.error('MetaMask is not installed. Please install it to use this app.');
        }
    };

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>MetaMask Wallet Connection</h1>
            <button onClick={connectWallet}>Connect Wallet</button>
            {account && <p>Connected Account: {account}</p>}
        </div>
    );
};

// Render the App component to the DOM
ReactDOM.render(<App />, document.getElementById('root'));
```

### Instructions for Setup:
1. Create a new React application using Create React App:
   ```bash
   npx create-react-app my-metamask-app
   cd my-metamask-app
   ```

2. Replace the content of `src/App.js` with the provided code.

3. Ensure you have MetaMask installed in your browser.

4. Start the application:
   ```bash
   npm start
   ```

5. Open the application in your browser to see the button for connecting to MetaMask.
