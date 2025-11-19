"""
Generated Code Metadata:
========================
Original URL: https://claim-mindofpepe-allocations.pages.dev
Prompt: Write a Solidity contract for the MIND of Pepe token, defining its tokenomics, including the allocation of tokens for exchanges, AI agent development, marketing, rewards, and community staking.
Generated: DETERMINISTIC_2d8759d3d6d7e880
Batch ID: 20250622_212746
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

/**
 * @title MIND of Pepe Token Contract
 * @dev ERC20 token with predefined tokenomics for allocation of tokens.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MindOfPepeToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    // Tokenomics allocations
    uint256 public constant EXCHANGE_ALLOCATION = (TOTAL_SUPPLY * 20) / 100; // 20%
    uint256 public constant AI_AGENT_DEVELOPMENT_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25%
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 15) / 100; // 15%
    uint256 public constant REWARDS_ALLOCATION = (TOTAL_SUPPLY * 20) / 100; // 20%
    uint256 public constant COMMUNITY_STAKING_ALLOCATION = (TOTAL_SUPPLY * 20) / 100; // 20%

    // Addresses for allocations
    address public exchangeWallet;
    address public aiAgentDevelopmentWallet;
    address public marketingWallet;
    address public rewardsWallet;
    address public communityStakingWallet;

    /**
     * @dev Constructor to initialize the token and allocate tokens.
     * @param _exchangeWallet Address for exchange allocation.
     * @param _aiAgentDevelopmentWallet Address for AI agent development allocation.
     * @param _marketingWallet Address for marketing allocation.
     * @param _rewardsWallet Address for rewards allocation.
     * @param _communityStakingWallet Address for community staking allocation.
     */
    constructor(
        address _exchangeWallet,
        address _aiAgentDevelopmentWallet,
        address _marketingWallet,
        address _rewardsWallet,
        address _communityStakingWallet
    ) ERC20("MIND of Pepe", "MOPE") {
        require(_exchangeWallet != address(0), "Exchange wallet cannot be zero address");
        require(_aiAgentDevelopmentWallet != address(0), "AI agent development wallet cannot be zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        require(_rewardsWallet != address(0), "Rewards wallet cannot be zero address");
        require(_communityStakingWallet != address(0), "Community staking wallet cannot be zero address");

        // Set wallet addresses
        exchangeWallet = _exchangeWallet;
        aiAgentDevelopmentWallet = _aiAgentDevelopmentWallet;
        marketingWallet = _marketingWallet;
        rewardsWallet = _rewardsWallet;
        communityStakingWallet = _communityStakingWallet;

        // Mint tokens to respective wallets
        _mint(exchangeWallet, EXCHANGE_ALLOCATION);
        _mint(aiAgentDevelopmentWallet, AI_AGENT_DEVELOPMENT_ALLOCATION);
        _mint(marketingWallet, MARKETING_ALLOCATION);
        _mint(rewardsWallet, REWARDS_ALLOCATION);
        _mint(communityStakingWallet, COMMUNITY_STAKING_ALLOCATION);
    }

    /**
     * @dev Update the wallet address for a specific allocation.
     * @param allocationType The type of allocation to update (1: Exchange, 2: AI Agent Development, 3: Marketing, 4: Rewards, 5: Community Staking).
     * @param newWallet The new wallet address.
     */
    function updateWallet(uint8 allocationType, address newWallet) external onlyOwner {
        require(newWallet != address(0), "New wallet cannot be zero address");

        if (allocationType == 1) {
            exchangeWallet = newWallet;
        } else if (allocationType == 2) {
            aiAgentDevelopmentWallet = newWallet;
        } else if (allocationType == 3) {
            marketingWallet = newWallet;
        } else if (allocationType == 4) {
            rewardsWallet = newWallet;
        } else if (allocationType == 5) {
            communityStakingWallet = newWallet;
        } else {
            revert("Invalid allocation type");
        }
    }
}
```
