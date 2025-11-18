"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berryeth.vip
Prompt: Create a DApp frontend using React.js that displays the $BERRY token chart and allows users to claim tokens directly from the contract.
Generated: DETERMINISTIC_4e9dedb4f46a572c
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: src/App.js
import React, { useState, useEffect } from "react";
import Web3 from "web3";
import Chart from "chart.js/auto";
import "./App.css";

// Replace with your $BERRY token contract ABI and address
const TOKEN_CONTRACT_ABI = [{ /* Your contract ABI */ }];
const TOKEN_CONTRACT_ADDRESS = "0xYourTokenContractAddress";

// Main React component
const App = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [contract, setContract] = useState(null);
  const [claiming, setClaiming] = useState(false);

  useEffect(() => {
    // Initialize Web3 and load user account
    const initWeb3 = async () => {
      if (window.ethereum) {
        try {
          const web3Instance = new Web3(window.ethereum);
          await window.ethereum.request({ method: "eth_requestAccounts" });
          const accounts = await web3Instance.eth.getAccounts();
          setWeb3(web3Instance);
          setAccount(accounts[0]);

          const tokenContract = new web3Instance.eth.Contract(
            TOKEN_CONTRACT_ABI,
            TOKEN_CONTRACT_ADDRESS
          );
          setContract(tokenContract);
        } catch (error) {
          console.error("Error initializing Web3:", error);
        }
      } else {
        alert("Please install MetaMask to use this DApp!");
      }
    };

    initWeb3();
  }, []);

  useEffect(() => {
    // Fetch and render $BERRY token chart
    const fetchChartData = async () => {
      try {
        // Replace with actual logic to fetch token price data
        const mockData = [
          { time: "2023-01-01", value: 0.5 },
          { time: "2023-02-01", value: 0.7 },
          { time: "2023-03-01", value: 0.6 },
          { time: "2023-04-01", value: 0.8 },
        ];

        const ctx = document.getElementById("berryTokenChart").getContext("2d");
        new Chart(ctx, {
          type: "line",
          data: {
            labels: mockData.map((data) => data.time),
            datasets: [
              {
                label: "$BERRY Token Price (USD)",
                data: mockData.map((data) => data.value),
                borderColor: "#4CAF50",
                backgroundColor: "rgba(76, 175, 80, 0.1)",
              },
            ],
          },
          options: {
            responsive: true,
            plugins: {
              legend: { display: true },
            },
          },
        });
      } catch (error) {
        console.error("Error fetching chart data:", error);
      }
    };

    fetchChartData();
  }, []);

  const claimTokens = async () => {
    if (!contract || !account) {
      alert("Please connect your wallet before claiming tokens!");
      return;
    }

    setClaiming(true);

    try {
      // Call claim function from the contract (replace with actual method name)
      await contract.methods.claimTokens().send({ from: account });
      alert("Tokens successfully claimed!");
    } catch (error) {
      console.error("Error claiming tokens:", error);
      alert("Failed to claim tokens. Please try again.");
    }

    setClaiming(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>$BERRY Token DApp</h1>
        <p>Connected Account: {account || "Not connected"}</p>
      </header>

      <main>
        <div className="chart-container">
          <canvas id="berryTokenChart"></canvas>
        </div>

        <button
          onClick={claimTokens}
          disabled={claiming}
          className={`claim-button ${claiming ? "disabled" : ""}`}
        >
          {claiming ? "Claiming..." : "Claim $BERRY Tokens"}
        </button>
      </main>
    </div>
  );
};

export default App;

// File: src/App.css
.App {
  text-align: center;
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

.App-header {
  background-color: #282c34;
  padding: 20px;
  color: white;
}

.chart-container {
  width: 80%;
  margin: 20px auto;
}

.claim-button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.claim-button.disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

// File: src/index.js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
```

### Notes:
1. Replace `TOKEN_CONTRACT_ABI` and `TOKEN_CONTRACT_ADDRESS` with actual contract details.
2. Ensure the `claimTokens` method name matches the smart contract method syntax.
3. Use proper API or data source for fetching real token price data.
