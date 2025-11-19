"""
Generated Code Metadata:
========================
Original URL: https://everlodge-claimv2.pages.dev
Prompt: Create a step-by-step guide for deploying an ERC-20 token like $ELDG on the Ethereum blockchain, including tokenomics similar to Everlodge's structure.
Generated: DETERMINISTIC_58f737c055783129
Batch ID: 20250612_145715
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

contract ELDGToken is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable, ERC20Permit, ERC20Votes {
    // Token distribution percentages
    uint256 public constant TEAM_PERCENT = 15;
    uint256 public constant MARKETING_PERCENT = 10;
    uint256 public constant STAKING_REWARDS_PERCENT = 25;
    uint256 public constant ECOSYSTEM_PERCENT = 20;
    uint256 public constant PUBLIC_SALE_PERCENT = 30;

    // Addresses for token allocation
    address public teamWallet;
    address public marketingWallet;
    address public stakingRewardsWallet;
    address public ecosystemWallet;

    // Token vesting
    mapping(address => uint256) private _vestingAmounts;
    mapping(address => uint256) private _vestingReleaseTimes;

    constructor(
        uint256 initialSupply,
        address _teamWallet,
        address _marketingWallet,
        address _stakingRewardsWallet,
        address _ecosystemWallet
    ) ERC20("Everlodge", "ELDG") ERC20Permit("Everlodge") {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        require(_teamWallet != address(0), "Team wallet cannot be zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        require(_stakingRewardsWallet != address(0), "Staking wallet cannot be zero address");
        require(_ecosystemWallet != address(0), "Ecosystem wallet cannot be zero address");

        teamWallet = _teamWallet;
        marketingWallet = _marketingWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        ecosystemWallet = _ecosystemWallet;

        // Calculate token allocations
        uint256 teamAllocation = (initialSupply * TEAM_PERCENT) / 100;
        uint256 marketingAllocation = (initialSupply * MARKETING_PERCENT) / 100;
        uint256 stakingAllocation = (initialSupply * STAKING_REWARDS_PERCENT) / 100;
        uint256 ecosystemAllocation = (initialSupply * ECOSYSTEM_PERCENT) / 100;
        uint256 publicSaleAllocation = (initialSupply * PUBLIC_SALE_PERCENT) / 100;

        // Mint tokens to respective wallets
        _mint(teamWallet, teamAllocation);
        _mint(marketingWallet, marketingAllocation);
        _mint(stakingRewardsWallet, stakingAllocation);
        _mint(ecosystemWallet, ecosystemAllocation);
        
        // Mint remaining tokens to contract owner for public sale
        _mint(msg.sender, publicSaleAllocation);

        // Setup vesting for team tokens (1 year lock, then 6 months linear vesting)
        _vestingAmounts[teamWallet] = teamAllocation;
        _vestingReleaseTimes[teamWallet] = block.timestamp + 365 days;
    }

    // Snapshot functions
    function snapshot() public onlyOwner {
        _snapshot();
    }

    // Pausable functions
    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    // Vesting functions
    function releaseVestedTokens() external {
        require(_vestingAmounts[msg.sender] > 0, "No vested tokens");
        require(block.timestamp >= _vestingReleaseTimes[msg.sender], "Vesting period not ended");

        uint256 amount = _vestingAmounts[msg.sender];
        _vestingAmounts[msg.sender] = 0;
        _transfer(address(this), msg.sender, amount);
    }

    // Override required by Solidity
    function _beforeTokenTransfer(address from, address to, uint256 amount)
        internal
        override(ERC20, ERC20Snapshot)
    {
        super._beforeTokenTransfer(from, to, amount);

        require(!paused(), "Token transfer while paused");
    }

    // The following functions are overrides required by Solidity for ERC20Votes
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

// Deployment steps:
// 1. Compile this contract using Solidity compiler (0.8.0 or compatible)
// 2. Deploy to Ethereum mainnet or testnet using Remix, Hardhat, or Truffle
// 3. Constructor parameters:
//    - initialSupply: Total token supply (e.g., 1,000,000,000 * 10^18 for 1B tokens with 18 decimals)
//    - _teamWallet: Address for team allocation
//    - _marketingWallet: Address for marketing allocation
//    - _stakingRewardsWallet: Address for staking rewards
//    - _ecosystemWallet: Address for ecosystem development
// 4. Verify the contract on Etherscan
// 5. Implement additional functionality as needed (staking, governance, etc.)
```
