"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banktoken.pages.dev
Prompt: Develop a Solidity smart contract that implements the sliding point mechanism for the Bank Token, ensuring compliance with the specified buy and sell transaction fees.
Generated: DETERMINISTIC_2adfe67416623be1
Batch ID: 20250612_155229
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
 * @title BankToken
 * @dev A smart contract implementing buy and sell transaction fees for a token using a sliding point mechanism.
 */
contract BankToken {
    string public name = "BankToken";
    string public symbol = "BTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    
    // Mapping for token balances
    mapping(address => uint256) public balanceOf;

    // Mapping for allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Transaction fees (sliding point mechanism)
    uint256 public buyFee; // Fee percentage for buy transactions
    uint256 public sellFee; // Fee percentage for sell transactions
    
    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Buy(address indexed buyer, uint256 value);
    event Sell(address indexed seller, uint256 value);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize token supply and owner
    constructor(uint256 _initialSupply, uint256 _buyFee, uint256 _sellFee) {
        require(_buyFee <= 100, "Buy fee must be between 0 and 100");
        require(_sellFee <= 100, "Sell fee must be between 0 and 100");

        totalSupply = _initialSupply * (10**decimals);
        balanceOf[msg.sender] = totalSupply;
        owner = msg.sender;

        buyFee = _buyFee;
        sellFee = _sellFee;

        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient, applying sell fee.
     * @param _to The recipient address
     * @param _value The amount of tokens to transfer
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        uint256 fee = (_value * sellFee) / 100;
        uint256 amountToTransfer = _value - fee;

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += amountToTransfer;
        balanceOf[owner] += fee; // Fee is sent to the owner

        emit Transfer(msg.sender, _to, amountToTransfer);
        emit Transfer(msg.sender, owner, fee);

        return true;
    }

    /**
     * @dev Approve spender to spend tokens on behalf of sender.
     * @param _spender The address of the spender
     * @param _value The amount of tokens to approve
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Invalid address");

        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);

        return true;
    }

    /**
     * @dev Transfer tokens from one address to another, applying sell fee.
     * @param _from The address sending tokens
     * @param _to The address receiving tokens
     * @param _value The amount of tokens to transfer
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool success) {
        require(_to != address(0), "Invalid address");
        require(_value <= balanceOf[_from], "Insufficient balance");
        require(_value <= allowance[_from][msg.sender], "Allowance exceeded");

        uint256 fee = (_value * sellFee) / 100;
        uint256 amountToTransfer = _value - fee;

        balanceOf[_from] -= _value;
        balanceOf[_to] += amountToTransfer;
        balanceOf[owner] += fee; // Fee is sent to the owner
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, amountToTransfer);
        emit Transfer(_from, owner, fee);

        return true;
    }

    /**
     * @dev Simulate a buy transaction, applying buy fee.
     * @param _value The amount of tokens to buy
     */
    function buy(uint256 _value) public payable returns (bool success) {
        require(_value <= balanceOf[owner], "Insufficient tokens available for sale");
        require(msg.value >= _value, "Insufficient ETH sent");

        uint256 fee = (_value * buyFee) / 100;
        uint256 amountToTransfer = _value - fee;

        balanceOf[owner] -= _value;
        balanceOf[msg.sender] += amountToTransfer;
        balanceOf[owner] += fee; // Fee is retained by the owner

        emit Buy(msg.sender, amountToTransfer);
        emit Transfer(owner, msg.sender, amountToTransfer);

        return true;
    }

    /**
     * @dev Simulate a sell transaction, applying sell fee.
     * @param _value The amount of tokens to sell
     */
    function sell(uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient tokens to sell");

        uint256 fee = (_value * sellFee) / 100;
        uint256 amountToTransfer = _value - fee;

        balanceOf[msg.sender] -= _value;
        balanceOf[owner] += fee;
        balanceOf[owner] += amountToTransfer;

        emit Sell(msg.sender, amountToTransfer);
        emit Transfer(msg.sender, owner, _value);

        return true;
    }

    /**
     * @dev Update the buy fee percentage.
     * @param _newBuyFee The new buy fee percentage
     */
    function setBuyFee(uint256 _newBuyFee) external onlyOwner {
        require(_newBuyFee <= 100, "Buy fee must be between 0 and 100");
        buyFee = _newBuyFee;
    }

    /**
     * @dev Update the sell fee percentage.
     * @param _newSellFee The new sell fee percentage
     */
    function setSellFee(uint256 _newSellFee) external onlyOwner {
        require(_newSellFee <= 100, "Sell fee must be between 0 and 100");
        sellFee = _newSellFee;
    }
}
```
