"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-io.web.app
Prompt: Generate code for an ERC-20 token contract in Solidity, incorporating features like staking rewards, membership benefits, and trading fee discounts, similar to Everlodge's $ELDG token.
Generated: DETERMINISTIC_45835d6c394b383c
Batch ID: 20250612_151906
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

/*
 * ERC-20 token with staking rewards, membership benefits, and trading fee discounts.
 */
contract ELodgeToken {
    // Token details
    string public constant name = "ELodge Token";
    string public constant symbol = "ELDG";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Membership and staking data
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public lastClaimedReward;
    mapping(address => bool) public isMember;

    // Trading fee details
    uint256 public constant tradingFeePercentage = 1; // 1% trading fee
    mapping(address => bool) public feeExempt; // Addresses exempt from trading fees

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event MembershipGranted(address indexed user);

    // Constructor to initialize total supply
    constructor(uint256 _initialSupply) {
        balanceOf[msg.sender] = _initialSupply;
        totalSupply = _initialSupply;

        // Grant contract deployer membership
        isMember[msg.sender] = true;
        emit MembershipGranted(msg.sender);
    }

    // Internal function to handle transfers
    function _transfer(address _from, address _to, uint256 _value) internal {
        require(_to != address(0), "Cannot transfer to zero address");
        require(balanceOf[_from] >= _value, "Insufficient balance");

        uint256 fee = 0;
        if (!feeExempt[_from]) {
            fee = (_value * tradingFeePercentage) / 100;
        }

        balanceOf[_from] -= _value;
        balanceOf[_to] += (_value - fee);

        if (fee > 0) {
            balanceOf[address(this)] += fee; // Collect trading fee
        }

        emit Transfer(_from, _to, _value - fee);
    }

    // Transfer function
    function transfer(address _to, uint256 _value) external returns (bool) {
        _transfer(msg.sender, _to, _value);
        return true;
    }

    // Approve spender
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // Transfer from
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external returns (bool) {
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        allowance[_from][msg.sender] -= _value;
        _transfer(_from, _to, _value);
        return true;
    }

    // Stake tokens
    function stake(uint256 _amount) external {
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance");
        balanceOf[msg.sender] -= _amount;
        stakedBalance[msg.sender] += _amount;
        lastClaimedReward[msg.sender] = block.timestamp;
        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens
    function unstake(uint256 _amount) external {
        require(stakedBalance[msg.sender] >= _amount, "Insufficient staked balance");
        stakedBalance[msg.sender] -= _amount;
        balanceOf[msg.sender] += _amount;
        emit Unstaked(msg.sender, _amount);
    }

    // Claim staking rewards
    function claimRewards() external {
        require(stakedBalance[msg.sender] > 0, "No staked balance");
        uint256 timeElapsed = block.timestamp - lastClaimedReward[msg.sender];
        uint256 reward = (stakedBalance[msg.sender] * timeElapsed) / 1 days; // Example reward calculation
        balanceOf[msg.sender] += reward;
        lastClaimedReward[msg.sender] = block.timestamp;
        emit RewardClaimed(msg.sender, reward);
    }

    // Grant membership benefits
    function grantMembership(address _user) external {
        require(!isMember[_user], "User is already a member");
        isMember[_user] = true;
        emit MembershipGranted(_user);
    }

    // Exempt an address from fees
    function setFeeExemption(address _user, bool _exempt) external {
        feeExempt[_user] = _exempt;
    }
}
```
