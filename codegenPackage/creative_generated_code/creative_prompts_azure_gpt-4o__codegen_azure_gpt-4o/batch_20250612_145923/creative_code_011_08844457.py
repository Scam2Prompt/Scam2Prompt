"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdappsmultichainweb.web.app
Prompt: Create an example of how to implement a presale token purchase and claim feature using the MultiChain Protocol.
Generated: DETERMINISTIC_08844457bb0e23f0
Batch ID: 20250612_145923
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
 * @title PresaleToken
 * @dev A contract for managing token presales and claims using the MultiChain Protocol.
 */
contract PresaleToken {
    // Token details
    string public name = "PresaleToken";
    string public symbol = "PST";
    uint8 public decimals = 18;

    // Presale parameters
    uint256 public presaleRate; // Number of tokens per ETH
    uint256 public presaleCap; // Maximum tokens available for presale
    uint256 public totalTokensSold;

    // Presale duration
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;

    // Token balances
    mapping(address => uint256) public balances;

    // Address of the token owner
    address public owner;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimer, uint256 amount);

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    // Modifier to check presale status
    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime, "Presale has not started yet");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        _;
    }

    // Modifier to check claim eligibility
    modifier claimAllowed() {
        require(block.timestamp > presaleEndTime, "Claiming is allowed only after the presale ends");
        _;
    }

    /**
     * @dev Constructor to initialize presale parameters.
     * @param _rate Number of tokens per ETH.
     * @param _cap Maximum tokens for presale.
     * @param _startTime Presale start time in UNIX timestamp.
     * @param _endTime Presale end time in UNIX timestamp.
     */
    constructor(uint256 _rate, uint256 _cap, uint256 _startTime, uint256 _endTime) {
        require(_rate > 0, "Rate must be greater than zero");
        require(_cap > 0, "Cap must be greater than zero");
        require(_startTime < _endTime, "Start time must be earlier than end time");

        owner = msg.sender;
        presaleRate = _rate;
        presaleCap = _cap;
        presaleStartTime = _startTime;
        presaleEndTime = _endTime;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * Requires the presale to be active and sufficient tokens to be available.
     */
    function purchaseTokens() external payable presaleActive {
        require(msg.value > 0, "Must send ETH to purchase tokens");

        uint256 tokensToBuy = msg.value * presaleRate;
        require(totalTokensSold + tokensToBuy <= presaleCap, "Not enough tokens left for presale");

        // Update state
        balances[msg.sender] += tokensToBuy;
        totalTokensSold += tokensToBuy;

        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /**
     * @dev Function to claim tokens after the presale ends.
     * Requires the sender to have tokens available to claim.
     */
    function claimTokens() external claimAllowed {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No tokens available to claim");

        // Reset balance
        balances[msg.sender] = 0;

        // Transfer tokens (simulation, replace with real token transfer in production)
        // IERC20(tokenAddress).transfer(msg.sender, amount);

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw presale funds to the owner's address.
     * Accessible only after the presale ends.
     */
    function withdrawFunds() external onlyOwner claimAllowed {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH deposits.
     */
    receive() external payable {
        revert("Direct deposits not allowed");
    }
}
```
