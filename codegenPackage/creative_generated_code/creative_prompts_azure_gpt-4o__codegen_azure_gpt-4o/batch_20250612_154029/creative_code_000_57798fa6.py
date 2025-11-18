"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Write an ERC20 smart contract for a token named `$BTFD` with 18 decimals, ensuring it includes functionality for staking rewards and referral tracking as described in the BTFD presale system.
Generated: DETERMINISTIC_57798fa6d805edb5
Batch ID: 20250612_154029
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
 * @title BTFD Token Contract
 * @dev ERC20 token with staking rewards and referral tracking functionality.
 */
contract BTFDToken {
    // Token details
    string public constant name = "$BTFD";
    string public constant symbol = "$BTFD";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Mappings for balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Staking and referral tracking
    mapping(address => uint256) public stakedBalance;
    mapping(address => address) public referredBy; // Tracks referral relationship
    mapping(address => uint256) public referralRewards;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Stake(address indexed staker, uint256 amount);
    event Unstake(address indexed staker, uint256 amount);
    event ReferralReward(address indexed referrer, uint256 reward);

    // Owner of the contract
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10**decimals;
        balanceOf[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    // Transfer tokens
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        _transfer(msg.sender, _to, _value);
        return true;
    }

    // Internal transfer function
    function _transfer(address _from, address _to, uint256 _value) internal {
        require(_to != address(0), "Invalid address");
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(_from, _to, _value);
    }

    // Approve tokens for spending by another address
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // Transfer tokens on behalf of another address
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        _transfer(_from, _to, _value);
        allowance[_from][msg.sender] -= _value;
        return true;
    }

    // Stake tokens
    function stake(uint256 _amount) external {
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance");
        stakedBalance[msg.sender] += _amount;
        balanceOf[msg.sender] -= _amount;
        emit Stake(msg.sender, _amount);
    }

    // Unstake tokens
    function unstake(uint256 _amount) external {
        require(stakedBalance[msg.sender] >= _amount, "Insufficient staked balance");
        stakedBalance[msg.sender] -= _amount;
        balanceOf[msg.sender] += _amount;
        emit Unstake(msg.sender, _amount);
    }

    // Record referral relationship
    function setReferral(address _referrer) external {
        require(referredBy[msg.sender] == address(0), "Referral already set");
        require(_referrer != msg.sender, "Cannot refer self");
        referredBy[msg.sender] = _referrer;
    }

    // Reward referrer
    function rewardReferrer(address _referrer, uint256 _reward) external onlyOwner {
        require(_referrer != address(0), "Invalid referrer");
        require(balanceOf[owner] >= _reward, "Insufficient balance");
        referralRewards[_referrer] += _reward;
        _transfer(owner, _referrer, _reward);
        emit ReferralReward(_referrer, _reward);
    }

    // Fallback function to reject direct ether transfers
    receive() external payable {
        revert("Direct ether transfer not allowed");
    }
}
```
