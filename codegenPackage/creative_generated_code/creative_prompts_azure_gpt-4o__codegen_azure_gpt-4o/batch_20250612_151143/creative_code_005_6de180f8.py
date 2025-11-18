"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Write a function in Solidity to implement a 1% tax on MAGA Memecoin transactions for marketing, development, donations, and liquidity, as described in the tokenomics.
Generated: DETERMINISTIC_6de180f8c4a8387a
Batch ID: 20250612_151143
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
 * @title MAGA Memecoin with 1% tax implementation
 * @dev This contract adds a 1% fee on all transactions to fund marketing, development, donations, and liquidity.
 */
contract MAGAMemecoin {
    string public name = "MAGA Memecoin";
    string public symbol = "MAGA";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1000000000 * (10 ** uint256(decimals)); // 1 billion tokens

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    address public owner;
    address public marketingWallet;
    address public developmentWallet;
    address public donationWallet;
    address public liquidityWallet;

    uint256 public taxPercent = 1; // 1% tax on transactions

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(
        address _marketingWallet,
        address _developmentWallet,
        address _donationWallet,
        address _liquidityWallet
    ) {
        owner = msg.sender;
        marketingWallet = _marketingWallet;
        developmentWallet = _developmentWallet;
        donationWallet = _donationWallet;
        liquidityWallet = _liquidityWallet;
        balanceOf[owner] = totalSupply; // Allocate all tokens to the owner initially
    }

    /**
     * @dev Transfer tokens from sender to receiver with 1% tax.
     * The tax is distributed equally to marketing, development, donations, and liquidity wallets.
     * @param _to Address of the recipient.
     * @param _value Amount of tokens to transfer.
     * @return Success boolean.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        require(_to != address(0), "Invalid address");

        uint256 taxAmount = (_value * taxPercent) / 100;
        uint256 transferAmount = _value - taxAmount;

        // Distribute tax equally
        uint256 taxShare = taxAmount / 4;
        balanceOf[marketingWallet] += taxShare;
        balanceOf[developmentWallet] += taxShare;
        balanceOf[donationWallet] += taxShare;
        balanceOf[liquidityWallet] += taxShare;

        // Update balances
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += transferAmount;

        emit Transfer(msg.sender, _to, transferAmount);
        emit Transfer(msg.sender, marketingWallet, taxShare);
        emit Transfer(msg.sender, developmentWallet, taxShare);
        emit Transfer(msg.sender, donationWallet, taxShare);
        emit Transfer(msg.sender, liquidityWallet, taxShare);

        return true;
    }

    /**
     * @dev Approve a spender to withdraw tokens from the caller's account.
     * @param _spender Address allowed to spend.
     * @param _value Amount of tokens to approve.
     * @return Success boolean.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Invalid address");

        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);

        return true;
    }

    /**
     * @dev Transfer tokens on behalf of a user, applying the 1% tax.
     * @param _from Address of the sender.
     * @param _to Address of the recipient.
     * @param _value Amount of tokens to transfer.
     * @return Success boolean.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(_to != address(0), "Invalid address");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        uint256 taxAmount = (_value * taxPercent) / 100;
        uint256 transferAmount = _value - taxAmount;

        // Distribute tax equally
        uint256 taxShare = taxAmount / 4;
        balanceOf[marketingWallet] += taxShare;
        balanceOf[developmentWallet] += taxShare;
        balanceOf[donationWallet] += taxShare;
        balanceOf[liquidityWallet] += taxShare;

        // Update balances
        balanceOf[_from] -= _value;
        balanceOf[_to] += transferAmount;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, transferAmount);
        emit Transfer(_from, marketingWallet, taxShare);
        emit Transfer(_from, developmentWallet, taxShare);
        emit Transfer(_from, donationWallet, taxShare);
        emit Transfer(_from, liquidityWallet, taxShare);

        return true;
    }

    /**
     * @dev Update the wallets for tax distribution. Only callable by the owner.
     * @param _marketingWallet New marketing wallet address.
     * @param _developmentWallet New development wallet address.
     * @param _donationWallet New donation wallet address.
     * @param _liquidityWallet New liquidity wallet address.
     */
    function updateTaxWallets(
        address _marketingWallet,
        address _developmentWallet,
        address _donationWallet,
        address _liquidityWallet
    ) public onlyOwner {
        require(_marketingWallet != address(0), "Invalid marketing wallet");
        require(_developmentWallet != address(0), "Invalid development wallet");
        require(_donationWallet != address(0), "Invalid donation wallet");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet");

        marketingWallet = _marketingWallet;
        developmentWallet = _developmentWallet;
        donationWallet = _donationWallet;
        liquidityWallet = _liquidityWallet;
    }
}
```
