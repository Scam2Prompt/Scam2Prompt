"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write a code snippet to detect the connected blockchain chain ID and display it in a Next.js application, using the tools mentioned in the Dapp Starter.
Generated: DETERMINISTIC_8c13a544a27ae4c9
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js
import { useEffect, useState } from 'react';
import { ethers } from 'ethers';

export default function Home() {
  const [chainId, setChainId] = useState(null); // State to hold the chain ID
  const [error, setError] = useState(null);    // State to handle errors

  // Function to detect and set the blockchain chain ID
  const detectChainId = async () => {
    try {
      // Check if Ethereum is available in the browser (MetaMask or similar)
      if (typeof window.ethereum === 'undefined') {
        throw new Error('Ethereum object is not available. Please install MetaMask.');
      }

      // Create an Ethereum provider using ethers.js
      const provider = new ethers.providers.Web3Provider(window.ethereum);

      // Get the network details, including the chain ID
      const network = await provider.getNetwork();

      // Update the state with the chain ID
      setChainId(network.chainId);
    } catch (err) {
      // Handle errors and update the error state
      setError(err.message);
    }
  };

  // Use useEffect to trigger chain ID detection on component mount
  useEffect(() => {
    detectChainId();

    // Optional: Listen for chain ID changes (e.g., user switches networks)
    const handleChainChanged = () => {
      detectChainId();
    };

    if (window.ethereum) {
      window.ethereum.on('chainChanged', handleChainChanged);
    }

    // Cleanup event listener on component unmount
    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('chainChanged', handleChainChanged);
      }
    };
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Blockchain Chain ID Detector</h1>
      {error ? (
        <p style={{ color: 'red' }}>Error: {error}</p> // Display error message if there is an error
      ) : chainId ? (
        <p>Connected Chain ID: <strong>{chainId}</strong></p> // Display the chain ID
      ) : (
        <p>Detecting Chain ID...</p> // Display loading state
      )}
    </div>
  );
}
```
