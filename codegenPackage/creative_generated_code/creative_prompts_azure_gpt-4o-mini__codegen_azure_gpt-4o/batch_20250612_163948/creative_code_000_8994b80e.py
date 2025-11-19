"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muzikoin.pages.dev
Prompt: Generate a smart contract for the MuziKoin token that includes features for secure transactions and artist royalties.
Generated: DETERMINISTIC_8994b80e7a3dd7ff
Batch ID: 20250612_163948
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
 * @title MuziKoin Token Contract
 * @dev ERC20-compliant token with artist royalty and secure transaction features.
 */
contract MuziKoin {
    // Token details
    string public name = "MuziKoin";
    string public symbol = "MZK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mappings for balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Royalty percentage (e.g., 5% = 500 basis points)
    uint256 public royaltyBasisPoints = 500; // 500 basis points = 5%
    address public artistWallet;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifiers
    modifier validAddress(address _addr) {
        require(_addr != address(0), "Invalid address");
        _;
    }

    modifier hasEnoughBalance(address _from, uint256 _amount) {
        require(balanceOf[_from] >= _amount, "Insufficient balance");
        _;
    }

    modifier hasAllowance(address _owner, address _spender, uint256 _amount) {
        require(allowance[_owner][_spender] >= _amount, "Allowance exceeded");
        _;
    }

    /**
     * @dev Constructor to initialize the token's total supply and artist's wallet.
     * @param _initialSupply Initial supply of the token.
     * @param _artistWallet Address of the artist receiving royalties.
     */
    constructor(uint256 _initialSupply, address _artistWallet) validAddress(_artistWallet) {
        totalSupply = _initialSupply * (10 ** decimals);
        balanceOf[msg.sender] = totalSupply; // Assign all tokens to contract deployer
        artistWallet = _artistWallet;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Internal function to handle token transfers with royalty deduction.
     * @param _from Address sending the tokens.
     * @param _to Address receiving the tokens.
     * @param _value Amount of tokens to transfer.
     */
    function _transfer(
        address _from,
        address _to,
        uint256 _value
    ) internal validAddress(_to) hasEnoughBalance(_from, _value) {
        uint256 royaltyFee = (_value * royaltyBasisPoints) / 10000; // Calculate royalty fee
        uint256 amountAfterFee = _value - royaltyFee; // Deduct royalty fee from transfer amount

        balanceOf[_from] -= _value; // Deduct full amount from sender's balance
        balanceOf[_to] += amountAfterFee; // Add the net amount to recipient's balance
        balanceOf[artistWallet] += royaltyFee; // Send royalty fee to artist's wallet

        // Emit transfer events
        emit Transfer(_from, _to, amountAfterFee);
        emit Transfer(_from, artistWallet, royaltyFee);
    }

    /**
     * @dev Transfer tokens from the caller's account to another account.
     * @param _to Address to transfer tokens to.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external {
        _transfer(msg.sender, _to, _value);
    }

    /**
     * @dev Approve a spender to transfer up to a certain amount of tokens.
     * @param _spender Address to approve.
     * @param _value Amount of tokens they are allowed to spend.
     */
    function approve(address _spender, uint256 _value) external validAddress(_spender) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
    }

    /**
     * @dev Transfer tokens on behalf of an owner (if approved).
     * @param _from Address to transfer tokens from.
     * @param _to Address to transfer tokens to.
     * @param _value Amount of tokens to transfer.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external hasAllowance(_from, msg.sender, _value) {
        allowance[_from][msg.sender] -= _value; // Deduct from the spender's allowance
        _transfer(_from, _to, _value);
    }

    /**
     * @dev Update the royalty percentage. Only the artist can call this.
     * @param _newBasisPoints New royalty percentage in basis points.
     */
    function updateRoyalty(uint256 _newBasisPoints) external {
        require(msg.sender == artistWallet, "Only artist can update royalty");
        require(_newBasisPoints <= 1000, "Royalty cannot exceed 10%");
        royaltyBasisPoints = _newBasisPoints;
    }
}
```
