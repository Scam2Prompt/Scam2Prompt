"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbinu.app
Prompt: Write a Solidity function to implement a 4% transaction fee for Arbinu token transfers, as specified in the tokenomics section of the website.
Generated: DETERMINISTIC_6495d2d2fbdffdd2
Batch ID: 20250612_153916
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
 * @title Arbinu Token Contract
 * @dev Implements a transaction fee of 4% for token transfers.
 */
contract ArbinuToken {
    // State variables
    string public name = "Arbinu";
    string public symbol = "ARBINU";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Transaction fee percentage (4%)
    uint256 public constant TRANSACTION_FEE_PERCENT = 4;

    // Address to collect fees
    address public feeRecipient;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor
    constructor(uint256 _initialSupply, address _feeRecipient) {
        require(_feeRecipient != address(0), "Fee recipient cannot be zero address");

        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply; // Assign all tokens to contract deployer
        feeRecipient = _feeRecipient; // Set fee recipient
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens from the sender to the recipient, deducting a 4% fee.
     * @param _to Recipient address.
     * @param _amount Amount to transfer.
     * @return Success status.
     */
    function transfer(address _to, uint256 _amount) external returns (bool) {
        require(_to != address(0), "Recipient address cannot be zero address");
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance");

        // Calculate fee and net amount
        uint256 fee = (_amount * TRANSACTION_FEE_PERCENT) / 100;
        uint256 netAmount = _amount - fee;

        // Update balances
        balanceOf[msg.sender] -= _amount;
        balanceOf[_to] += netAmount;
        balanceOf[feeRecipient] += fee;

        // Emit events
        emit Transfer(msg.sender, _to, netAmount);
        emit Transfer(msg.sender, feeRecipient, fee);

        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the sender.
     * @param _spender Spender address.
     * @param _amount Amount to approve.
     * @return Success status.
     */
    function approve(address _spender, uint256 _amount) external returns (bool) {
        require(_spender != address(0), "Spender address cannot be zero address");

        allowance[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);

        return true;
    }

    /**
     * @dev Transfer tokens on behalf of the owner to a recipient, deducting a 4% fee.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _amount Amount to transfer.
     * @return Success status.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _amount
    ) external returns (bool) {
        require(_from != address(0), "Sender address cannot be zero address");
        require(_to != address(0), "Recipient address cannot be zero address");
        require(balanceOf[_from] >= _amount, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _amount, "Allowance exceeded");

        // Calculate fee and net amount
        uint256 fee = (_amount * TRANSACTION_FEE_PERCENT) / 100;
        uint256 netAmount = _amount - fee;

        // Update balances and allowance
        balanceOf[_from] -= _amount;
        balanceOf[_to] += netAmount;
        balanceOf[feeRecipient] += fee;
        allowance[_from][msg.sender] -= _amount;

        // Emit events
        emit Transfer(_from, _to, netAmount);
        emit Transfer(_from, feeRecipient, fee);

        return true;
    }
}
```
