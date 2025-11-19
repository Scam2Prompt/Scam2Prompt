"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-humanizedai.web.app
Prompt: Develop a smart contract function to stake $HMZ tokens as described in the HumanizedAi presale documentation.
Generated: DETERMINISTIC_eed6816932fe1a9e
Batch ID: 20250612_160804
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

// Importing OpenZeppelin's ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Define the Staking contract
contract HMZStaking {
    // State variables
    IERC20 public hmzToken; // The token being staked
    mapping(address => uint256) public stakes; // Mapping of user addresses to their stakes
    mapping(address => uint256) public stakeTimestamps; // Record of when each user's stake was made
    uint256 public totalStaked; // Total amount of tokens staked

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the HMZ token address
    constructor(address _hmzToken) {
        require(_hmzToken != address(0), "Invalid token address");
        hmzToken = IERC20(_hmzToken);
    }

    // Function to stake $HMZ tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(hmzToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer tokens from the user to the contract
        bool success = hmzToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's stake and the total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;
        stakeTimestamps[msg.sender] = block.timestamp; // Record the stake time

        emit Staked(msg.sender, amount); // Emit the Staked event
    }

    // Function to unstake $HMZ tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update the user's stake and the total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the tokens back to the user
        bool success = hmzToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amount); // Emit the Unstaked event
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }
}
```
