"""
Generated Code Metadata:
========================
Original URL: https://stake-coredaos.org
Prompt: Write a function in Solidity to redeem stCORE tokens for CORE tokens, ensuring the unlock time is checked before executing the redemption.
Generated: DETERMINISTIC_59d66515bc7acf16
Batch ID: 20250612_154651
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

/**
 * @title Staked CORE Token Redeemer
 * @notice Allows redemption of stCORE tokens for CORE tokens after a certain unlock time.
 */
contract StakedCoreRedeemer {
    // Mapping of user unlock times
    mapping(address => uint256) public userUnlockTimes;

    // Mapping of user stCORE balances
    mapping(address => uint256) public stCoreBalances;

    // Address of the stCORE token contract
    address public stCoreToken;

    // Address of the CORE token contract
    address public coreToken;

    // Event emitted when stCORE tokens are redeemed for CORE tokens
    event Redeemed(address indexed user, uint256 amount);

    /**
     * @notice Constructor for the StakedCoreRedeemer contract.
     * @param _stCoreToken Address of the stCORE token contract.
     * @param _coreToken Address of the CORE token contract.
     */
    constructor(address _stCoreToken, address _coreToken) {
        require(_stCoreToken != address(0), "stCORE token address cannot be zero");
        require(_coreToken != address(0), "CORE token address cannot be zero");

        stCoreToken = _stCoreToken;
        coreToken = _coreToken;
    }

    /**
     * @notice Sets the unlock time for a user.
     * @param _user Address of the user.
     * @param _unlockTime Unlock time in seconds.
     */
    function setUnlockTime(address _user, uint256 _unlockTime) public {
        require(msg.sender == stCoreToken, "Only stCORE token contract can set unlock time");
        userUnlockTimes[_user] = _unlockTime;
    }

    /**
     * @notice Deposits stCORE tokens for a user.
     * @param _user Address of the user.
     * @param _amount Amount of stCORE tokens to deposit.
     */
    function deposit(address _user, uint256 _amount) public {
        require(msg.sender == stCoreToken, "Only stCORE token contract can deposit");
        stCoreBalances[_user] += _amount;
    }

    /**
     * @notice Redeems stCORE tokens for CORE tokens.
     * @param _amount Amount of stCORE tokens to redeem.
     */
    function redeem(uint256 _amount) public {
        address user = msg.sender;
        require(stCoreBalances[user] >= _amount, "Insufficient stCORE balance");
        require(userUnlockTimes[user] != 0, "Unlock time not set for user");
        require(block.timestamp >= userUnlockTimes[user], "Unlock time not reached");

        stCoreBalances[user] -= _amount;

        // Transfer CORE tokens to the user
        IERC20(coreToken).transfer(user, _amount);

        emit Redeemed(user, _amount);
    }

    /**
     * @notice Allows the stCORE token contract to update stCORE balances.
     * @param _user Address of the user.
     * @param _amount Amount of stCORE tokens to update.
     */
    function updateStCoreBalance(address _user, uint256 _amount) public {
        require(msg.sender == stCoreToken, "Only stCORE token contract can update balance");
        stCoreBalances[_user] = _amount;
    }
}
```
