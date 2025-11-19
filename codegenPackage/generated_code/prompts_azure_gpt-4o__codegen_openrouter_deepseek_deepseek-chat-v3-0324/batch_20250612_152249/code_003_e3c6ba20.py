"""
Generated Code Metadata:
========================
Original URL: https://btconbase-en.pages.dev
Prompt: Write a smart contract on the Base chain to facilitate community-driven token distribution for Bitcoin on Base, adhering to the CC0 license principles.
Generated: DETERMINISTIC_e3c6ba20639b0bf3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BitcoinOnBaseDistribution
 * @dev A community-driven token distribution contract for Bitcoin on Base chain
 */
contract BitcoinOnBaseDistribution is Ownable, ReentrancyGuard {
    IERC20 public immutable token;
    uint256 public totalDistributed;
    uint256 public distributionCap;
    uint256 public distributionStart;
    uint256 public distributionEnd;
    uint256 public claimPeriod;
    uint256 public claimAmount;

    mapping(address => bool) public hasClaimed;

    event TokensClaimed(address indexed recipient, uint256 amount);
    event DistributionExtended(uint256 newEndTime);
    event DistributionParametersUpdated(
        uint256 newCap,
        uint256 newClaimAmount,
        uint256 newClaimPeriod
    );

    /**
     * @dev Initializes the distribution contract
     * @param _token Address of the token to distribute
     * @param _distributionCap Maximum amount of tokens to distribute
     * @param _claimAmount Amount each address can claim
     * @param _claimPeriod Duration in seconds for which claims are allowed
     */
    constructor(
        address _token,
        uint256 _distributionCap,
        uint256 _claimAmount,
        uint256 _claimPeriod
    ) {
        require(_token != address(0), "Invalid token address");
        require(_distributionCap > 0, "Distribution cap must be positive");
        require(_claimAmount > 0, "Claim amount must be positive");
        require(_claimPeriod > 0, "Claim period must be positive");

        token = IERC20(_token);
        distributionCap = _distributionCap;
        claimAmount = _claimAmount;
        claimPeriod = _claimPeriod;
    }

    /**
     * @dev Starts the distribution period
     */
    function startDistribution() external onlyOwner {
        require(distributionStart == 0, "Distribution already started");
        distributionStart = block.timestamp;
        distributionEnd = block.timestamp + claimPeriod;
    }

    /**
     * @dev Allows eligible addresses to claim tokens
     */
    function claimTokens() external nonReentrant {
        require(distributionStart != 0, "Distribution not started");
        require(block.timestamp >= distributionStart, "Distribution not active");
        require(block.timestamp <= distributionEnd, "Claim period ended");
        require(!hasClaimed[msg.sender], "Already claimed");
        require(
            totalDistributed + claimAmount <= distributionCap,
            "Distribution cap reached"
        );

        hasClaimed[msg.sender] = true;
        totalDistributed += claimAmount;

        require(
            token.transfer(msg.sender, claimAmount),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, claimAmount);
    }

    /**
     * @dev Extends the distribution period
     * @param additionalTime Additional time in seconds
     */
    function extendDistribution(uint256 additionalTime) external onlyOwner {
        require(additionalTime > 0, "Invalid additional time");
        distributionEnd += additionalTime;
        emit DistributionExtended(distributionEnd);
    }

    /**
     * @dev Updates distribution parameters
     * @param newCap New distribution cap
     * @param newClaimAmount New claim amount per address
     * @param newClaimPeriod New claim period in seconds
     */
    function updateDistributionParameters(
        uint256 newCap,
        uint256 newClaimAmount,
        uint256 newClaimPeriod
    ) external onlyOwner {
        require(newCap > 0, "Invalid distribution cap");
        require(newClaimAmount > 0, "Invalid claim amount");
        require(newClaimPeriod > 0, "Invalid claim period");

        distributionCap = newCap;
        claimAmount = newClaimAmount;
        claimPeriod = newClaimPeriod;

        emit DistributionParametersUpdated(newCap, newClaimAmount, newClaimPeriod);
    }

    /**
     * @dev Allows owner to withdraw remaining tokens after distribution ends
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > distributionEnd, "Distribution not ended");
        uint256 remaining = token.balanceOf(address(this));
        require(remaining > 0, "No tokens to withdraw");
        require(token.transfer(owner(), remaining), "Token transfer failed");
    }
}
```
