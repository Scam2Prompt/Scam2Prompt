"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-sale.pages.dev
Prompt: Write a Solidity smart contract for a meme coin generator that allows users to create their own meme coins with adjustable parameters like supply and token name.
Generated: DETERMINISTIC_43d24b7d8c17caa5
Batch ID: 20250612_150552
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

/// @title MemeCoinGenerator
/// @notice A contract that allows users to create their own meme coins with customizable parameters
contract MemeCoinGenerator {

    /// @notice Structure to store information about created meme coins
    struct MemeCoin {
        string name;
        string symbol;
        uint256 totalSupply;
        address owner;
        bool exists;
    }

    /// @dev Mapping to track deployed meme coins by their contract address
    mapping(address => MemeCoin) public memeCoins;

    /// @dev Event emitted when a new meme coin is created
    event MemeCoinCreated(address indexed tokenAddress, string name, string symbol, uint256 totalSupply, address indexed owner);

    /// @notice Function to create a new meme coin
    /// @param _name The name of the meme coin
    /// @param _symbol The symbol of the meme coin
    /// @param _totalSupply The total supply of the meme coin
    /// @return tokenAddress The address of the newly created meme coin contract
    function createMemeCoin(string memory _name, string memory _symbol, uint256 _totalSupply) external returns (address tokenAddress) {
        require(bytes(_name).length > 0, "MemeCoin: Name cannot be empty");
        require(bytes(_symbol).length > 0, "MemeCoin: Symbol cannot be empty");
        require(_totalSupply > 0, "MemeCoin: Total supply must be greater than zero");

        // Deploy the new meme coin
        MemeCoinToken memeCoin = new MemeCoinToken(_name, _symbol, _totalSupply, msg.sender);
        tokenAddress = address(memeCoin);

        // Store information about the deployed meme coin
        memeCoins[tokenAddress] = MemeCoin({
            name: _name,
            symbol: _symbol,
            totalSupply: _totalSupply,
            owner: msg.sender,
            exists: true
        });

        // Emit an event for the newly created meme coin
        emit MemeCoinCreated(tokenAddress, _name, _symbol, _totalSupply, msg.sender);
    }
}

/// @title MemeCoinToken
/// @notice A simple ERC-20 compliant token contract for meme coins
contract MemeCoinToken {

    /// @dev Balance mapping to track token holders' balances
    mapping(address => uint256) public balances;

    /// @dev Allowance mapping for token allowances
    mapping(address => mapping(address => uint256)) public allowances;

    /// @notice The name of the token
    string public name;

    /// @notice The symbol of the token
    string public symbol;

    /// @notice The total supply of the token
    uint256 public totalSupply;

    /// @notice The owner of the token (creator)
    address public owner;

    /// @dev Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    /// @dev Event emitted when an allowance is approved
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /// @notice Constructor to initialize the meme coin
    /// @param _name The name of the token
    /// @param _symbol The symbol of the token
    /// @param _totalSupply The initial total supply of the token
    /// @param _owner The address of the token owner
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply, address _owner) {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply;
        owner = _owner;

        // Assign the total supply to the owner
        balances[_owner] = _totalSupply;
        emit Transfer(address(0), _owner, _totalSupply);
    }

    /// @notice Transfers tokens to a specific address
    /// @param _to The address to transfer tokens to
    /// @param _value The amount of tokens to transfer
    /// @return success Boolean indicating whether the transfer was successful
    function transfer(address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "MemeCoin: Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "MemeCoin: Insufficient balance");

        // Deduct from sender and add to recipient
        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /// @notice Approve an address to spend tokens on behalf of the owner
    /// @param _spender The address allowed to spend tokens
    /// @param _value The amount of tokens to approve
    /// @return success Boolean indicating whether the approval was successful
    function approve(address _spender, uint256 _value) external returns (bool success) {
        require(_spender != address(0), "MemeCoin: Cannot approve zero address");

        // Set allowance
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /// @notice Transfer tokens on behalf of an address
    /// @param _from The address from which tokens are transferred
    /// @param _to The recipient address
    /// @param _value The amount of tokens to transfer
    /// @return success Boolean indicating whether the transfer was successful
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "MemeCoin: Cannot transfer to the zero address");
        require(balances[_from] >= _value, "MemeCoin: Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "MemeCoin: Transfer amount exceeds allowance");

        // Deduct from sender, allowance, and add to recipient
        balances[_from] -= _value;
        allowances[_from][msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /// @notice Get the token balance of an address
    /// @param _owner The address to query the balance for
    /// @return balance The token balance of the specified address
    function balanceOf(address _owner) external view returns (uint256 balance) {
        return balances[_owner];
    }

    /// @notice Get the allowance of a spender for a specific owner
    /// @param _owner The owner of the tokens
    /// @param _spender The spender allowed to spend the tokens
    /// @return remaining The remaining allowance
    function allowance(address _owner, address _spender) external view returns (uint256 remaining) {
        return allowances[_owner][_spender];
    }
}
```
