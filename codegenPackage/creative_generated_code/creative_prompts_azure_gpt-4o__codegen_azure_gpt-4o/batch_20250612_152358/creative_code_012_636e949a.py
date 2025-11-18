"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-99bitcoins.pages.dev
Prompt: Generate Solidity code for a smart contract that handles token presale allocations, including percentages for staking, liquidity, and marketing, as described in the 99Bitcoins tokenomics.
Generated: DETERMINISTIC_636e949a3775792a
Batch ID: 20250612_152358
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

/**
 * @title TokenPresale
 * @dev Smart contract to manage token presale allocations for staking, liquidity, and marketing.
 */
contract TokenPresale {
    // Define the owner of the contract
    address public owner;

    // Allocation percentages
    uint256 public stakingPercentage;   // e.g., 50%
    uint256 public liquidityPercentage; // e.g., 30%
    uint256 public marketingPercentage; // e.g., 20%

    // Total tokens allocated for presale
    uint256 public totalPresaleTokens;

    // Balances for each allocation
    uint256 public stakingTokens;
    uint256 public liquidityTokens;
    uint256 public marketingTokens;

    // Events
    event TokensAllocated(
        uint256 stakingTokens,
        uint256 liquidityTokens,
        uint256 marketingTokens
    );

    event TokensWithdrawn(address indexed recipient, uint256 amount);

    /**
     * @dev Modifier to restrict access to only the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _stakingPercentage Percentage allocated for staking
     * @param _liquidityPercentage Percentage allocated for liquidity
     * @param _marketingPercentage Percentage allocated for marketing
     * @param _totalPresaleTokens Total tokens allocated for the presale
     */
    constructor(
        uint256 _stakingPercentage,
        uint256 _liquidityPercentage,
        uint256 _marketingPercentage,
        uint256 _totalPresaleTokens
    ) {
        require(
            _stakingPercentage + _liquidityPercentage + _marketingPercentage == 100,
            "Percentages must add up to 100"
        );
        require(_totalPresaleTokens > 0, "Total presale tokens must be greater than zero");

        owner = msg.sender;
        stakingPercentage = _stakingPercentage;
        liquidityPercentage = _liquidityPercentage;
        marketingPercentage = _marketingPercentage;
        totalPresaleTokens = _totalPresaleTokens;

        // Allocate tokens based on percentages
        stakingTokens = (totalPresaleTokens * stakingPercentage) / 100;
        liquidityTokens = (totalPresaleTokens * liquidityPercentage) / 100;
        marketingTokens = (totalPresaleTokens * marketingPercentage) / 100;

        emit TokensAllocated(stakingTokens, liquidityTokens, marketingTokens);
    }

    /**
     * @dev Withdraw tokens from the staking allocation
     * @param _amount Amount of tokens to withdraw
     * @param _recipient Address of the recipient
     */
    function withdrawStakingTokens(uint256 _amount, address _recipient) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(_amount <= stakingTokens, "Insufficient staking tokens");

        stakingTokens -= _amount;
        emit TokensWithdrawn(_recipient, _amount);
        // Transfer logic would go here
    }

    /**
     * @dev Withdraw tokens from the liquidity allocation
     * @param _amount Amount of tokens to withdraw
     * @param _recipient Address of the recipient
     */
    function withdrawLiquidityTokens(uint256 _amount, address _recipient) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(_amount <= liquidityTokens, "Insufficient liquidity tokens");

        liquidityTokens -= _amount;
        emit TokensWithdrawn(_recipient, _amount);
        // Transfer logic would go here
    }

    /**
     * @dev Withdraw tokens from the marketing allocation
     * @param _amount Amount of tokens to withdraw
     * @param _recipient Address of the recipient
     */
    function withdrawMarketingTokens(uint256 _amount, address _recipient) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(_amount <= marketingTokens, "Insufficient marketing tokens");

        marketingTokens -= _amount;
        emit TokensWithdrawn(_recipient, _amount);
        // Transfer logic would go here
    }

    /**
     * @dev Fallback function to prevent sending ETH directly to the contract
     */
    fallback() external payable {
        revert("Contract does not accept direct payments");
    }

    receive() external payable {
        revert("Contract does not accept direct payments");
    }
}
```
