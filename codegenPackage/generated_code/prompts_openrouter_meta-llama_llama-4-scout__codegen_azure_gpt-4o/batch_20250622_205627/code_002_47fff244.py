"""
Generated Code Metadata:
========================
Original URL: https://landx.pages.dev
Prompt: "Design a smart contract in Solidity that enables the tokenization of farmland crops, ensuring the contract is secured by a farm audit, security deposit, and lien on the land."
Generated: DETERMINISTIC_47fff244d06d80ed
Batch ID: 20250622_205627
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
 * @title FarmlandTokenization
 * @dev A smart contract for tokenizing farmland crops, secured by farm audit, security deposit, and lien on the land.
 */
contract FarmlandTokenization {
    // Token details
    string public name = "Farmland Crop Token";
    string public symbol = "FCT";
    uint8 public decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Mapping to track balances of token holders
    mapping(address => uint256) public balanceOf;

    // Mapping to track allowances for token transfers
    mapping(address => mapping(address => uint256)) public allowance;

    // Owner of the contract
    address public owner;

    // Security deposit amount
    uint256 public securityDeposit;

    // Farm audit status
    bool public farmAuditPassed;

    // Lien status
    bool public lienOnLand;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event SecurityDepositUpdated(uint256 amount);
    event FarmAuditStatusUpdated(bool status);
    event LienStatusUpdated(bool status);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to ensure farm audit and lien are in place
    modifier farmSecured() {
        require(farmAuditPassed, "Farm audit must be passed");
        require(lienOnLand, "Lien on land must be established");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _initialSupply Initial supply of tokens.
     * @param _securityDeposit Initial security deposit amount.
     */
    constructor(uint256 _initialSupply, uint256 _securityDeposit) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply;
        securityDeposit = _securityDeposit;
        farmAuditPassed = false;
        lienOnLand = false;
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) public farmSecured returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        require(_to != address(0), "Invalid recipient address");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the owner.
     * @param _spender Spender address.
     * @param _value Amount of tokens to approve.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Invalid spender address");

        allowance[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) public farmSecured returns (bool success) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        require(_to != address(0), "Invalid recipient address");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Update the security deposit amount.
     * @param _amount New security deposit amount.
     */
    function updateSecurityDeposit(uint256 _amount) public onlyOwner {
        securityDeposit = _amount;
        emit SecurityDepositUpdated(_amount);
    }

    /**
     * @dev Update the farm audit status.
     * @param _status New farm audit status.
     */
    function updateFarmAuditStatus(bool _status) public onlyOwner {
        farmAuditPassed = _status;
        emit FarmAuditStatusUpdated(_status);
    }

    /**
     * @dev Update the lien status on the land.
     * @param _status New lien status.
     */
    function updateLienStatus(bool _status) public onlyOwner {
        lienOnLand = _status;
        emit LienStatusUpdated(_status);
    }
}
```
