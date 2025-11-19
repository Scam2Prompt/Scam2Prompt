"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bullperks.pages.dev
Prompt: Explain how to implement a staking mechanism for BLP tokens within the BullPerks ecosystem, including sample code.
Generated: DETERMINISTIC_0dac82a02aaf1a81
Batch ID: 20250612_161035
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A contract for staking BLP tokens
contract BLPStaking is Ownable {
    // Token interface for BLP tokens
    IERC20 public blpToken;

    // Structure to keep track of each user's staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Time of staking
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) private stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the BLP token address
    constructor(address _blpToken) {
        require(_blpToken != address(0), "Invalid BLP token address");
        blpToken = IERC20(_blpToken);
    }

    // Function to stake BLP tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(blpToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer the tokens from the user to the contract
        blpToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake BLP tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Reduce user's stake amount
        stakes[msg.sender].amount -= amount;

        // Transfer the tokens back to the user
        blpToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the user's stake information
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }

    // Function to withdraw all staked tokens (for owner, if needed)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(blpToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        blpToken.transfer(msg.sender, amount);
    }
}
```

### Notes:
- This smart contract allows users to stake and unstake their BLP tokens.
- The contract correctly utilizes OpenZeppelin's contracts for ERC20 compatibility and ownership management.
- Events are emitted for staking and unstaking actions for better tracking and logging.
- Error handling is incorporated through require statements to prevent invalid operations.
