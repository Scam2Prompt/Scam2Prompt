"""
Generated Code Metadata:
========================
Original URL: https://usdcprinter.xyz
Prompt: Develop a simple Ethereum smart contract in Solidity that distributes USDC rewards to holders on every transaction, similar to $UPRINT.
Generated: DETERMINISTIC_665ebd2b3ee112f8
Batch ID: 20250622_211952
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

// Importing the ERC20 interface for USDC
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract to distribute USDC rewards to holders
contract USDCRewards is Ownable {
    // USDC token address (mainnet address)
    address public usdcTokenAddress;
    IERC20 public usdcToken;

    // Mapping to track the balance of rewards for each holder
    mapping(address => uint256) public rewards;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Event to log reward distribution
    event RewardsDistributed(address indexed holder, uint256 amount);

    // Constructor to set the USDC token address
    constructor(address _usdcTokenAddress) {
        usdcTokenAddress = _usdcTokenAddress;
        usdcToken = IERC20(_usdcTokenAddress);
    }

    // Function to distribute rewards to holders
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(usdcToken.balanceOf(address(this)) >= amount, "Insufficient USDC balance in contract");

        // Distributing rewards to all holders
        for (uint256 i = 0; i < holders.length; i++) {
            address holder = holders[i];
            uint256 reward = calculateReward(holder, amount);
            rewards[holder] += reward;
            totalRewardsDistributed += reward;

            // Emit event for reward distribution
            emit RewardsDistributed(holder, reward);
        }
    }

    // Function to calculate reward for a holder
    function calculateReward(address holder, uint256 totalAmount) internal view returns (uint256) {
        // Placeholder logic for reward calculation
        // This should be replaced with actual logic based on holder's balance or other criteria
        return totalAmount / holders.length; // Simple equal distribution
    }

    // Function for holders to claim their rewards
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the reward balance for the holder
        rewards[msg.sender] = 0;

        // Transfer USDC rewards to the holder
        require(usdcToken.transfer(msg.sender, reward), "USDC transfer failed");
    }

    // Function to withdraw USDC from the contract (only owner)
    function withdrawUSDC(uint256 amount) external onlyOwner {
        require(usdcToken.balanceOf(address(this)) >= amount, "Insufficient USDC balance");
        require(usdcToken.transfer(msg.sender, amount), "USDC transfer failed");
    }
}
```
