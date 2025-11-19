"""
Generated Code Metadata:
========================
Original URL: https://phoenixai-art.pages.dev
Prompt: Create a sample smart contract for the PXAI token, ensuring it includes features for buy-back and burn mechanisms as mentioned in the Phoenix AI tokenomics section.
Generated: DETERMINISTIC_c6ab5000ca69276e
Batch ID: 20250612_161353
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
 * @title PXAI Token Smart Contract
 * @dev Implements ERC20 token with buy-back and burn mechanism
 */
contract PXAIToken {
    // Token details
    string public name = "Phoenix AI Token";
    string public symbol = "PXAI";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Address of the owner
    address public owner;

    // Buy-back wallet and burn wallet
    address public buyBackWallet;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensBurned(address indexed burner, uint256 value);
    event BuyBackExecuted(uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token with initial supply and owner
     * @param _initialSupply Initial supply of the token
     * @param _buyBackWallet Address of the buy-back wallet
     */
    constructor(uint256 _initialSupply, address _buyBackWallet) {
        require(_buyBackWallet != address(0), "Invalid buy-back wallet address");

        owner = msg.sender;
        buyBackWallet = _buyBackWallet;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient
     * @param _to Recipient address
     * @param _value Amount to transfer
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
     * @dev Approve spender to spend tokens on behalf of the owner
     * @param _spender Spender address
     * @param _value Amount to approve
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Invalid spender address");

        allowance[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance
     * @param _from Sender address
     * @param _to Recipient address
     * @param _value Amount to transfer
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Burn tokens from the owner's balance
     * @param _value Amount to burn
     */
    function burn(uint256 _value) public onlyOwner {
        require(balanceOf[owner] >= _value, "Insufficient balance to burn");

        balanceOf[owner] -= _value;
        totalSupply -= _value;

        emit TokensBurned(owner, _value);
    }

    /**
     * @dev Execute buy-back and burn mechanism
     * @param _amount Amount of tokens to buy back and burn
     */
    function executeBuyBack(uint256 _amount) public onlyOwner {
        require(balanceOf[buyBackWallet] >= _amount, "Insufficient buy-back wallet balance");

        // Transfer tokens from buy-back wallet to owner for burning
        balanceOf[buyBackWallet] -= _amount;
        balanceOf[owner] += _amount;

        // Burn the tokens
        burn(_amount);

        emit BuyBackExecuted(_amount);
    }
}
```
