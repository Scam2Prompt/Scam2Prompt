"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-jessecoinorg.pages.dev
Prompt: Generate a Solidity contract that ensures the total supply of JESSE tokens remains fixed at 100,000,000 while allowing presale transactions up to the cap.
Generated: DETERMINISTIC_b21ffec8db016ab2
Batch ID: 20250612_153400
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
 * @title JESSE Token Contract
 * @dev This contract implements an ERC20-like token with a fixed supply of 100,000,000.
 *      It includes functionality for presale transactions up to a maximum cap.
 */
contract JesseToken {
    // Token attributes
    string public name = "JESSE Token";
    string public symbol = "JESSE";
    uint8 public decimals = 18;
    uint256 public totalSupply = 100_000_000 * (10 ** uint256(decimals)); // Fixed total supply

    // Balances map to track token ownership
    mapping(address => uint256) public balanceOf;
    // Allowance mapping for delegated token transfers
    mapping(address => mapping(address => uint256)) public allowance;

    // Presale attributes
    uint256 public presaleCap = 10_000_000 * (10 ** uint256(decimals)); // 10% of total supply
    uint256 public presaleSold = 0; // Track presale tokens sold

    // Owner address for administrative control
    address public owner;

    // Events for transparency and logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Presale(address indexed buyer, uint256 value);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Constructor initializes the owner and allocates total supply to the owner
    constructor() {
        owner = msg.sender;
        balanceOf[owner] = totalSupply; // Assign all tokens to the contract owner initially
    }

    /**
     * @dev Transfer token to a specified account
     * @param _to The address to transfer to
     * @param _value The amount to be transferred
     */
    function transfer(address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "Invalid address"); // Prevent transferring to the zero address
        require(balanceOf[msg.sender] >= _value, "Insufficient balance"); // Ensure sender has enough tokens

        balanceOf[msg.sender] -= _value; // Deduct from sender
        balanceOf[_to] += _value; // Add to recipient
        emit Transfer(msg.sender, _to, _value); // Emit Transfer event
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the owner
     * @param _spender The address authorized to spend
     * @param _value The maximum amount they can spend
     */
    function approve(address _spender, uint256 _value) external returns (bool success) {
        require(_spender != address(0), "Invalid spender address"); // Prevent zero address approval

        allowance[msg.sender][_spender] = _value; // Set allowance
        emit Approval(msg.sender, _spender, _value); // Emit Approval event
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of the owner (delegated transfer)
     * @param _from The address to transfer from
     * @param _to The address to transfer to
     * @param _value The amount to be transferred
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "Invalid recipient address"); // Prevent transferring to the zero address
        require(balanceOf[_from] >= _value, "Insufficient balance"); // Ensure sender has enough tokens
        require(allowance[_from][msg.sender] >= _value, "Transfer amount exceeds allowance"); // Ensure allowance covers the transfer

        balanceOf[_from] -= _value; // Deduct from sender
        balanceOf[_to] += _value; // Add to recipient
        allowance[_from][msg.sender] -= _value; // Reduce allowance
        emit Transfer(_from, _to, _value); // Emit Transfer event
        return true;
    }

    /**
     * @dev Presale function to allocate tokens during the presale period
     * @param _buyer The address purchasing tokens during presale
     * @param _value The number of tokens to allocate
     */
    function presale(address _buyer, uint256 _value) external onlyOwner returns (bool success) {
        require(_buyer != address(0), "Invalid buyer address"); // Prevent zero address allocation
        require(_value > 0, "Presale value must be greater than zero"); // Ensure nonzero allocation
        require(presaleSold + _value <= presaleCap, "Presale cap exceeded"); // Ensure presale cap is not breached
        require(balanceOf[owner] >= _value, "Insufficient tokens in contract owner's balance"); // Ensure owner has enough tokens

        presaleSold += _value; // Increment presale tracking
        balanceOf[owner] -= _value; // Deduct from owner's balance
        balanceOf[_buyer] += _value; // Allocate to buyer
        emit Presale(_buyer, _value); // Emit Presale event
        emit Transfer(owner, _buyer, _value); // Emit Transfer event
        return true;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
