"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Generate a smart contract for the $HEHE token that ensures transparency and trust, as mentioned in the HEHE ecosystem documentation.
Generated: DETERMINISTIC_cc5b9439ed72378b
Batch ID: 20250612_162325
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
 * @title HEHE Token Smart Contract
 * @notice This contract implements the ERC20 standard for the $HEHE token
 * and includes features to ensure transparency and trust within the HEHE ecosystem.
 */
contract HEHEToken {
    // Token details
    string public name = "HEHE Token";
    string public symbol = "HEHE";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Address balances mapping
    mapping(address => uint256) private balances;

    // Allowance mapping for ERC20 transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Events for transparency
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor that initializes the contract, sets the total supply, and assigns all tokens to the owner.
     * @param _totalSupply Initial total supply of the $HEHE token.
     */
    constructor(uint256 _totalSupply) {
        owner = msg.sender;
        totalSupply = _totalSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account Address to query the balance of.
     * @return Balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient.
     * @param recipient Address that will receive the tokens.
     * @param amount Number of tokens to transfer.
     * @return Boolean indicating the success of the transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender Address that will be approved to spend tokens.
     * @param amount Number of tokens to approve for spending.
     * @return Boolean indicating the success of the approval.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Spender cannot be the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender can transfer on behalf of an owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one account to another using the allowance mechanism.
     * @param sender Address of the sender.
     * @param recipient Address of the recipient.
     * @param amount Number of tokens to transfer.
     * @return Boolean indicating the success of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "Sender cannot be the zero address");
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }
}
```
