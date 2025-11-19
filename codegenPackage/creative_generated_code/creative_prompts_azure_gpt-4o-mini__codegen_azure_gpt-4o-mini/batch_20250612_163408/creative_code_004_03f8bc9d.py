"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://docs.matrixinfos.com
Prompt: Develop a Solidity contract that facilitates the staking of $MATRIX Tokens, ensuring decentralized governance and user privacy.
Generated: DETERMINISTIC_03f8bc9d3a6d8f47
Batch ID: 20250612_163408
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

// Importing OpenZeppelin Contracts for safe ERC20 operations and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MatrixStaking
 * @dev A contract for staking MATRIX tokens with decentralized governance.
 */
contract MatrixStaking is Ownable {
    // Token to be staked
    IERC20 public matrixToken;

    // Struct to store user staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to track stakes of each user
    mapping(address => Stake) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 timestamp);

    /**
     * @dev Constructor to set MATRIX token address.
     * @param _matrixToken The address of the MATRIX token contract.
     */
    constructor(IERC20 _matrixToken) {
        require(address(_matrixToken) != address(0), "Invalid token address");
        matrixToken = _matrixToken;
    }

    /**
     * @dev Function to stake MATRIX tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to this contract
        matrixToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Function to withdraw staked MATRIX tokens.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount to withdraw");
        
        uint256 amountToWithdraw = userStake.amount;

        // Reset user's stake before transferring to prevent re-entrancy
        userStake.amount = 0;

        // Transfer staked tokens back to user
        matrixToken.transfer(msg.sender, amountToWithdraw);

        emit Withdrawn(msg.sender, amountToWithdraw, block.timestamp);
    }

    /**
     * @dev Function to get the staked amount of the user.
     * @param user The address of the user.
     * @return The amount of tokens staked by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
