"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: Provide a code example using Solidity to create a scholarship funding mechanism where IQRA Tokens can be pooled and distributed to eligible learners.
Generated: DETERMINISTIC_36dca3833b5ababb
Batch ID: 20250612_151246
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ScholarshipFundingMechanism
 * @author [Your Name]
 * @notice A contract to manage IQRA Token pools for scholarship funding.
 */
contract ScholarshipFundingMechanism is ReentrancyGuard, Ownable {
    // Mapping of learner addresses to their eligibility status
    mapping(address => bool) public eligibleLearners;

    // Mapping of IQRA Token pools to their respective funding goals
    mapping(address => uint256) public fundingPools;

    // Mapping of IQRA Token pools to their respective distributions
    mapping(address => mapping(address => uint256)) public distributions;

    // IQRA Token contract instance
    IERC20 public iqraToken;

    /**
     * @notice Event emitted when a learner is marked as eligible
     * @param learner Address of the learner
     * @param eligible Eligibility status
     */
    event LearnerEligibilityUpdated(address learner, bool eligible);

    /**
     * @notice Event emitted when a funding pool is created
     * @param pool Address of the funding pool
     * @param fundingGoal Funding goal of the pool
     */
    event FundingPoolCreated(address pool, uint256 fundingGoal);

    /**
     * @notice Event emitted when IQRA Tokens are distributed to a learner
     * @param pool Address of the funding pool
     * @param learner Address of the learner
     * @param amount Distributed amount
     */
    event IqraTokensDistributed(address pool, address learner, uint256 amount);

    /**
     * @notice Constructor to initialize the contract with IQRA Token instance
     * @param _iqraToken Address of the IQRA Token contract
     */
    constructor(address _iqraToken) {
        require(_iqraToken != address(0), "IQRA Token address cannot be zero");
        iqraToken = IERC20(_iqraToken);
    }

    /**
     * @notice Add a learner to the eligibility list
     * @param learner Address of the learner
     */
    function addEligibleLearner(address learner) public onlyOwner {
        require(learner != address(0), "Learner address cannot be zero");
        eligibleLearners[learner] = true;
        emit LearnerEligibilityUpdated(learner, true);
    }

    /**
     * @notice Remove a learner from the eligibility list
     * @param learner Address of the learner
     */
    function removeEligibleLearner(address learner) public onlyOwner {
        require(learner != address(0), "Learner address cannot be zero");
        eligibleLearners[learner] = false;
        emit LearnerEligibilityUpdated(learner, false);
    }

    /**
     * @notice Create a funding pool with a specific funding goal
     * @param pool Address of the funding pool
     * @param fundingGoal Funding goal of the pool
     */
    function createFundingPool(address pool, uint256 fundingGoal) public onlyOwner {
        require(pool != address(0), "Funding pool address cannot be zero");
        require(fundingGoal > 0, "Funding goal must be greater than zero");
        fundingPools[pool] = fundingGoal;
        emit FundingPoolCreated(pool, fundingGoal);
    }

    /**
     * @notice Distribute IQRA Tokens to eligible learners from a funding pool
     * @param pool Address of the funding pool
     * @param learner Address of the learner
     * @param amount Distributed amount
     */
    function distributeIqraTokens(address pool, address learner, uint256 amount) public nonReentrant {
        require(pool != address(0), "Funding pool address cannot be zero");
        require(learner != address(0), "Learner address cannot be zero");
        require(amount > 0, "Distributed amount must be greater than zero");
        require(eligibleLearners[learner], "Learner is not eligible");
        require(fundingPools[pool] >= amount, "Insufficient funds in the pool");

        // Update funding pool balance
        fundingPools[pool] -= amount;

        // Update distribution record
        distributions[pool][learner] += amount;

        // Transfer IQRA Tokens to the learner
        require(iqraToken.transfer(learner, amount), "IQRA Token transfer failed");

        emit IqraTokensDistributed(pool, learner, amount);
    }

    /**
     * @notice Refund IQRA Tokens to the funding pool owner if the funding goal is not met
     * @param pool Address of the funding pool
     */
    function refundIqraTokens(address pool) public nonReentrant {
        require(pool != address(0), "Funding pool address cannot be zero");
        require(fundingPools[pool] > 0, "No funds to refund");

        // Transfer IQRA Tokens back to the owner
        require(iqraToken.transfer(msg.sender, fundingPools[pool]), "IQRA Token transfer failed");

        // Reset funding pool balance
        fundingPools[pool] = 0;
    }
}
```
