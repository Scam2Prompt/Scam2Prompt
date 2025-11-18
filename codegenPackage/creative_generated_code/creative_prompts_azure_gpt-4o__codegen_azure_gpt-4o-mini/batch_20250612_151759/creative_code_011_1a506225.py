"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe--dashboard.pages.dev
Prompt: Write a Solidity function for distributing rewards automatically to users participating in a sports betting platform powered by $MPEPE tokens.
Generated: DETERMINISTIC_1a50622533f45597
Batch ID: 20250612_151759
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

// Interface for ERC20 token contract
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Main contract for the sports betting platform
contract SportsBetting {
    // State variables
    IERC20 public mpepeToken; // The ERC20 token used for rewards
    mapping(address => uint256) public userRewards; // Mapping of user addresses to their rewards

    // Event to log reward distribution
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(address _mpepeToken) {
        require(_mpepeToken != address(0), "Invalid token address");
        mpepeToken = IERC20(_mpepeToken);
    }

    // Function to distribute rewards to users
    function distributeRewards(address[] calldata users, uint256[] calldata amounts) external {
        require(users.length == amounts.length, "Users and amounts length mismatch");

        uint256 totalRewards = 0; // Variable to track total rewards to be distributed

        // Calculate total rewards to be distributed
        for (uint256 i = 0; i < amounts.length; i++) {
            require(amounts[i] > 0, "Amount must be greater than zero");
            userRewards[users[i]] += amounts[i]; // Update user rewards
            totalRewards += amounts[i]; // Add to total rewards
        }

        // Check the contract's balance before transferring
        require(mpepeToken.balanceOf(address(this)) >= totalRewards, "Insufficient balance for distribution");

        // Distribute rewards to each user
        for (uint256 i = 0; i < users.length; i++) {
            uint256 amount = amounts[i];
            address user = users[i];
            if (userRewards[user] > 0) {
                require(mpepeToken.transfer(user, userRewards[user]), "Transfer failed");
                emit RewardsDistributed(user, userRewards[user]); // Emit event
                userRewards[user] = 0; // Reset user reward after distribution
            }
        }
    }

    // Function to retrieve the balance of the contract
    function contractBalance() external view returns (uint256) {
        return mpepeToken.balanceOf(address(this));
    }
}
```
