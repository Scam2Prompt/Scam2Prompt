"""
Generated Code Metadata:
========================
Original URL: https://teddyprc20.com
Prompt: What are the tokenomics of Teddy Bear ($BEAR), and how does its contract renouncement and LP locking impact its value on PulseChain?
Generated: DETERMINISTIC_b381e6cc99bfbaea
Batch ID: 20250622_212219
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
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

/**
 * @title Teddy Bear Token ($BEAR)
 * @dev Implementation of the Teddy Bear ERC20 token with tokenomics features
 */
contract TeddyBearToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TEAM_ALLOCATION = 100_000_000 * 10**18; // 10% for team
    uint256 public constant MARKETING_ALLOCATION = 50_000_000 * 10**18; // 5% for marketing
    uint256 public constant LP_ALLOCATION = 200_000_000 * 10**18; // 20% for liquidity pool
    uint256 public constant COMMUNITY_ALLOCATION = 650_000_000 * 10**18; // 65% for community
    
    // Tax structure (can be updated by owner before renouncement)
    uint256 public buyTax = 3; // 3% buy tax
    uint256 public sellTax = 5; // 5% sell tax
    address public marketingWallet;
    address public teamWallet;
    
    // LP and contract management
    address public lpPair;
    bool public isLpLocked;
    uint256 public lpLockTime;
    bool public isContractRenounced;
    
    // Exclusions from fees
    mapping(address => bool) private _isExcludedFromFee;
    
    // Events
    event TokensBurned(uint256 amount);
    event TaxesUpdated(uint256 newBuyTax, uint256 newSellTax);
    event LpLocked(uint256 lockTime);
    event ContractRenounced();
    
    constructor(
        address _marketingWallet,
        address _teamWallet,
        address _routerAddress
    ) ERC20("Teddy Bear", "BEAR") {
        marketingWallet = _marketingWallet;
        teamWallet = _teamWallet;
        
        // Mint initial allocations
        _mint(teamWallet, TEAM_ALLOCATION);
        _mint(marketingWallet, MARKETING_ALLOCATION);
        _mint(address(this), LP_ALLOCATION);
        _mint(msg.sender, COMMUNITY_ALLOCATION);
        
        // Create LP pair
        IUniswapV2Factory factory = IUniswapV2Factory(
            IUniswapV2Router02(_routerAddress).factory()
        );
        lpPair = factory.createPair(address(this), IUniswapV2Router02(_routerAddress).WETH());
        
        // Exclude important addresses from fees
        _isExcludedFromFee[owner()] = true;
        _isExcludedFromFee[address(this)] = true;
        _isExcludedFromFee[marketingWallet] = true;
        _isExcludedFromFee[teamWallet] = true;
    }
    
    /**
     * @dev Override transfer to implement tax logic
     */
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        uint256 taxAmount = 0;
        
        // Apply tax only if not excluded and it's a buy/sell
        if (!_isExcludedFromFee[from] && !_isExcludedFromFee[to]) {
            if (from == lpPair) {
                // Buy tax
                taxAmount = (amount * buyTax) / 100;
            } else if (to == lpPair) {
                // Sell tax
                taxAmount = (amount * sellTax) / 100;
            }
            
            if (taxAmount > 0) {
                super._transfer(from, marketingWallet, taxAmount);
                amount -= taxAmount;
            }
        }
        
        super._transfer(from, to, amount);
    }
    
    /**
     * @dev Lock LP tokens for a specified time
     */
    function lockLp(uint256 lockTimeInDays) external onlyOwner {
        require(!isContractRenounced, "Contract is renounced");
        require(!isLpLocked, "LP already locked");
        
        lpLockTime = block.timestamp + (lockTimeInDays * 1 days);
        isLpLocked = true;
        
        emit LpLocked(lpLockTime);
    }
    
    /**
     * @dev Renounce contract ownership (irreversible)
     */
    function renounceContract() external onlyOwner {
        require(isLpLocked, "LP must be locked first");
        isContractRenounced = true;
        renounceOwnership();
        
        emit ContractRenounced();
    }
    
    /**
     * @dev Update tax rates (only before renouncement)
     */
    function updateTaxes(uint256 _buyTax, uint256 _sellTax) external onlyOwner {
        require(!isContractRenounced, "Contract is renounced");
        require(_buyTax <= 10 && _sellTax <= 10, "Tax too high");
        
        buyTax = _buyTax;
        sellTax = _sellTax;
        
        emit TaxesUpdated(_buyTax, _sellTax);
    }
    
    /**
     * @dev Exclude/include address from fees
     */
    function setExcludedFromFee(address account, bool excluded) external onlyOwner {
        require(!isContractRenounced, "Contract is renounced");
        _isExcludedFromFee[account] = excluded;
    }
    
    /**
     * @dev Burn tokens from community allocation
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
        emit TokensBurned(amount);
    }
    
    /**
     * @dev Get remaining LP lock time
     */
    function getRemainingLockTime() external view returns (uint256) {
        if (!isLpLocked || block.timestamp >= lpLockTime) {
            return 0;
        }
        return lpLockTime - block.timestamp;
    }
}
```
