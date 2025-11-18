"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marvinonbase.pages.dev
Prompt: Implement a burn mechanism in Solidity for a token, where a percentage of transaction fees is automatically sent to a burn address, inspired by Marvin's collaboration with Shiba Inu.
Generated: DETERMINISTIC_7450961304fffaed
Batch ID: 20250612_152358
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
 * @title BurnableToken
 * @dev Implements a burn mechanism for a token where a percentage of transaction fees is sent to a burn address.
 */
contract BurnableToken {
    // Token state variables
    string public name = "BurnableToken";
    string public symbol = "BTKN";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    address public owner;

    // Burn address (commonly the zero address)
    address public constant BURN_ADDRESS = address(0);

    // Transaction fee percentage (e.g., 2%)
    uint256 public transactionFeePercent = 2;

    // Mapping to track balances
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed from, uint256 value);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        balances[owner] = _initialSupply;
        emit Transfer(address(0), owner, _initialSupply);
    }

    /**
     * @dev Transfer tokens with burn mechanism.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     * @return Success status of the transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        // Calculate transaction fee and burn amount
        uint256 fee = (_value * transactionFeePercent) / 100;
        uint256 amountToBurn = fee; // Full fee is burned
        uint256 amountToTransfer = _value - fee;

        // Perform the transfer
        balances[msg.sender] -= _value;
        balances[_to] += amountToTransfer;
        emit Transfer(msg.sender, _to, amountToTransfer);

        // Burn the fee
        totalSupply -= amountToBurn;
        emit Burn(msg.sender, amountToBurn);

        return true;
    }

    /**
     * @dev Approve tokens for spending by a third party.
     * @param _spender The address authorized to spend the tokens.
     * @param _value The amount of tokens authorized for spending.
     * @return Success status of the approval.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of another account (requires approval).
     * @param _from The address to transfer tokens from.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     * @return Success status of the transfer.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        // Calculate transaction fee and burn amount
        uint256 fee = (_value * transactionFeePercent) / 100;
        uint256 amountToBurn = fee; // Full fee is burned
        uint256 amountToTransfer = _value - fee;

        // Perform the transfer
        balances[_from] -= _value;
        balances[_to] += amountToTransfer;
        allowances[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, amountToTransfer);

        // Burn the fee
        totalSupply -= amountToBurn;
        emit Burn(_from, amountToBurn);

        return true;
    }

    /**
     * @dev Update the transaction fee percentage. Can only be called by the owner.
     * @param _newFeePercent The new transaction fee percentage.
     */
    function updateTransactionFeePercent(uint256 _newFeePercent) external onlyOwner {
        require(_newFeePercent <= 100, "Fee percentage cannot exceed 100");
        transactionFeePercent = _newFeePercent;
    }

    /**
     * @dev Check the balance of an account.
     * @param _account The account to check.
     * @return The balance of the account.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Check the allowance of a spender for an owner's tokens.
     * @param _owner The owner of the tokens.
     * @param _spender The spender authorized to spend the tokens.
     * @return The allowance of the spender.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
