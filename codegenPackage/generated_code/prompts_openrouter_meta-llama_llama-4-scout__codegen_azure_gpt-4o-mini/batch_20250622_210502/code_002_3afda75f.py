"""
Generated Code Metadata:
========================
Original URL: https://cybro-en.pages.dev
Prompt: "Generate a smart contract code for a liquidity pool on Blast L2, similar to CYBRO's native staking."
Generated: DETERMINISTIC_3afda75fab07d322
Batch ID: 20250622_210502
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// LiquidityPool contract for managing liquidity and staking
contract LiquidityPool is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public token; // The token that will be staked
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastStakedTime; // Last time the user staked

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Update state variables
        stakedAmount[msg.sender] = stakedAmount[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        lastStakedTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update state variables
        stakedAmount[msg.sender] = stakedAmount[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to the user
        token.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get total staked tokens in the pool
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Insufficient contract balance");
        token.transfer(msg.sender, amount);
    }
}
```
