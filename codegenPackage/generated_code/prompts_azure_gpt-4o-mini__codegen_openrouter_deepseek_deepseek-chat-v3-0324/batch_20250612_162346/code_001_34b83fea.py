"""
Generated Code Metadata:
========================
Original URL: https://brett-dvf.pages.dev
Prompt: Explain how to implement a smart contract for the $BRETT token on the BASE blockchain, including tokenomics details.
Generated: DETERMINISTIC_34b83fea01ee0b18
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";

contract BRETT is ERC20, ERC20Burnable, ERC20Pausable, Ownable, ERC20Permit {
    // Tokenomics constants
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10 ** 18; // 1B tokens
    uint256 public constant TEAM_ALLOCATION = 200_000_000 * 10 ** 18; // 20%
    uint256 public constant ECOSYSTEM_FUND = 150_000_000 * 10 ** 18; // 15%
    uint256 public constant LIQUIDITY_POOL = 100_000_000 * 10 ** 18; // 10%
    uint256 public constant COMMUNITY_REWARDS = 50_000_000 * 10 ** 18; // 5%
    uint256 public constant PUBLIC_SALE = 500_000_000 * 10 ** 18; // 50%

    // Addresses for allocations
    address public teamWallet;
    address public ecosystemWallet;
    address public liquidityPoolWallet;
    address public communityRewardsWallet;
    address public publicSaleWallet;

    // Vesting for team allocation (2 years with 6 month cliff)
    uint256 public constant VESTING_START = 0; // Will be set in constructor
    uint256 public constant VESTING_DURATION = 730 days; // 2 years
    uint256 public constant CLIFF_DURATION = 180 days; // 6 months
    uint256 public teamTokensReleased;

    // Tax mechanism (2% buy/sell tax)
    uint256 public constant TAX_PERCENT = 2;
    address public taxWallet;
    mapping(address => bool) public isExcludedFromTax;

    event TokensReleased(uint256 amount);
    event TaxCollected(address indexed from, uint256 amount);

    constructor(
        address initialOwner,
        address _teamWallet,
        address _ecosystemWallet,
        address _liquidityPoolWallet,
        address _communityRewardsWallet,
        address _publicSaleWallet,
        address _taxWallet
    ) ERC20("BRETT", "BRETT") Ownable(initialOwner) ERC20Permit("BRETT") {
        require(_teamWallet != address(0), "Team wallet cannot be zero");
        require(_ecosystemWallet != address(0), "Ecosystem wallet cannot be zero");
        require(_liquidityPoolWallet != address(0), "Liquidity wallet cannot be zero");
        require(_communityRewardsWallet != address(0), "Community wallet cannot be zero");
        require(_publicSaleWallet != address(0), "Public sale wallet cannot be zero");
        require(_taxWallet != address(0), "Tax wallet cannot be zero");

        teamWallet = _teamWallet;
        ecosystemWallet = _ecosystemWallet;
        liquidityPoolWallet = _liquidityPoolWallet;
        communityRewardsWallet = _communityRewardsWallet;
        publicSaleWallet = _publicSaleWallet;
        taxWallet = _taxWallet;

        // Exclude tax wallets from tax
        isExcludedFromTax[_teamWallet] = true;
        isExcludedFromTax[_ecosystemWallet] = true;
        isExcludedFromTax[_liquidityPoolWallet] = true;
        isExcludedFromTax[_communityRewardsWallet] = true;
        isExcludedFromTax[_publicSaleWallet] = true;
        isExcludedFromTax[_taxWallet] = true;

        // Mint initial allocations
        _mint(ecosystemWallet, ECOSYSTEM_FUND);
        _mint(liquidityPoolWallet, LIQUIDITY_POOL);
        _mint(communityRewardsWallet, COMMUNITY_REWARDS);
        _mint(publicSaleWallet, PUBLIC_SALE);

        // Team tokens are vested
        _mint(address(this), TEAM_ALLOCATION);
        VESTING_START = block.timestamp;
    }

    // Override transfer to implement tax mechanism
    function _update(
        address from,
        address to,
        uint256 amount
    ) internal virtual override(ERC20, ERC20Pausable) {
        if (from != address(0) && to != address(0) && !isExcludedFromTax[from] && !isExcludedFromTax[to]) {
            uint256 taxAmount = (amount * TAX_PERCENT) / 100;
            uint256 transferAmount = amount - taxAmount;
            
            super._update(from, taxWallet, taxAmount);
            super._update(from, to, transferAmount);
            
            emit TaxCollected(from, taxAmount);
        } else {
            super._update(from, to, amount);
        }
    }

    // Release vested team tokens
    function releaseTeamTokens() external {
        require(block.timestamp >= VESTING_START + CLIFF_DURATION, "Cliff period not ended");
        
        uint256 totalReleasable = releasableAmount();
        require(totalReleasable > 0, "No tokens to release");
        
        teamTokensReleased += totalReleasable;
        _transfer(address(this), teamWallet, totalReleasable);
        
        emit TokensReleased(totalReleasable);
    }

    // Calculate releasable amount
    function releasableAmount() public view returns (uint256) {
        if (block.timestamp < VESTING_START + CLIFF_DURATION) {
            return 0;
        } else if (block.timestamp >= VESTING_START + VESTING_DURATION) {
            return TEAM_ALLOCATION - teamTokensReleased;
        } else {
            uint256 elapsedTime = block.timestamp - (VESTING_START + CLIFF_DURATION);
            uint256 totalReleasable = (TEAM_ALLOCATION * elapsedTime) / (VESTING_DURATION - CLIFF_DURATION);
            return totalReleasable - teamTokensReleased;
        }
    }

    // Pause/unpause token transfers
    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    // Exclude/include addresses from tax
    function excludeFromTax(address account, bool excluded) external onlyOwner {
        isExcludedFromTax[account] = excluded;
    }

    // Change tax wallet
    function setTaxWallet(address newTaxWallet) external onlyOwner {
        require(newTaxWallet != address(0), "Tax wallet cannot be zero");
        taxWallet = newTaxWallet;
    }
}
```
