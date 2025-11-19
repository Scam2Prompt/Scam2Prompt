"""
Generated Code Metadata:
========================
Original URL: https://lermlinstrate.pages.dev
Prompt: Generate a smart contract code snippet in Solidity to deploy a token with a similar tokenomics structure as $MP on the Merlin Chain.
Generated: DETERMINISTIC_255aa37d5de94b29
Batch ID: 20250622_210802
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";

contract MPToken is ERC20, ERC20Burnable, Ownable, ERC20Permit {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TEAM_ALLOCATION = 200_000_000 * 10**18; // 20%
    uint256 public constant ECOSYSTEM_FUND = 300_000_000 * 10**18; // 30%
    uint256 public constant COMMUNITY_REWARDS = 200_000_000 * 10**18; // 20%
    uint256 public constant LIQUIDITY_POOL = 300_000_000 * 10**18; // 30%

    address public teamWallet;
    address public ecosystemWallet;
    address public communityWallet;
    address public liquidityPool;

    bool public teamTokensReleased;
    bool public ecosystemTokensReleased;
    bool public communityTokensReleased;
    bool public liquidityTokensReleased;

    constructor(
        address _teamWallet,
        address _ecosystemWallet,
        address _communityWallet,
        address _liquidityPool
    ) ERC20("MP Token", "MP") ERC20Permit("MP Token") {
        require(_teamWallet != address(0), "Invalid team wallet");
        require(_ecosystemWallet != address(0), "Invalid ecosystem wallet");
        require(_communityWallet != address(0), "Invalid community wallet");
        require(_liquidityPool != address(0), "Invalid liquidity pool");

        teamWallet = _teamWallet;
        ecosystemWallet = _ecosystemWallet;
        communityWallet = _communityWallet;
        liquidityPool = _liquidityPool;

        // Mint initial liquidity pool tokens
        _mint(_liquidityPool, LIQUIDITY_POOL);
        liquidityTokensReleased = true;
    }

    function releaseTeamTokens() external onlyOwner {
        require(!teamTokensReleased, "Team tokens already released");
        _mint(teamWallet, TEAM_ALLOCATION);
        teamTokensReleased = true;
    }

    function releaseEcosystemFund() external onlyOwner {
        require(!ecosystemTokensReleased, "Ecosystem fund already released");
        _mint(ecosystemWallet, ECOSYSTEM_FUND);
        ecosystemTokensReleased = true;
    }

    function releaseCommunityRewards() external onlyOwner {
        require(!communityTokensReleased, "Community rewards already released");
        _mint(communityWallet, COMMUNITY_REWARDS);
        communityTokensReleased = true;
    }

    function totalSupply() public view virtual override returns (uint256) {
        return MAX_SUPPLY;
    }

    function transfer(address to, uint256 amount) public override returns (bool) {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        return super.transfer(to, amount);
    }

    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override returns (bool) {
        require(balanceOf(from) >= amount, "Insufficient balance");
        return super.transferFrom(from, to, amount);
    }
}
```
