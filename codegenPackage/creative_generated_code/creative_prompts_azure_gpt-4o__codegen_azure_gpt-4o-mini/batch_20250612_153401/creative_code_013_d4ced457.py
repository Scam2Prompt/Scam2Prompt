"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Develop a feature in Solidity that locks team tokens for 18 months and burns unsold tokens after the presale, as outlined in ETFSwap's anti-dump plan.
Generated: DETERMINISTIC_d4ced457e525bf35
Batch ID: 20250612_153401
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ETFSwapTokenLocker
 * @dev This contract locks team tokens for 18 months and burns unsold tokens after the presale.
 */
contract ETFSwapTokenLocker is Ownable {
    // The ERC20 token being managed
    ERC20Burnable public token;

    // Lock duration in seconds (18 months)
    uint256 public constant LOCK_DURATION = 18 * 30 * 24 * 60 * 60; // 18 months

    // Address of the team
    address public teamAddress;

    // Timestamp when the tokens were locked
    uint256 public lockTimestamp;

    // Boolean to track if tokens have been locked
    bool public tokensLocked;

    // Event emitted when tokens are locked
    event TokensLocked(uint256 amount, uint256 timestamp);

    // Event emitted when unsold tokens are burned
    event UnsoldTokensBurned(uint256 amount);

    /**
     * @dev Constructor to initialize the token and team address.
     * @param _token Address of the ERC20 token
     * @param _teamAddress Address of the team
     */
    constructor(address _token, address _teamAddress) {
        require(_token != address(0), "Token address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");

        token = ERC20Burnable(_token);
        teamAddress = _teamAddress;
    }

    /**
     * @dev Locks the specified amount of tokens for the team.
     * @param amount The amount of tokens to lock
     */
    function lockTokens(uint256 amount) external onlyOwner {
        require(!tokensLocked, "Tokens are already locked");
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer tokens from owner to this contract
        token.transferFrom(msg.sender, address(this), amount);
        lockTimestamp = block.timestamp;
        tokensLocked = true;

        emit TokensLocked(amount, lockTimestamp);
    }

    /**
     * @dev Burns unsold tokens after the presale.
     * @param amount The amount of unsold tokens to burn
     */
    function burnUnsoldTokens(uint256 amount) external onlyOwner {
        require(tokensLocked, "Tokens must be locked before burning unsold tokens");
        require(block.timestamp > lockTimestamp + LOCK_DURATION, "Lock period is not over yet");
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Burn the specified amount of unsold tokens
        token.burn(amount);

        emit UnsoldTokensBurned(amount);
    }

    /**
     * @dev Allows the contract to receive ETH (if any).
     */
    receive() external payable {}
}
```
