"""
Generated Code Metadata:
========================
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Generate code to deploy a decentralized finance (DeFi) dapp on Linea's ecosystem, ensuring compatibility with its 100% EVM bytecode.
Generated: DETERMINISTIC_ebd550d35cc001cd
Batch ID: 20250612_152240
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://linea-mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/ERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/security/ReentrancyGuard.sol": {
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
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/security/ReentrancyGuard.sol";

/**
 * @title Linea DeFi Dapp
 * @author [Your Name]
 * @notice A decentralized finance (DeFi) dapp deployed on Linea's ecosystem.
 */
contract LineaDeFiDapp is ERC20, ReentrancyGuard {
    // Mapping of user balances
    mapping(address => uint256) public userBalances;

    // Event emitted when a user deposits funds
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user withdraws funds
    event Withdrawal(address indexed user, uint256 amount);

    // Event emitted when a user swaps tokens
    event Swap(address indexed user, uint256 amountIn, uint256 amountOut);

    /**
     * @dev Constructor function
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {}

    /**
     * @dev Deposit function
     * @param amount Amount to deposit
     */
    function deposit(uint256 amount) public nonReentrant {
        // Check if the amount is valid
        require(amount > 0, "Invalid deposit amount");

        // Update the user's balance
        userBalances[msg.sender] += amount;

        // Emit the deposit event
        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Withdrawal function
     * @param amount Amount to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant {
        // Check if the amount is valid
        require(amount > 0, "Invalid withdrawal amount");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance
        userBalances[msg.sender] -= amount;

        // Transfer the tokens to the user
        _transfer(address(this), msg.sender, amount);

        // Emit the withdrawal event
        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Swap function
     * @param amountIn Amount to swap in
     * @param amountOut Amount to swap out
     */
    function swap(uint256 amountIn, uint256 amountOut) public nonReentrant {
        // Check if the amounts are valid
        require(amountIn > 0, "Invalid swap amount in");
        require(amountOut > 0, "Invalid swap amount out");

        // Update the user's balance
        userBalances[msg.sender] -= amountIn;

        // Transfer the tokens to the contract
        _transfer(msg.sender, address(this), amountIn);

        // Emit the swap event
        emit Swap(msg.sender, amountIn, amountOut);
    }

    /**
     * @dev Fallback function
     */
    fallback() external payable {}

    /**
     * @dev Receive function
     */
    receive() external payable {}
}
```

```javascript
// deploy.js
const { ethers } = require("hardhat");

async function main() {
  // Get the contract factory
  const factory = await ethers.getContractFactory("LineaDeFiDapp");

  // Deploy the contract
  const contract = await factory.deploy("Linea DeFi Dapp", "LDD");

  // Wait for the contract to be deployed
  await contract.deployed();

  // Print the contract address
  console.log(`Contract deployed to: ${contract.address}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```json
// hardhat.config.js
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-waffle");

module.exports = {
  solidity: {
    compilers: [
      {
        version: "0.8.10",
        optimizer: {
          enabled: true,
          runs: 200,
        },
      },
    ],
  },
  networks: {
    linea: {
      url: "https://linea-mainnet.infura.io/v3/YOUR_PROJECT_ID",
      accounts: ["YOUR_PRIVATE_KEY"],
    },
  },
  etherscan: {
    apiKey: "YOUR_ETHERSCAN_API_KEY",
  },
};
```
