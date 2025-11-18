"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shidoclaim.pages.dev
Prompt: Write code to implement staking functionality for Shido tokens, referencing the network's Proof-of-Stake mechanism and gas-free operations.
Generated: DETERMINISTIC_8d58e33fcf17c7a4
Batch ID: 20250612_152656
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token and ownership handling
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev This contract allows users to stake Shido tokens in a Proof-of-Stake mechanism.
 */
contract StakingContract is Ownable {
    // State variable to store the reference to the Shido token
    IERC20 public shidoToken;

    // Mapping to hold staked amounts for each address
    mapping(address => uint256) public stakes;

    // Event to notify when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event to notify when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract with the Shido token address.
     * @param _shidoToken Address of the Shido token contract.
     */
    constructor(address _shidoToken) {
        require(_shidoToken != address(0), "Invalid token address");
        shidoToken = IERC20(_shidoToken);
    }

    /**
     * @dev Function to stake Shido tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(shidoToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        shidoToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake Shido tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update the user's stake
        stakes[msg.sender] -= amount;

        // Transfer tokens back to the user
        shidoToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to get the staked amount of a user.
     * @param user Address of the user.
     * @return uint256 Amount staked by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    /**
     * @dev Function to withdraw any tokens sent to the contract by mistake (only owner).
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(shidoToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        shidoToken.transfer(msg.sender, amount);
    }
}
```
