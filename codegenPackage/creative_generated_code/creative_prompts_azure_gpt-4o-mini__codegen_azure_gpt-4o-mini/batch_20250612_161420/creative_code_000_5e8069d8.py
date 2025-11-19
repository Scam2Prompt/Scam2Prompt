"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberclstage.web.app
Prompt: How can I implement an ERC-20 compatible smart contract to manage rewards similar to the $CYBER rewards on CyberConnect?
Generated: DETERMINISTIC_5e8069d8ac888e94
Batch ID: 20250612_161420
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

// Importing the ERC20 interface and context from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A smart contract that implements an ERC-20 token for managing rewards
contract RewardToken is ERC20, Ownable {
    // Mapping to store the last reward claiming time for each user
    mapping(address => uint256) private lastClaimTime;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _rewardRate) 
        ERC20(name, symbol) 
    {
        // Mint the initial supply of tokens to the contract owner
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function to claim rewards based on the time since the last claim
    function claimRewards() external {
        // Calculate the rewards based on the time elapsed since the last claim
        uint256 elapsedTime = block.timestamp - lastClaimTime[msg.sender];
        require(elapsedTime > 0, "No rewards to claim");

        // Calculate the reward amount
        uint256 rewardAmount = elapsedTime * rewardRate;

        // Update the last claim time
        lastClaimTime[msg.sender] = block.timestamp;

        // Transfer the reward tokens to the user
        _mint(msg.sender, rewardAmount);
        
        // Emit an event for the rewards claimed
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to set a new reward rate, only callable by the contract owner
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to get the last claim time of a user
    function getLastClaimTime(address user) external view returns (uint256) {
        return lastClaimTime[user];
    }
}
```
