"""
Generated Code Metadata:
========================
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Develop a basic smart contract in Solidity that utilizes DOP's selective transparency feature to control the visibility of specific tokens or asset amounts on a blockchain.
Generated: DETERMINISTIC_58803024f7212a7f
Batch ID: 20250622_205117
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

/**
 * @title SelectiveTransparencyToken
 * @dev A smart contract that implements selective transparency for token balances.
 * Users can choose to make their token balances visible or hidden.
 */
contract SelectiveTransparencyToken {
    // Token name and symbol
    string public name = "SelectiveTransparencyToken";
    string public symbol = "STT";
    uint8 public decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Mapping to store balances of users
    mapping(address => uint256) private balances;

    // Mapping to store visibility preferences of users
    mapping(address => bool) public visibilityPreferences;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event VisibilityChanged(address indexed user, bool isVisible);

    // Constructor to initialize the total supply and assign it to the deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
    }

    /**
     * @dev Transfers tokens from the sender to the recipient.
     * @param _to The recipient address.
     * @param _value The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Gets the balance of a specific address.
     * If the address has set its visibility preference to false, the balance will not be returned.
     * @param _owner The address to query the balance of.
     * @return The balance of the address if visible, otherwise 0.
     */
    function balanceOf(address _owner) external view returns (uint256) {
        if (visibilityPreferences[_owner]) {
            return balances[_owner];
        } else {
            return 0; // Return 0 if the balance is hidden
        }
    }

    /**
     * @dev Sets the visibility preference for the sender's balance.
     * @param _isVisible True to make the balance visible, false to hide it.
     */
    function setVisibilityPreference(bool _isVisible) external {
        visibilityPreferences[msg.sender] = _isVisible;
        emit VisibilityChanged(msg.sender, _isVisible);
    }

    /**
     * @dev Internal function to get the actual balance of an address.
     * This function bypasses visibility preferences and is used internally.
     * @param _owner The address to query the balance of.
     * @return The actual balance of the address.
     */
    function _actualBalanceOf(address _owner) internal view returns (uint256) {
        return balances[_owner];
    }
}
```
