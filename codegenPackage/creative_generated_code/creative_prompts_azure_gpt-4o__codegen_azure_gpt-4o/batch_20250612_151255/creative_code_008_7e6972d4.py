"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Write a Solidity contract for token distribution based on the tokenomics described in WienerAI, ensuring allocations for presale, staking, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_7e6972d4c537bce0
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Solidity contract for token distribution based on the described tokenomics:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenDistribution
 * @dev A contract for managing the distribution of tokens according to tokenomics.
 */
contract TokenDistribution {
    // Tokenomics allocations
    uint256 public constant PRESALE_ALLOCATION = 40; // 40% for presale
    uint256 public constant STAKING_ALLOCATION = 25; // 25% for staking rewards
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 15; // 15% for community rewards
    uint256 public constant LIQUIDITY_ALLOCATION = 10; // 10% for liquidity
    uint256 public constant MARKETING_ALLOCATION = 10; // 10% for marketing

    // Total token supply
    uint256 public totalSupply;

    // Allocation tracking
    uint256 public presaleDistributed;
    uint256 public stakingDistributed;
    uint256 public communityRewardsDistributed;
    uint256 public liquidityDistributed;
    uint256 public marketingDistributed;

    // Owner of the contract
    address public owner;

    // Events
    event TokensDistributed(address indexed recipient, uint256 amount, string allocationType);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        owner = msg.sender; // Set the owner
        totalSupply = _totalSupply; // Set the total token supply
    }

    /**
     * @dev Distribute tokens for presale.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to distribute.
     */
    function distributePresale(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(presaleDistributed + amount <= (totalSupply * PRESALE_ALLOCATION) / 100, "Exceeds presale allocation");

        presaleDistributed += amount;
        emit TokensDistributed(recipient, amount, "Presale");
    }

    /**
     * @dev Distribute tokens for staking rewards.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to distribute.
     */
    function distributeStaking(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(stakingDistributed + amount <= (totalSupply * STAKING_ALLOCATION) / 100, "Exceeds staking allocation");

        stakingDistributed += amount;
        emit TokensDistributed(recipient, amount, "Staking");
    }

    /**
     * @dev Distribute tokens for community rewards.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to distribute.
     */
    function distributeCommunityRewards(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(
            communityRewardsDistributed + amount <= (totalSupply * COMMUNITY_REWARDS_ALLOCATION) / 100,
            "Exceeds community rewards allocation"
        );

        communityRewardsDistributed += amount;
        emit TokensDistributed(recipient, amount, "Community Rewards");
    }

    /**
     * @dev Distribute tokens for liquidity.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to distribute.
     */
    function distributeLiquidity(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(liquidityDistributed + amount <= (totalSupply * LIQUIDITY_ALLOCATION) / 100, "Exceeds liquidity allocation");

        liquidityDistributed += amount;
        emit TokensDistributed(recipient, amount, "Liquidity");
    }

    /**
     * @dev Distribute tokens for marketing.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to distribute.
     */
    function distributeMarketing(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(marketingDistributed + amount <= (totalSupply * MARKETING_ALLOCATION) / 100, "Exceeds marketing allocation");

        marketingDistributed += amount;
        emit TokensDistributed(recipient, amount, "Marketing");
    }

    /**
     * @dev Get remaining allocation for a specific type.
     * @param allocationType Type of allocation ("Presale", "Staking", "Community Rewards", "Liquidity", "Marketing").
     * @return Remaining amount.
     */
    function getRemainingAllocation(string memory allocationType) external view returns (uint256) {
        if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("Presale"))) {
            return (totalSupply * PRESALE_ALLOCATION) / 100 - presaleDistributed;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("Staking"))) {
            return (totalSupply * STAKING_ALLOCATION) / 100 - stakingDistributed;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("Community Rewards"))) {
            return (totalSupply * COMMUNITY_REWARDS_ALLOCATION) / 100 - communityRewardsDistributed;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("Liquidity"))) {
            return (totalSupply * LIQUIDITY_ALLOCATION) / 100 - liquidityDistributed;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("Marketing"))) {
            return (totalSupply * MARKETING_ALLOCATION) / 100 - marketingDistributed;
        } else {
            revert("Invalid allocation type");
        }
    }
}
```
