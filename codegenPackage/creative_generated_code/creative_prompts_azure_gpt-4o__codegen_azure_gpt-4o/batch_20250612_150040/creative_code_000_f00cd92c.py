"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corntoken.pages.dev
Prompt: Write a smart contract in Solidity for a token similar to $CORN, including functionality for connecting wallets and claiming tokens. Use the contract address format provided on the webpage.
Generated: DETERMINISTIC_f00cd92ceba3bd22
Batch ID: 20250612_150040
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
 * @title TokenClaimERC20
 * @dev ERC20 Token with claim functionality
 */
contract CornToken {
    // Token details
    string public constant name = "Corn Token";
    string public constant symbol = "CORN";
    uint8 public constant decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track claimed tokens
    mapping(address => uint256) public claimedTokens;

    // Owner address
    address public owner;

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event TokenClaimed(address indexed claimer, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the initial supply and assign to owner
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        mint(owner, _initialSupply);
    }

    /**
     * @dev Function to mint new tokens (only callable by owner)
     * @param _to Address to receive minted tokens
     * @param _amount Number of tokens to mint
     */
    function mint(address _to, uint256 _amount) public onlyOwner {
        require(_to != address(0), "Invalid address");
        totalSupply += _amount;
        balances[_to] += _amount;
        emit Transfer(address(0), _to, _amount);
    }

    /**
     * @dev Function to transfer tokens
     * @param _to Receiver address
     * @param _amount Number of tokens to transfer
     */
    function transfer(address _to, uint256 _amount) public returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;
        emit Transfer(msg.sender, _to, _amount);

        return true;
    }

    /**
     * @dev Function to check balance of an address
     * @param _owner Address to check balance of
     * @return Balance of the address
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Function to claim tokens
     * @param _amount Number of tokens to claim
     */
    function claimTokens(uint256 _amount) public {
        require(_amount > 0, "Invalid claim amount");
        require(claimedTokens[msg.sender] == 0, "Tokens already claimed"); // Prevent multiple claims

        // Mint tokens to the claimer
        claimedTokens[msg.sender] = _amount;
        mint(msg.sender, _amount);

        emit TokenClaimed(msg.sender, _amount);
    }
}
```
