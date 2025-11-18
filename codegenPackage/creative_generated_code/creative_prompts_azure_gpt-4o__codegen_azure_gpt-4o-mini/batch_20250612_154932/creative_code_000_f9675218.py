"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aria.fyi
Prompt: Write a smart contract in Solidity to interact with the ARIA20 token on Ethereum, including functions for staking and transferring tokens as described in the Arianee Protocol documentation.
Generated: DETERMINISTIC_f96752186bfc4788
Batch ID: 20250612_154932
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

// Importing ERC20 interface for interacting with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ARIA20 Staking Contract
 * @dev This contract allows users to stake ARIA20 tokens and manage their staking.
 */
contract ARIA20Staking is Ownable, ReentrancyGuard {
    // State variable for the ARIA20 token contract
    IERC20 public aria20Token;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to store user stakes
    mapping(address => Stake) public stakes;

    // Events for staking and withdrawing
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the ARIA20 token address
    constructor(address _aria20TokenAddress) {
        require(_aria20TokenAddress != address(0), "Invalid token address");
        aria20Token = IERC20(_aria20TokenAddress);
    }

    /**
     * @dev Allows a user to stake a specified amount of ARIA20 tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(aria20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= amount;

        // Transfer the tokens back to the user
        require(aria20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Returns the amount of staked tokens for a user.
     * @param user Address of the user.
     * @return The amount of staked tokens.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
    
    /**
     * @dev Allows the owner to set a new ARIA20 token contract address.
     * @param newAria20TokenAddress New token contract address.
     */
    function setAria20TokenAddress(address newAria20TokenAddress) external onlyOwner {
        require(newAria20TokenAddress != address(0), "Invalid token address");
        aria20Token = IERC20(newAria20TokenAddress);
    }
}
```
