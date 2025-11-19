"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to create their own meme coin on the Oracle Meme's Meme Coin Generator.
Generated: DETERMINISTIC_8be61c11772ef7af
Batch ID: 20250612_160940
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
 * @title MemeCoinGenerator
 * @dev Smart contract that allows users to create their own meme coin
 */
contract MemeCoinGenerator {
    // Event emitted when a new meme coin is created
    event MemeCoinCreated(address indexed owner, address indexed memeCoinAddress, string name, string symbol, uint256 supply);

    // Struct to store details of each meme coin
    struct MemeCoin {
        string name;
        string symbol;
        uint256 totalSupply;
        address owner;
        address tokenAddress;
    }

    // Array to store all created meme coins
    MemeCoin[] public memeCoins;

    /**
     * @dev Function to create a new meme coin
     * @param _name Name of the meme coin
     * @param _symbol Symbol of the meme coin
     * @param _totalSupply Total supply of the meme coin
     */
    function createMemeCoin(string memory _name, string memory _symbol, uint256 _totalSupply) external {
        // Validate inputs
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_symbol).length > 0, "Symbol cannot be empty");
        require(_totalSupply > 0, "Total supply must be greater than zero");

        // Create a new instance of the MemeCoin contract
        MemeCoinToken newMemeCoin = new MemeCoinToken(_name, _symbol, _totalSupply, msg.sender);

        // Store the meme coin details
        MemeCoin memory memeCoin = MemeCoin({
            name: _name,
            symbol: _symbol,
            totalSupply: _totalSupply,
            owner: msg.sender,
            tokenAddress: address(newMemeCoin)
        });
        memeCoins.push(memeCoin);

        // Emit event for created meme coin
        emit MemeCoinCreated(msg.sender, address(newMemeCoin), _name, _symbol, _totalSupply);
    }

    /**
     * @dev Function to retrieve the count of created meme coins
     * @return The number of meme coins created
     */
    function getMemeCoinCount() external view returns (uint256) {
        return memeCoins.length;
    }
}

/**
 * @title MemeCoinToken
 * @dev ERC20-like token contract for meme coins
 */
contract MemeCoinToken {
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    uint256 public totalSupply;
    address public owner;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Events for token transfers and approvals
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the meme coin
     * @param _name Name of the meme coin
     * @param _symbol Symbol of the meme coin
     * @param _totalSupply Total supply of the meme coin
     * @param _owner Owner of the meme coin (creator)
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply, address _owner) {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply;
        owner = _owner;
        balanceOf[_owner] = _totalSupply;
        emit Transfer(address(0), _owner, _totalSupply);
    }

    /**
     * @dev Function to transfer tokens to another address
     * @param _to Address to transfer tokens to
     * @param _value Amount of tokens to transfer
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        require(_to != address(0), "Invalid recipient address");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the caller
     * @param _spender Address to approve
     * @param _value Amount of tokens to approve
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Function to transfer tokens from one address to another (allowance-based)
     * @param _from Address to transfer tokens from
     * @param _to Address to transfer tokens to
     * @param _value Amount of tokens to transfer
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        require(_to != address(0), "Invalid recipient address");

        balanceOf[_from] -= _value;
        allowance[_from][msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(_from, _to, _value);
        return true;
    }
}
```
