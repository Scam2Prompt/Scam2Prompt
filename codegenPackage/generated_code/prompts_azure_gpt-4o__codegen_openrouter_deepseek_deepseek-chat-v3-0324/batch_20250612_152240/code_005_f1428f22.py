"""
Generated Code Metadata:
========================
Original URL: https://appbitcoinminetrixclaim.pages.dev
Prompt: Write a Solidity contract for tokenomics management, ensuring the allocation percentages for Bitcoin mining, marketing, community rewards, and staking rewards match the BTCMTX tokenomics.
Generated: DETERMINISTIC_f1428f2232996342
Batch ID: 20250612_152240
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

contract BTCMTXToken is ERC20, Ownable {
    // Allocation percentages (basis points: 10000 = 100%)
    uint256 public constant BITCOIN_MINING_ALLOCATION = 3000; // 30%
    uint256 public constant MARKETING_ALLOCATION = 2500;      // 25%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 2500; // 25%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 2000;   // 20%

    // Allocation addresses
    address public bitcoinMiningAddress;
    address public marketingAddress;
    address public communityRewardsAddress;
    address public stakingRewardsAddress;

    // Track allocated tokens
    bool private allocationsDistributed = false;

    event AllocationAddressesSet(
        address bitcoinMining,
        address marketing,
        address communityRewards,
        address stakingRewards
    );

    constructor(
        uint256 initialSupply,
        address _bitcoinMiningAddress,
        address _marketingAddress,
        address _communityRewardsAddress,
        address _stakingRewardsAddress
    ) ERC20("BTCMTX Token", "BTCMTX") {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        require(
            _bitcoinMiningAddress != address(0) &&
            _marketingAddress != address(0) &&
            _communityRewardsAddress != address(0) &&
            _stakingRewardsAddress != address(0),
            "Allocation addresses cannot be zero"
        );

        bitcoinMiningAddress = _bitcoinMiningAddress;
        marketingAddress = _marketingAddress;
        communityRewardsAddress = _communityRewardsAddress;
        stakingRewardsAddress = _stakingRewardsAddress;

        _mint(address(this), initialSupply);
    }

    function distributeAllocations() external onlyOwner {
        require(!allocationsDistributed, "Allocations already distributed");
        uint256 totalSupply = balanceOf(address(this));

        // Calculate allocation amounts
        uint256 bitcoinMiningAmount = (totalSupply * BITCOIN_MINING_ALLOCATION) / 10000;
        uint256 marketingAmount = (totalSupply * MARKETING_ALLOCATION) / 10000;
        uint256 communityRewardsAmount = (totalSupply * COMMUNITY_REWARDS_ALLOCATION) / 10000;
        uint256 stakingRewardsAmount = (totalSupply * STAKING_REWARDS_ALLOCATION) / 10000;

        // Distribute tokens
        _transfer(address(this), bitcoinMiningAddress, bitcoinMiningAmount);
        _transfer(address(this), marketingAddress, marketingAmount);
        _transfer(address(this), communityRewardsAddress, communityRewardsAmount);
        _transfer(address(this), stakingRewardsAddress, stakingRewardsAmount);

        allocationsDistributed = true;
    }

    function updateAllocationAddresses(
        address _bitcoinMiningAddress,
        address _marketingAddress,
        address _communityRewardsAddress,
        address _stakingRewardsAddress
    ) external onlyOwner {
        require(
            _bitcoinMiningAddress != address(0) &&
            _marketingAddress != address(0) &&
            _communityRewardsAddress != address(0) &&
            _stakingRewardsAddress != address(0),
            "Allocation addresses cannot be zero"
        );

        bitcoinMiningAddress = _bitcoinMiningAddress;
        marketingAddress = _marketingAddress;
        communityRewardsAddress = _communityRewardsAddress;
        stakingRewardsAddress = _stakingRewardsAddress;

        emit AllocationAddressesSet(
            _bitcoinMiningAddress,
            _marketingAddress,
            _communityRewardsAddress,
            _stakingRewardsAddress
        );
    }

    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
