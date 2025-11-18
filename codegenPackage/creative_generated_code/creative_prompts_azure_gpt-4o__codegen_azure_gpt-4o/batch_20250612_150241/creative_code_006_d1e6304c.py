"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presale.pages.dev
Prompt: Generate a Solidity contract that implements the tokenomics of $99BTC, including allocations for presale, staking, project funds, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_d1e6304ce1c52ee5
Batch ID: 20250612_150241
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
 * @title $99BTC Token Contract
 * @dev Implements tokenomics for $99BTC including allocations for presale, staking, 
 * project funds, community rewards, liquidity, and marketing.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NinetyNineBTC is ERC20, Ownable {
    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 30; // 30% for presale
    uint256 public constant STAKING_ALLOCATION = 20; // 20% for staking
    uint256 public constant PROJECT_FUNDS_ALLOCATION = 15; // 15% for project funds
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 15; // 15% for community rewards
    uint256 public constant LIQUIDITY_ALLOCATION = 10; // 10% for liquidity
    uint256 public constant MARKETING_ALLOCATION = 10; // 10% for marketing

    uint256 public constant TOTAL_SUPPLY = 10_000_000 * 10**18; // Total supply: 10,000,000 tokens

    // Addresses for allocations
    address public presaleAddress;
    address public stakingAddress;
    address public projectFundsAddress;
    address public communityRewardsAddress;
    address public liquidityAddress;
    address public marketingAddress;

    /**
     * @dev Constructor that initializes the token and allocates initial supply.
     * @param _presaleAddress Address for presale allocation
     * @param _stakingAddress Address for staking allocation
     * @param _projectFundsAddress Address for project funds allocation
     * @param _communityRewardsAddress Address for community rewards allocation
     * @param _liquidityAddress Address for liquidity allocation
     * @param _marketingAddress Address for marketing allocation
     */
    constructor(
        address _presaleAddress,
        address _stakingAddress,
        address _projectFundsAddress,
        address _communityRewardsAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) ERC20("$99BTC", "99BTC") {
        // Validate addresses
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_stakingAddress != address(0), "Staking address cannot be zero");
        require(_projectFundsAddress != address(0), "Project funds address cannot be zero");
        require(_communityRewardsAddress != address(0), "Community rewards address cannot be zero");
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");

        // Assign addresses
        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        projectFundsAddress = _projectFundsAddress;
        communityRewardsAddress = _communityRewardsAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;

        // Allocate tokens
        _mint(presaleAddress, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100);
        _mint(stakingAddress, (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100);
        _mint(projectFundsAddress, (TOTAL_SUPPLY * PROJECT_FUNDS_ALLOCATION) / 100);
        _mint(communityRewardsAddress, (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100);
        _mint(liquidityAddress, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100);
        _mint(marketingAddress, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100);
    }

    /**
     * @dev Allows the owner to update allocation addresses in case of misconfiguration.
     * @param allocationType Type of allocation to update (e.g., "presale", "staking", etc.)
     * @param newAddress New address for the allocation
     */
    function updateAllocationAddress(string memory allocationType, address newAddress) external onlyOwner {
        require(newAddress != address(0), "New address cannot be zero");

        if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("presale"))) {
            presaleAddress = newAddress;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("staking"))) {
            stakingAddress = newAddress;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("projectFunds"))) {
            projectFundsAddress = newAddress;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("communityRewards"))) {
            communityRewardsAddress = newAddress;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("liquidity"))) {
            liquidityAddress = newAddress;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("marketing"))) {
            marketingAddress = newAddress;
        } else {
            revert("Invalid allocation type");
        }
    }
}
```
