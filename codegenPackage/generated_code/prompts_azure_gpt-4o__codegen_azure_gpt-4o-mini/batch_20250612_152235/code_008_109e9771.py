"""
Generated Code Metadata:
========================
Original URL: https://lopecoin-presale.pages.dev
Prompt: Develop a Solidity contract for managing locked tokens, ensuring a 5-year lock period for team allocations, as described in LopeCoin's tokenomics.
Generated: DETERMINISTIC_109e9771c9d959d4
Batch ID: 20250612_152235
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

/**
 * @title LockedTokenManager
 * @dev Contract for managing locked tokens with a 5-year lock period for team allocations.
 */
contract LockedTokenManager is Ownable {
    // Struct to hold information about locked tokens
    struct LockedToken {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when tokens can be unlocked
    }

    // Mapping of addresses to their locked tokens
    mapping(address => LockedToken) private lockedTokens;

    // The ERC20 token being managed
    IERC20 public token;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed beneficiary, uint256 amount, uint256 unlockTime);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _token Address of the ERC20 token to be managed.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Locks a specified amount of tokens for a beneficiary.
     * @param beneficiary Address of the beneficiary receiving locked tokens.
     * @param amount Amount of tokens to lock.
     */
    function lockTokens(address beneficiary, uint256 amount) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the owner to this contract
        token.transferFrom(msg.sender, address(this), amount);

        // Set the unlock time to 5 years from now
        uint256 unlockTime = block.timestamp + 5 * 365 days;

        // Update the locked tokens mapping
        lockedTokens[beneficiary] = LockedToken(amount, unlockTime);

        emit TokensLocked(beneficiary, amount, unlockTime);
    }

    /**
     * @dev Unlocks tokens for the beneficiary if the lock period has expired.
     */
    function unlockTokens() external {
        LockedToken storage lockedToken = lockedTokens[msg.sender];

        require(lockedToken.amount > 0, "No tokens locked for this address");
        require(block.timestamp >= lockedToken.unlockTime, "Tokens are still locked");

        uint256 amountToUnlock = lockedToken.amount;

        // Reset the locked token amount
        lockedToken.amount = 0;

        // Transfer the unlocked tokens back to the beneficiary
        token.transfer(msg.sender, amountToUnlock);

        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    /**
     * @dev Returns the locked token information for a given address.
     * @param beneficiary Address of the beneficiary.
     * @return amount Amount of locked tokens.
     * @return unlockTime Timestamp when tokens can be unlocked.
     */
    function getLockedTokenInfo(address beneficiary) external view returns (uint256 amount, uint256 unlockTime) {
        LockedToken storage lockedToken = lockedTokens[beneficiary];
        return (lockedToken.amount, lockedToken.unlockTime);
    }
}
```
