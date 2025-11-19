"""
Generated Code Metadata:
========================
Original URL: https://usual-portal.web.app
Prompt: Design a tokenomics model for a new DeFi project, incorporating a governance token with a similar distribution mechanism as $USUAL.
Generated: DETERMINISTIC_5ad8b93abede8157
Batch ID: 20250622_212323
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GovernanceToken is ERC20, ERC20Votes, Ownable {
    using SafeMath for uint256;

    // Token distribution parameters
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens
    uint256 public constant COMMUNITY_ALLOCATION = 60_000_000 * 10**18; // 60%
    uint256 public constant TEAM_ALLOCATION = 15_000_000 * 10**18; // 15%
    uint256 public constant INVESTORS_ALLOCATION = 15_000_000 * 10**18; // 15%
    uint256 public constant TREASURY_ALLOCATION = 10_000_000 * 10**18; // 10%

    // Vesting parameters
    uint256 public constant VESTING_PERIOD = 365 days; // 1 year
    uint256 public constant CLIFF_PERIOD = 90 days; // 3 months
    uint256 public constant VESTING_START = 0; // Starts at deployment

    // Addresses
    address public communityPool;
    address public teamWallet;
    address public investorsWallet;
    address public treasuryWallet;

    // Track vested tokens
    uint256 public teamVested;
    uint256 public investorsVested;
    uint256 public lastVestingClaim;

    event TokensClaimed(address indexed recipient, uint256 amount);

    constructor(
        address _communityPool,
        address _teamWallet,
        address _investorsWallet,
        address _treasuryWallet
    ) ERC20("Usual Governance Token", "USUAL") ERC20Permit("Usual Governance Token") {
        require(_communityPool != address(0), "Invalid community pool address");
        require(_teamWallet != address(0), "Invalid team wallet address");
        require(_investorsWallet != address(0), "Invalid investors wallet address");
        require(_treasuryWallet != address(0), "Invalid treasury wallet address");

        communityPool = _communityPool;
        teamWallet = _teamWallet;
        investorsWallet = _investorsWallet;
        treasuryWallet = _treasuryWallet;

        // Mint initial allocations
        _mint(communityPool, COMMUNITY_ALLOCATION);
        _mint(treasuryWallet, TREASURY_ALLOCATION);

        lastVestingClaim = block.timestamp;
    }

    /**
     * @dev Claim vested tokens for team and investors
     */
    function claimVestedTokens() external {
        require(block.timestamp >= VESTING_START + CLIFF_PERIOD, "Cliff period not ended");
        
        uint256 elapsedTime = block.timestamp.sub(lastVestingClaim);
        require(elapsedTime > 0, "No time elapsed since last claim");

        uint256 totalVestingPeriod = VESTING_PERIOD.sub(CLIFF_PERIOD);
        uint256 remainingTeam = TEAM_ALLOCATION.sub(teamVested);
        uint256 remainingInvestors = INVESTORS_ALLOCATION.sub(investorsVested);

        uint256 teamAmount = remainingTeam.mul(elapsedTime).div(totalVestingPeriod);
        uint256 investorsAmount = remainingInvestors.mul(elapsedTime).div(totalVestingPeriod);

        if (teamAmount > 0) {
            teamVested = teamVested.add(teamAmount);
            _mint(teamWallet, teamAmount);
            emit TokensClaimed(teamWallet, teamAmount);
        }

        if (investorsAmount > 0) {
            investorsVested = investorsVested.add(investorsAmount);
            _mint(investorsWallet, investorsAmount);
            emit TokensClaimed(investorsWallet, investorsAmount);
        }

        lastVestingClaim = block.timestamp;
    }

    // The following functions are overrides required by Solidity.
    function _afterTokenTransfer(address from, address to, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._afterTokenTransfer(from, to, amount);
    }

    function _mint(address to, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._mint(to, amount);
    }

    function _burn(address account, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._burn(account, amount);
    }
}
```
