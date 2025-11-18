"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-neiroeth.pages.dev
Prompt: Write a Solidity smart contract that donates a percentage of Neiro token transactions to a specified charity wallet address. Include functionality to update the charity wallet address by community vote.
Generated: DETERMINISTIC_82d561d4f5e25b7a
Batch ID: 20250612_151343
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

/// @title Neiro Token Charity Donation Smart Contract
/// @notice This contract allows for charitable donations from Neiro token transactions.
/// @dev It allows community voting to change the charity wallet address.

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NeiroCharity is Ownable {
    using Counters for Counters.Counter;

    // Events
    event CharityWalletUpdated(address indexed newCharityWallet);
    event DonationMade(address indexed from, uint256 amount);
    event VoteCast(address indexed voter, bool inFavor);
    
    // State variables
    IERC20 public neiroToken; // Reference to the Neiro token contract
    address public charityWallet; // Current charity wallet address
    Counters.Counter private voteCounter; // Counter for total votes
    mapping(address => bool) public hasVoted; // Track voters to prevent double voting
    mapping(bool => uint256) public votes; // Votes for and against the charity wallet update

    // Percentage of transaction to donate
    uint256 public donationPercentage = 5; // 5% donation

    // Modifiers
    modifier onlyUniqueVoter() {
        require(!hasVoted[msg.sender], "You have already voted.");
        _;
    }

    // Constructor
    constructor(IERC20 _neiroToken, address _charityWallet) {
        neiroToken = _neiroToken;
        charityWallet = _charityWallet;
    }

    /// @notice Function to execute a token transfer with a donation to charity
    /// @param recipient The address to receive the tokens
    /// @param amount The amount of tokens to send
    function donateAndTransfer(address recipient, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        uint256 donation = (amount * donationPercentage) / 100;
        uint256 transferAmount = amount - donation;

        // Transfer the tokens
        neiroToken.transferFrom(msg.sender, recipient, transferAmount);
        neiroToken.transferFrom(msg.sender, charityWallet, donation);

        emit DonationMade(msg.sender, donation);
    }

    /// @notice Function to propose a new charity wallet address
    /// @param newCharityWallet The new charity wallet address
    function proposeCharityWallet(address newCharityWallet) external onlyOwner {
        charityWallet = newCharityWallet;
        emit CharityWalletUpdated(newCharityWallet);
    }

    /// @notice Function to vote for or against the proposed charity wallet change
    /// @param inFavor True if voting in favor, false if against
    function vote(bool inFavor) external onlyUniqueVoter {
        hasVoted[msg.sender] = true;
        votes[inFavor] += 1;
        voteCounter.increment();

        emit VoteCast(msg.sender, inFavor);
    }

    /// @notice Function to finalize the vote and update the charity wallet if passed
    function finalizeVote(address newCharityWallet) external onlyOwner {
        require(voteCounter.current() > 0, "No votes cast");
        uint256 totalVotes = voteCounter.current();
        
        if (votes[true] > totalVotes / 2) { // Simple majority
            charityWallet = newCharityWallet;
            emit CharityWalletUpdated(newCharityWallet);
        }

        // Reset votes for the next voting cycle
        resetVoting();
    }

    /// @notice Reset the voting state variables
    function resetVoting() private {
        voteCounter.reset();
        votes[true] = 0;
        votes[false] = 0;

        // Reset voters
        for (uint i = 0; i < 100; i++) { // Placeholder for potential unique voters
            if (hasVoted[msg.sender]) {
                hasVoted[msg.sender] = false;
            }
        }
    }
}
```
