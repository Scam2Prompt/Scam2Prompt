"""
Generated Code Metadata:
========================
Original URL: https://rexas-de.web.app
Prompt: Generate a Rexas Finance token (RXS) smart contract using a library like OpenZeppelin, incorporating the tokenomics outlined in the Rexas Finance whitepaper.
Generated: DETERMINISTIC_47e5301048efd4aa
Batch ID: 20250622_210046
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/draft-ERC20Permit.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";

contract RXSToken is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable, ERC20Permit, ERC20Votes {
    // Token distribution addresses
    address public treasuryWallet;
    address public teamWallet;
    address public stakingRewardsWallet;
    address public ecosystemFundWallet;
    address public liquidityPoolWallet;

    // Token distribution percentages
    uint256 public constant TREASURY_PERCENT = 20;
    uint256 public constant TEAM_PERCENT = 15;
    uint256 public constant STAKING_REWARDS_PERCENT = 25;
    uint256 public constant ECOSYSTEM_FUND_PERCENT = 20;
    uint256 public constant LIQUIDITY_POOL_PERCENT = 20;

    // Token vesting periods
    uint256 public constant TEAM_VESTING_PERIOD = 730 days; // 2 years
    uint256 public constant ECOSYSTEM_VESTING_PERIOD = 365 days; // 1 year

    // Vesting tracking
    uint256 public teamVestingStart;
    uint256 public ecosystemVestingStart;
    uint256 public teamVestedAmount;
    uint256 public ecosystemVestedAmount;

    constructor(
        address _treasuryWallet,
        address _teamWallet,
        address _stakingRewardsWallet,
        address _ecosystemFundWallet,
        address _liquidityPoolWallet
    ) ERC20("Rexas Finance", "RXS") ERC20Permit("Rexas Finance") {
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero address");
        require(_teamWallet != address(0), "Team wallet cannot be zero address");
        require(_stakingRewardsWallet != address(0), "Staking rewards wallet cannot be zero address");
        require(_ecosystemFundWallet != address(0), "Ecosystem fund wallet cannot be zero address");
        require(_liquidityPoolWallet != address(0), "Liquidity pool wallet cannot be zero address");

        treasuryWallet = _treasuryWallet;
        teamWallet = _teamWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        ecosystemFundWallet = _ecosystemFundWallet;
        liquidityPoolWallet = _liquidityPoolWallet;

        // Total supply: 1 billion tokens with 18 decimals
        uint256 totalSupply = 1_000_000_000 * (10 ** decimals());

        // Mint initial allocations
        _mint(treasuryWallet, totalSupply * TREASURY_PERCENT / 100);
        _mint(stakingRewardsWallet, totalSupply * STAKING_REWARDS_PERCENT / 100);
        _mint(liquidityPoolWallet, totalSupply * LIQUIDITY_POOL_PERCENT / 100);

        // Mint vesting allocations
        _mint(address(this), totalSupply * TEAM_PERCENT / 100); // Team tokens
        _mint(address(this), totalSupply * ECOSYSTEM_FUND_PERCENT / 100); // Ecosystem tokens

        // Start vesting periods
        teamVestingStart = block.timestamp;
        ecosystemVestingStart = block.timestamp;
    }

    // Snapshot functionality
    function snapshot() public onlyOwner {
        _snapshot();
    }

    // Pause/unpause functionality
    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    // Vesting functions
    function claimTeamTokens() public {
        require(msg.sender == teamWallet, "Only team wallet can claim");
        uint256 elapsedTime = block.timestamp - teamVestingStart;
        uint256 totalTeamTokens = totalSupply() * TEAM_PERCENT / 100;
        
        if (elapsedTime >= TEAM_VESTING_PERIOD) {
            uint256 remainingTokens = totalTeamTokens - teamVestedAmount;
            _transfer(address(this), teamWallet, remainingTokens);
            teamVestedAmount = totalTeamTokens;
        } else {
            uint256 claimableAmount = (totalTeamTokens * elapsedTime) / TEAM_VESTING_PERIOD - teamVestedAmount;
            _transfer(address(this), teamWallet, claimableAmount);
            teamVestedAmount += claimableAmount;
        }
    }

    function claimEcosystemTokens() public {
        require(msg.sender == ecosystemFundWallet, "Only ecosystem wallet can claim");
        uint256 elapsedTime = block.timestamp - ecosystemVestingStart;
        uint256 totalEcosystemTokens = totalSupply() * ECOSYSTEM_FUND_PERCENT / 100;
        
        if (elapsedTime >= ECOSYSTEM_VESTING_PERIOD) {
            uint256 remainingTokens = totalEcosystemTokens - ecosystemVestedAmount;
            _transfer(address(this), ecosystemFundWallet, remainingTokens);
            ecosystemVestedAmount = totalEcosystemTokens;
        } else {
            uint256 claimableAmount = (totalEcosystemTokens * elapsedTime) / ECOSYSTEM_VESTING_PERIOD - ecosystemVestedAmount;
            _transfer(address(this), ecosystemFundWallet, claimableAmount);
            ecosystemVestedAmount += claimableAmount;
        }
    }

    // Overrides required by Solidity
    function _beforeTokenTransfer(address from, address to, uint256 amount)
        internal
        whenNotPaused
        override(ERC20, ERC20Snapshot)
    {
        super._beforeTokenTransfer(from, to, amount);
    }

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
