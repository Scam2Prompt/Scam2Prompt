"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koi-finance.pages.dev
Prompt: Create a function to lock KOI tokens into a vote-escrow NFT for DAO governance participation, including calculating vote shares based on lock duration.
Generated: DETERMINISTIC_96b9c1520889b144
Batch ID: 20250612_151310
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

// Interface for the ERC20 token (KOI)
interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Interface for the Vote Escrow NFT
interface IVoteEscrow {
    function lockTokens(address user, uint256 amount, uint256 duration) external;
}

// Main contract for locking KOI tokens
contract KoiLock {
    IERC20 public koiToken; // The KOI token contract
    IVoteEscrow public voteEscrow; // The vote-escrow NFT contract

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount, uint256 duration);

    // Constructor to initialize contracts
    constructor(address _koiToken, address _voteEscrow) {
        require(_koiToken != address(0), "Invalid KOI token address");
        require(_voteEscrow != address(0), "Invalid Vote Escrow address");

        koiToken = IERC20(_koiToken);
        voteEscrow = IVoteEscrow(_voteEscrow);
    }

    // Function to lock KOI tokens into the vote-escrow NFT
    function lockKoiTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer KOI tokens from user to this contract
        bool transferSuccess = koiToken.transferFrom(msg.sender, address(this), amount);
        require(transferSuccess, "Token transfer failed");

        // Lock the tokens in the vote-escrow NFT
        voteEscrow.lockTokens(msg.sender, amount, duration);

        // Emit an event for the successful lock
        emit TokensLocked(msg.sender, amount, duration);
    }

    // Function to calculate vote shares based on lock duration
    function calculateVoteShares(uint256 amount, uint256 duration) public pure returns (uint256) {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Vote shares calculation logic (example: 1 share per token per duration unit)
        uint256 voteShares = amount * duration;
        return voteShares;
    }
}
```

In this contract:
- The `KoiLock` contract allows users to lock KOI tokens into a vote-escrow NFT.
- The `lockKoiTokens` function facilitates the locking process and includes error handling.
- The `calculateVoteShares` function computes the vote shares based on the amount of tokens and the lock duration.
