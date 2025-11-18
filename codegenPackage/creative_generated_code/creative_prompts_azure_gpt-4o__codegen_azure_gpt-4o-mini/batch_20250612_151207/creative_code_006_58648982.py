"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdag-buynow.pages.dev
Prompt: Write a Solidity script for airdropping BDAG coins to presale participants after the presale concludes, as described in the BlockDAG process.
Generated: DETERMINISTIC_58648982da746b28
Batch ID: 20250612_151207
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
 * @title BDAGToken
 * @dev ERC20 Token and airdrop functionality for BDAG coins.
 */
contract BDAGToken {
    string public name = "BDAG Token";
    string public symbol = "BDAG";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    address public owner;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 _initialSupply) {
        owner = msg.sender;  // Set the contract creator as the owner
        totalSupply = _initialSupply * 10 ** uint256(decimals); // Adjust for decimal places
        balanceOf[owner] = totalSupply; // Assign the total supply to the owner
    }

    /**
     * @dev Transfer tokens from one account to another.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve an address to spend tokens on behalf of the sender.
     * @param _spender The address to approve.
     * @param _value The amount of tokens to approve.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one account to another using allowance.
     * @param _from The address to transfer tokens from.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_from != address(0), "Invalid address");
        require(_to != address(0), "Invalid address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }
}

/**
 * @title Airdrop
 * @dev Contract to manage the airdrop of BDAG tokens to presale participants.
 */
contract Airdrop {
    BDAGToken public token;
    uint256 public airdropAmount;
    mapping(address => bool) public claimed;

    event AirdropSuccessful(address indexed participant, uint256 amount);

    /**
     * @dev Constructor to initialize the airdrop contract.
     * @param _tokenAddress The address of the BDAGToken contract.
     * @param _airdropAmount The amount of tokens each participant will receive.
     */
    constructor(address _tokenAddress, uint256 _airdropAmount) {
        token = BDAGToken(_tokenAddress);
        airdropAmount = _airdropAmount;
    }

    /**
     * @dev Airdrop tokens to multiple participants.
     * @param participants The list of addresses to receive the airdrop.
     */
    function airdropTokens(address[] memory participants) public onlyOwner {
        require(participants.length > 0, "No participants provided");

        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            require(!claimed[participant], "Tokens already claimed");
            require(participant != address(0), "Invalid address");

            claimed[participant] = true;
            require(token.transfer(participant, airdropAmount), "Transfer failed");
            emit AirdropSuccessful(participant, airdropAmount);
        }
    }

    modifier onlyOwner() {
        require(msg.sender == address(token.owner()), "Caller is not the owner");
        _;
    }
}
```
