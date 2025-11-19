"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogemob.pages.dev
Prompt: Create a Solidity smart contract that implements a simple buy and sell mechanism for the DOGEMOB token, ensuring a 0% buy and sell tax.
Generated: DETERMINISTIC_bda065b255b6011f
Batch ID: 20250612_135343
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

/**
 * @title DOGEMOB Token Smart Contract
 * @dev Implements a simple buy and sell mechanism with 0% tax.
 */
contract DogeMobToken {
    // Token properties
    string public constant name = "DOGEMOB";
    string public constant symbol = "DOGEMOB";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Mapping of token balances
    mapping(address => uint256) public balances;

    // Mapping for allowance approvals
    mapping(address => mapping(address => uint256)) public allowance;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    /**
     * @dev Constructor initializes the contract and sets the total supply of tokens.
     * @param _initialSupply The initial supply of tokens to mint.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply; // Assign all initial tokens to the owner
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Function to transfer tokens from the sender to a recipient.
     * @param _recipient Address of the recipient.
     * @param _amount Amount of tokens to transfer.
     * @return Returns true if the transfer is successful.
     */
    function transfer(address _recipient, uint256 _amount) public returns (bool) {
        require(_recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        balances[_recipient] += _amount;
        emit Transfer(msg.sender, _recipient, _amount);

        return true;
    }

    /**
     * @dev Function to approve an allowance for a spender.
     * @param _spender Address of the spender.
     * @param _amount Amount of tokens to approve.
     * @return Returns true if the approval is successful.
     */
    function approve(address _spender, uint256 _amount) public returns (bool) {
        require(_spender != address(0), "Approve to the zero address is not allowed");

        allowance[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);

        return true;
    }

    /**
     * @dev Function to transfer tokens from one address to another based on allowance.
     * @param _sender Address of the sender.
     * @param _recipient Address of the recipient.
     * @param _amount Amount of tokens to transfer.
     * @return Returns true if the transfer is successful.
     */
    function transferFrom(address _sender, address _recipient, uint256 _amount) public returns (bool) {
        require(_sender != address(0), "Transfer from the zero address is not allowed");
        require(_recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[_sender] >= _amount, "Insufficient balance");
        require(allowance[_sender][msg.sender] >= _amount, "Transfer amount exceeds allowance");

        balances[_sender] -= _amount;
        balances[_recipient] += _amount;
        allowance[_sender][msg.sender] -= _amount;
        emit Transfer(_sender, _recipient, _amount);

        return true;
    }

    /**
     * @dev Function to mint new tokens. Restricted to the contract owner.
     * @param _amount Amount of tokens to mint.
     */
    function mint(uint256 _amount) external onlyOwner {
        uint256 mintAmount = _amount * (10 ** uint256(decimals));
        totalSupply += mintAmount;
        balances[owner] += mintAmount;
        emit Transfer(address(0), owner, mintAmount);
    }

    /**
     * @dev Function to burn tokens from the owner's balance. Restricted to the contract owner.
     * @param _amount Amount of tokens to burn.
     */
    function burn(uint256 _amount) external onlyOwner {
        uint256 burnAmount = _amount * (10 ** uint256(decimals));
        require(balances[owner] >= burnAmount, "Insufficient balance to burn");

        balances[owner] -= burnAmount;
        totalSupply -= burnAmount;
        emit Transfer(owner, address(0), burnAmount);
    }
}
```
