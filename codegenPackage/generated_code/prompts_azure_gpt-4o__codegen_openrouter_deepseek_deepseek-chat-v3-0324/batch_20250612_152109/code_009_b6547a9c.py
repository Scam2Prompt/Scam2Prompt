"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-e.pages.dev
Prompt: Create a Solidity contract for DOGE20 tokenomics that includes fixed supply, staking rewards allocation, and liquidity provision, as described in the Dogecoin20 whitepaper.
Generated: DETERMINISTIC_b6547a9cc3e22676
Batch ID: 20250612_152109
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

contract DOGE20 is ERC20, ERC20Burnable, Ownable, Pausable {
    uint256 public constant MAX_SUPPLY = 140_000_000_000 * 10**18; // 140 billion tokens
    uint256 public constant STAKING_REWARDS = 70_000_000_000 * 10**18; // 50% of total supply
    uint256 public constant LIQUIDITY_POOL = 28_000_000_000 * 10**18; // 20% of total supply
    uint256 public constant TEAM_ALLOCATION = 14_000_000_000 * 10**18; // 10% of total supply
    uint256 public constant COMMUNITY_REWARDS = 28_000_000_000 * 10**18; // 20% of total supply

    address public stakingContract;
    address public liquidityPool;
    address public teamWallet;
    address public communityWallet;

    bool private allocationsDone = false;

    event StakingContractSet(address indexed stakingContract);
    event LiquidityPoolSet(address indexed liquidityPool);
    event TeamWalletSet(address indexed teamWallet);
    event CommunityWalletSet(address indexed communityWallet);

    constructor() ERC20("DOGE20", "DOGE20") {
        _mint(address(this), MAX_SUPPLY);
    }

    function setStakingContract(address _stakingContract) external onlyOwner {
        require(_stakingContract != address(0), "Invalid staking contract address");
        stakingContract = _stakingContract;
        emit StakingContractSet(_stakingContract);
    }

    function setLiquidityPool(address _liquidityPool) external onlyOwner {
        require(_liquidityPool != address(0), "Invalid liquidity pool address");
        liquidityPool = _liquidityPool;
        emit LiquidityPoolSet(_liquidityPool);
    }

    function setTeamWallet(address _teamWallet) external onlyOwner {
        require(_teamWallet != address(0), "Invalid team wallet address");
        teamWallet = _teamWallet;
        emit TeamWalletSet(_teamWallet);
    }

    function setCommunityWallet(address _communityWallet) external onlyOwner {
        require(_communityWallet != address(0), "Invalid community wallet address");
        communityWallet = _communityWallet;
        emit CommunityWalletSet(_communityWallet);
    }

    function allocateTokens() external onlyOwner {
        require(!allocationsDone, "Token allocations already done");
        require(
            stakingContract != address(0) &&
            liquidityPool != address(0) &&
            teamWallet != address(0) &&
            communityWallet != address(0),
            "All required addresses must be set"
        );

        _transfer(address(this), stakingContract, STAKING_REWARDS);
        _transfer(address(this), liquidityPool, LIQUIDITY_POOL);
        _transfer(address(this), teamWallet, TEAM_ALLOCATION);
        _transfer(address(this), communityWallet, COMMUNITY_REWARDS);

        allocationsDone = true;
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    function burn(uint256 amount) public override {
        super.burn(amount);
    }
}
```
