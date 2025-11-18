"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-en.web.app
Prompt: Generate a Solidity function to enable users to claim their $SCOTTY tokens after the presale ends, with a 7-day withdrawal restriction.
Generated: DETERMINISTIC_6506726cd184f5bd
Batch ID: 20250612_151405
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

contract ScottyTokenClaim {
    // Address of the token contract
    address public tokenAddress;
    // Owner of the contract
    address public owner;
    // Timestamp when presale ends
    uint256 public presaleEndTime;
    // Mapping to track claimed tokens for each user
    mapping(address => uint256) public claimedTokens;
    // Mapping for user balances
    mapping(address => uint256) public presaleBalances;

    // Events
    event TokensClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to owner functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _tokenAddress, uint256 _presaleEndTime) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleEndTime > block.timestamp, "Presale end time must be in the future");

        tokenAddress = _tokenAddress;
        presaleEndTime = _presaleEndTime;
        owner = msg.sender;
    }

    // Function to set presale balances
    // This function allows the owner to set presale balances for users
    function setPresaleBalance(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        presaleBalances[user] = amount;
    }

    // Function for users to claim their tokens after the presale ends and the 7-day restriction period
    function claimTokens() external {
        require(block.timestamp > presaleEndTime + 7 days, "Claim period not started");
        require(presaleBalances[msg.sender] > 0, "No tokens to claim");

        uint256 amountToClaim = presaleBalances[msg.sender];
        presaleBalances[msg.sender] = 0; // Reset the user's balance to prevent re-claiming
        claimedTokens[msg.sender] += amountToClaim;

        // Transfer tokens to the user
        require(
            IERC20(tokenAddress).transfer(msg.sender, amountToClaim),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, amountToClaim);
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
