"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Design a decentralized finance application using Código's CIDL and generate the necessary smart contract boilerplate code and client libraries.
Generated: DETERMINISTIC_f0bf787a4f2e25d5
Batch ID: 20250622_211342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Solidity for the smart contract and JavaScript for the client library. I'll use OpenZeppelin's contracts for the ERC20 token and assume CIDL (Contract Interface Description Language) is similar to OpenZeppelin's contract structure.

**Decentralized Finance Application Smart Contract (Solidity)**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Decentralized Finance Application Smart Contract
 * @author [Your Name]
 * @notice This contract manages a decentralized finance application
 */
contract DecentralizedFinanceApp is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of user balances
    mapping(address => uint256) public userBalances;

    // Mapping of investment plans
    mapping(uint256 => InvestmentPlan) public investmentPlans;

    // Investment plan ID counter
    uint256 public investmentPlanIdCounter;

    /**
     * @dev Investment plan structure
     */
    struct InvestmentPlan {
        uint256 id;
        uint256 minInvestment;
        uint256 maxInvestment;
        uint256 interestRate;
        uint256 duration;
        bool active;
    }

    /**
     * @dev Constructor
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Create a new investment plan
     * @param minInvestment Minimum investment amount
     * @param maxInvestment Maximum investment amount
     * @param interestRate Interest rate
     * @param duration Investment duration
     */
    function createInvestmentPlan(
        uint256 minInvestment,
        uint256 maxInvestment,
        uint256 interestRate,
        uint256 duration
    ) public onlyOwner {
        investmentPlanIdCounter++;
        investmentPlans[investmentPlanIdCounter] = InvestmentPlan(
            investmentPlanIdCounter,
            minInvestment,
            maxInvestment,
            interestRate,
            duration,
            true
        );
    }

    /**
     * @dev Invest in a plan
     * @param planId Investment plan ID
     * @param amount Investment amount
     */
    function invest(uint256 planId, uint256 amount) public {
        require(investmentPlans[planId].active, "Plan not active");
        require(amount >= investmentPlans[planId].minInvestment, "Insufficient investment amount");
        require(amount <= investmentPlans[planId].maxInvestment, "Exceeds maximum investment amount");

        userBalances[msg.sender] += amount;
        _mint(address(this), amount);
    }

    /**
     * @dev Withdraw from a plan
     * @param planId Investment plan ID
     * @param amount Withdrawal amount
     */
    function withdraw(uint256 planId, uint256 amount) public {
        require(investmentPlans[planId].active, "Plan not active");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        userBalances[msg.sender] -= amount;
        _burn(address(this), amount);
    }

    /**
     * @dev Get user balance
     * @param user User address
     * @return User balance
     */
    function getUserBalance(address user) public view returns (uint256) {
        return userBalances[user];
    }
}
```

**Client Library (JavaScript)**
```javascript
const Web3 = require('web3');
const { DecentralizedFinanceApp } = require('./DecentralizedFinanceApp');

/**
 * @class DecentralizedFinanceAppClient
 */
class DecentralizedFinanceAppClient {
  /**
   * @dev Constructor
   * @param web3 Web3 instance
   * @param contractAddress Contract address
   */
  constructor(web3, contractAddress) {
    this.web3 = web3;
    this.contract = new web3.eth.Contract(DecentralizedFinanceApp.abi, contractAddress);
  }

  /**
   * @dev Create a new investment plan
   * @param minInvestment Minimum investment amount
   * @param maxInvestment Maximum investment amount
   * @param interestRate Interest rate
   * @param duration Investment duration
   * @returns Transaction hash
   */
  async createInvestmentPlan(minInvestment, maxInvestment, interestRate, duration) {
    try {
      const accounts = await this.web3.eth.getAccounts();
      const tx = await this.contract.methods.createInvestmentPlan(minInvestment, maxInvestment, interestRate, duration).send({ from: accounts[0] });
      return tx.transactionHash;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }

  /**
   * @dev Invest in a plan
   * @param planId Investment plan ID
   * @param amount Investment amount
   * @returns Transaction hash
   */
  async invest(planId, amount) {
    try {
      const accounts = await this.web3.eth.getAccounts();
      const tx = await this.contract.methods.invest(planId, amount).send({ from: accounts[0], value: amount });
      return tx.transactionHash;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }

  /**
   * @dev Withdraw from a plan
   * @param planId Investment plan ID
   * @param amount Withdrawal amount
   * @returns Transaction hash
   */
  async withdraw(planId, amount) {
    try {
      const accounts = await this.web3.eth.getAccounts();
      const tx = await this.contract.methods.withdraw(planId, amount).send({ from: accounts[0] });
      return tx.transactionHash;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }

  /**
   * @dev Get user balance
   * @param user User address
   * @returns User balance
   */
  async getUserBalance(user) {
    try {
      const balance = await this.contract.methods.getUserBalance(user).call();
      return balance;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }
}

module.exports = DecentralizedFinanceAppClient;
```

**DecentralizedFinanceApp ABI (JSON)**
```json
[
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "name",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "symbol",
        "type": "string"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "investmentPlanIdCounter",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "investmentPlans",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "id",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "minInvestment",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "maxInvestment",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "interestRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "duration",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "active",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name
