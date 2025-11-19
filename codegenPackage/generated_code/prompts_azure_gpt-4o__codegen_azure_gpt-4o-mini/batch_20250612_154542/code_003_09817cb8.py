"""
Generated Code Metadata:
========================
Original URL: https://rewardusdctoken.com
Prompt: Write a Solidity function to calculate and distribute USDC rewards to holders of RUSDC tokens based on transaction fees collected from buy and sell operations.
Generated: DETERMINISTIC_09817cb8c407c089
Batch ID: 20250612_154542
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RUSDCRewards is Ownable {
    // USDC token interface
    IERC20 public usdcToken;
    
    // Mapping to track the balance of RUSDC holders
    mapping(address => uint256) public rusdcBalances;
    
    // Total RUSDC supply
    uint256 public totalRUSDC;

    // Event to log rewards distribution
    event RewardsDistributed(uint256 amount);

    // Constructor to initialize the contract with the USDC token address
    constructor(address _usdcToken) {
        usdcToken = IERC20(_usdcToken);
    }

    // Function to update RUSDC balances (to be called on buy/sell operations)
    function updateRUSDCBalance(address holder, uint256 amount) external onlyOwner {
        require(holder != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        rusdcBalances[holder] += amount;
        totalRUSDC += amount;
    }

    // Function to distribute USDC rewards based on RUSDC holdings
    function distributeRewards(uint256 totalFees) external onlyOwner {
        require(totalFees > 0, "Total fees must be greater than zero");
        require(totalRUSDC > 0, "No RUSDC holders to distribute rewards");

        // Calculate rewards per RUSDC token
        uint256 rewardPerRUSDC = totalFees / totalRUSDC;

        // Distribute rewards to each holder
        for (uint256 i = 0; i < totalRUSDC; i++) {
            address holder = getHolderAt(i); // Placeholder for actual holder retrieval logic
            uint256 holderBalance = rusdcBalances[holder];
            if (holderBalance > 0) {
                uint256 reward = holderBalance * rewardPerRUSDC;
                require(usdcToken.balanceOf(address(this)) >= reward, "Insufficient USDC balance in contract");
                usdcToken.transfer(holder, reward);
            }
        }

        emit RewardsDistributed(totalFees);
    }

    // Function to retrieve the holder at a specific index (to be implemented)
    function getHolderAt(uint256 index) internal view returns (address) {
        // Placeholder for actual implementation
        // This function should return the address of the RUSDC holder at the given index
        return address(0);
    }

    // Function to withdraw USDC from the contract (only owner)
    function withdrawUSDC(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(usdcToken.balanceOf(address(this)) >= amount, "Insufficient USDC balance in contract");
        usdcToken.transfer(msg.sender, amount);
    }
}
```
