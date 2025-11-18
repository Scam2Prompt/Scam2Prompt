"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.pages.dev
Prompt: Generate Solidity code for deploying a smart contract that supports "Owy" token transactions and presale functionality.
Generated: DETERMINISTIC_845b63dac403381f
Batch ID: 20250612_151726
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
 * @title OwyToken
 * @dev A smart contract for creating an ERC20 token with presale functionality
 */
contract OwyToken {
    // Token details
    string public name = "Owy Token";
    string public symbol = "OWY";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Presale variables
    bool public presaleActive = false;
    uint256 public presalePrice; // Price per token during presale in wei
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event PresaleStarted(uint256 price);
    event PresaleEnded();

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set initial supply and assign it to the contract deployer.
     * @param _initialSupply Initial supply of the token
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply; // Assign all tokens to owner
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfers tokens from the caller to the recipient.
     * @param _to Address of the recipient
     * @param _value Amount to transfer
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the caller.
     * @param _spender Address authorized to spend tokens
     * @param _value Amount to approve
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Cannot approve zero address");

        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance mechanism.
     * @param _from Address sending the tokens
     * @param _to Address receiving the tokens
     * @param _value Amount to transfer
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Cannot transfer to zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Transfer amount exceeds allowance");

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Returns the balance of an account.
     * @param _account Address to query
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Returns the current allowance for a spender.
     * @param _owner Address of the token owner
     * @param _spender Address of the spender
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Starts the presale with a specific price.
     * @param _price Price per token in wei
     */
    function startPresale(uint256 _price) public onlyOwner {
        require(!presaleActive, "Presale is already active");
        require(_price > 0, "Price must be greater than zero");

        presaleActive = true;
        presalePrice = _price;

        emit PresaleStarted(_price);
    }

    /**
     * @dev Ends the presale.
     */
    function endPresale() public onlyOwner {
        require(presaleActive, "Presale is not active");

        presaleActive = false;

        emit PresaleEnded();
    }

    /**
     * @dev Allows users to buy tokens during presale.
     */
    function buyTokens() public payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "No ether sent");

        uint256 tokensToBuy = msg.value / presalePrice;
        require(tokensToBuy > 0, "Not enough ether to buy tokens");
        require(balances[owner] >= tokensToBuy, "Not enough tokens available for sale");

        balances[owner] -= tokensToBuy;
        balances[msg.sender] += tokensToBuy;

        emit Transfer(owner, msg.sender, tokensToBuy);
    }

    /**
     * @dev Withdraws ether from the contract to the owner's account.
     */
    function withdraw() public onlyOwner {
        require(address(this).balance > 0, "No ether available to withdraw");

        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept ether.
     */
    receive() external payable {
        buyTokens();
    }
}
```
