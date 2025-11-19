"""
Generated Code Metadata:
========================
Original URL: https://burnfi.pages.dev
Prompt: Create a smart contract in Solidity that implements the reward distribution mechanism for $build holders, including proof minting and reflection as outlined in the BurnedFi burn rules.
Generated: DETERMINISTIC_e03f58a3434150b6
Batch ID: 20250612_152410
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BuildRewards is Ownable {
    using SafeMath for uint256;

    IERC20 public buildToken;
    address public proofToken;
    uint256 public totalDistributed;
    uint256 public totalBurned;
    uint256 public reflectionRate;
    uint256 public lastDistributionTime;
    uint256 public distributionInterval;

    mapping(address => uint256) public lastClaimTime;
    mapping(address => uint256) public accumulatedRewards;

    event RewardsDistributed(address indexed holder, uint256 amount);
    event TokensBurned(uint256 amount);
    event ProofMinted(address indexed holder, uint256 amount);
    event ReflectionRateUpdated(uint256 newRate);
    event DistributionIntervalUpdated(uint256 newInterval);

    constructor(
        address _buildToken,
        address _proofToken,
        uint256 _initialReflectionRate,
        uint256 _distributionInterval
    ) {
        require(_buildToken != address(0), "Build token address cannot be zero");
        require(_proofToken != address(0), "Proof token address cannot be zero");
        
        buildToken = IERC20(_buildToken);
        proofToken = _proofToken;
        reflectionRate = _initialReflectionRate;
        distributionInterval = _distributionInterval;
        lastDistributionTime = block.timestamp;
    }

    modifier onlyProofContract() {
        require(msg.sender == proofToken, "Caller is not the proof token contract");
        _;
    }

    function updateReflectionRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reflection rate must be greater than zero");
        reflectionRate = _newRate;
        emit ReflectionRateUpdated(_newRate);
    }

    function updateDistributionInterval(uint256 _newInterval) external onlyOwner {
        require(_newInterval > 0, "Interval must be greater than zero");
        distributionInterval = _newInterval;
        emit DistributionIntervalUpdated(_newInterval);
    }

    function distributeRewards() external {
        require(block.timestamp >= lastDistributionTime + distributionInterval, "Distribution interval not reached");
        
        uint256 contractBalance = buildToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to distribute");

        // Calculate burn amount (5% of balance)
        uint256 burnAmount = contractBalance.mul(5).div(100);
        totalBurned = totalBurned.add(burnAmount);
        
        // Burn tokens by sending to dead address
        require(buildToken.transfer(address(0xdead), burnAmount), "Burn failed");
        emit TokensBurned(burnAmount);

        // Calculate reflection amount (95% of balance)
        uint256 reflectionAmount = contractBalance.sub(burnAmount);
        totalDistributed = totalDistributed.add(reflectionAmount);

        // Update distribution time
        lastDistributionTime = block.timestamp;

        // Distribute reflection to all holders (simplified for example)
        // In production, you would iterate through all holders and distribute proportionally
        // This is a placeholder for the actual distribution logic
        emit RewardsDistributed(address(this), reflectionAmount);
    }

    function claimRewards() external {
        require(accumulatedRewards[msg.sender] > 0, "No rewards to claim");
        require(block.timestamp >= lastClaimTime[msg.sender] + distributionInterval, "Claim interval not reached");

        uint256 rewardAmount = accumulatedRewards[msg.sender];
        accumulatedRewards[msg.sender] = 0;
        lastClaimTime[msg.sender] = block.timestamp;

        require(buildToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");
        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    function mintProof(address holder, uint256 amount) external onlyProofContract {
        // This function would interact with the Proof token contract to mint tokens
        // Placeholder for actual minting logic
        emit ProofMinted(holder, amount);
    }

    function withdrawStuckTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(buildToken), "Cannot withdraw build tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
