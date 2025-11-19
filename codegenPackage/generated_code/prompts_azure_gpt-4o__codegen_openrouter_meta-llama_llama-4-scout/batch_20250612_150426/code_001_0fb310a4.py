"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter.productsway.com
Prompt: Generate a script using Hardhat to deploy a smart contract and connect it to a DApp built with the Dapp Starter kit.
Generated: DETERMINISTIC_0fb310a4e5cc8eed
Batch ID: 20250612_150426
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rinkeby.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// hardhat.config.js
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-etherscan");
require("hardhat-gas-reporter");

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: "0.8.9",
  networks: {
    mainnet: {
      url: "https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
      accounts: ["YOUR_PRIVATE_KEY"],
    },
    rinkeby: {
      url: "https://rinkeby.infura.io/v3/YOUR_PROJECT_ID",
      accounts: ["YOUR_PRIVATE_KEY"],
    },
  },
  etherscan: {
    apiKey: "YOUR_ETHERSCAN_API_KEY",
  },
  gasReporter: {
    currency: "USD",
    gasPrice: 21,
    enabled: process.env.REPORT_GAS !== undefined,
    coinmarketcap: process.env.COINMARKETCAP_API_KEY,
  },
};
```

```javascript
// scripts/deploy.js
const { ethers } = require("hardhat");

async function main() {
  try {
    // Get the contract factory
    const contractFactory = await ethers.getContractFactory("YourContract");

    // Deploy the contract
    const contract = await contractFactory.deploy();

    // Wait for the contract to be deployed
    await contract.deployed();

    console.log(`Contract deployed to: ${contract.address}`);
  } catch (error) {
    console.error(error);
    process.exitCode = 1;
  }
}

main();
```

```solidity
// contracts/YourContract.sol
pragma solidity ^0.8.9;

contract YourContract {
    // Your contract code here
}
```

```javascript
// frontend/src/App.js
import Web3 from "web3";
import { YourContract } from "../build/YourContract";

const web3 = new Web3(window.ethereum);

const App = () => {
  const [account, setAccount] = useState("");
  const [contract, setContract] = useState(null);

  useEffect(() => {
    const init = async () => {
      try {
        const accounts = await web3.eth.getAccounts();
        setAccount(accounts[0]);

        const contractInstance = new web3.eth.Contract(
          YourContract.abi,
          YourContract.address
        );
        setContract(contractInstance);
      } catch (error) {
        console.error(error);
      }
    };
    init();
  }, []);

  const handleCallContract = async () => {
    try {
      const result = await contract.methods.yourContractMethod().call();
      console.log(result);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Your DApp</h1>
      <p>Account: {account}</p>
      <button onClick={handleCallContract}>Call Contract</button>
    </div>
  );
};

export default App;
```

```javascript
// frontend/src/index.js
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

```bash
# package.json
{
  "name": "your-dapp",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.1",
    "@testing-library/react": "^13.3.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web3": "^1.8.0",
    "web3-eth-contracts": "^1.8.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": ["react-app", "react-app/jest"]
  }
}
```
