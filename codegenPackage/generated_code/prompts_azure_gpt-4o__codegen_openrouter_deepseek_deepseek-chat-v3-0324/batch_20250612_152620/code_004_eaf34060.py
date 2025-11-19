"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-minetrix.web.app
Prompt: Write a smart contract in Solidity that implements the tokenomics described for BTCMTX, including allocation percentages for mining, marketing, community rewards, and staking rewards.
Generated: DETERMINISTIC_eaf34060f8ef8733
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract BTCMTX is ERC20, Ownable, Pausable {
    // Token allocation percentages (basis points)
    uint256 public constant MINING_ALLOCATION = 5000;  // 50%
    uint256 public constant MARKETING_ALLOCATION = 1500;  // 15%
    uint256 public constant COMMUNITY_REWARDS = 2000;  // 20%
    uint256 public constant STAKING_REWARDS = 1500;  // 15%
    
    // Allocation addresses
    address public miningPool;
    address public marketingWallet;
    address public communityRewardsPool;
    address public stakingRewardsPool;
    
    // Total supply cap (1 billion tokens with 18 decimals)
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;
    
    // Track minted allocations
    bool private _allocationsMinted = false;
    
    event AllocationAddressesUpdated(
        address miningPool,
        address marketingWallet,
        address communityRewardsPool,
        address stakingRewardsPool
    );
    
    constructor(
        address _miningPool,
        address _marketingWallet,
        address _communityRewardsPool,
        address _stakingRewardsPool
    ) ERC20("Bitcoin Minetrix", "BTCMTX") {
        require(
            _miningPool != address(0) &&
            _marketingWallet != address(0) &&
            _communityRewardsPool != address(0) &&
            _stakingRewardsPool != address(0),
            "BTCMTX: allocation addresses cannot be zero"
        );
        
        miningPool = _miningPool;
        marketingWallet = _marketingWallet;
        communityRewardsPool = _communityRewardsPool;
        stakingRewardsPool = _stakingRewardsPool;
    }
    
    /**
     * @dev Mint initial token allocations according to the tokenomics.
     * Can only be called once by the owner.
     */
    function mintAllocations() external onlyOwner {
        require(!_allocationsMinted, "BTCMTX: allocations already minted");
        
        _mint(miningPool, (TOTAL_SUPPLY * MINING_ALLOCATION) / 10000);
        _mint(marketingWallet, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10000);
        _mint(communityRewardsPool, (TOTAL_SUPPLY * COMMUNITY_REWARDS) / 10000);
        _mint(stakingRewardsPool, (TOTAL_SUPPLY * STAKING_REWARDS) / 10000);
        
        _allocationsMinted = true;
    }
    
    /**
     * @dev Update allocation addresses.
     * Can only be called by the owner.
     */
    function updateAllocationAddresses(
        address _miningPool,
        address _marketingWallet,
        address _communityRewardsPool,
        address _stakingRewardsPool
    ) external onlyOwner {
        require(
            _miningPool != address(0) &&
            _marketingWallet != address(0) &&
            _communityRewardsPool != address(0) &&
            _stakingRewardsPool != address(0),
            "BTCMTX: allocation addresses cannot be zero"
        );
        
        miningPool = _miningPool;
        marketingWallet = _marketingWallet;
        communityRewardsPool = _communityRewardsPool;
        stakingRewardsPool = _stakingRewardsPool;
        
        emit AllocationAddressesUpdated(
            _miningPool,
            _marketingWallet,
            _communityRewardsPool,
            _stakingRewardsPool
        );
    }
    
    /**
     * @dev Pause token transfers.
     * Can only be called by the owner.
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause token transfers.
     * Can only be called by the owner.
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    /**
     * @dev Hook that is called before any transfer of tokens.
     * Includes minting and burning.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
