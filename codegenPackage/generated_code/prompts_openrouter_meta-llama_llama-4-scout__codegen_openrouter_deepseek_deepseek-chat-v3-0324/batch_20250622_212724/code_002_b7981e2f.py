"""
Generated Code Metadata:
========================
Original URL: https://peppermeme.org
Prompt: Generate a smart contract code snippet in Solidity for a token with a total supply of 1 billion, similar to the $PEPPER token economics described on the webpage.
Generated: DETERMINISTIC_b7981e2fffc35370
Batch ID: 20250622_212724
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

contract PEPPER is ERC20, Ownable {
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    
    // Addresses for token allocation
    address public treasuryAddress;
    address public teamAddress;
    address public marketingAddress;
    address public liquidityAddress;
    
    // Allocation percentages (multiplied by 100 for precision)
    uint256 public constant TREASURY_PERCENT = 3000; // 30%
    uint256 public constant TEAM_PERCENT = 2000;     // 20%
    uint256 public constant MARKETING_PERCENT = 1500; // 15%
    uint256 public constant LIQUIDITY_PERCENT = 3500; // 35%
    
    // Timelock for team tokens (6 months)
    uint256 public constant TEAM_LOCK_DURATION = 180 days;
    uint256 public teamUnlockTime;
    bool public teamTokensReleased = false;
    
    constructor(
        address _treasury,
        address _team,
        address _marketing,
        address _liquidity
    ) ERC20("PEPPER", "PEPPER") {
        require(_treasury != address(0), "Treasury address cannot be zero");
        require(_team != address(0), "Team address cannot be zero");
        require(_marketing != address(0), "Marketing address cannot be zero");
        require(_liquidity != address(0), "Liquidity address cannot be zero");
        
        treasuryAddress = _treasury;
        teamAddress = _team;
        marketingAddress = _marketing;
        liquidityAddress = _liquidity;
        
        teamUnlockTime = block.timestamp + TEAM_LOCK_DURATION;
        
        // Mint total supply to contract
        _mint(address(this), TOTAL_SUPPLY);
        
        // Distribute initial allocations
        _transfer(address(this), treasuryAddress, (TOTAL_SUPPLY * TREASURY_PERCENT) / 10000);
        _transfer(address(this), marketingAddress, (TOTAL_SUPPLY * MARKETING_PERCENT) / 10000);
        _transfer(address(this), liquidityAddress, (TOTAL_SUPPLY * LIQUIDITY_PERCENT) / 10000);
        
        // Team tokens remain locked in contract until unlock time
    }
    
    // Function to release team tokens after lock duration
    function releaseTeamTokens() external onlyOwner {
        require(block.timestamp >= teamUnlockTime, "Team tokens are still locked");
        require(!teamTokensReleased, "Team tokens already released");
        
        uint256 teamAmount = (TOTAL_SUPPLY * TEAM_PERCENT) / 10000;
        _transfer(address(this), teamAddress, teamAmount);
        teamTokensReleased = true;
    }
    
    // Function to change treasury address (only owner)
    function setTreasuryAddress(address _newTreasury) external onlyOwner {
        require(_newTreasury != address(0), "New treasury address cannot be zero");
        treasuryAddress = _newTreasury;
    }
    
    // Function to change marketing address (only owner)
    function setMarketingAddress(address _newMarketing) external onlyOwner {
        require(_newMarketing != address(0), "New marketing address cannot be zero");
        marketingAddress = _newMarketing;
    }
    
    // Function to change liquidity address (only owner)
    function setLiquidityAddress(address _newLiquidity) external onlyOwner {
        require(_newLiquidity != address(0), "New liquidity address cannot be zero");
        liquidityAddress = _newLiquidity;
    }
    
    // Function to change team address (only owner)
    function setTeamAddress(address _newTeam) external onlyOwner {
        require(_newTeam != address(0), "New team address cannot be zero");
        teamAddress = _newTeam;
    }
}
```
