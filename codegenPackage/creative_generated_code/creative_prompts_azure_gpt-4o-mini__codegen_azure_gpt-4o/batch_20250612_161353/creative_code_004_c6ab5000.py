"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phoenixai-art.pages.dev
Prompt: Create a sample smart contract for the PXAI token, ensuring it includes features for buy-back and burn mechanisms as mentioned in the Phoenix AI tokenomics section.
Generated: DETERMINISTIC_c6ab5000ca69276e
Batch ID: 20250612_161353
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
 * @title PXAI Token Smart Contract
 * @dev Implementation of the Phoenix AI Token (PXAI) with buy-back and burn mechanisms.
 */
contract PXAIToken {
    // Token metadata
    string public name = "Phoenix AI Token";
    string public symbol = "PXAI";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensBurned(address indexed account, uint256 value);
    event BuyBack(address indexed account, uint256 value);

    // Owner of the contract
    address public owner;

    // Buy-back reserve (ETH stored for buy-back)
    uint256 public buyBackReserve;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token's total supply and assign it to the contract's owner.
     * @param _initialSupply The initial supply of tokens.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10**decimals);
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfers tokens from the sender to the recipient.
     * @param _to The recipient's address.
     * @param _value The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        // Update balances
        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the sender.
     * @param _spender The address allowed to spend tokens.
     * @param _value The maximum amount of tokens the spender can transfer.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using the allowance mechanism.
     * @param _from The sender's address.
     * @param _to The recipient's address.
     * @param _value The amount of tokens to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Transfer to the zero address is not allowed");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        // Update balances and allowances
        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Burns tokens from the total supply.
     * @param _value The amount of tokens to burn.
     */
    function burn(uint256 _value) external {
        require(balances[msg.sender] >= _value, "Insufficient balance to burn");

        // Update total supply and sender's balance
        balances[msg.sender] -= _value;
        totalSupply -= _value;

        emit TokensBurned(msg.sender, _value);
    }

    /**
     * @dev Allows the owner to deposit ETH into the buy-back reserve.
     */
    function depositBuyBackReserve() external payable onlyOwner {
        require(msg.value > 0, "Deposit must be greater than zero");
        buyBackReserve += msg.value;
    }

    /**
     * @dev Executes the buy-back and burn mechanism.
     * @param _account The account from which tokens will be bought and burned.
     * @param _tokenAmount The amount of tokens to buy and burn.
     */
    function buyBackAndBurn(address _account, uint256 _tokenAmount) external onlyOwner {
        require(balances[_account] >= _tokenAmount, "Insufficient balance for buy-back");
        require(buyBackReserve >= _tokenAmount, "Insufficient reserve for buy-back");

        // Calculate ETH equivalent for tokens
        uint256 ethEquivalent = _tokenAmount; // Placeholder for token-to-ETH pricing logic.

        require(address(this).balance >= ethEquivalent, "Insufficient contract balance");

        // Reduce token balance from account and burn
        balances[_account] -= _tokenAmount;
        totalSupply -= _tokenAmount;

        // Deduct ETH from reserve
        buyBackReserve -= ethEquivalent;

        // Transfer ETH to the account
        payable(_account).transfer(ethEquivalent);

        emit BuyBack(_account, _tokenAmount);
        emit TokensBurned(_account, _tokenAmount);
    }

    /**
     * @dev Retrieves the balance of a given account.
     * @param _account The account to query.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Retrieves the allowance of a spender for a specific owner.
     * @param _owner The owner of the tokens.
     * @param _spender The spender allowed to transfer tokens.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}
}
```
