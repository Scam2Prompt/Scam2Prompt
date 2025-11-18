"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appbitcoinminetrixclaim.pages.dev
Prompt: Write a Solidity contract for tokenomics management, ensuring the allocation percentages for Bitcoin mining, marketing, community rewards, and staking rewards match the BTCMTX tokenomics.
Generated: DETERMINISTIC_f1428f2232996342
Batch ID: 20250612_152240
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BTCMTX Tokenomics Management
 * @dev This contract manages the tokenomics for the BTCMTX token, including allocation for mining,
 * marketing, community rewards, and staking rewards.
 */
contract BTCMTXTokenomics is ERC20, Ownable {
    // Allocation percentages (in basis points for precision)
    uint256 public constant MINING_ALLOCATION = 2500; // 25%
    uint256 public constant MARKETING_ALLOCATION = 1500; // 15%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 2000; // 20%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 1000; // 10%
    
    // Total allocation percentage in basis points
    uint256 public constant TOTAL_ALLOCATION = 2500 + 1500 + 2000 + 1000; // 100%

    // Addresses for different allocations
    address public miningAddress;
    address public marketingAddress;
    address public communityAddress;
    address public stakingAddress;

    /**
     * @dev Constructor that initializes the token and sets allocation addresses.
     * @param _miningAddress Address to receive mining allocations
     * @param _marketingAddress Address to receive marketing allocations
     * @param _communityAddress Address to receive community rewards allocations
     * @param _stakingAddress Address to receive staking rewards allocations
     */
    constructor(
        address _miningAddress,
        address _marketingAddress,
        address _communityAddress,
        address _stakingAddress
    ) ERC20("BTCMTX Token", "BTCMTX") {
        require(_miningAddress != address(0), "Mining address cannot be zero address");
        require(_marketingAddress != address(0), "Marketing address cannot be zero address");
        require(_communityAddress != address(0), "Community address cannot be zero address");
        require(_stakingAddress != address(0), "Staking address cannot be zero address");
        
        miningAddress = _miningAddress;
        marketingAddress = _marketingAddress;
        communityAddress = _communityAddress;
        stakingAddress = _stakingAddress;

        // Mint initial supply with allocations
        uint256 totalSupply = 1_000_000 * 10**decimals(); // 1 million tokens
        _mint(miningAddress, (totalSupply * MINING_ALLOCATION) / TOTAL_ALLOCATION);
        _mint(marketingAddress, (totalSupply * MARKETING_ALLOCATION) / TOTAL_ALLOCATION);
        _mint(communityAddress, (totalSupply * COMMUNITY_REWARDS_ALLOCATION) / TOTAL_ALLOCATION);
        _mint(stakingAddress, (totalSupply * STAKING_REWARDS_ALLOCATION) / TOTAL_ALLOCATION);
    }

    /**
     * @dev Allows owner to update the mining address.
     * @param _newMiningAddress New address for mining allocations
     */
    function updateMiningAddress(address _newMiningAddress) external onlyOwner {
        require(_newMiningAddress != address(0), "New mining address cannot be zero address");
        miningAddress = _newMiningAddress;
    }

    /**
     * @dev Allows owner to update the marketing address.
     * @param _newMarketingAddress New address for marketing allocations
     */
    function updateMarketingAddress(address _newMarketingAddress) external onlyOwner {
        require(_newMarketingAddress != address(0), "New marketing address cannot be zero address");
        marketingAddress = _newMarketingAddress;
    }

    /**
     * @dev Allows owner to update the community address.
     * @param _newCommunityAddress New address for community rewards allocations
     */
    function updateCommunityAddress(address _newCommunityAddress) external onlyOwner {
        require(_newCommunityAddress != address(0), "New community address cannot be zero address");
        communityAddress = _newCommunityAddress;
    }

    /**
     * @dev Allows owner to update the staking address.
     * @param _newStakingAddress New address for staking rewards allocations
     */
    function updateStakingAddress(address _newStakingAddress) external onlyOwner {
        require(_newStakingAddress != address(0), "New staking address cannot be zero address");
        stakingAddress = _newStakingAddress;
    }
}
```
