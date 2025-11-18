"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswapdefi.org
Prompt: Create a Solidity contract to automate token staking in PancakeSwap's Syrup Pools and withdraw rewards periodically.
Generated: DETERMINISTIC_b550ccdd6230c9a9
Batch ID: 20250612_154829
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

// Importing OpenZeppelin contracts for safe math and ERC20 token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for PancakeSwap's Syrup Pools
interface ISyrupPool {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _amount) external;
    function pendingCake(address _user) external view returns (uint256);
}

// Staking contract for PancakeSwap syrup pools
contract PancakeSwapStaker {
    using SafeMath for uint256;

    // State variables
    address public owner;
    IERC20 public token; // The token to stake
    ISyrupPool public syrupPool; // The pancake syrup pool

    // Events
    event Staked(uint256 amount);
    event Withdrawn(uint256 amount);
    event RewardsClaimed(uint256 rewards);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _token, address _syrupPool) {
        require(_token != address(0), "Invalid token address");
        require(_syrupPool != address(0), "Invalid syrup pool address");

        owner = msg.sender;
        token = IERC20(_token);
        syrupPool = ISyrupPool(_syrupPool);
    }

    // Function to stake tokens in the syrup pool
    function stake(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the owner to this contract
        token.transferFrom(msg.sender, address(this), _amount);
        // Approve the syrup pool to spend the tokens
        token.approve(address(syrupPool), _amount);
        // Deposit the tokens into the syrup pool
        syrupPool.deposit(_amount);

        emit Staked(_amount);
    }

    // Function to withdraw staked tokens from the syrup pool
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        syrupPool.withdraw(_amount);
        
        // Transfer withdrawn tokens back to the owner
        token.transfer(msg.sender, _amount);

        emit Withdrawn(_amount);
    }

    // Function to claim pending rewards from the syrup pool
    function claimRewards() external onlyOwner {
        uint256 rewards = syrupPool.pendingCake(address(this));
        require(rewards > 0, "No rewards to claim");

        // Assuming there is a mechanism to handle rewards, like sending them to the owner
        // (This would depend on the implementation details of the syrup pool)
        // Here we would usually call the appropriate function to claim the rewards

        emit RewardsClaimed(rewards);
    }

    // Function to get the pending rewards for the contract
    function getPendingRewards() external view returns (uint256) {
        return syrupPool.pendingCake(address(this));
    }

    // Function to withdraw all rewards and staked tokens
    function emergencyWithdraw() external onlyOwner {
        // Withdraw all staked tokens
        uint256 stakedBalance = token.balanceOf(address(this));
        syrupPool.withdraw(stakedBalance);
        
        // Transfer all tokens back to the owner
        token.transfer(msg.sender, stakedBalance);
    }

    // Function to change the owner of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        owner = newOwner;
    }
}
```
