"""
Generated Code Metadata:
========================
Original URL: https://dcqqb.com
Prompt: "Design a simple smart contract in Solidity for an Ethereum-based DeFi application and provide deployment instructions."
Generated: DETERMINISTIC_bbb100091e5fa80b
Batch ID: 20250622_211317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleDeFi
 * @dev A simple DeFi smart contract for depositing and withdrawing ETH with interest
 */
contract SimpleDeFi {
    // State variables
    address public owner;
    uint256 public totalDeposits;
    uint256 public constant INTEREST_RATE = 5; // 5% interest rate
    uint256 public constant MIN_DEPOSIT = 0.01 ether;
    uint256 public constant LOCK_PERIOD = 7 days;

    // Mapping to track user deposits and timestamps
    mapping(address => uint256) public deposits;
    mapping(address => uint256) public depositTimestamps;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 interest);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier validDeposit() {
        require(msg.value >= MIN_DEPOSIT, "Deposit amount too low");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Deposit ETH into the contract
     */
    function deposit() external payable validDeposit {
        deposits[msg.sender] += msg.value;
        depositTimestamps[msg.sender] = block.timestamp;
        totalDeposits += msg.value;

        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw deposited ETH plus interest
     */
    function withdraw() external {
        require(deposits[msg.sender] > 0, "No deposits found");
        require(
            block.timestamp >= depositTimestamps[msg.sender] + LOCK_PERIOD,
            "Funds are locked"
        );

        uint256 principal = deposits[msg.sender];
        uint256 interest = (principal * INTEREST_RATE) / 100;
        uint256 totalAmount = principal + interest;

        // Reset user's deposit before transfer to prevent reentrancy
        deposits[msg.sender] = 0;
        totalDeposits -= principal;

        // Transfer funds
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, principal, interest);
    }

    /**
     * @dev Get contract's ETH balance
     * @return The contract's current ETH balance
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Get user's current balance including accrued interest
     * @param _user The address of the user
     * @return The user's total balance (principal + interest)
     */
    function getUserBalance(address _user) external view returns (uint256) {
        if (deposits[_user] == 0) return 0;
        
        uint256 principal = deposits[_user];
        uint256 interest = (principal * INTEREST_RATE) / 100;
        return principal + interest;
    }

    /**
     * @dev Withdraw contract's ETH (owner only)
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed");
    }
}
```

### Deployment Instructions (using Hardhat):

1. Install required packages:
```bash
npm install --save-dev hardhat @nomiclabs/hardhat-waffle ethereum-waffle chai @nomiclabs/hardhat-ethers ethers
```

2. Create a `deploy.js` script:
```javascript
const hre = require("hardhat");

async function main() {
  const SimpleDeFi = await hre.ethers.getContractFactory("SimpleDeFi");
  const simpleDeFi = await SimpleDeFi.deploy();
  
  await simpleDeFi.deployed();
  console.log("SimpleDeFi deployed to:", simpleDeFi.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

3. Create a `hardhat.config.js`:
```javascript
require("@nomiclabs/hardhat-waffle");

module.exports = {
  solidity: "0.8.0",
  networks: {
    ropsten: {
      url: "YOUR_ROPSTEN_URL",
      accounts: ["YOUR_PRIVATE_KEY"]
    },
    mainnet: {
      url: "YOUR_MAINNET_URL",
      accounts: ["YOUR_PRIVATE_KEY"]
    }
  }
};
```

4. Compile and deploy:
```bash
npx hardhat compile
npx hardhat run scripts/deploy.js --network ropsten
```
