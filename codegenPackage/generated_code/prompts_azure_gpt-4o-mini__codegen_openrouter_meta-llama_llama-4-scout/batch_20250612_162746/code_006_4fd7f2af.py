"""
Generated Code Metadata:
========================
Original URL: https://chitzoinu.pages.dev
Prompt: Write a Solidity contract that implements the token locking feature mentioned on the Chitzo Inu website.
Generated: DETERMINISTIC_4fd7f2af98c26424
Batch ID: 20250612_162746
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenLockingContract
 * @author [Your Name]
 * @notice This contract implements a token locking feature.
 */
contract TokenLockingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user addresses to their locked token balances
    mapping(address => uint256) public lockedBalances;

    // Mapping of user addresses to their lock expiration timestamps
    mapping(address => uint256) public lockExpirations;

    // Mapping of user addresses to their unlockers (accounts that can unlock the tokens)
    mapping(address => address) public unlockers;

    // ERC20 token contract instance
    ERC20 public token;

    /**
     * @notice Constructor
     * @param _token Address of the ERC20 token contract
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = ERC20(_token);
    }

    /**
     * @notice Locks tokens for a user
     * @param _user Address of the user
     * @param _amount Amount of tokens to lock
     * @param _expiration Timestamp when the tokens will be unlocked
     */
    function lockTokens(address _user, uint256 _amount, uint256 _expiration) external {
        require(_user != address(0), "User address cannot be zero");
        require(_amount > 0, "Amount must be greater than zero");
        require(_expiration > block.timestamp, "Expiration timestamp must be in the future");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's locked balance and lock expiration
        lockedBalances[_user] = lockedBalances[_user].add(_amount);
        lockExpirations[_user] = _expiration;

        emit TokensLocked(_user, _amount, _expiration);
    }

    /**
     * @notice Unlocks tokens for a user
     * @param _user Address of the user
     */
    function unlockTokens(address _user) external {
        require(_user != address(0), "User address cannot be zero");
        require(unlockers[_user] == msg.sender, "Only the designated unlocker can unlock tokens");

        // Check if the lock has expired
        require(lockExpirations[_user] <= block.timestamp, "Tokens are not yet unlocked");

        // Transfer tokens from the contract to the user
        uint256 lockedBalance = lockedBalances[_user];
        require(token.transfer(_user, lockedBalance), "Token transfer failed");

        // Reset the user's locked balance and lock expiration
        lockedBalances[_user] = 0;
        lockExpirations[_user] = 0;

        emit TokensUnlocked(_user, lockedBalance);
    }

    /**
     * @notice Sets the unlocker for a user
     * @param _user Address of the user
     * @param _unlocker Address of the unlocker
     */
    function setUnlocker(address _user, address _unlocker) external {
        require(_user != address(0), "User address cannot be zero");
        require(_unlocker != address(0), "Unlocker address cannot be zero");

        unlockers[_user] = _unlocker;

        emit UnlockedSet(_user, _unlocker);
    }

    /**
     * @notice Event emitted when tokens are locked
     * @param _user Address of the user
     * @param _amount Amount of tokens locked
     * @param _expiration Timestamp when the tokens will be unlocked
     */
    event TokensLocked(address indexed _user, uint256 _amount, uint256 _expiration);

    /**
     * @notice Event emitted when tokens are unlocked
     * @param _user Address of the user
     * @param _amount Amount of tokens unlocked
     */
    event TokensUnlocked(address indexed _user, uint256 _amount);

    /**
     * @notice Event emitted when an unlocker is set
     * @param _user Address of the user
     * @param _unlocker Address of the unlocker
     */
    event UnlockedSet(address indexed _user, address _unlocker);
}
```
