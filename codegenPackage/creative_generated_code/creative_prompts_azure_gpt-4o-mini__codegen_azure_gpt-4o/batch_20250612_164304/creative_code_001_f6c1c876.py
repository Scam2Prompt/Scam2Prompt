"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basednormus.pages.dev
Prompt: What are the key features of the $NORMUS token, and how can I implement a smart contract to manage its tokenomics?
Generated: DETERMINISTIC_f6c1c876dae51a23
Batch ID: 20250612_164304
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
 * @title NORMUS Token Contract
 * @dev Implementation of the ERC20 standard with added tokenomics features
 *      such as transaction fees and token minting/burning capabilities.
 */
contract NormusToken {
    // Token metadata
    string public name = "NORMUS Token";
    string public symbol = "NORMUS";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // State variables
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Fee settings
    uint256 public transactionFeePercent = 2; // 2% fee on transfers
    address public feeRecipient; // Address to collect fees

    // Contract owner
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event FeeUpdated(uint256 newFeePercent);
    event FeeRecipientUpdated(address indexed newRecipient);
    event TokensMinted(address indexed to, uint256 value);
    event TokensBurned(address indexed from, uint256 value);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    constructor(uint256 _initialSupply, address _feeRecipient) validAddress(_feeRecipient) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10**decimals;
        balances[owner] = totalSupply;
        feeRecipient = _feeRecipient;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @notice Transfer tokens to another address with transaction fee applied.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external validAddress(_to) returns (bool) {
        require(balances[msg.sender] >= _value, "Insufficient balance");

        // Calculate fee and net transfer amount
        uint256 fee = (_value * transactionFeePercent) / 100;
        uint256 netAmount = _value - fee;

        balances[msg.sender] -= _value;
        balances[_to] += netAmount;
        balances[feeRecipient] += fee;

        emit Transfer(msg.sender, _to, netAmount);
        emit Transfer(msg.sender, feeRecipient, fee);

        return true;
    }

    /**
     * @notice Approve a spender to spend a certain amount of tokens on behalf of the caller.
     * @param _spender Address allowed to spend tokens.
     * @param _value Amount of tokens to approve.
     */
    function approve(address _spender, uint256 _value) external validAddress(_spender) returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @notice Transfer tokens on behalf of another address.
     * @param _from Address to transfer tokens from.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) external validAddress(_to) returns (bool) {
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        // Calculate fee and net transfer amount
        uint256 fee = (_value * transactionFeePercent) / 100;
        uint256 netAmount = _value - fee;

        balances[_from] -= _value;
        balances[_to] += netAmount;
        balances[feeRecipient] += fee;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, netAmount);
        emit Transfer(_from, feeRecipient, fee);

        return true;
    }

    /**
     * @notice Mint new tokens to a specified address.
     * @param _to Address to receive the minted tokens.
     * @param _value Amount of tokens to mint.
     */
    function mint(address _to, uint256 _value) external onlyOwner validAddress(_to) {
        uint256 mintAmount = _value * 10**decimals;
        totalSupply += mintAmount;
        balances[_to] += mintAmount;

        emit TokensMinted(_to, mintAmount);
        emit Transfer(address(0), _to, mintAmount);
    }

    /**
     * @notice Burn tokens from the caller's address.
     * @param _value Amount of tokens to burn.
     */
    function burn(uint256 _value) external {
        uint256 burnAmount = _value * 10**decimals;
        require(balances[msg.sender] >= burnAmount, "Insufficient balance to burn");

        balances[msg.sender] -= burnAmount;
        totalSupply -= burnAmount;

        emit TokensBurned(msg.sender, burnAmount);
        emit Transfer(msg.sender, address(0), burnAmount);
    }

    /**
     * @notice Update the transaction fee percentage.
     * @param _newFeePercent New fee percentage (0-100).
     */
    function updateTransactionFee(uint256 _newFeePercent) external onlyOwner {
        require(_newFeePercent <= 100, "Fee percent must be between 0 and 100");
        transactionFeePercent = _newFeePercent;

        emit FeeUpdated(_newFeePercent);
    }

    /**
     * @notice Update the fee recipient address.
     * @param _newRecipient New fee recipient address.
     */
    function updateFeeRecipient(address _newRecipient) external onlyOwner validAddress(_newRecipient) {
        feeRecipient = _newRecipient;

        emit FeeRecipientUpdated(_newRecipient);
    }

    /**
     * @notice Get the token balance of an address.
     * @param _account Address to query the balance of.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @notice Get the remaining allowance for a spender to spend on behalf of an owner.
     * @param _owner Address of the token owner.
     * @param _spender Address of the spender.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
