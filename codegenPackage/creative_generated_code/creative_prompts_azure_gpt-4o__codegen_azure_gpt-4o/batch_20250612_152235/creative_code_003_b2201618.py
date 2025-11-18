"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonmouse.pages.dev
Prompt: Write a smart contract in Solidity that aligns with Moon Mouse's roadmap and tokenomics structure for distributing $MMOUSE tokens after the presale.
Generated: DETERMINISTIC_b22016180d4b028c
Batch ID: 20250612_152235
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
 * @title Moon Mouse Token Distribution Contract
 * @author Moon Mouse Team
 * @notice This contract handles the distribution of $MMOUSE tokens post-presale as per Moon Mouse's roadmap and tokenomics.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MoonMouseTokenDistributor {
    // Address of the $MMOUSE token contract
    IERC20 public mmouseToken;

    // Presale wallet for collecting funds
    address public presaleWallet;

    // Address of the team wallet
    address public teamWallet;

    // Address of the marketing wallet
    address public marketingWallet;

    // Tokenomics percentages
    uint256 public constant TEAM_ALLOCATION = 20; // 20% for the team
    uint256 public constant MARKETING_ALLOCATION = 10; // 10% for marketing
    uint256 public constant PRESALE_BUYER_ALLOCATION = 70; // 70% distributed to presale buyers

    // Events for transparency
    event TokensDistributed(
        uint256 teamAmount,
        uint256 marketingAmount,
        uint256 presaleBuyerAmount
    );

    event TokensClaimed(address indexed buyer, uint256 amount);

    // Mapping of presale buyers to their allocation
    mapping(address => uint256) public buyerAllocations;
    
    // Track whether distribution has been completed
    bool public distributionComplete;

    // Constructor to initialize the contract with token and wallet addresses
    constructor(
        address _mmouseToken,
        address _presaleWallet,
        address _teamWallet,
        address _marketingWallet
    ) {
        require(_mmouseToken != address(0), "Invalid MMOUSE token address");
        require(_presaleWallet != address(0), "Invalid presale wallet address");
        require(_teamWallet != address(0), "Invalid team wallet address");
        require(_marketingWallet != address(0), "Invalid marketing wallet address");

        mmouseToken = IERC20(_mmouseToken);
        presaleWallet = _presaleWallet;
        teamWallet = _teamWallet;
        marketingWallet = _marketingWallet;
    }

    /**
     * @notice Distributes tokens per the tokenomics structure.
     * @dev This function can only be called once by the presale wallet.
     */
    function distributeTokens(uint256 totalTokens) external {
        require(msg.sender == presaleWallet, "Caller is not the presale wallet");
        require(!distributionComplete, "Distribution already completed");
        require(totalTokens > 0, "Total tokens must be greater than zero");
        require(
            mmouseToken.balanceOf(address(this)) >= totalTokens,
            "Insufficient token balance"
        );

        // Calculate allocations
        uint256 teamAmount = (totalTokens * TEAM_ALLOCATION) / 100;
        uint256 marketingAmount = (totalTokens * MARKETING_ALLOCATION) / 100;
        uint256 presaleBuyerAmount = totalTokens - teamAmount - marketingAmount;

        // Distribute tokens
        mmouseToken.transfer(teamWallet, teamAmount);
        mmouseToken.transfer(marketingWallet, marketingAmount);

        emit TokensDistributed(teamAmount, marketingAmount, presaleBuyerAmount);

        // Mark distribution as complete
        distributionComplete = true;
    }

    /**
     * @notice Allows presale buyers to claim their allocated tokens.
     */
    function claimTokens() external {
        require(distributionComplete, "Distribution not completed yet");

        uint256 buyerAllocation = buyerAllocations[msg.sender];
        require(buyerAllocation > 0, "No tokens allocated to caller");

        // Reset allocation to prevent reentrancy
        buyerAllocations[msg.sender] = 0;

        // Transfer tokens to buyer
        mmouseToken.transfer(msg.sender, buyerAllocation);

        emit TokensClaimed(msg.sender, buyerAllocation);
    }

    /**
     * @notice Sets allocations for presale buyers.
     * @dev Can only be called by the presale wallet before distribution.
     */
    function setBuyerAllocations(address[] calldata buyers, uint256[] calldata allocations) external {
        require(msg.sender == presaleWallet, "Caller is not the presale wallet");
        require(!distributionComplete, "Cannot set allocations after distribution");
        require(buyers.length == allocations.length, "Mismatched input lengths");

        for (uint256 i = 0; i < buyers.length; i++) {
            require(buyers[i] != address(0), "Invalid buyer address");
            require(allocations[i] > 0, "Allocation must be greater than zero");
            buyerAllocations[buyers[i]] = allocations[i];
        }
    }
}
```
