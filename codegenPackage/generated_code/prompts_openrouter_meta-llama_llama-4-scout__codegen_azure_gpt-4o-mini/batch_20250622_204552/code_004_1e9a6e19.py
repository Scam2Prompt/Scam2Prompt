"""
Generated Code Metadata:
========================
Original URL: https://tess-9x2.pages.dev
Prompt: Design a smart contract for secure token distribution on autopilot, inspired by Magna's audited smart contracts on Ethereum and Solana.
Generated: DETERMINISTIC_1e9a6e197c78a6be
Batch ID: 20250622_204552
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

/**
 * @title AutoTokenDistributor
 * @dev A smart contract for secure token distribution on autopilot.
 * This contract allows the owner to set up a distribution schedule for ERC20 tokens.
 */
contract AutoTokenDistributor is Ownable {
    using SafeMath for uint256;

    // Struct to hold distribution details
    struct Distribution {
        address token; // Address of the ERC20 token
        uint256 amount; // Amount of tokens to distribute
        uint256 startTime; // Start time of the distribution
        uint256 interval; // Time interval between distributions
        uint256 totalDistributions; // Total number of distributions
        uint256 distributedCount; // Count of distributions made
    }

    // Mapping of distribution IDs to their details
    mapping(uint256 => Distribution) public distributions;
    uint256 public distributionCount;

    // Event emitted when a distribution is created
    event DistributionCreated(uint256 indexed distributionId, address indexed token, uint256 amount, uint256 startTime, uint256 interval, uint256 totalDistributions);
    
    // Event emitted when tokens are distributed
    event TokensDistributed(uint256 indexed distributionId, address indexed recipient, uint256 amount);

    /**
     * @dev Creates a new token distribution.
     * @param _token Address of the ERC20 token to distribute.
     * @param _amount Amount of tokens to distribute.
     * @param _startTime Start time for the distribution.
     * @param _interval Time interval between distributions.
     * @param _totalDistributions Total number of distributions to make.
     */
    function createDistribution(
        address _token,
        uint256 _amount,
        uint256 _startTime,
        uint256 _interval,
        uint256 _totalDistributions
    ) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than zero");
        require(_totalDistributions > 0, "Total distributions must be greater than zero");
        require(_startTime >= block.timestamp, "Start time must be in the future");

        // Create a new distribution
        distributions[distributionCount] = Distribution({
            token: _token,
            amount: _amount,
            startTime: _startTime,
            interval: _interval,
            totalDistributions: _totalDistributions,
            distributedCount: 0
        });

        emit DistributionCreated(distributionCount, _token, _amount, _startTime, _interval, _totalDistributions);
        distributionCount++;
    }

    /**
     * @dev Distributes tokens to the specified recipient.
     * @param _distributionId ID of the distribution to execute.
     * @param _recipient Address of the recipient.
     */
    function distributeTokens(uint256 _distributionId, address _recipient) external {
        Distribution storage distribution = distributions[_distributionId];

        // Ensure the distribution exists
        require(distribution.token != address(0), "Distribution does not exist");
        require(distribution.distributedCount < distribution.totalDistributions, "All distributions completed");
        
        // Calculate the next distribution time
        uint256 nextDistributionTime = distribution.startTime.add(distribution.interval.mul(distribution.distributedCount));
        require(block.timestamp >= nextDistributionTime, "Not time for distribution yet");

        // Transfer tokens to the recipient
        require(IERC20(distribution.token).balanceOf(address(this)) >= distribution.amount, "Insufficient contract balance");
        require(IERC20(distribution.token).transfer(_recipient, distribution.amount), "Token transfer failed");

        // Increment the distributed count
        distribution.distributedCount++;

        emit TokensDistributed(_distributionId, _recipient, distribution.amount);
    }

    /**
     * @dev Withdraws any ERC20 tokens accidentally sent to the contract.
     * @param _token Address of the ERC20 token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(IERC20(_token).balanceOf(address(this)) >= _amount, "Insufficient balance");

        require(IERC20(_token).transfer(msg.sender, _amount), "Token transfer failed");
    }
}
```
