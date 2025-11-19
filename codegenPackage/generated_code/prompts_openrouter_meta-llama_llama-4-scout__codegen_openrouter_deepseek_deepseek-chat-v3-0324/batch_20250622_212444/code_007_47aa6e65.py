"""
Generated Code Metadata:
========================
Original URL: https://dikmansdeli.ru
Prompt: "Design an XVS tokenomics model to incentivize long-term holding and participation in the Venus Protocol ecosystem, assuming a specific market capitalization target."
Generated: DETERMINISTIC_47aa6e65e760b45d
Batch ID: 20250622_212444
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract XVSToken is ERC20, ERC20Votes, Ownable {
    uint256 public constant MAX_SUPPLY = 10_000_000_000 * 1e18; // 10 billion XVS
    uint256 public constant MARKET_CAP_TARGET = 1_000_000_000 * 1e18; // $1 billion target
    uint256 public constant VESTING_PERIOD = 365 days; // 1 year vesting
    uint256 public constant LOCK_PERIOD = 90 days; // 90 days lock for early withdraw
    
    uint256 public totalVested;
    uint256 public emissionRate;
    uint256 public lastEmissionUpdate;
    
    struct VestingInfo {
        uint256 amount;
        uint256 startTime;
        uint256 claimed;
    }
    
    mapping(address => VestingInfo) public vestingInfo;
    
    event TokensVested(address indexed user, uint256 amount, uint256 startTime);
    event TokensClaimed(address indexed user, uint256 amount);
    event EmissionRateUpdated(uint256 newRate);
    
    constructor() ERC20("Venus Token", "XVS") ERC20Permit("Venus Token") {
        _mint(msg.sender, MAX_SUPPLY * 20 / 100); // 20% initial distribution
        emissionRate = (MAX_SUPPLY * 80 / 100) / (10 * 365 days); // 10 year emission schedule
        lastEmissionUpdate = block.timestamp;
    }
    
    function vestTokens(uint256 amount) external {
        require(amount > 0, "XVS: Amount must be positive");
        require(balanceOf(msg.sender) >= amount, "XVS: Insufficient balance");
        
        _burn(msg.sender, amount);
        
        VestingInfo storage info = vestingInfo[msg.sender];
        info.amount += amount;
        info.startTime = block.timestamp;
        totalVested += amount;
        
        emit TokensVested(msg.sender, amount, block.timestamp);
    }
    
    function claimVestedTokens() external {
        VestingInfo storage info = vestingInfo[msg.sender];
        require(info.amount > 0, "XVS: No vested tokens");
        
        uint256 claimable = _calculateClaimable(info);
        require(claimable > 0, "XVS: No tokens to claim");
        
        info.claimed += claimable;
        totalVested -= claimable;
        
        if (info.claimed == info.amount) {
            delete vestingInfo[msg.sender];
        }
        
        _mint(msg.sender, claimable);
        emit TokensClaimed(msg.sender, claimable);
    }
    
    function _calculateClaimable(VestingInfo memory info) internal view returns (uint256) {
        if (block.timestamp < info.startTime + LOCK_PERIOD) {
            return 0;
        }
        
        uint256 elapsed = block.timestamp - info.startTime;
        if (elapsed >= VESTING_PERIOD) {
            return info.amount - info.claimed;
        }
        
        return (info.amount * elapsed / VESTING_PERIOD) - info.claimed;
    }
    
    function updateEmissionRate() external onlyOwner {
        uint256 currentSupply = totalSupply();
        if (currentSupply >= MARKET_CAP_TARGET) {
            emissionRate = emissionRate / 2; // Halve emission if target reached
            emit EmissionRateUpdated(emissionRate);
        }
        lastEmissionUpdate = block.timestamp;
    }
    
    function _afterTokenTransfer(address from, address to, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._afterTokenTransfer(from, to, amount);
    }
    
    function _mint(address to, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._mint(to, amount);
    }
    
    function _burn(address account, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._burn(account, amount);
    }
    
    function circulatingSupply() public view returns (uint256) {
        return totalSupply() - totalVested;
    }
}
```
