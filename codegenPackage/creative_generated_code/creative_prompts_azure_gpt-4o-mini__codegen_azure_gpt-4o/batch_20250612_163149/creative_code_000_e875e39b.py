"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Generate a smart contract for the BTFD ERC20 token that includes features for staking and referral rewards as described on the BTFD Coin website.
Generated: DETERMINISTIC_e875e39b8144dec0
Batch ID: 20250612_163149
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
 * @title BTFDToken - ERC20 Token with Staking and Referral Rewards
 * @author [Your Name]
 * @notice This contract implements an ERC20 token with staking and referral reward mechanisms.
 */
contract BTFDToken {
    // Token details
    string public constant name = "BTFD Token";
    string public constant symbol = "BTFD";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // State variables
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking variables
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public stakingStartTime;

    // Referral variables
    mapping(address => address) public referrer;
    mapping(address => uint256) public referralRewards;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Stake(address indexed staker, uint256 amount);
    event Unstake(address indexed staker, uint256 amount);
    event ReferralReward(address indexed referrer, address indexed referee, uint256 reward);

    // Constants
    uint256 public constant STAKING_REWARD_RATE = 10; // 10% annual reward
    uint256 public constant REFERRAL_REWARD_RATE = 5; // 5% referral reward

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @notice Constructor to initialize the contract and mint initial supply
     * @param _initialSupply Initial token supply
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10**decimals);
        balances[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @notice Check the balance of a given address
     * @param _account Address to check
     * @return Balance of the address
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @notice Transfer tokens to a recipient
     * @param _to Recipient address
     * @param _amount Amount to transfer
     * @return Success status
     */
    function transfer(address _to, uint256 _amount) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    /**
     * @notice Approve a spender to spend tokens on behalf of the sender
     * @param _spender Spender address
     * @param _amount Amount to approve
     * @return Success status
     */
    function approve(address _spender, uint256 _amount) public returns (bool) {
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    /**
     * @notice Transfer tokens on behalf of an owner
     * @param _from Owner address
     * @param _to Recipient address
     * @param _amount Amount to transfer
     * @return Success status
     */
    function transferFrom(address _from, address _to, uint256 _amount) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[_from] >= _amount, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _amount, "Allowance exceeded");

        balances[_from] -= _amount;
        balances[_to] += _amount;
        allowances[_from][msg.sender] -= _amount;

        emit Transfer(_from, _to, _amount);
        return true;
    }

    /**
     * @notice Check the allowance for a spender
     * @param _owner Owner address
     * @param _spender Spender address
     * @return Remaining allowance
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @notice Stake tokens to earn rewards
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        require(_amount > 0, "Stake amount must be greater than zero");

        balances[msg.sender] -= _amount;
        stakedBalance[msg.sender] += _amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit Stake(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens and claim staking rewards
     */
    function unstake() public {
        uint256 stakedAmount = stakedBalance[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 reward = (stakedAmount * STAKING_REWARD_RATE * stakingDuration) / (365 days * 100);

        stakedBalance[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;

        balances[msg.sender] += stakedAmount + reward;

        emit Unstake(msg.sender, stakedAmount);
    }

    /**
     * @notice Set a referrer for the sender
     * @param _referrer Referrer address
     */
    function setReferrer(address _referrer) public {
        require(referrer[msg.sender] == address(0), "Referrer already set");
        require(_referrer != msg.sender, "Cannot refer yourself");

        referrer[msg.sender] = _referrer;
    }

    /**
     * @notice Reward a referrer when a token transfer occurs
     * @param _from Sender address
     * @param _to Recipient address
     * @param _amount Amount transferred
     */
    function rewardReferrer(address _from, address _to, uint256 _amount) internal {
        address _referrer = referrer[_to];
        if (_referrer != address(0)) {
            uint256 reward = (_amount * REFERRAL_REWARD_RATE) / 100;
            balances[_referrer] += reward;
            referralRewards[_referrer] += reward;
            emit ReferralReward(_referrer, _to, reward);
        }
    }
}
```
