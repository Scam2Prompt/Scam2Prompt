"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: Write a Solidity contract that prevents token inflation by implementing a fixed supply mechanism, inspired by DOGE20's solution to Dogecoin's infinite supply issue.
Generated: DETERMINISTIC_6213f7c11e95d506
Batch ID: 20250612_152827
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
 * @title FixedSupplyToken
 * @dev A fixed supply ERC20 token inspired by DOGE20's solution to Dogecoin's infinite supply issue.
 *      The total supply of the token is fixed at deployment and cannot be changed.
 */
contract FixedSupplyToken {
    // Token details
    string public name = "FixedSupplyToken";
    string public symbol = "FST";
    uint8 public decimals = 18;

    // Fixed total supply of tokens
    uint256 public totalSupply;

    // Mapping to store balances of accounts
    mapping(address => uint256) public balanceOf;

    // Mapping for allowance management
    mapping(address => mapping(address => uint256)) public allowance;

    // Event emitted on token transfers
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted on approval of token allowances
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor that initializes the fixed supply of tokens and assigns them to the deployer.
     * @param _initialSupply The fixed total supply of the token.
     */
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");

        totalSupply = _initialSupply * (10 ** decimals); // Scale the supply by the decimals
        balanceOf[msg.sender] = totalSupply; // Allocate all tokens to the deployer

        emit Transfer(address(0), msg.sender, totalSupply); // Emit the transfer event for minting
    }

    /**
     * @dev Transfers tokens from the sender to the recipient.
     * @param _to The address of the recipient.
     * @param _value The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        // Perform the transfer
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value); // Emit the transfer event
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the sender.
     * @param _spender The address of the spender.
     * @param _value The amount of tokens the spender is approved to spend.
     * @return True if the approval is successful.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        require(_spender != address(0), "Cannot approve the zero address");

        allowance[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value); // Emit the approval event
        return true;
    }

    /**
     * @dev Transfers tokens from one account to another, using the allowance mechanism.
     * @param _from The address of the sender.
     * @param _to The address of the recipient.
     * @param _value The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external returns (bool) {
        require(_from != address(0), "Cannot transfer from the zero address");
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        // Perform the transfer
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value); // Emit the transfer event
        return true;
    }
}
```
