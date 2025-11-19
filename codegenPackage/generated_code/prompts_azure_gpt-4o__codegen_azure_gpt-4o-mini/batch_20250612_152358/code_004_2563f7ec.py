"""
Generated Code Metadata:
========================
Original URL: https://bullperks.pages.dev
Prompt: Develop a smart contract on the BNB Chain (BEP20) for token claiming after an IDO, inspired by the BullClaimer feature described on BullPerks.
Generated: DETERMINISTIC_2563f7ec884ce47c
Batch ID: 20250612_152358
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

// Importing the BEP20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title IDO Token Claiming Contract
 * @dev This contract allows users to claim tokens after an Initial DEX Offering (IDO).
 */
contract IDOTokenClaim is Ownable {
    // State variables
    IERC20 public token; // The token to be claimed
    mapping(address => uint256) public claims; // Mapping to track claims per address
    uint256 public totalClaimed; // Total tokens claimed
    uint256 public claimStartTime; // Start time for claiming
    uint256 public claimEndTime; // End time for claiming

    // Events
    event TokensClaimed(address indexed claimant, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address and claim period.
     * @param _token Address of the BEP20 token to be claimed.
     * @param _claimStartTime Start time for claiming tokens.
     * @param _claimEndTime End time for claiming tokens.
     */
    constructor(IERC20 _token, uint256 _claimStartTime, uint256 _claimEndTime) {
        require(address(_token) != address(0), "Invalid token address");
        require(_claimStartTime < _claimEndTime, "Invalid claim period");

        token = _token;
        claimStartTime = _claimStartTime;
        claimEndTime = _claimEndTime;
    }

    /**
     * @dev Function to claim tokens.
     * @param amount Amount of tokens to claim.
     */
    function claimTokens(uint256 amount) external {
        require(block.timestamp >= claimStartTime, "Claim period has not started");
        require(block.timestamp <= claimEndTime, "Claim period has ended");
        require(amount > 0, "Amount must be greater than zero");
        require(claims[msg.sender] + amount <= getMaxClaimable(msg.sender), "Exceeds claimable amount");

        // Update the claims mapping
        claims[msg.sender] += amount;
        totalClaimed += amount;

        // Transfer tokens to the claimant
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(msg.sender, amount);

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to get the maximum claimable amount for an address.
     * @param claimant Address of the claimant.
     * @return uint256 Maximum claimable amount.
     */
    function getMaxClaimable(address claimant) public view returns (uint256) {
        // Logic to determine the maximum claimable amount
        // This can be customized based on your IDO logic
        return 1000 * 10**18; // Example: fixed amount for demonstration
    }

    /**
     * @dev Function to withdraw remaining tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Function to set a new claim period.
     * @param _claimStartTime New start time for claiming tokens.
     * @param _claimEndTime New end time for claiming tokens.
     */
    function setClaimPeriod(uint256 _claimStartTime, uint256 _claimEndTime) external onlyOwner {
        require(_claimStartTime < _claimEndTime, "Invalid claim period");
        claimStartTime = _claimStartTime;
        claimEndTime = _claimEndTime;
    }
}
```
