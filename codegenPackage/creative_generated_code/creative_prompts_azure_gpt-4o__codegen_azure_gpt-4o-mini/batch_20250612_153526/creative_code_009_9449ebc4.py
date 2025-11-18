"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelpdao-io.pages.dev
Prompt: Generate code to integrate Kelp DAO's rsETH token into a DeFi lending platform, ensuring users can access restaking rewards while maintaining liquidity.
Generated: DETERMINISTIC_9449ebc498f73ea0
Batch ID: 20250612_153526
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Kelp DAO rsETH Token
interface IrsETH is IERC20 {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getRewards() external returns (uint256);
}

// DeFi Lending Platform
contract DeFiLendingPlatform is Ownable {
    using SafeMath for uint256;

    IrsETH public rsETH; // Instance of the rsETH token
    mapping(address => uint256) public userBalances; // User balance mapping
    mapping(address => uint256) public userRewards; // User rewards mapping

    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the rsETH token address
    constructor(address _rsETHAddress) {
        require(_rsETHAddress != address(0), "Invalid rsETH address");
        rsETH = IrsETH(_rsETHAddress);
    }

    // Function to deposit rsETH into the lending platform
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        // Transfer rsETH from user to this contract
        rsETH.transferFrom(msg.sender, address(this), amount);

        // Update user balance
        userBalances[msg.sender] = userBalances[msg.sender].add(amount);
        // Stake the deposited amount for rewards
        rsETH.stake(amount);

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw rsETH from the lending platform
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance before withdrawal
        userBalances[msg.sender] = userBalances[msg.sender].sub(amount);
        // Withdraw the specified amount
        rsETH.withdraw(amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = getPendingRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update user's rewards balance
        userRewards[msg.sender] = userRewards[msg.sender].add(rewards);
        // Transfer rewards to the user
        require(rsETH.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to calculate pending rewards for a user
    function getPendingRewards(address user) internal returns (uint256) {
        uint256 rewards = rsETH.getRewards();
        return rewards;
    }

    // Function to withdraw contract funds in case of emergency
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rsETH.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        rsETH.withdraw(balance);
    }
}
```
