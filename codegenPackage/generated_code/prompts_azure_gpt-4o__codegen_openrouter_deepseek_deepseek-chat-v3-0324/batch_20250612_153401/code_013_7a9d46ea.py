"""
Generated Code Metadata:
========================
Original URL: https://mileimoneda-io.web.app
Prompt: Write an ERC-20 token contract in Solidity that includes features for airdrops and liquidity pool management, modeled after the Milei Moneda tokenomics.
Generated: DETERMINISTIC_7a9d46eabd00ff20
Batch ID: 20250612_153401
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

contract MileiMoneda is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution parameters
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TEAM_ALLOCATION = 100_000_000 * 10**18; // 10% for team
    uint256 public constant AIRDROP_ALLOCATION = 50_000_000 * 10**18; // 5% for airdrops
    uint256 public constant LIQUIDITY_POOL_ALLOCATION = 300_000_000 * 10**18; // 30% for liquidity
    
    // Addresses
    address public teamWallet;
    address public liquidityPool;
    
    // Airdrop tracking
    mapping(address => bool) public airdropRecipients;
    uint256 public airdropAmount = 500 * 10**18; // 500 tokens per airdrop
    
    // Liquidity management
    bool public liquidityLocked = false;
    uint256 public liquidityLockDuration = 365 days; // 1 year lock
    uint256 public liquidityLockTime;
    
    // Events
    event AirdropDistributed(address indexed recipient, uint256 amount);
    event LiquidityPoolSet(address indexed pool);
    event LiquidityLocked(uint256 unlockTime);
    
    constructor(address _teamWallet) ERC20("Milei Moneda", "MEDA") {
        require(_teamWallet != address(0), "Invalid team wallet address");
        
        teamWallet = _teamWallet;
        
        // Mint initial allocations
        _mint(teamWallet, TEAM_ALLOCATION);
        _mint(address(this), AIRDROP_ALLOCATION);
        _mint(address(this), LIQUIDITY_POOL_ALLOCATION);
        
        // Mint remaining to owner for further distribution
        uint256 remaining = TOTAL_SUPPLY.sub(TEAM_ALLOCATION)
            .sub(AIRDROP_ALLOCATION)
            .sub(LIQUIDITY_POOL_ALLOCATION);
        _mint(msg.sender, remaining);
    }
    
    /**
     * @dev Distribute airdrop tokens to multiple recipients
     * @param recipients Array of addresses to receive airdrop
     */
    function distributeAirdrop(address[] calldata recipients) external onlyOwner {
        require(address(this).balance > 0, "Contract has no tokens for airdrop");
        require(recipients.length > 0, "No recipients provided");
        
        uint256 totalRequired = airdropAmount.mul(recipients.length);
        require(balanceOf(address(this)) >= totalRequired, "Insufficient airdrop balance");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(recipient != address(0), "Invalid recipient address");
            require(!airdropRecipients[recipient], "Recipient already received airdrop");
            
            _transfer(address(this), recipient, airdropAmount);
            airdropRecipients[recipient] = true;
            
            emit AirdropDistributed(recipient, airdropAmount);
        }
    }
    
    /**
     * @dev Set the liquidity pool address and lock liquidity
     * @param _liquidityPool Address of the liquidity pool
     */
    function setLiquidityPool(address _liquidityPool) external onlyOwner {
        require(_liquidityPool != address(0), "Invalid liquidity pool address");
        require(!liquidityLocked, "Liquidity already locked");
        
        liquidityPool = _liquidityPool;
        _transfer(address(this), liquidityPool, LIQUIDITY_POOL_ALLOCATION);
        
        liquidityLocked = true;
        liquidityLockTime = block.timestamp.add(liquidityLockDuration);
        
        emit LiquidityPoolSet(liquidityPool);
        emit LiquidityLocked(liquidityLockTime);
    }
    
    /**
     * @dev Update airdrop amount
     * @param newAmount New airdrop amount per recipient
     */
    function updateAirdropAmount(uint256 newAmount) external onlyOwner {
        require(newAmount > 0, "Airdrop amount must be positive");
        airdropAmount = newAmount;
    }
    
    /**
     * @dev Withdraw any remaining tokens after airdrop distribution
     */
    function withdrawRemainingAirdrop() external onlyOwner {
        require(block.timestamp > liquidityLockTime, "Liquidity is still locked");
        uint256 remaining = balanceOf(address(this));
        require(remaining > 0, "No remaining tokens");
        
        _transfer(address(this), owner(), remaining);
    }
    
    /**
     * @dev Override transfer to prevent transfers during liquidity lock period
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (sender == liquidityPool && liquidityLocked && block.timestamp < liquidityLockTime) {
            revert("Liquidity is locked");
        }
        super._transfer(sender, recipient, amount);
    }
}
```
