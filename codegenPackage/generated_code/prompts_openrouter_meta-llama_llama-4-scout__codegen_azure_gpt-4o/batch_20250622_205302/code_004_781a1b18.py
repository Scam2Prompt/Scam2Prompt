"""
Generated Code Metadata:
========================
Original URL: https://bitcoin2.biz
Prompt: Design a user interface for a decentralized crypto exchange (DEX) like Uniswap, including features for listing ERC20 tokens.
Generated: DETERMINISTIC_781a1b188ff94be8
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a basic user interface for a decentralized crypto exchange (DEX) using React.js and Web3.js. This code includes features for listing ERC20 tokens.

```javascript
// File: src/App.js
import React, { useState, useEffect } from "react";
import Web3 from "web3";
import TokenList from "./components/TokenList";
import "./App.css";

// Constants
const ERC20_ABI = [
  {
    constant: true,
    inputs: [],
    name: "name",
    outputs: [{ name: "", type: "string" }],
    type: "function",
  },
  {
    constant: true,
    inputs: [],
    name: "symbol",
    outputs: [{ name: "", type: "string" }],
    type: "function",
  },
  {
    constant: true,
    inputs: [],
    name: "decimals",
    outputs: [{ name: "", type: "uint8" }],
    type: "function",
  },
  {
    constant: true,
    inputs: [{ name: "_owner", type: "address" }],
    name: "balanceOf",
    outputs: [{ name: "balance", type: "uint256" }],
    type: "function",
  },
];

function App() {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [tokens, setTokens] = useState([]);
  const [tokenAddress, setTokenAddress] = useState("");

  // Initialize Web3 and connect to wallet
  useEffect(() => {
    async function initWeb3() {
      if (window.ethereum) {
        try {
          const web3Instance = new Web3(window.ethereum);
          await window.ethereum.request({ method: "eth_requestAccounts" });
          const accounts = await web3Instance.eth.getAccounts();
          setWeb3(web3Instance);
          setAccount(accounts[0]);
        } catch (error) {
          console.error("Error connecting to wallet:", error);
        }
      } else {
        console.error("Ethereum wallet not detected.");
      }
    }
    initWeb3();
  }, []);

  // Add a new token to the list
  const addToken = async () => {
    if (!web3 || !tokenAddress) {
      alert("Please connect your wallet and enter a valid token address.");
      return;
    }

    try {
      const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);
      const name = await tokenContract.methods.name().call();
      const symbol = await tokenContract.methods.symbol().call();
      const decimals = await tokenContract.methods.decimals().call();
      const balance = await tokenContract.methods.balanceOf(account).call();

      const tokenData = {
        address: tokenAddress,
        name,
        symbol,
        decimals,
        balance: web3.utils.fromWei(balance, "ether"),
      };

      setTokens([...tokens, tokenData]);
      setTokenAddress(""); // Clear input field
    } catch (error) {
      console.error("Error fetching token data:", error);
      alert("Failed to fetch token data. Please check the token address.");
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Decentralized Crypto Exchange</h1>
        <p>Connected Account: {account || "Not connected"}</p>
      </header>

      <main>
        <section>
          <h2>Add ERC20 Token</h2>
          <input
            type="text"
            placeholder="Enter token address"
            value={tokenAddress}
            onChange={(e) => setTokenAddress(e.target.value)}
          />
          <button onClick={addToken}>Add Token</button>
        </section>

        <section>
          <h2>Token List</h2>
          <TokenList tokens={tokens} />
        </section>
      </main>
    </div>
  );
}

export default App;

// File: src/components/TokenList.js
import React from "react";
import PropTypes from "prop-types";

const TokenList = ({ tokens }) => {
  return (
    <div>
      {tokens.length === 0 ? (
        <p>No tokens added yet.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Symbol</th>
              <th>Decimals</th>
              <th>Balance</th>
              <th>Address</th>
            </tr>
          </thead>
          <tbody>
            {tokens.map((token, index) => (
              <tr key={index}>
                <td>{token.name}</td>
                <td>{token.symbol}</td>
                <td>{token.decimals}</td>
                <td>{token.balance}</td>
                <td>{token.address}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

TokenList.propTypes = {
  tokens: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string.isRequired,
      symbol: PropTypes.string.isRequired,
      decimals: PropTypes.number.isRequired,
      balance: PropTypes.string.isRequired,
      address: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default TokenList;

// File: src/App.css
.App {
  text-align: center;
  font-family: Arial, sans-serif;
}

.App-header {
  background-color: #282c34;
  padding: 20px;
  color: white;
}

input {
  margin: 10px;
  padding: 5px;
}

button {
  padding: 5px 10px;
  cursor: pointer;
}

table {
  margin: 20px auto;
  border-collapse: collapse;
  width: 80%;
}

table th,
table td {
  border: 1px solid #ddd;
  padding: 8px;
}

table th {
  background-color: #f2f2f2;
  text-align: left;
}
```

### Notes:
- This code assumes you have a React project set up (`npx create-react-app`).
- Install dependencies: `npm install web3 prop-types`.
- The `TokenList` component is used to display the list of added tokens.
- Error handling is included for wallet connection and token data fetching.
- Styling is basic and can be enhanced further.
