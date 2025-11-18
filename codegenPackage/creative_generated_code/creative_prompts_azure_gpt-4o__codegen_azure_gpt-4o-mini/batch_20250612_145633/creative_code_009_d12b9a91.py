"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeindexlive.pages.dev
Prompt: Create a step-by-step guide for implementing a staking rewards system for $MEMEX tokens using a blockchain framework like Hardhat or Truffle.
Generated: DETERMINISTIC_d12b9a9118a11955
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary Hardhat libraries
const { ethers } = require("hardhat");

async function main() {
    // Compile the contracts
    await hre.run('compile');

    // Deploy the MEMEX token contract
    const MEMEX = await ethers.getContractFactory("MEMEX");
    const memex = await MEMEX.deploy();
    await memex.deployed();
    console.log("MEMEX Token deployed to:", memex.address);

    // Deploy the Staking contract
    const Staking = await ethers.getContractFactory("Staking");
    const staking = await Staking.deploy(memex.address);
    await staking.deployed();
    console.log("Staking contract deployed to:", staking.address);

    // Transfer some tokens to the Staking contract for rewards
    const rewardAmount = ethers.utils.parseUnits("10000.0", 18); // 10,000 MEMEX tokens
    await memex.transfer(staking.address, rewardAmount);
    console.log(`Transferred ${rewardAmount.toString()} MEMEX tokens to the Staking contract.`);
}

// Error handling to catch any issues during deployment
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });

// MEMEX Token Contract
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MEMEX is ERC20 {
    constructor() ERC20("MEMEX Token", "MEMEX") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1,000,000 MEMEX tokens to the deployer
    }
}

// Staking Contract
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract Staking is ReentrancyGuard {
    IERC20 public memexToken; // Reference to the MEMEX token
    mapping(address => uint256) public stakes; // User stakes
    mapping(address => uint256) public rewards; // User rewards
    uint256 public rewardRate = 100; // Reward rate (MEMEX tokens per block)

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the MEMEX token address
    constructor(address _memexToken) {
        memexToken = IERC20(_memexToken);
    }

    // Function to stake MEMEX tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        stakes[msg.sender] += amount; // Update user's stake
        memexToken.transferFrom(msg.sender, address(this), amount); // Transfer tokens to the contract
        emit Staked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0; // Reset rewards before transfer
        memexToken.transfer(msg.sender, reward); // Transfer rewards to user
        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards
    function calculateReward(address user) internal view returns (uint256) {
        return stakes[user] * rewardRate; // Simple reward calculation
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
