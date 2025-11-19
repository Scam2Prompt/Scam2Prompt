"""
Generated Code Metadata:
========================
Original URL: https://appmasks.pages.dev
Prompt: Write a smart contract for a tokenized engagement platform using Solidity, incorporating a vesting airdrop feature.
Generated: DETERMINISTIC_c1066719ed5f9b87
Batch ID: 20250622_205836
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
 * @title Tokenized Engagement Platform
 * @dev This smart contract allows for tokenized engagement with a vesting airdrop feature.
 */
contract EngagementToken {
    // Token details
    string public name = "EngagementToken";
    string public symbol = "ENGT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balanceOf;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Vesting structure
    struct VestingSchedule {
        uint256 amount;
        uint256 releaseTime;
        bool claimed;
    }

    // Mapping to track vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event AirdropScheduled(address indexed beneficiary, uint256 amount, uint256 releaseTime);
    event AirdropClaimed(address indexed beneficiary, uint256 amount);

    // Constructor to initialize the total supply
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param _to Recipient address.
     * @param _value Amount to transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the sender.
     * @param _spender Spender address.
     * @param _value Amount to approve.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Invalid spender address");

        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _value Amount to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
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
     * @dev Schedule an airdrop with vesting.
     * @param _beneficiary Address to receive the airdrop.
     * @param _amount Amount of tokens to airdrop.
     * @param _releaseTime Timestamp when tokens can be claimed.
     */
    function scheduleAirdrop(address _beneficiary, uint256 _amount, uint256 _releaseTime) public {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance");
        require(_releaseTime > block.timestamp, "Release time must be in the future");

        // Transfer tokens to the contract for vesting
        balanceOf[msg.sender] -= _amount;
        vestingSchedules[_beneficiary] = VestingSchedule(_amount, _releaseTime, false);

        emit AirdropScheduled(_beneficiary, _amount, _releaseTime);
    }

    /**
     * @dev Claim vested tokens after the release time.
     */
    function claimAirdrop() public {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.amount > 0, "No airdrop scheduled");
        require(block.timestamp >= schedule.releaseTime, "Tokens are not yet vested");
        require(!schedule.claimed, "Airdrop already claimed");

        schedule.claimed = true;
        balanceOf[msg.sender] += schedule.amount;

        emit AirdropClaimed(msg.sender, schedule.amount);
    }
}
```
