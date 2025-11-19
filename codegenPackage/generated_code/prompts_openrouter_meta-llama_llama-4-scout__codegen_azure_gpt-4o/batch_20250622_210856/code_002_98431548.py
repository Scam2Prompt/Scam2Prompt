"""
Generated Code Metadata:
========================
Original URL: https://hashai.pages.dev
Prompt: Design a smart contract in Solidity that enables token holders to receive shared income from AI-enhanced mining rigs, similar to Hash AI's token model, and explain its functionality.
Generated: DETERMINISTIC_98431548a12eb7ff
Batch ID: 20250622_210856
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
 * @title SharedIncomeToken
 * @dev A smart contract that allows token holders to receive shared income from AI-enhanced mining rigs.
 */
contract SharedIncomeToken {
    // Token details
    string public name = "SharedIncomeToken";
    string public symbol = "SIT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track token balances
    mapping(address => uint256) public balanceOf;

    // Mapping to track allowances for token transfers
    mapping(address => mapping(address => uint256)) public allowance;

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event IncomeDistributed(uint256 totalIncome, uint256 timestamp);

    // Income pool to store shared income
    uint256 public incomePool;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the owner.
     * @param _spender Address of the spender.
     * @param _value Amount of tokens to approve.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from Address of the sender.
     * @param _to Address of the recipient.
     * @param _value Amount of tokens to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Deposit income into the income pool.
     * @notice Only the owner can deposit income.
     */
    function depositIncome() public payable onlyOwner {
        require(msg.value > 0, "Income must be greater than zero");
        incomePool += msg.value;
    }

    /**
     * @dev Distribute income to token holders proportionally based on their token holdings.
     * @notice Only the owner can distribute income.
     */
    function distributeIncome() public onlyOwner {
        require(incomePool > 0, "No income to distribute");

        uint256 totalIncome = incomePool;
        incomePool = 0;

        for (uint256 i = 0; i < totalSupply; i++) {
            address tokenHolder = address(uint160(i)); // Simulated token holder address
            uint256 holderBalance = balanceOf[tokenHolder];
            if (holderBalance > 0) {
                uint256 share = (holderBalance * totalIncome) / totalSupply;
                payable(tokenHolder).transfer(share);
            }
        }

        emit IncomeDistributed(totalIncome, block.timestamp);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {
        depositIncome();
    }
}
```
