"""
Generated Code Metadata:
========================
Original URL: https://beefxyz.pages.dev
Prompt: Design a community-driven token distribution plan for a new meme coin, inspired by $BEEF's 75% DEX liquidity pool allocation.
Generated: DETERMINISTIC_79e4cafddbd0bbe2
Batch ID: 20250622_210027
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

contract MemeCoin is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution parameters
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1B tokens
    uint256 public constant DEX_LIQUIDITY_POOL = 750_000_000 * 10**18; // 75% for DEX liquidity
    uint256 public constant COMMUNITY_REWARDS = 150_000_000 * 10**18; // 15% for community rewards
    uint256 public constant TEAM_TOKENS = 50_000_000 * 10**18; // 5% for team (vested)
    uint256 public constant MARKETING = 50_000_000 * 10**18; // 5% for marketing

    // Addresses
    address public dexLiquidityPool;
    address public communityRewardsPool;
    address public teamWallet;
    address public marketingWallet;

    // Vesting parameters
    uint256 public constant VESTING_PERIOD = 365 days; // 1 year vesting
    uint256 public constant VESTING_CLIFF = 90 days; // 3 month cliff
    uint256 public vestingStartTime;
    uint256 public totalVestedTokens;
    uint256 public totalReleasedTokens;

    // Events
    event TokensReleased(uint256 amount);
    event LiquidityPoolSet(address indexed pool);
    event CommunityPoolSet(address indexed pool);

    constructor(
        address _dexLiquidityPool,
        address _communityRewardsPool,
        address _teamWallet,
        address _marketingWallet
    ) ERC20("MemeCoin", "MEME") {
        require(_dexLiquidityPool != address(0), "Invalid DEX pool address");
        require(_communityRewardsPool != address(0), "Invalid community pool address");
        require(_teamWallet != address(0), "Invalid team wallet");
        require(_marketingWallet != address(0), "Invalid marketing wallet");

        dexLiquidityPool = _dexLiquidityPool;
        communityRewardsPool = _communityRewardsPool;
        teamWallet = _teamWallet;
        marketingWallet = _marketingWallet;

        // Mint initial distribution
        _mint(dexLiquidityPool, DEX_LIQUIDITY_POOL);
        _mint(communityRewardsPool, COMMUNITY_REWARDS);
        _mint(marketingWallet, MARKETING);

        // Start vesting for team tokens
        vestingStartTime = block.timestamp;
        totalVestedTokens = TEAM_TOKENS;
    }

    // Function to release vested team tokens
    function releaseVestedTokens() external onlyOwner {
        require(block.timestamp >= vestingStartTime + VESTING_CLIFF, "Vesting cliff not reached");
        
        uint256 unreleased = releasableAmount();
        require(unreleased > 0, "No tokens to release");

        totalReleasedTokens = totalReleasedTokens.add(unreleased);
        _mint(teamWallet, unreleased);

        emit TokensReleased(unreleased);
    }

    // Calculate releasable amount
    function releasableAmount() public view returns (uint256) {
        if (block.timestamp < vestingStartTime + VESTING_CLIFF) {
            return 0;
        } else if (block.timestamp >= vestingStartTime + VESTING_PERIOD) {
            return totalVestedTokens.sub(totalReleasedTokens);
        } else {
            uint256 timeElapsed = block.timestamp.sub(vestingStartTime.add(VESTING_CLIFF));
            uint256 vestingDuration = VESTING_PERIOD.sub(VESTING_CLIFF);
            uint256 vestedAmount = totalVestedTokens.mul(timeElapsed).div(vestingDuration);
            return vestedAmount.sub(totalReleasedTokens);
        }
    }

    // Update DEX liquidity pool address
    function setDexLiquidityPool(address _newPool) external onlyOwner {
        require(_newPool != address(0), "Invalid address");
        dexLiquidityPool = _newPool;
        emit LiquidityPoolSet(_newPool);
    }

    // Update community rewards pool address
    function setCommunityRewardsPool(address _newPool) external onlyOwner {
        require(_newPool != address(0), "Invalid address");
        communityRewardsPool = _newPool;
        emit CommunityPoolSet(_newPool);
    }

    // Prevent accidental ETH transfers
    receive() external payable {
        revert("ETH transfers not allowed");
    }
}
```
