"""
Generated Code Metadata:
========================
Original URL: https://mint-tether.web.app
Prompt: Generate a Solidity code for a smart contract that handles Tether token minting with a free mint option for token holders.
Generated: DETERMINISTIC_7563e126dad0aedb
Batch ID: 20250622_204907
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
 * @title TetherToken
 * @dev A simple ERC20-like token contract with minting functionality and a free mint option for token holders.
 */
contract TetherToken {
    // State variables
    string public name = "TetherToken";
    string public symbol = "USDT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed to, uint256 value);

    // Modifier to check for sufficient balance
    modifier hasSufficientBalance(address _from, uint256 _amount) {
        require(balances[_from] >= _amount, "Insufficient balance");
        _;
    }

    // Modifier to check for valid addresses
    modifier validAddress(address _addr) {
        require(_addr != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Returns the balance of a given address.
     * @param _owner The address to query the balance of.
     * @return The balance of the address.
     */
    function balanceOf(address _owner) external view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to The address to transfer to.
     * @param _value The amount to be transferred.
     * @return A boolean indicating success.
     */
    function transfer(address _to, uint256 _value)
        external
        validAddress(_to)
        hasSufficientBalance(msg.sender, _value)
        returns (bool)
    {
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the caller.
     * @param _spender The address authorized to spend.
     * @param _value The maximum amount they can spend.
     * @return A boolean indicating success.
     */
    function approve(address _spender, uint256 _value)
        external
        validAddress(_spender)
        returns (bool)
    {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another.
     * @param _from The address to transfer from.
     * @param _to The address to transfer to.
     * @param _value The amount to be transferred.
     * @return A boolean indicating success.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    )
        external
        validAddress(_to)
        hasSufficientBalance(_from, _value)
        returns (bool)
    {
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");
        allowances[_from][msg.sender] -= _value;
        balances[_from] -= _value;
        balances[_to] += _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender is allowed to spend.
     * @param _owner The address of the token owner.
     * @param _spender The address of the spender.
     * @return The remaining allowance.
     */
    function allowance(address _owner, address _spender)
        external
        view
        returns (uint256)
    {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Mints new tokens to a specified address.
     * @param _to The address to mint tokens to.
     * @param _value The amount of tokens to mint.
     */
    function mint(address _to, uint256 _value)
        external
        validAddress(_to)
    {
        totalSupply += _value;
        balances[_to] += _value;
        emit Mint(_to, _value);
        emit Transfer(address(0), _to, _value);
    }

    /**
     * @dev Allows token holders to mint a small amount of tokens for free.
     * @param _value The amount of tokens to mint.
     */
    function freeMint(uint256 _value) external {
        require(balances[msg.sender] > 0, "Must hold tokens to free mint");
        require(_value <= 100 * (10**decimals), "Free mint limit exceeded"); // Limit free mint to 100 tokens
        totalSupply += _value;
        balances[msg.sender] += _value;
        emit Mint(msg.sender, _value);
        emit Transfer(address(0), msg.sender, _value);
    }
}
```
