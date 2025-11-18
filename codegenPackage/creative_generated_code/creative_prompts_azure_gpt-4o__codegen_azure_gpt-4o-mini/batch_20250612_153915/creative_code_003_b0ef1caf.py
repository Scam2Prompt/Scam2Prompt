"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.me
Prompt: Create a smart contract for staking Toncoin on the TON blockchain and explain how to deploy it using TON tools.
Generated: DETERMINISTIC_b0ef1cafb1a2c627
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary libraries from the TON blockchain
import "@tonlabs/ton-core/contracts/TON.sol";

// Smart contract for staking Toncoin
contract ToncoinStaking {
    // Declare state variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public stakes; // Mapping to store stakes of each user
    mapping(address => uint256) public rewardDebt; // Mapping to store reward debts
    uint256 public totalStaked; // Total amount of Toncoin staked
    uint256 public rewardsPerToken; // Rewards distributed per token staked

    // Events to be emitted
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsUpdated(uint256 rewardsPerToken);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract creator as the owner
    }

    // Function to stake Toncoin
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 Toncoin");
        stakes[msg.sender] += amount; // Update user's stake
        totalStaked += amount; // Update total staked amount

        // Transfer Toncoin from user to contract
        TON.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount); // Emit Staked event
    }

    // Function to unstake Toncoin
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 Toncoin");
        require(stakes[msg.sender] >= amount, "Not enough staked Toncoin");

        stakes[msg.sender] -= amount; // Update user's stake
        totalStaked -= amount; // Update total staked amount

        // Transfer Toncoin from contract to user
        TON.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount); // Emit Unstaked event
    }

    // Function to update rewards
    function updateRewards(uint256 newRewardsPerToken) external onlyOwner {
        rewardsPerToken = newRewardsPerToken; // Update rewards per token
        emit RewardsUpdated(newRewardsPerToken); // Emit RewardsUpdated event
    }

    // Function to claim rewards (to be implemented)
    function claimRewards() external {
        // Logic for claiming rewards can be added here
    }

    // Function to get the current stakes of a user
    function getUserStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to get total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```

### Deployment Instructions

1. **Set up the TON SDK**: Install the TON SDK and set up your environment according to the official documentation.

2. **Compile the Smart Contract**:
   Use the TON compiler (`tondev` or equivalent) to compile the smart contract:
   ```bash
   tondev compile YourContractName.sol
   ```

3. **Deploy the Contract**:
   Use the deployment scripts provided by the TON SDK. Generally, you would use:
   ```bash
   tondev deploy YourContractName --constructor-params "[]" --sign
   ```

4. **Interact with the Smart Contract**:
   After deployment, you can interact with your smart contract using the TON CLI or by building a front-end application to communicate with the contract.

Make sure to test thoroughly on the testnet before deploying to the mainnet.
