"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corgiaixyz.pages.dev
Prompt: Create a smart contract in Solidity for the $CORGIAI token that includes staking functionality and token burn mechanisms as outlined in the CorgiAI roadmap.
Generated: DETERMINISTIC_d59a0c6629e502f0
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// CorgiAI token contract
contract CorgiAIToken is ERC20, Ownable, ReentrancyGuard {
    // Variables for staking
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }
    
    mapping(address => Stake) private stakes;
    uint256 public totalStaked;
    uint256 public burnRate; // Percentage to burn on transfer (e.g., 5 = 5%)
    uint256 public constant BURN_RATE_DIVISOR = 100; // Used to calculate the burn

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to initialize the token
    constructor(uint256 initialSupply, uint256 _burnRate) ERC20("CorgiAI Token", "$CORGIAI") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        burnRate = _burnRate;
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance for staking");
        
        // Transfer tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);
        
        // Update the stake mapping and total staked amount
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakedAt = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update the stake and total staked amount
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Override transfer function to include burn mechanism
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        uint256 burnAmount = (amount * burnRate) / BURN_RATE_DIVISOR;

        if (burnAmount > 0) {
            // Burn the calculated amount
            super._transfer(sender, address(0), burnAmount);
            emit TokensBurned(sender, burnAmount);
        }

        uint256 amountAfterBurn = amount - burnAmount;
        super._transfer(sender, recipient, amountAfterBurn);
    }

    // Get staked amount for a specific user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Get staking duration for a specific user
    function getStakingDuration(address user) external view returns (uint256) {
        if (stakes[user].amount == 0) {
            return 0;
        }
        return block.timestamp - stakes[user].stakedAt;
    }

    // Owner-only function to update burn rate
    function updateBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= BURN_RATE_DIVISOR, "Burn rate must be <= 100%");
        burnRate = newBurnRate;
    }
}
```
