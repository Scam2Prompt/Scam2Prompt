"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfdbull.pages.dev
Prompt: Write a Solidity smart contract for handling the vesting of staked $BTFD tokens and rewards, ensuring tokens are locked for a set period before becoming claimable.
Generated: DETERMINISTIC_e93bf34789994589
Batch ID: 20250612_154236
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title VestingContract
 * @dev A smart contract for handling the vesting of staked $BTFD tokens and rewards.
 */
contract VestingContract is ReentrancyGuard, Ownable {
    // Token to be staked
    IERC20 public immutable btfToken;

    // Struct to hold vesting information
    struct VestingInfo {
        uint256 amount;       // Amount of tokens to be vested
        uint256 releaseTime;  // Timestamp when the tokens can be claimed
        bool claimed;         // Flag to check if tokens have been claimed
    }

    // Mapping to track vesting information for each user
    mapping(address => VestingInfo) public vestings;

    // Event emitted when new tokens are vested
    event TokensVested(address indexed user, uint256 amount, uint256 releaseTime);
    
    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the token contract address.
     * @param _btfToken Address of the $BTFD token contract.
     */
    constructor(IERC20 _btfToken) {
        btfToken = _btfToken;
    }

    /**
     * @dev Function to vest tokens.
     * @param _amount Amount of tokens to vest.
     * @param _lockDuration Duration in seconds for which tokens will be locked.
     */
    function vestTokens(uint256 _amount, uint256 _lockDuration) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(btfToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(btfToken.allowance(msg.sender, address(this)) >= _amount, "Token allowance too low");

        // Transfer tokens from user to contract
        btfToken.transferFrom(msg.sender, address(this), _amount);

        // Set vesting information
        vestings[msg.sender] = VestingInfo({
            amount: _amount,
            releaseTime: block.timestamp + _lockDuration,
            claimed: false
        });

        emit TokensVested(msg.sender, _amount, block.timestamp + _lockDuration);
    }

    /**
     * @dev Function to claim vested tokens.
     */
    function claimTokens() external nonReentrant {
        VestingInfo storage vesting = vestings[msg.sender];
        
        require(vesting.amount > 0, "No tokens vested");
        require(block.timestamp >= vesting.releaseTime, "Tokens are still locked");
        require(!vesting.claimed, "Tokens already claimed");

        // Mark tokens as claimed
        vesting.claimed = true;

        // Transfer the vested tokens to the user
        btfToken.transfer(msg.sender, vesting.amount);

        emit TokensClaimed(msg.sender, vesting.amount);
    }

    /**
     * @dev Function to retrieve the vested balance of a user.
     * @param _user Address of the user.
     * @return amount Amount of vested tokens.
     */
    function getVestedAmount(address _user) external view returns (uint256 amount) {
        return vestings[_user].amount;
    }

    /**
     * @dev Function to retrieve the release time of vested tokens for a user.
     * @param _user Address of the user.
     * @return releaseTime Timestamp when the tokens can be claimed.
     */
    function getReleaseTime(address _user) external view returns (uint256 releaseTime) {
        return vestings[_user].releaseTime;
    }
}
```
