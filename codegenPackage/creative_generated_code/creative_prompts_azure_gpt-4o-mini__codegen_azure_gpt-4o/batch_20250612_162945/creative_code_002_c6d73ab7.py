"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drdegens.top
Prompt: Create a smart contract for a crowdfunding project on DegenPad that utilizes $DEGEN tips from the Farcaster community.
Generated: DETERMINISTIC_c6d73ab74f1cafa4
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready Ethereum smart contract for the requested crowdfunding project using Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Crowdfunding Smart Contract for DegenPad using $DEGEN tips
 * @author [Your Name]
 * @notice This smart contract allows users to contribute $DEGEN tokens to a crowdfunding project on DegenPad.
 * @dev This contract implements basic crowdfunding functionality with $DEGEN token integration.
 */

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DegenPadCrowdfunding {
    // Address of the $DEGEN token contract
    IERC20 public immutable degenToken;

    // Address of the project owner
    address public immutable owner;

    // Crowdfunding goal in $DEGEN tokens
    uint256 public immutable fundingGoal;

    // Total amount of funds raised
    uint256 public totalFundsRaised;

    // Mapping of contributors and their contributed amounts
    mapping(address => uint256) public contributions;

    // Boolean to track if the funding goal is reached
    bool public fundingGoalReached = false;

    // Boolean to track if the project owner has withdrawn funds
    bool public fundsWithdrawn = false;

    // Events
    event ContributionMade(address indexed contributor, uint256 amount);
    event FundingGoalReached(uint256 totalFundsRaised);
    event FundsWithdrawn(uint256 amount);
    event RefundIssued(address indexed contributor, uint256 amount);

    /**
     * @dev Constructor to initialize the crowdfunding contract.
     * @param _degenToken Address of the $DEGEN token contract.
     * @param _fundingGoal Crowdfunding goal in $DEGEN tokens.
     */
    constructor(IERC20 _degenToken, uint256 _fundingGoal) {
        require(address(_degenToken) != address(0), "Invalid $DEGEN token address");
        require(_fundingGoal > 0, "Funding goal must be greater than 0");

        degenToken = _degenToken;
        owner = msg.sender; // Contract deployer is the project owner
        fundingGoal = _fundingGoal;
    }

    /**
     * @notice Allows contributors to send $DEGEN tokens to the crowdfunding project.
     * @param amount The amount of $DEGEN tokens to contribute.
     */
    function contribute(uint256 amount) external {
        require(amount > 0, "Contribution amount must be greater than 0");
        require(!fundingGoalReached, "Funding goal already reached");

        // Transfer $DEGEN tokens from the contributor to the contract
        bool success = degenToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update contribution data
        contributions[msg.sender] += amount;
        totalFundsRaised += amount;

        emit ContributionMade(msg.sender, amount);

        // Check if the funding goal is reached
        if (totalFundsRaised >= fundingGoal) {
            fundingGoalReached = true;
            emit FundingGoalReached(totalFundsRaised);
        }
    }

    /**
     * @notice Allows the project owner to withdraw funds if the funding goal is reached.
     */
    function withdrawFunds() external {
        require(msg.sender == owner, "Only the project owner can withdraw funds");
        require(fundingGoalReached, "Funding goal has not been reached");
        require(!fundsWithdrawn, "Funds have already been withdrawn");

        uint256 amount = degenToken.balanceOf(address(this));
        fundsWithdrawn = true;

        // Transfer the funds to the project owner
        bool success = degenToken.transfer(owner, amount);
        require(success, "Token transfer failed");

        emit FundsWithdrawn(amount);
    }

    /**
     * @notice Allows contributors to request a refund if the funding goal is not reached.
     */
    function requestRefund() external {
        require(!fundingGoalReached, "Funding goal has been reached, refunds not available");
        
        uint256 contributedAmount = contributions[msg.sender];
        require(contributedAmount > 0, "No contributions found for refund");

        // Reset contributor's contributed amount
        contributions[msg.sender] = 0;

        // Refund the contributor
        bool success = degenToken.transfer(msg.sender, contributedAmount);
        require(success, "Token transfer failed");

        emit RefundIssued(msg.sender, contributedAmount);
    }
}
```

**Notes for Deployment**:
1. Make sure the `$DEGEN` token contract adheres to the ERC20 standard.
2. Deploy the contract with the correct `$DEGEN` token address and funding goal.
3. Test thoroughly before deploying to a production environment.
