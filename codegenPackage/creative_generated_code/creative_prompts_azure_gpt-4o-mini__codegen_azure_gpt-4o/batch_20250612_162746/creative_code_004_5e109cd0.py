"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://to-ousd.pages.dev
Prompt: Create a function that allows users to opt-in to receive stablecoin yield from OUSD while holding it in a smart contract.
Generated: DETERMINISTIC_5e109cd0960a36d9
Batch ID: 20250612_162746
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

/// @title Opt-In Stablecoin Yield Contract
/// @notice This contract allows users to deposit OUSD and earn yield on their stablecoins.
/// @dev The contract interacts with the OUSD protocol to distribute yield.

interface IOUSD {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract StablecoinYield {
    // OUSD token address
    address public ousdToken;
    // Mapping to track user deposits
    mapping(address => uint256) public userBalances;

    /// @notice Event emitted when a user opts in to yield
    event OptedIn(address indexed user, uint256 amount);
    /// @notice Event emitted when a user withdraws their funds
    event Withdrawn(address indexed user, uint256 amount);

    /// @param _ousdToken The address of the OUSD token contract
    constructor(address _ousdToken) {
        require(_ousdToken != address(0), "Invalid OUSD token address");
        ousdToken = _ousdToken;
    }

    /// @notice Allows a user to deposit OUSD and opt-in for yield
    /// @param _amount The amount of OUSD to deposit
    function optIn(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be greater than zero");

        IOUSD token = IOUSD(ousdToken);
        uint256 senderBalance = token.balanceOf(msg.sender);
        require(senderBalance >= _amount, "Insufficient OUSD balance");

        // Transfer OUSD from the user to the contract
        bool success = token.transferFrom(msg.sender, address(this), _amount);
        require(success, "OUSD transfer failed");

        // Update the user's balance
        userBalances[msg.sender] += _amount;

        emit OptedIn(msg.sender, _amount);
    }

    /// @notice Allows a user to withdraw their OUSD and stop earning yield
    function withdraw() external {
        uint256 userBalance = userBalances[msg.sender];
        require(userBalance > 0, "No funds to withdraw");

        IOUSD token = IOUSD(ousdToken);

        // Transfer OUSD back to the user
        bool success = token.transfer(msg.sender, userBalance);
        require(success, "OUSD transfer failed");

        // Reset the user's balance
        userBalances[msg.sender] = 0;

        emit Withdrawn(msg.sender, userBalance);
    }

    /// @notice Returns the user's current deposit balance
    /// @param _user The address of the user
    /// @return The amount of OUSD deposited by the user
    function getBalance(address _user) external view returns (uint256) {
        return userBalances[_user];
    }
}
```
