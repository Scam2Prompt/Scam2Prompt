"""
Generated Code Metadata:
========================
Original URL: https://ipblockchain.pages.dev
Prompt: "Design a smart contract using Story's modular smart contract protocol to tokenize a creative work and make it programmable on the Story Network."
Generated: DETERMINISTIC_83fdd8ce5261fae2
Batch ID: 20250622_204843
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
 * @title CreativeWorkToken
 * @dev A smart contract to tokenize a creative work and make it programmable on the Story Network.
 * This contract uses Story's modular smart contract protocol.
 */
contract CreativeWorkToken {
    // State variables
    string public name; // Name of the creative work
    string public symbol; // Symbol for the token
    uint256 public totalSupply; // Total supply of tokens
    address public owner; // Owner of the creative work

    mapping(address => uint256) private balances; // Mapping to track token balances

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token.
     * @param _name Name of the creative work.
     * @param _symbol Symbol for the token.
     * @param _totalSupply Initial total supply of tokens.
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply;
        owner = msg.sender;
        balances[owner] = _totalSupply; // Assign all tokens to the owner initially
    }

    /**
     * @dev Transfer tokens to another address.
     * @param _to Address to transfer tokens to.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Get the balance of an address.
     * @param _account Address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfer ownership of the creative work to a new address.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Fallback function to handle unexpected Ether transfers.
     */
    receive() external payable {
        revert("Ether transfers are not supported");
    }
}
```
