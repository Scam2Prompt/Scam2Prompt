"""
Generated Code Metadata:
========================
Original URL: https://memekombat-in.pages.dev
Prompt: Design a tokenomics system for a new gaming platform, inspired by Meme Kombat's 50% presale, 30% staking and battle rewards, 10% DEX, and 10% community rewards.
Generated: DETERMINISTIC_23ee60bda485f10c
Batch ID: 20250622_210443
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GameToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant PRESALE_PERCENT = 50;
    uint256 public constant STAKING_REWARDS_PERCENT = 30;
    uint256 public constant DEX_PERCENT = 10;
    uint256 public constant COMMUNITY_REWARDS_PERCENT = 10;

    // Addresses for different allocations
    address public presaleAddress;
    address public stakingRewardsAddress;
    address public dexAddress;
    address public communityRewardsAddress;

    // Total supply
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    constructor(
        address _presaleAddress,
        address _stakingRewardsAddress,
        address _dexAddress,
        address _communityRewardsAddress
    ) ERC20("GameToken", "GAME") {
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_stakingRewardsAddress != address(0), "Staking rewards address cannot be zero");
        require(_dexAddress != address(0), "DEX address cannot be zero");
        require(_communityRewardsAddress != address(0), "Community rewards address cannot be zero");

        presaleAddress = _presaleAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        dexAddress = _dexAddress;
        communityRewardsAddress = _communityRewardsAddress;

        // Mint tokens according to distribution
        _mint(presaleAddress, TOTAL_SUPPLY.mul(PRESALE_PERCENT).div(100));
        _mint(stakingRewardsAddress, TOTAL_SUPPLY.mul(STAKING_REWARDS_PERCENT).div(100));
        _mint(dexAddress, TOTAL_SUPPLY.mul(DEX_PERCENT).div(100));
        _mint(communityRewardsAddress, TOTAL_SUPPLY.mul(COMMUNITY_REWARDS_PERCENT).div(100));
    }

    // Function to update presale address (only owner)
    function setPresaleAddress(address _presaleAddress) external onlyOwner {
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        presaleAddress = _presaleAddress;
    }

    // Function to update staking rewards address (only owner)
    function setStakingRewardsAddress(address _stakingRewardsAddress) external onlyOwner {
        require(_stakingRewardsAddress != address(0), "Staking rewards address cannot be zero");
        stakingRewardsAddress = _stakingRewardsAddress;
    }

    // Function to update DEX address (only owner)
    function setDexAddress(address _dexAddress) external onlyOwner {
        require(_dexAddress != address(0), "DEX address cannot be zero");
        dexAddress = _dexAddress;
    }

    // Function to update community rewards address (only owner)
    function setCommunityRewardsAddress(address _communityRewardsAddress) external onlyOwner {
        require(_communityRewardsAddress != address(0), "Community rewards address cannot be zero");
        communityRewardsAddress = _communityRewardsAddress;
    }

    // Prevent token transfers before trading is enabled
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);
        
        // Allow minting and initial distribution
        if (from == address(0)) {
            return;
        }

        // Add additional transfer restrictions if needed
        // Example: require(tradingEnabled, "Trading is not enabled yet");
    }
}
```
