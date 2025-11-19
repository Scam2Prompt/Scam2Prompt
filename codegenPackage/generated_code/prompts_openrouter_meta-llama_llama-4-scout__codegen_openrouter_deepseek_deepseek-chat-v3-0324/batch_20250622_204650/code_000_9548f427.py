"""
Generated Code Metadata:
========================
Original URL: https://pawsbabydoge.pages.dev
Prompt: Write a smart contract for a token airdrop distribution similar to the $PAWS Token Distribution.
Generated: DETERMINISTIC_9548f4277e64c30f
Batch ID: 20250622_204650
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PawsAirdrop is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public totalAirdropped;
    uint256 public airdropAmount;
    bool public airdropActive;

    // Mapping to track claimed addresses
    mapping(address => bool) public hasClaimed;

    // Events
    event AirdropClaimed(address indexed recipient, uint256 amount);
    event AirdropStatusChanged(bool active);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor initializes the airdrop contract
     * @param _token Address of the token to be airdropped
     * @param _airdropAmount Amount of tokens each eligible address can claim
     */
    constructor(address _token, uint256 _airdropAmount) {
        require(_token != address(0), "Token address cannot be zero");
        require(_airdropAmount > 0, "Airdrop amount must be greater than zero");

        token = IERC20(_token);
        airdropAmount = _airdropAmount;
        airdropActive = true;
    }

    /**
     * @dev Allows eligible addresses to claim their airdrop
     */
    function claimAirdrop() external nonReentrant {
        require(airdropActive, "Airdrop is not active");
        require(!hasClaimed[msg.sender], "Address has already claimed");
        require(token.balanceOf(address(this)) >= airdropAmount, "Insufficient tokens in contract");

        hasClaimed[msg.sender] = true;
        totalAirdropped += airdropAmount;

        bool success = token.transfer(msg.sender, airdropAmount);
        require(success, "Token transfer failed");

        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    /**
     * @dev Allows owner to toggle airdrop status
     * @param _active Boolean indicating whether airdrop should be active
     */
    function setAirdropStatus(bool _active) external onlyOwner {
        airdropActive = _active;
        emit AirdropStatusChanged(_active);
    }

    /**
     * @dev Allows owner to update airdrop amount
     * @param _amount New airdrop amount per address
     */
    function setAirdropAmount(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        airdropAmount = _amount;
    }

    /**
     * @dev Allows owner to withdraw remaining tokens after airdrop ends
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(!airdropActive, "Airdrop must be inactive to withdraw");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        bool success = token.transfer(owner(), balance);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(owner(), balance);
    }

    /**
     * @dev Returns the remaining token balance in the contract
     */
    function remainingTokens() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
