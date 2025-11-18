"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-screator-ethereum-free.pages.dev
Prompt: Provide a Solidity smart contract template for creating a token with full ownership and automatic liquidity pool transfer, as described on the "Tokens Creator" site.
Generated: DETERMINISTIC_89b4f7990cd2e71f
Batch ID: 20250612_145916
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
 * @title TokenWithLiquidity
 * @dev A template for creating an ERC20 token with full ownership control and automatic liquidity pool transfer.
 */
contract TokenWithLiquidity {
    // Token metadata
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    // Owner of the token
    address public owner;

    // Account balances
    mapping(address => uint256) public balanceOf;

    // Allowances for transferFrom functionality
    mapping(address => mapping(address => uint256)) public allowance;

    // Liquidity pool address
    address public liquidityPool;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to the owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize token details and set the owner.
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _decimals Number of decimals
     * @param _totalSupply Initial total supply
     * @param _liquidityPool Address of the liquidity pool
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _totalSupply,
        address _liquidityPool
    ) {
        require(_liquidityPool != address(0), "Liquidity pool address cannot be zero");

        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _totalSupply;
        owner = msg.sender;
        liquidityPool = _liquidityPool;

        // Assign the initial supply to the contract owner
        balanceOf[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to Recipient address
     * @param _value Amount of tokens to transfer
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Recipient address cannot be zero");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        // Deduct from sender and add to recipient
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the token owner.
     * @param _spender Address of the spender
     * @param _value Amount of tokens to approve
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Spender address cannot be zero");

        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance mechanism.
     * @param _from Sender address
     * @param _to Recipient address
     * @param _value Amount of tokens to transfer
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Recipient address cannot be zero");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        // Deduct from sender and add to recipient
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;

        // Update the allowance
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Transfers tokens automatically to the liquidity pool.
     * @param _value Amount of tokens to transfer
     */
    function transferToLiquidityPool(uint256 _value) public returns (bool) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        // Deduct from sender and add to liquidity pool
        balanceOf[msg.sender] -= _value;
        balanceOf[liquidityPool] += _value;

        emit Transfer(msg.sender, liquidityPool, _value);
        return true;
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) public onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");

        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Allows the owner to update the liquidity pool address.
     * @param _newLiquidityPool Address of the new liquidity pool
     */
    function updateLiquidityPool(address _newLiquidityPool) public onlyOwner {
        require(_newLiquidityPool != address(0), "New liquidity pool address cannot be zero");

        liquidityPool = _newLiquidityPool;
    }
}
```
