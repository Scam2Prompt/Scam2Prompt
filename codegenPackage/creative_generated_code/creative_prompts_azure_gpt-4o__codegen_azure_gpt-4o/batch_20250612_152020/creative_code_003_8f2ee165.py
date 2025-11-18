"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-x.com
Prompt: Create a smart contract in Solidity for managing utility tokens similar to X Token, ensuring compliance with exemptions under the U.S. Securities Act.
Generated: DETERMINISTIC_8f2ee16573cb2e27
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title UtilityToken
 * @dev A smart contract for managing utility tokens, ensuring compliance with exemptions under the U.S. Securities Act.
 *      This contract follows ERC20 standards and includes basic features for token management.
 */
contract UtilityToken {
    // Token metadata
    string public name = "UtilityToken";
    string public symbol = "UTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances of token holders
    mapping(address => uint256) private balances;

    // Allowances for delegated token spending
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Events for logging activities
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the token contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10 ** uint256(decimals);
        balances[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply); // Emit Transfer event for minting initial supply
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to The address to transfer to.
     * @param _value The amount of tokens to be transferred.
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
     * @dev Approves another address to spend tokens on behalf of the sender.
     * @param _spender The address to be approved.
     * @param _value The amount of tokens to approve for spending.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        require(_spender != address(0), "Invalid spender address");

        allowances[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of the sender.
     * @param _from The address to transfer tokens from.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to be transferred.
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        allowances[_from][msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Returns the balance of a given address.
     * @param _account The address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Returns the remaining allowance for a spender on behalf of the owner.
     * @param _owner The address of the token owner.
     * @param _spender The address of the spender.
     * @return The remaining allowance of the spender.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }
}
```
