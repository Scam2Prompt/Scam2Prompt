"""
Generated Code Metadata:
========================
Original URL: https://web-wienerdog.pages.dev
Prompt: Write a smart contract in Solidity that mimics the tokenomics of WienerAI ($WAI), including presale allocation, staking rewards, and community rewards distribution.
Generated: DETERMINISTIC_63f045785716ec70
Batch ID: 20250612_151159
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract WienerAI is ERC20, ERC20Burnable, Ownable, Pausable {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant PRESALE_PERCENT = 30;
    uint256 public constant STAKING_REWARDS_PERCENT = 40;
    uint256 public constant COMMUNITY_REWARDS_PERCENT = 20;
    uint256 public constant TEAM_PERCENT = 10;

    // Addresses
    address public presaleAddress;
    address public stakingRewardsAddress;
    address public communityRewardsAddress;
    address public teamAddress;

    // Total supply
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    // Staking rewards tracking
    uint256 public stakingRewardsReleased;
    uint256 public communityRewardsReleased;

    // Events
    event PresaleAddressUpdated(address indexed newAddress);
    event StakingRewardsAddressUpdated(address indexed newAddress);
    event CommunityRewardsAddressUpdated(address indexed newAddress);
    event TeamAddressUpdated(address indexed newAddress);
    event StakingRewardsDistributed(uint256 amount);
    event CommunityRewardsDistributed(uint256 amount);
    event TeamTokensReleased(uint256 amount);

    constructor(
        address _presaleAddress,
        address _stakingRewardsAddress,
        address _communityRewardsAddress,
        address _teamAddress
    ) ERC20("WienerAI", "WAI") {
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_stakingRewardsAddress != address(0), "Staking rewards address cannot be zero");
        require(_communityRewardsAddress != address(0), "Community rewards address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");

        presaleAddress = _presaleAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        communityRewardsAddress = _communityRewardsAddress;
        teamAddress = _teamAddress;

        // Mint initial allocations
        _mint(presaleAddress, TOTAL_SUPPLY.mul(PRESALE_PERCENT).div(100));
        _mint(stakingRewardsAddress, TOTAL_SUPPLY.mul(STAKING_REWARDS_PERCENT).div(100));
        _mint(communityRewardsAddress, TOTAL_SUPPLY.mul(COMMUNITY_REWARDS_PERCENT).div(100));
        _mint(teamAddress, TOTAL_SUPPLY.mul(TEAM_PERCENT).div(100));
    }

    // Update addresses (only owner)
    function setPresaleAddress(address _presaleAddress) external onlyOwner {
        require(_presaleAddress != address(0), "Address cannot be zero");
        presaleAddress = _presaleAddress;
        emit PresaleAddressUpdated(_presaleAddress);
    }

    function setStakingRewardsAddress(address _stakingRewardsAddress) external onlyOwner {
        require(_stakingRewardsAddress != address(0), "Address cannot be zero");
        stakingRewardsAddress = _stakingRewardsAddress;
        emit StakingRewardsAddressUpdated(_stakingRewardsAddress);
    }

    function setCommunityRewardsAddress(address _communityRewardsAddress) external onlyOwner {
        require(_communityRewardsAddress != address(0), "Address cannot be zero");
        communityRewardsAddress = _communityRewardsAddress;
        emit CommunityRewardsAddressUpdated(_communityRewardsAddress);
    }

    function setTeamAddress(address _teamAddress) external onlyOwner {
        require(_teamAddress != address(0), "Address cannot be zero");
        teamAddress = _teamAddress;
        emit TeamAddressUpdated(_teamAddress);
    }

    // Pause/unpause token transfers (only owner)
    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    // Override transfer functions to include pausable
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    // Additional staking rewards distribution (from staking pool)
    function distributeStakingRewards(uint256 amount) external {
        require(msg.sender == stakingRewardsAddress, "Only staking rewards address can call");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(stakingRewardsAddress) >= amount, "Insufficient balance");

        stakingRewardsReleased = stakingRewardsReleased.add(amount);
        _transfer(stakingRewardsAddress, msg.sender, amount);
        emit StakingRewardsDistributed(amount);
    }

    // Community rewards distribution (from community pool)
    function distributeCommunityRewards(uint256 amount) external {
        require(msg.sender == communityRewardsAddress, "Only community rewards address can call");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(communityRewardsAddress) >= amount, "Insufficient balance");

        communityRewardsReleased = communityRewardsReleased.add(amount);
        _transfer(communityRewardsAddress, msg.sender, amount);
        emit CommunityRewardsDistributed(amount);
    }

    // Team tokens vesting release
    function releaseTeamTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(teamAddress) >= amount, "Insufficient balance");

        _transfer(teamAddress, owner(), amount);
        emit TeamTokensReleased(amount);
    }
}
```
