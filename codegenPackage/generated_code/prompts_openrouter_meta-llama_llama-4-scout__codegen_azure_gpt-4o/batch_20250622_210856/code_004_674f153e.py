"""
Generated Code Metadata:
========================
Original URL: https://babywif-io.pages.dev
Prompt: Design a basic smart contract in Solidity for a token with a similar distribution plan as Baby Wif, including presale, liquidity, marketing, and development allocations.
Generated: DETERMINISTIC_674f153e4361b36c
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
 * @title BabyWifToken
 * @dev A basic ERC20 token with a distribution plan for presale, liquidity, marketing, and development allocations.
 */
contract BabyWifToken {
    // Token details
    string public name = "BabyWifToken";
    string public symbol = "BWT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) public balanceOf;

    // Allowance mapping
    mapping(address => mapping(address => uint256)) public allowance;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Distribution allocations
    uint256 public presaleAllocation;
    uint256 public liquidityAllocation;
    uint256 public marketingAllocation;
    uint256 public developmentAllocation;

    // Addresses for allocations
    address public presaleAddress;
    address public liquidityAddress;
    address public marketingAddress;
    address public developmentAddress;

    // Constructor to initialize the token and allocations
    constructor(
        uint256 _totalSupply,
        uint256 _presaleAllocation,
        uint256 _liquidityAllocation,
        uint256 _marketingAllocation,
        uint256 _developmentAllocation,
        address _presaleAddress,
        address _liquidityAddress,
        address _marketingAddress,
        address _developmentAddress
    ) {
        require(
            _presaleAllocation + _liquidityAllocation + _marketingAllocation + _developmentAllocation == _totalSupply,
            "Allocations must sum to total supply"
        );

        totalSupply = _totalSupply;
        presaleAllocation = _presaleAllocation;
        liquidityAllocation = _liquidityAllocation;
        marketingAllocation = _marketingAllocation;
        developmentAllocation = _developmentAllocation;

        presaleAddress = _presaleAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;
        developmentAddress = _developmentAddress;

        // Distribute tokens to respective addresses
        balanceOf[presaleAddress] = presaleAllocation;
        balanceOf[liquidityAddress] = liquidityAllocation;
        balanceOf[marketingAddress] = marketingAllocation;
        balanceOf[developmentAddress] = developmentAllocation;

        emit Transfer(address(0), presaleAddress, presaleAllocation);
        emit Transfer(address(0), liquidityAddress, liquidityAllocation);
        emit Transfer(address(0), marketingAddress, marketingAllocation);
        emit Transfer(address(0), developmentAddress, developmentAllocation);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param _to Recipient address.
     * @param _value Amount to transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the sender.
     * @param _spender Spender address.
     * @param _value Amount to approve.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Invalid spender address");

        allowance[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _value Amount to transfer.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }
}
```
