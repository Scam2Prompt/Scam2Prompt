"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Write a Solidity contract to implement Ziber's token distribution rules, ensuring 80% of tokens are available for open sale, 10% are allocated to the team, and 10% are distributed as bonuses to Bitcoin and Ethereum owners.
Generated: DETERMINISTIC_695e97d62b6d8fa4
Batch ID: 20250612_151531
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

contract ZiberToken is ERC20, Ownable {
    uint256 public constant TOTAL_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    uint256 public constant OPEN_SALE_PERCENT = 80;
    uint256 public constant TEAM_ALLOCATION_PERCENT = 10;
    uint256 public constant BONUS_ALLOCATION_PERCENT = 10;
    
    address public teamWallet;
    address public bonusDistributionContract;
    
    bool public teamTokensAllocated = false;
    bool public bonusTokensAllocated = false;
    
    constructor(address _teamWallet) ERC20("Ziber Token", "ZIBER") {
        require(_teamWallet != address(0), "Invalid team wallet address");
        teamWallet = _teamWallet;
        
        // Mint open sale tokens to contract owner
        uint256 openSaleAmount = (TOTAL_SUPPLY * OPEN_SALE_PERCENT) / 100;
        _mint(owner(), openSaleAmount);
    }
    
    function allocateTeamTokens() external onlyOwner {
        require(!teamTokensAllocated, "Team tokens already allocated");
        
        uint256 teamAmount = (TOTAL_SUPPLY * TEAM_ALLOCATION_PERCENT) / 100;
        _mint(teamWallet, teamAmount);
        
        teamTokensAllocated = true;
    }
    
    function setBonusDistributionContract(address _bonusContract) external onlyOwner {
        require(_bonusContract != address(0), "Invalid bonus contract address");
        bonusDistributionContract = _bonusContract;
    }
    
    function allocateBonusTokens() external onlyOwner {
        require(!bonusTokensAllocated, "Bonus tokens already allocated");
        require(bonusDistributionContract != address(0), "Bonus contract not set");
        
        uint256 bonusAmount = (TOTAL_SUPPLY * BONUS_ALLOCATION_PERCENT) / 100;
        _mint(bonusDistributionContract, bonusAmount);
        
        bonusTokensAllocated = true;
    }
    
    function burn(uint256 amount) external {
        _burn(_msgSender(), amount);
    }
}
```
