"""
Generated Code Metadata:
========================
Original URL: https://wallstreet-pepe.vercel.app
Prompt: Generate a smart contract code snippet in Solidity to create a simple tokenomics system for $WEPE Token with a total supply of 200,000,000,000 $WEPE.
Generated: DETERMINISTIC_1d5823ca0c111694
Batch ID: 20250622_212351
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

contract WEPEToken is ERC20, Ownable {
    uint256 public constant TOTAL_SUPPLY = 200_000_000_000 * 10**18;
    
    // Token distribution percentages
    uint256 public constant TEAM_PERCENT = 15;
    uint256 public constant MARKETING_PERCENT = 10;
    uint256 public constant LIQUIDITY_PERCENT = 30;
    uint256 public constant COMMUNITY_PERCENT = 25;
    uint256 public constant RESERVE_PERCENT = 20;
    
    // Addresses for token allocation
    address public teamWallet;
    address public marketingWallet;
    address public liquidityWallet;
    address public communityWallet;
    address public reserveWallet;
    
    constructor(
        address _teamWallet,
        address _marketingWallet,
        address _liquidityWallet,
        address _communityWallet,
        address _reserveWallet
    ) ERC20("WEPE Token", "WEPE") {
        require(_teamWallet != address(0), "Team wallet cannot be zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");
        require(_communityWallet != address(0), "Community wallet cannot be zero address");
        require(_reserveWallet != address(0), "Reserve wallet cannot be zero address");
        
        teamWallet = _teamWallet;
        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;
        communityWallet = _communityWallet;
        reserveWallet = _reserveWallet;
        
        // Mint total supply to contract
        _mint(address(this), TOTAL_SUPPLY);
        
        // Distribute tokens according to percentages
        _distributeTokens();
    }
    
    function _distributeTokens() private {
        uint256 teamAmount = (TOTAL_SUPPLY * TEAM_PERCENT) / 100;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_PERCENT) / 100;
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_PERCENT) / 100;
        uint256 communityAmount = (TOTAL_SUPPLY * COMMUNITY_PERCENT) / 100;
        uint256 reserveAmount = (TOTAL_SUPPLY * RESERVE_PERCENT) / 100;
        
        // Verify distribution sums to total supply
        require(
            teamAmount + marketingAmount + liquidityAmount + communityAmount + reserveAmount == TOTAL_SUPPLY,
            "Token distribution does not match total supply"
        );
        
        // Transfer tokens to respective wallets
        _transfer(address(this), teamWallet, teamAmount);
        _transfer(address(this), marketingWallet, marketingAmount);
        _transfer(address(this), liquidityWallet, liquidityAmount);
        _transfer(address(this), communityWallet, communityAmount);
        _transfer(address(this), reserveWallet, reserveAmount);
    }
    
    // Function to update team wallet address (only owner)
    function updateTeamWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero address");
        teamWallet = _newWallet;
    }
    
    // Function to update marketing wallet address (only owner)
    function updateMarketingWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero address");
        marketingWallet = _newWallet;
    }
    
    // Function to update liquidity wallet address (only owner)
    function updateLiquidityWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero address");
        liquidityWallet = _newWallet;
    }
    
    // Function to update community wallet address (only owner)
    function updateCommunityWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero address");
        communityWallet = _newWallet;
    }
    
    // Function to update reserve wallet address (only owner)
    function updateReserveWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero address");
        reserveWallet = _newWallet;
    }
}
```
