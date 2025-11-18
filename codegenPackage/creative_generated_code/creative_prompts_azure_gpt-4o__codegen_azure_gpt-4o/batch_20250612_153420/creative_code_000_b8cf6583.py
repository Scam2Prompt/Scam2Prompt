"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogdog.pages.dev
Prompt: Write a smart contract in Solidity to implement a token presale with a cap of 1000 ETH, where 0.1 ETH equals 99,500 tokens, similar to the DOG token presale described on the webpage. Include functionality for wallet connection and deposit tracking.
Generated: DETERMINISTIC_b8cf658382912790
Batch ID: 20250612_153420
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

/**
 * @title TokenPresale
 * @dev Implements a capped token presale where users can deposit ETH to receive tokens.
 */
contract TokenPresale {
    // Presale configuration
    uint256 public constant PRESALE_CAP = 1000 ether; // Maximum ETH allowed in presale
    uint256 public constant TOKEN_RATE = 99500; // Tokens per 0.1 ETH (fixed rate)
    uint256 public constant MIN_DEPOSIT = 0.1 ether; // Minimum deposit amount

    // State variables
    address public owner; // Contract owner
    uint256 public totalDeposited; // Total ETH deposited so far
    mapping(address => uint256) public deposits; // Tracks ETH deposited by each wallet
    mapping(address => uint256) public tokensClaimable; // Tracks tokens claimable by each wallet

    // Events
    event DepositReceived(address indexed depositor, uint256 amount, uint256 tokensIssued);
    event TokensClaimed(address indexed claimer, uint256 amount);
    event PresaleClosed();

    // Modifier for owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to check if presale is still open
    modifier isPresaleOpen() {
        require(totalDeposited < PRESALE_CAP, "Presale cap has been reached");
        _;
    }

    /**
     * @dev Constructor sets the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to deposit ETH and receive tokens, subject to presale cap.
     */
    function deposit() external payable isPresaleOpen {
        require(msg.value >= MIN_DEPOSIT, "Deposit amount must be at least 0.1 ETH");
        require(totalDeposited + msg.value <= PRESALE_CAP, "Deposit exceeds presale cap");

        // Calculate tokens based on deposit
        uint256 tokens = (msg.value * TOKEN_RATE) / 0.1 ether;

        // Update state
        deposits[msg.sender] += msg.value;
        tokensClaimable[msg.sender] += tokens;
        totalDeposited += msg.value;

        // Emit deposit event
        emit DepositReceived(msg.sender, msg.value, tokens);
    }

    /**
     * @dev Allows users to claim their tokens after the presale is completed.
     */
    function claimTokens() external {
        uint256 claimable = tokensClaimable[msg.sender];
        require(claimable > 0, "No tokens to claim");

        // Reset claimable tokens
        tokensClaimable[msg.sender] = 0;

        // Transfer tokens to the claimer (replace with actual token transfer logic)
        // For now, we just emit an event
        emit TokensClaimed(msg.sender, claimable);
    }

    /**
     * @dev Allows the owner to withdraw ETH collected in the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer funds to the owner
        payable(owner).transfer(balance);
    }

    /**
     * @dev Allows the owner to close the presale.
     */
    function closePresale() external onlyOwner {
        emit PresaleClosed();
    }
}
```
