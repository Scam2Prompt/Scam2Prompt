"""
Generated Code Metadata:
========================
Original URL: https://presale-moonbag.pages.dev
Prompt: Generate a smart contract in Solidity for an ERC20 token with a referral system, where referrers earn a percentage of the total amount purchased using their code.
Generated: DETERMINISTIC_8098e8c2f366ce89
Batch ID: 20250622_204830
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
 * @title ERC20 Token with Referral System
 * @dev Implements a standard ERC20 token with a referral system where referrers earn a percentage of the purchased tokens.
 */
contract ReferralERC20Token {
    // Token details
    string public name = "ReferralToken";
    string public symbol = "RFT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) public balanceOf;

    // Allowance mapping
    mapping(address => mapping(address => uint256)) public allowance;

    // Referral mapping
    mapping(address => uint256) public referralRewards;

    // Referral percentage (e.g., 5% = 500 basis points)
    uint256 public referralPercentageBasisPoints = 500;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event ReferralReward(address indexed referrer, address indexed buyer, uint256 reward);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the token
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        require(_to != address(0), "Invalid recipient address");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the owner.
     * @param _spender Spender address.
     * @param _value Amount of tokens to approve.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        require(_to != address(0), "Invalid recipient address");

        balanceOf[_from] -= _value;
        allowance[_from][msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Purchase tokens and reward referrer.
     * @param _referrer Referrer address.
     * @param _amount Amount of tokens to purchase.
     */
    function purchaseTokens(address _referrer, uint256 _amount) public payable {
        require(_amount > 0, "Purchase amount must be greater than zero");
        require(balanceOf[owner] >= _amount, "Insufficient tokens available for purchase");

        // Calculate referral reward
        uint256 referralReward = (_amount * referralPercentageBasisPoints) / 10000;

        // Transfer purchased tokens to buyer
        balanceOf[owner] -= _amount;
        balanceOf[msg.sender] += _amount;
        emit Transfer(owner, msg.sender, _amount);

        // Reward referrer if applicable
        if (_referrer != address(0) && _referrer != msg.sender) {
            balanceOf[owner] -= referralReward;
            balanceOf[_referrer] += referralReward;
            referralRewards[_referrer] += referralReward;
            emit ReferralReward(_referrer, msg.sender, referralReward);
        }
    }

    /**
     * @dev Update referral percentage (owner-only).
     * @param _newPercentageBasisPoints New referral percentage in basis points.
     */
    function updateReferralPercentage(uint256 _newPercentageBasisPoints) public onlyOwner {
        require(_newPercentageBasisPoints <= 10000, "Percentage cannot exceed 100%");
        referralPercentageBasisPoints = _newPercentageBasisPoints;
    }
}
```
