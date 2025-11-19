"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write a code snippet to detect the connected blockchain chain ID and display it in a Next.js application, using the tools mentioned in the Dapp Starter.
Generated: DETERMINISTIC_8c13a544a27ae4c9
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { useEffect, useState } from 'react';
import Web3 from 'web3';

// Define the component
const ChainIdDisplay = () => {
  // State to hold the chain ID
  const [chainId, setChainId] = useState(null);
  const [error, setError] = useState(null);

  // Function to detect the connected blockchain chain ID
  const detectChainId = async () => {
    try {
      // Check if window.ethereum is available (MetaMask or other wallet)
      if (window.ethereum) {
        // Create a new instance of Web3
        const web3 = new Web3(window.ethereum);
        
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the chain ID
        const id = await web3.eth.getChainId();
        setChainId(id);
      } else {
        throw new Error('Ethereum provider not found. Please install MetaMask or another wallet.');
      }
    } catch (err) {
      // Handle errors and set error state
      console.error('Error detecting chain ID:', err);
      setError(err.message);
    }
  };

  // Use effect to detect chain ID on component mount
  useEffect(() => {
    detectChainId();
  }, []);

  // Render the component
  return (
    <div>
      <h1>Connected Blockchain Chain ID</h1>
      {error ? (
        <p style={{ color: 'red' }}>{error}</p>
      ) : (
        <p>{chainId !== null ? `Chain ID: ${chainId}` : 'Loading...'}</p>
      )}
    </div>
  );
};

// Export the component for use in other parts of the application
export default ChainIdDisplay;
```
