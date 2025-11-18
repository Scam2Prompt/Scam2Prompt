"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-minetrix.web.app
Prompt: Write a smart contract in Solidity that implements the tokenomics described for BTCMTX, including allocation percentages for mining, marketing, community rewards, and staking rewards.
Generated: DETERMINISTIC_eaf34060f8ef8733
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

/**
 * @title BTCMTX Token Contract
 * @dev Implementation of a token with specific tokenomics allocations for mining, marketing, community rewards, and staking rewards.
 * This contract follows ERC20 standards.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BTCMTX is ERC20, Ownable {
    // Allocation percentages (in basis points: 1% = 100)
    uint256 public constant MINING_ALLOCATION = 4000;       // 40%
    uint256 public constant MARKETING_ALLOCATION = 2000;    // 20%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 2000; // 20%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 2000;   // 20%
    uint256 public constant TOTAL_ALLOCATION = 10000;      // 100%
    
    // Addresses for allocation
    address public miningAddress;
    address public marketingAddress;
    address public communityRewardsAddress;
    address public stakingRewardsAddress;

    // Total supply
    uint256 private immutable _initialSupply;

    /**
     * @dev Constructor that initializes the token and allocates initial supply.
     * @param _miningAddress Address where mining allocation will be sent.
     * @param _marketingAddress Address where marketing allocation will be sent.
     * @param _communityRewardsAddress Address where community rewards will be sent.
     * @param _stakingRewardsAddress Address where staking rewards will be sent.
     * @param _initialSupply Total initial token supply.
     */
    constructor(
        address _miningAddress,
        address _marketingAddress,
        address _communityRewardsAddress,
        address _stakingRewardsAddress,
        uint256 _initialSupply
    ) ERC20("BTCMTX", "BTCMTX") {
        require(_miningAddress != address(0), "Invalid mining address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");
        require(_stakingRewardsAddress != address(0), "Invalid staking rewards address");

        // Set allocation addresses
        miningAddress = _miningAddress;
        marketingAddress = _marketingAddress;
        communityRewardsAddress = _communityRewardsAddress;
        stakingRewardsAddress = _stakingRewardsAddress;

        // Initial supply allocation
        _initialSupply = _initialSupply;
        _mint(address(this), _initialSupply); // Mint tokens to the contract for distribution
        _distributeInitialSupply();           // Distribute tokens based on allocation percentages
    }

    /**
     * @dev Distributes the initial supply to the specified allocation addresses based on percentages.
     */
    function _distributeInitialSupply() private {
        uint256 miningTokens = (_initialSupply * MINING_ALLOCATION) / TOTAL_ALLOCATION;
        uint256 marketingTokens = (_initialSupply * MARKETING_ALLOCATION) / TOTAL_ALLOCATION;
        uint256 communityRewardsTokens = (_initialSupply * COMMUNITY_REWARDS_ALLOCATION) / TOTAL_ALLOCATION;
        uint256 stakingRewardsTokens = (_initialSupply * STAKING_REWARDS_ALLOCATION) / TOTAL_ALLOCATION;

        // Transfer allocated tokens
        _transfer(address(this), miningAddress, miningTokens);
        _transfer(address(this), marketingAddress, marketingTokens);
        _transfer(address(this), communityRewardsAddress, communityRewardsTokens);
        _transfer(address(this), stakingRewardsAddress, stakingRewardsTokens);
    }

    /**
     * @dev Allows the owner to update allocation addresses if necessary.
     * @param _miningAddress New mining allocation address.
     * @param _marketingAddress New marketing allocation address.
     * @param _communityRewardsAddress New community rewards allocation address.
     * @param _stakingRewardsAddress New staking rewards allocation address.
     */
    function updateAllocationAddresses(
        address _miningAddress,
        address _marketingAddress,
        address _communityRewardsAddress,
        address _stakingRewardsAddress
    ) external onlyOwner {
        require(_miningAddress != address(0), "Invalid mining address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");
        require(_stakingRewardsAddress != address(0), "Invalid staking rewards address");

        miningAddress = _miningAddress;
        marketingAddress = _marketingAddress;
        communityRewardsAddress = _communityRewardsAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
