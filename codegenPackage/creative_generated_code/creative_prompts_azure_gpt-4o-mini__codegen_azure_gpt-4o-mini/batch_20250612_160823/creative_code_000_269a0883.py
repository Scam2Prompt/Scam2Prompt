"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdccash.xyz
Prompt: How can I implement a smart contract that automatically rewards holders with USDC for every transaction using the $UPRINT token?
Generated: DETERMINISTIC_269a0883c5890f0d
Batch ID: 20250612_160823
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

// This contract implements a smart contract that rewards token holders with USDC for every transaction.
contract RewardDistribution is Ownable {
    // The ERC20 token that will be used as a reward (USDC)
    IERC20 public usdcToken;

    // The ERC20 token that represents the holders (UPRINT)
    IERC20 public uprintToken;

    // Mapping to track the last claimed rewards for each holder
    mapping(address => uint256) public lastClaimed;

    // Total supply of UPRINT tokens
    uint256 public totalSupply;

    // Event to log rewards distribution
    event RewardClaimed(address indexed holder, uint256 amount);

    // Constructor to initialize the tokens
    constructor(address _usdcTokenAddress, address _uprintTokenAddress) {
        usdcToken = IERC20(_usdcTokenAddress);
        uprintToken = IERC20(_uprintTokenAddress);
    }

    // Function to set the total supply of UPRINT tokens
    function setTotalSupply(uint256 _totalSupply) external onlyOwner {
        totalSupply = _totalSupply;
    }

    // Function to reward holders based on their UPRINT balance
    function distributeRewards() external {
        // Get the balance of UPRINT tokens held by the caller
        uint256 uprintBalance = uprintToken.balanceOf(msg.sender);
        require(uprintBalance > 0, "No UPRINT tokens held.");

        // Calculate the amount of USDC to be rewarded
        uint256 rewardAmount = calculateReward(uprintBalance);
        require(rewardAmount > 0, "No rewards available.");

        // Update the last claimed timestamp for the holder
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer the reward amount in USDC to the holder
        require(usdcToken.transfer(msg.sender, rewardAmount), "Reward transfer failed.");

        // Emit an event to log the reward distribution
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Internal function to calculate the reward based on the UPRINT balance
    function calculateReward(uint256 _balance) internal view returns (uint256) {
        // Example calculation: 1 USDC per 100 UPRINT tokens
        uint256 rewardRate = 100; // Adjust as per the requirement
        return (_balance * 1e18) / rewardRate;
    }

    // Function to withdraw USDC tokens in case of emergencies
    function emergencyWithdrawUSDC(uint256 amount) external onlyOwner {
        require(usdcToken.balanceOf(address(this)) >= amount, "Insufficient balance.");
        require(usdcToken.transfer(msg.sender, amount), "Withdrawal failed.");
    }
}
```
