"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interface-git-web-1342-explore-token-details-sea-2009d5-uniswap.vercel.app
Prompt: Generate code for a web app that uses the Uniswap Interface to display token details, ensuring JavaScript is enabled.
Generated: DETERMINISTIC_2f41ed09053b533c
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from "react";
import { ethers } from "ethers";

// Constants
const UNISWAP_INTERFACE_ADDRESS = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"; // Uniswap Interface Address
const UNISWAP_INTERFACE_ABI = [
  // Minimal ABI for ERC20 tokens and Uniswap Factory
  {
    constant: true,
    inputs: [{ name: "_id", type: "uint256" }],
    name: "allPairs",
    outputs: [{ name: "", type: "address" }],
    payable: false,
    stateMutability: "view",
    type: "function",
  },
  {
    constant: true,
    inputs: [],
    name: "allPairsLength",
    outputs: [{ name: "", type: "uint256" }],
    payable: false,
    stateMutability: "view",
    type: "function",
  },
];

const ERC20_ABI = [
  {
    constant: true,
    inputs: [],
    name: "name",
    outputs: [{ name: "", type: "string" }],
    payable: false,
    stateMutability: "view",
    type: "function",
  },
  {
    constant: true,
    inputs: [],
    name: "symbol",
    outputs: [{ name: "", type: "string" }],
    payable: false,
    stateMutability: "view",
    type: "function",
  },
  {
    constant: true,
    inputs: [],
    name: "decimals",
    outputs: [{ name: "", type: "uint8" }],
    payable: false,
    stateMutability: "view",
    type: "function",
  },
];

const App = () => {
  const [tokens, setTokens] = useState([]); // State to store token details
  const [error, setError] = useState(null); // State to store errors

  useEffect(() => {
    const fetchTokenDetails = async () => {
      try {
        // Connecting to Ethereum provider (Metamask or other wallet)
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const uniswapInterface = new ethers.Contract(
          UNISWAP_INTERFACE_ADDRESS,
          UNISWAP_INTERFACE_ABI,
          provider
        );

        // Fetch the total number of pairs
        const pairCount = await uniswapInterface.allPairsLength();

        const tokenDetails = [];

        // Iterate through all pairs and fetch token details
        for (let i = 0; i < pairCount; i++) {
          const pairAddress = await uniswapInterface.allPairs(i);
          const tokenContract = new ethers.Contract(pairAddress, ERC20_ABI, provider);

          // Fetch token name, symbol, and decimals
          const name = await tokenContract.name();
          const symbol = await tokenContract.symbol();
          const decimals = await tokenContract.decimals();

          tokenDetails.push({ name, symbol, decimals });
        }

        // Update state with fetched tokens
        setTokens(tokenDetails);
      } catch (err) {
        // Handle errors (e.g., user not connected to wallet, network issues)
        setError("Failed to load token details. Please ensure your wallet is connected and try again.");
        console.error("Error fetching token details:", err);
      }
    };

    fetchTokenDetails();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Uniswap Token Details</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {tokens.length === 0 && !error && <p>Loading token details...</p>}
      {tokens.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Symbol</th>
              <th>Decimals</th>
            </tr>
          </thead>
          <tbody>
            {tokens.map((token, index) => (
              <tr key={index}>
                <td>{token.name}</td>
                <td>{token.symbol}</td>
                <td>{token.decimals}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default App;

// Ensure you have Metamask or another Ethereum wallet installed and connected.
// Run this React app using `npm start` or `yarn start` after adding it to a React project.
```
