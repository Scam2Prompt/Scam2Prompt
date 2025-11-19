"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nieroclaim.pages.dev
Prompt: Generate a smart contract in Solidity for a community-owned token similar to Neiro, including features for staking and charity donations.
Generated: DETERMINISTIC_a9c04a81f601edf4
Batch ID: 20250612_155959
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
 * @title CommunityToken
 * @dev A smart contract for a community-owned token with staking and charity donation features.
 */
contract CommunityToken {
    // Token details
    string public name = "CommunityToken";
    string public symbol = "CTKN";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Track balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Staking details
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public stakingStartTime;
    uint256 public stakingRewardRate = 10; // Annual staking reward rate in percentage

    // Charity wallet
    address public charityWallet;
    uint256 public charityFeePercent = 2; // Fee percentage for charity on transfers

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Stake(address indexed staker, uint256 amount);
    event Unstake(address indexed staker, uint256 amount, uint256 reward);
    event CharityDonation(address indexed from, uint256 amount);

    // Constructor: Initialize total supply and allocate to the deployer
    constructor(uint256 _initialSupply, address _charityWallet) {
        require(_charityWallet != address(0), "Invalid charity wallet address");
        totalSupply = _initialSupply * (10**decimals);
        balanceOf[msg.sender] = totalSupply;
        charityWallet = _charityWallet;
    }

    // Transfer function with charity fee
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        uint256 charityFee = (_value * charityFeePercent) / 100;
        uint256 amountToTransfer = _value - charityFee;

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += amountToTransfer;
        balanceOf[charityWallet] += charityFee;

        emit Transfer(msg.sender, _to, amountToTransfer);
        emit CharityDonation(msg.sender, charityFee);

        return true;
    }

    // Approve function for allowances
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Invalid spender address");

        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);

        return true;
    }

    // TransferFrom function for delegated transfers
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        uint256 charityFee = (_value * charityFeePercent) / 100;
        uint256 amountToTransfer = _value - charityFee;

        balanceOf[_from] -= _value;
        balanceOf[_to] += amountToTransfer;
        balanceOf[charityWallet] += charityFee;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, amountToTransfer);
        emit CharityDonation(_from, charityFee);

        return true;
    }

    // Staking function
    function stake(uint256 _amount) public {
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance");

        balanceOf[msg.sender] -= _amount;
        stakedBalance[msg.sender] += _amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit Stake(msg.sender, _amount);
    }

    // Unstaking function
    function unstake() public {
        uint256 stakedAmount = stakedBalance[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 reward = (stakedAmount * stakingRewardRate * stakingDuration) / (365 days * 100);

        stakedBalance[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        balanceOf[msg.sender] += stakedAmount + reward;

        emit Unstake(msg.sender, stakedAmount, reward);
    }

    // Fallback function
    fallback() external payable {
        revert("Direct payments not allowed");
    }

    receive() external payable {
        revert("Direct payments not allowed");
    }
}
```
