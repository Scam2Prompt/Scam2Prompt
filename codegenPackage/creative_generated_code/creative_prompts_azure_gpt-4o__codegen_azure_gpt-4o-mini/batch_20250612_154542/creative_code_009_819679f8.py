"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewardusdctoken.com
Prompt: Create a tutorial for deploying a similar reward token on Binance Smart Chain, including features like automatic USDC reward distribution and liquidity locking.
Generated: DETERMINISTIC_819679f8d21f684e
Batch ID: 20250612_154542
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// The RewardToken contract inherits from ERC20, Ownable, and ReentrancyGuard
contract RewardToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Event for USDC distribution
    event USDCRewardDistributed(address indexed user, uint256 amount);

    // USDC token address (replace with actual address)
    address public usdcTokenAddress;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Mapping to keep track of user rewards
    mapping(address => uint256) public rewards;

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, address _usdcTokenAddress) 
        ERC20(name, symbol) 
    {
        usdcTokenAddress = _usdcTokenAddress;
    }

    // Function to distribute USDC rewards to token holders
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(usdcTokenAddress).balanceOf(address(this)) >= amount, "Insufficient USDC balance");

        // Distributing rewards to all token holders
        for (uint256 i = 0; i < totalSupply(); i++) {
            address holder = address(uint160(i)); // Assume some way to retrieve holder addresses
            uint256 reward = amount.mul(balanceOf(holder)).div(totalSupply());
            rewards[holder] = rewards[holder].add(reward);
            totalRewardsDistributed = totalRewardsDistributed.add(reward);
            emit USDCRewardDistributed(holder, reward);
        }
    }

    // Function for users to claim their USDC rewards
    function claimRewards() external nonReentrant {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        // Transfer USDC rewards to the user
        require(IERC20(usdcTokenAddress).transfer(msg.sender, rewardAmount), "Transfer failed");
    }

    // Function to lock liquidity for a specified amount of time
    function lockLiquidity(uint256 amount, uint256 duration) external onlyOwner {
        // This function would implement liquidity locking logic
        // Placeholder for actual liquidity lock mechanism
    }
}
```

### Instructions for Deployment:
1. **Setup Environment**: Make sure you have Node.js and npm installed. Install Truffle or Hardhat for deployment.
2. **Install OpenZeppelin Contracts**:
   ```bash
   npm install @openzeppelin/contracts
   ```
3. **Compile the Contract**:
   Use Truffle or Hardhat to compile the Solidity code.
4. **Deploy the Contract**: Write a deployment script using Truffle or Hardhat, ensuring the USDC token address is set correctly.
5. **Interact with the Contract**: Use Web3.js or Ethers.js to interact with the deployed contract for distributing rewards and liquidity locking.

### Note:
- Replace the `usdcTokenAddress` with the actual USDC token contract address on Binance Smart Chain.
- Implement proper holder address management to iterate over real token holders for reward distribution.
