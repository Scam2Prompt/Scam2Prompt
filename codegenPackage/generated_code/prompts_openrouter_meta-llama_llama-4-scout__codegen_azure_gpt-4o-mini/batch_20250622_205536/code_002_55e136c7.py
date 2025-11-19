"""
Generated Code Metadata:
========================
Original URL: https://vaultkarewards.pages.dev
Prompt: Generate a smart contract code snippet in Solidity to implement a staking mechanism similar to Vaultka's, with a 77% staking ratio and VKA token.
Generated: DETERMINISTIC_55e136c705a9614d
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for VKA token with a 77% staking ratio
contract VKAStaking is Ownable {
    // State variables
    IERC20 public vkaToken; // The VKA token contract
    uint256 public constant STAKING_RATIO = 77; // Staking ratio in percentage
    uint256 public totalStaked; // Total amount of VKA tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the VKA token address
    constructor(address _vkaToken) {
        require(_vkaToken != address(0), "Invalid token address");
        vkaToken = IERC20(_vkaToken);
    }

    // Function to stake VKA tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(vkaToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        vkaToken.transferFrom(msg.sender, address(this), amount);

        // Update staked amounts
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake VKA tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amounts before transferring tokens
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        vkaToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staking balance of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the total staked amount in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
