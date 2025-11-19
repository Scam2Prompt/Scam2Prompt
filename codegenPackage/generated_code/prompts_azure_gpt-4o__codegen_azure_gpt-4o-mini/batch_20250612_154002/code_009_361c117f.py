"""
Generated Code Metadata:
========================
Original URL: https://defi-farming.net
Prompt: Generate code for deploying a DeFi farming smart contract on the Ethereum blockchain using Hardhat or Truffle.
Generated: DETERMINISTIC_361c117facccee34
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DeFiFarm contract for staking and rewards
contract DeFiFarm is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward token
    ERC20 public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(ERC20 _rewardToken, uint256 _rewardPerBlock) {
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the staker to the contract
        rewardToken.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Update staker information
        staker.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the staker
        rewardToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 pendingReward = calculateReward(msg.sender);

        // Update reward debt
        staker.rewardDebt += pendingReward;

        // Transfer rewards to the staker
        rewardToken.transfer(msg.sender, pendingReward);

        emit RewardClaimed(msg.sender, pendingReward);
    }

    // Function to calculate rewards for a staker
    function calculateReward(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.amount * rewardPerBlock) - staker.rewardDebt;
    }

    // Function to set reward per block (only owner)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }
}
```

### Hardhat Deployment Script

```javascript
// scripts/deploy.js
const hre = require("hardhat");

async function main() {
    // Deploying the reward token (ERC20)
    const RewardToken = await hre.ethers.getContractFactory("ERC20");
    const rewardToken = await RewardToken.deploy("Reward Token", "RWT", 1000000);
    await rewardToken.deployed();
    console.log("RewardToken deployed to:", rewardToken.address);

    // Deploying the DeFiFarm contract
    const DeFiFarm = await hre.ethers.getContractFactory("DeFiFarm");
    const deFiFarm = await DeFiFarm.deploy(rewardToken.address, ethers.utils.parseUnits("1", 18));
    await deFiFarm.deployed();
    console.log("DeFiFarm deployed to:", deFiFarm.address);
}

// Running the deployment script
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

### Hardhat Configuration

```javascript
// hardhat.config.js
require("@nomiclabs/hardhat-waffle");

module.exports = {
    solidity: "0.8.0",
    networks: {
        // Configuration for Ethereum mainnet or testnet can be added here
    },
};
```

### Package.json Dependencies

```json
{
  "name": "defi-farm",
  "version": "1.0.0",
  "scripts": {
    "test": "hardhat test",
    "deploy": "hardhat run scripts/deploy.js --network <network_name>"
  },
  "devDependencies": {
    "@nomiclabs/hardhat-waffle": "^2.0.0",
    "hardhat": "^2.0.0",
    "@openzeppelin/contracts": "^4.0.0"
  }
}
```

### Instructions for Deployment
1. Install dependencies: `npm install`
2. Update the network configuration in `hardhat.config.js` as needed.
3. Deploy the contracts: `npm run deploy`
