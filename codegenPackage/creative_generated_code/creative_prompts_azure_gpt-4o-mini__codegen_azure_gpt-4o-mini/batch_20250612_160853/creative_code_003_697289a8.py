"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-dapps.pages.dev
Prompt: How can I use the $HEHE token in a decentralized finance (DeFi) application? Provide an example of integrating it into a yield farming protocol.
Generated: DETERMINISTIC_697289a86ca63d84
Batch ID: 20250612_160853
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple yield farming contract for the $HEHE token
contract YieldFarming is Ownable {
    // The $HEHE token contract
    IERC20 public token;

    // User stake information
    struct UserStake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the last stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => UserStake) public stakes;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(address _token) {
        token = IERC20(_token);
    }

    // Modifier to check if the user has staked tokens
    modifier hasStaked() {
        require(stakes[msg.sender].amount > 0, "No tokens staked");
        _;
    }

    // Function to stake $HEHE tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        UserStake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external hasStaked {
        UserStake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= amount;

        // Transfer the tokens back to the user
        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the staked amount of a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to withdraw all staked tokens (emergency use case)
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance > 0, "No funds to withdraw");
        require(token.transfer(msg.sender, contractBalance), "Transfer failed");
    }
}
```

Note: To deploy this contract, you will need to have the OpenZeppelin Contracts library installed in your project. You can do this using npm:

```bash
npm install @openzeppelin/contracts
```

Make sure to replace the `address _token` in the constructor with the actual deployed address of the $HEHE token when deploying this contract.
