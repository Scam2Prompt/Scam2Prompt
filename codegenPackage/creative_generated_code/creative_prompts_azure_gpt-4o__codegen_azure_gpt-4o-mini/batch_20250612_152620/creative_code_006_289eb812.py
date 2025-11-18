"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-31k.pages.dev
Prompt: Create a Solidity contract for BTCMTX tokenomics, ensuring the allocation of 42.5% for Bitcoin mining, 35% for marketing, 12.5% for staking rewards, and 10% for community rewards.
Generated: DETERMINISTIC_289eb812b653521f
Batch ID: 20250612_152620
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

// Importing OpenZeppelin's ERC20 contract for standard token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BTCMTX Token
 * @dev This contract implements the BTCMTX token with specific allocation for mining, marketing, staking rewards, and community rewards.
 */
contract BTCMTX is ERC20, Ownable {
    // Allocation constants
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * (10 ** 18); // Total supply of the token
    uint256 public constant MINING_ALLOCATION = (TOTAL_SUPPLY * 425) / 1000; // 42.5% for mining
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 350) / 1000; // 35% for marketing
    uint256 public constant STAKING_REWARDS_ALLOCATION = (TOTAL_SUPPLY * 125) / 1000; // 12.5% for staking rewards
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = (TOTAL_SUPPLY * 100) / 1000; // 10% for community rewards

    // Addresses to receive allocated tokens
    address public miningWallet;
    address public marketingWallet;
    address public stakingRewardsWallet;
    address public communityRewardsWallet;

    // Constructor to initialize the token with its name and symbol
    constructor(
        address _miningWallet, 
        address _marketingWallet, 
        address _stakingRewardsWallet, 
        address _communityRewardsWallet
    ) ERC20("BTCMTX", "BTCMTX") {
        // Setting the wallet addresses
        miningWallet = _miningWallet;
        marketingWallet = _marketingWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        communityRewardsWallet = _communityRewardsWallet;

        // Minting the allocated tokens to respective wallets
        _mint(miningWallet, MINING_ALLOCATION);
        _mint(marketingWallet, MARKETING_ALLOCATION);
        _mint(stakingRewardsWallet, STAKING_REWARDS_ALLOCATION);
        _mint(communityRewardsWallet, COMMUNITY_REWARDS_ALLOCATION);
    }

    /**
     * @dev Function to update the wallet addresses.
     * Only the contract owner can update these addresses.
     * @param _miningWallet New address for mining allocation.
     * @param _marketingWallet New address for marketing allocation.
     * @param _stakingRewardsWallet New address for staking rewards allocation.
     * @param _communityRewardsWallet New address for community rewards allocation.
     */
    function updateWallets(
        address _miningWallet, 
        address _marketingWallet, 
        address _stakingRewardsWallet, 
        address _communityRewardsWallet
    ) external onlyOwner {
        // Update wallet addresses with checks for zero address
        require(_miningWallet != address(0), "Invalid mining wallet address");
        require(_marketingWallet != address(0), "Invalid marketing wallet address");
        require(_stakingRewardsWallet != address(0), "Invalid staking rewards wallet address");
        require(_communityRewardsWallet != address(0), "Invalid community rewards wallet address");

        miningWallet = _miningWallet;
        marketingWallet = _marketingWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        communityRewardsWallet = _communityRewardsWallet;
    }
}
```
