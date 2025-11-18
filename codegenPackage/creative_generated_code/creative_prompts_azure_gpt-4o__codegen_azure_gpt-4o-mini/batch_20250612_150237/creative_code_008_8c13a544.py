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
// Import necessary hooks and components from React and Next.js
import { useEffect, useState } from 'react';

// Function to detect the connected blockchain chain ID
const useChainId = () => {
  const [chainId, setChainId] = useState(null); // State to hold the chain ID

  useEffect(() => {
    // Function to handle chain ID changes
    const handleChainChanged = (chainId) => {
      console.log(`Chain changed to: ${chainId}`);
      setChainId(chainId); // Update state with new chain ID
    };

    // Check for Ethereum provider (e.g., MetaMask)
    const { ethereum } = window;

    if (ethereum) {
      // Set initial chain ID on load
      ethereum.request({ method: 'eth_chainId' })
        .then((id) => {
          console.log(`Connected to chain ID: ${id}`);
          setChainId(id);
        })
        .catch((error) => {
          console.error(`Failed to fetch chain ID: ${error.message}`);
        });

      // Listen for changes to the chain ID
      ethereum.on('chainChanged', handleChainChanged);

      // Clean up event listener on unmount
      return () => {
        ethereum.removeListener('chainChanged', handleChainChanged);
      };
    } else {
      console.error('Ethereum provider not found. Please install MetaMask or another wallet.');
    }
  }, []);

  return chainId; // Return the current chain ID
};

// Main component to display the connected chain ID
const ChainIdDisplay = () => {
  const chainId = useChainId(); // Get the current chain ID using the custom hook

  return (
    <div>
      <h1>Connected Blockchain Chain ID</h1>
      {chainId ? (
        <p>Chain ID: {chainId}</p> // Display the chain ID if available
      ) : (
        <p>Loading chain ID...</p> // Loading state while fetching chain ID
      )}
    </div>
  );
};

export default ChainIdDisplay; // Export the main component
```
