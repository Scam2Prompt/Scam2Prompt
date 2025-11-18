"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://team-finance-solana-dk4sprfr7-trustswap.vercel.app
Prompt: Provide a step-by-step guide to implement a customizable token lockup system similar to the "Create a Custom Token Lockup" feature on Team Finance.
Generated: DETERMINISTIC_d71b714ef04d367b
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, and production-ready implementation of a customizable token lockup system in Solidity. This code assumes you're working on the Ethereum blockchain and are familiar with ERC20 tokens.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenLockup
 * @dev This contract allows users to lock up ERC20 tokens for a specified period of time.
 */
contract TokenLockup {
    // Importing the interface for ERC20 tokens
    IERC20 public immutable token;

    // Structure to define a lockup entry
    struct Lockup {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when tokens can be unlocked
    }

    // Mapping from user address to their lockups
    mapping(address => Lockup[]) public lockups;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the ERC20 token to be locked.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Function to lock tokens in the contract.
     * @param _amount Amount of tokens to lock.
     * @param _lockupDuration Duration in seconds for the tokens to be locked.
     */
    function lockTokens(uint256 _amount, uint256 _lockupDuration) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_lockupDuration > 0, "Lockup duration must be greater than zero");

        uint256 unlockTime = block.timestamp + _lockupDuration;

        // Transfer tokens from the user to this contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Add new lockup entry
        lockups[msg.sender].push(Lockup(_amount, unlockTime));

        // Emit event for token lockup
        emit TokensLocked(msg.sender, _amount, unlockTime);
    }

    /**
     * @dev Function to unlock matured tokens and transfer them back to the user.
     */
    function unlockTokens() external {
        uint256 totalUnlocked = 0;
        Lockup[] storage userLockups = lockups[msg.sender];

        // Iterate through lockups to find matured entries
        for (uint256 i = 0; i < userLockups.length; i++) {
            if (userLockups[i].amount > 0 && block.timestamp >= userLockups[i].unlockTime) {
                totalUnlocked += userLockups[i].amount;
                userLockups[i].amount = 0; // Mark as unlocked
            }
        }

        require(totalUnlocked > 0, "No tokens available for unlocking");

        // Transfer unlocked tokens back to the user
        require(token.transfer(msg.sender, totalUnlocked), "Token transfer failed");

        // Emit event for token unlock
        emit TokensUnlocked(msg.sender, totalUnlocked);
    }

    /**
     * @dev Function to check user's lockup entries.
     * @param _user Address of the user whose lockups are to be checked.
     * @return Array of lockups (amount and unlockTime).
     */
    function getLockups(address _user) external view returns (Lockup[] memory) {
        return lockups[_user];
    }
}

/**
 * @dev Interface for ERC20 token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

### Notes:
1. **Dependencies**: The contract assumes an ERC20-compliant token interface (`IERC20`) is used.
2. **Security**: Ensure the ERC20 token contract supports `transferFrom` and `transfer`.
3. **Gas Efficiency**: It's recommended to optimize storage use further if the lockup count is expected to grow significantly.
4. **Testing**: Use unit tests to verify the functionality before deploying the contract in production.
