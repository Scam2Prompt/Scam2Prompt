"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenafinance.vercel.app
Prompt: Write a smart contract to manage the allocation of 2% of the $PLENA token supply for Quest participants, including whitelist spot tracking.
Generated: DETERMINISTIC_55ed7ca3e6db6f09
Batch ID: 20250612_153526
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
 * @title PLENA Allocation Contract for Quest Participants
 * @dev This contract manages the allocation of 2% of the $PLENA token supply to whitelist participants.
 */
contract PlenaQuestAllocation {
    // State variables
    address public owner; // Owner of the contract
    address public tokenAddress; // Address of the PLENA token contract
    uint256 public allocatedSupply; // Total allocated supply for quest participants
    mapping(address => bool) public whitelist; // Whitelist tracking

    event WhitelistAdded(address indexed participant);
    event WhitelistRemoved(address indexed participant);
    event TokensAllocated(address indexed participant, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the PLENA token contract.
     * @param _totalSupply Total supply of the PLENA token.
     */
    constructor(address _tokenAddress, uint256 _totalSupply) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
        allocatedSupply = (_totalSupply * 2) / 100; // 2% of total supply
    }

    /**
     * @dev Add a participant to the whitelist.
     * @param _participant Address of the participant to whitelist.
     */
    function addToWhitelist(address _participant) external onlyOwner {
        require(_participant != address(0), "Invalid participant address");
        require(!whitelist[_participant], "Participant already whitelisted");
        whitelist[_participant] = true;
        emit WhitelistAdded(_participant);
    }

    /**
     * @dev Remove a participant from the whitelist.
     * @param _participant Address of the participant to remove.
     */
    function removeFromWhitelist(address _participant) external onlyOwner {
        require(whitelist[_participant], "Participant not whitelisted");
        whitelist[_participant] = false;
        emit WhitelistRemoved(_participant);
    }

    /**
     * @dev Allocate tokens to a whitelisted participant.
     * @param _participant Address of the participant to allocate tokens.
     * @param _amount Amount of tokens to allocate.
     */
    function allocateTokens(address _participant, uint256 _amount) external onlyOwner {
        require(whitelist[_participant], "Participant not whitelisted");
        require(_amount <= allocatedSupply, "Insufficient allocated supply");
        require(_amount > 0, "Allocation amount must be greater than zero");

        allocatedSupply -= _amount;
        bool success = ERC20(tokenAddress).transfer(_participant, _amount);
        require(success, "Token transfer failed");

        emit TokensAllocated(_participant, _amount);
    }
}

// Interface for ERC20 token contract
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
