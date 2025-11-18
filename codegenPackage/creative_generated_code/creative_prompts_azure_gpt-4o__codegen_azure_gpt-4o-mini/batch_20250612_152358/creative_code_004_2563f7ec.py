"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bullperks.pages.dev
Prompt: Develop a smart contract on the BNB Chain (BEP20) for token claiming after an IDO, inspired by the BullClaimer feature described on BullPerks.
Generated: DETERMINISTIC_2563f7ec884ce47c
Batch ID: 20250612_152358
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

// Importing OpenZeppelin's ERC20 implementation and Ownable for access control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for BEP20 token claiming after an Initial DEX Offering (IDO)
contract BullClaimer is ERC20, Ownable {
    // Mapping to track the amount of tokens claimed by each user
    mapping(address => uint256) private _claimedAmounts;

    // Total supply of tokens for the IDO
    uint256 public totalSupplyIDO;
    // Timestamp for when the IDO starts
    uint256 public idoStartTime;
    // Duration of the claim period in seconds
    uint256 public claimPeriodDuration;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol, uint256 _totalSupplyIDO, uint256 _claimPeriodDuration) 
        ERC20(name, symbol) 
    {
        totalSupplyIDO = _totalSupplyIDO;
        claimPeriodDuration = _claimPeriodDuration;
        idoStartTime = block.timestamp; // Set the start time of the IDO to now
    }

    // Modifier to check if the claim period is active
    modifier onlyDuringClaimPeriod() {
        require(block.timestamp <= idoStartTime + claimPeriodDuration, "Claim period has ended");
        _;
    }

    // Function to claim tokens based on the user's contribution
    function claimTokens(uint256 amount) external onlyDuringClaimPeriod {
        // Check that the amount to claim does not exceed the allowed limit
        require(amount > 0, "Claim amount must be greater than zero");
        require(_claimedAmounts[msg.sender] + amount <= totalSupplyIDO, "Exceeds claimable amount");

        // Update the internal tracking of claimed amounts
        _claimedAmounts[msg.sender] += amount;

        // Transfer the tokens to the user
        _transfer(address(this), msg.sender, amount);

        // Emit an event for the token claim
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to withdraw leftover tokens after the claim period ends
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > idoStartTime + claimPeriodDuration, "Claim period still active");
        
        uint256 balance = balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer the remaining tokens to the owner
        _transfer(address(this), owner(), balance);
    }

    // Function to allow the owner to mint additional tokens if needed (optional)
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= totalSupplyIDO, "Cannot exceed total supply for IDO");
        _mint(to, amount);
    }

    // Function to check how many tokens a user has claimed
    function claimedTokens(address user) external view returns (uint256) {
        return _claimedAmounts[user];
    }

    // Override the transfer function to prevent token transfers during the claim period
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        require(block.timestamp > idoStartTime + claimPeriodDuration || from == address(0), "Token transfers are locked during claim period");
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
