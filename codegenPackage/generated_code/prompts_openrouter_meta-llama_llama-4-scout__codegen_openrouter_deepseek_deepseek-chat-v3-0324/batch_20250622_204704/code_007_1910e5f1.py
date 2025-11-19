"""
Generated Code Metadata:
========================
Original URL: https://pushd-en.pages.dev
Prompt: "How can I implement a tokenomics system similar to Pushd's, with a total supply of 250,000,000 tokens, and what are the benefits of such a system?"
Generated: DETERMINISTIC_1910e5f148e2dc78
Batch ID: 20250622_204704
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

contract PushdToken is ERC20, Ownable {
    using SafeMath for uint256;
    
    uint256 public constant TOTAL_SUPPLY = 250_000_000 * 10**18; // 250 million tokens with 18 decimals
    uint256 public constant TEAM_ALLOCATION = TOTAL_SUPPLY.mul(20).div(100); // 20%
    uint256 public constant ECOSYSTEM_FUND = TOTAL_SUPPLY.mul(30).div(100); // 30%
    uint256 public constant MARKETING_FUND = TOTAL_SUPPLY.mul(10).div(100); // 10%
    uint256 public constant LIQUIDITY_POOL = TOTAL_SUPPLY.mul(20).div(100); // 20%
    uint256 public constant PUBLIC_SALE = TOTAL_SUPPLY.mul(20).div(100); // 20%
    
    address public teamWallet;
    address public ecosystemWallet;
    address public marketingWallet;
    address public liquidityWallet;
    
    uint256 public teamVestingStart;
    uint256 public teamVestingDuration = 365 days; // 1 year vesting
    uint256 public teamVestingCliff = 90 days; // 3 month cliff
    
    mapping(address => bool) private _isExcludedFromFee;
    
    event TeamWalletUpdated(address indexed newWallet);
    event EcosystemWalletUpdated(address indexed newWallet);
    event MarketingWalletUpdated(address indexed newWallet);
    event LiquidityWalletUpdated(address indexed newWallet);
    
    constructor(
        address _teamWallet,
        address _ecosystemWallet,
        address _marketingWallet,
        address _liquidityWallet
    ) ERC20("Pushd Token", "PUSHD") {
        require(_teamWallet != address(0), "Team wallet cannot be zero address");
        require(_ecosystemWallet != address(0), "Ecosystem wallet cannot be zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");
        
        teamWallet = _teamWallet;
        ecosystemWallet = _ecosystemWallet;
        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;
        
        teamVestingStart = block.timestamp;
        
        // Mint initial allocations
        _mint(ecosystemWallet, ECOSYSTEM_FUND);
        _mint(marketingWallet, MARKETING_FUND);
        _mint(liquidityWallet, LIQUIDITY_POOL);
        
        // Public sale tokens can be minted later by owner
        _mint(owner(), PUBLIC_SALE);
        
        // Exclude wallets from fees
        _isExcludedFromFee[owner()] = true;
        _isExcludedFromFee[teamWallet] = true;
        _isExcludedFromFee[ecosystemWallet] = true;
        _isExcludedFromFee[marketingWallet] = true;
        _isExcludedFromFee[liquidityWallet] = true;
    }
    
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }
    
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()).sub(amount));
        return true;
    }
    
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        // Check team vesting
        if (sender == teamWallet && block.timestamp < teamVestingStart.add(teamVestingCliff)) {
            revert("Team tokens are still locked");
        }
        
        if (sender == teamWallet && block.timestamp < teamVestingStart.add(teamVestingDuration)) {
            uint256 vestedAmount = TEAM_ALLOCATION.mul(block.timestamp.sub(teamVestingStart)).div(teamVestingDuration);
            require(balanceOf(teamWallet).sub(amount) >= TEAM_ALLOCATION.sub(vestedAmount), "Team tokens are still vesting");
        }
        
        super._transfer(sender, recipient, amount);
    }
    
    function updateTeamWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "New wallet cannot be zero address");
        teamWallet = newWallet;
        _isExcludedFromFee[newWallet] = true;
        emit TeamWalletUpdated(newWallet);
    }
    
    function updateEcosystemWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "New wallet cannot be zero address");
        ecosystemWallet = newWallet;
        _isExcludedFromFee[newWallet] = true;
        emit EcosystemWalletUpdated(newWallet);
    }
    
    function updateMarketingWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "New wallet cannot be zero address");
        marketingWallet = newWallet;
        _isExcludedFromFee[newWallet] = true;
        emit MarketingWalletUpdated(newWallet);
    }
    
    function updateLiquidityWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "New wallet cannot be zero address");
        liquidityWallet = newWallet;
        _isExcludedFromFee[newWallet] = true;
        emit LiquidityWalletUpdated(newWallet);
    }
    
    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
    }
    
    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
    }
    
    function isExcludedFromFee(address account) public view returns(bool) {
        return _isExcludedFromFee[account];
    }
    
    function releaseTeamTokens() external onlyOwner {
        require(block.timestamp >= teamVestingStart.add(teamVestingCliff), "Team tokens are still locked");
        _mint(teamWallet, TEAM_ALLOCATION);
    }
}
```
