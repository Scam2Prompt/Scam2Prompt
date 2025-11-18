"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakesvap.github.io
Prompt: Write a Solidity smart contract for staking stablecoins on Wombat Exchange, ensuring it supports single-currency staking and calculates sustainable yield based on the stableswap 2.0 model.
Generated: DETERMINISTIC_b2bb2b0af3b81854
Batch ID: 20250612_151624
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

// Importing OpenZeppelin Libraries for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Wombat Exchange to interact with stablecoin staking
interface IWombatExchange {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getYield(address user) external view returns (uint256);
}

// Staking contract for stablecoins on Wombat Exchange
contract StablecoinStaking is Ownable {
    // State variables
    IERC20 public stablecoin; // The stablecoin to be staked
    IWombatExchange public wombatExchange; // Wombat Exchange interface
    mapping(address => uint256) public stakedAmounts; // Mapping to track staked amounts per user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event YieldClaimed(address indexed user, uint256 yield);

    // Constructor to initialize the stablecoin and Wombat Exchange contract addresses
    constructor(address _stablecoin, address _wombatExchange) {
        require(_stablecoin != address(0), "Stablecoin address is zero");
        require(_wombatExchange != address(0), "Wombat Exchange address is zero");

        stablecoin = IERC20(_stablecoin);
        wombatExchange = IWombatExchange(_wombatExchange);
    }

    // Function to stake stablecoins
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stablecoin.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer stablecoins from user to contract
        stablecoin.transferFrom(msg.sender, address(this), amount);
        stakedAmounts[msg.sender] += amount;

        // Stake the amount on Wombat Exchange
        wombatExchange.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake stablecoins
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Unstake the amount from Wombat Exchange
        wombatExchange.unstake(amount);

        // Transfer stablecoins back to user
        stablecoin.transfer(msg.sender, amount);
        stakedAmounts[msg.sender] -= amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim yield from the staked amount
    function claimYield() external {
        uint256 yield = wombatExchange.getYield(msg.sender);
        require(yield > 0, "No yield available to claim");

        // Transfer yield to user
        stablecoin.transfer(msg.sender, yield);

        emit YieldClaimed(msg.sender, yield);
    }

    // Function to check the balance of staked tokens for a user
    function stakedBalance(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }

    // Admin function to withdraw any ERC20 tokens mistakenly sent to the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(stablecoin), "Cannot withdraw staked stablecoin");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
