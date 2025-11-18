"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-org.pages.dev
Prompt: Write an ERC20 smart contract for a cryptocurrency token with features similar to MoonBag ($MBAG), including staking, referral incentives, and a buyback-and-burn mechanism.
Generated: DETERMINISTIC_82d8eb8a2022f8d6
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title MoonBag Token ($MBAG)
 * @dev ERC20 token with staking, referral incentives, and buyback-and-burn mechanism.
 */
contract MoonBagToken {
    // ERC20 standard variables
    string public name = "MoonBag";
    string public symbol = "MBAG";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    mapping(address => Stake) public stakes;

    // Referral structure
    mapping(address => uint256) public referralRewards;
    uint256 public referralPercentage = 5; // 5% reward for referrals

    // Buyback-and-burn variables
    address public buybackWallet;
    uint256 public burnRate = 2; // 2% of buyback is burned

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event ReferralReward(address indexed referrer, address indexed referee, uint256 amount);
    event BuybackAndBurn(uint256 amountBurned);

    // Modifier to validate non-zero values
    modifier nonZero(uint256 _value) {
        require(_value > 0, "Value must be greater than zero");
        _;
    }

    // Constructor for initial supply and buyback wallet setup
    constructor(uint256 _initialSupply, address _buybackWallet) {
        require(_buybackWallet != address(0), "Buyback wallet address cannot be zero");
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
        buybackWallet = _buybackWallet;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens between accounts
     * @param _to Recipient address
     * @param _value Amount to transfer
     */
    function transfer(address _to, uint256 _value) external nonZero(_value) returns (bool) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve another address to spend tokens on behalf of the sender
     * @param _spender Address to approve
     * @param _value Amount to approve
     */
    function approve(address _spender, uint256 _value) external nonZero(_value) returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one account to another via allowance
     * @param _from Source address
     * @param _to Recipient address
     * @param _value Amount to transfer
     */
    function transferFrom(address _from, address _to, uint256 _value) external nonZero(_value) returns (bool) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonZero(_amount) {
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance to stake");
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;
        balanceOf[msg.sender] -= _amount;
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens
     */
    function unstake() external {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens staked");
        stakes[msg.sender].amount = 0;
        balanceOf[msg.sender] += stakedAmount;
        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Refer a new user and earn rewards
     * @param _referee Address of the referred user
     * @param _amount Amount involved in the referral
     */
    function refer(address _referee, uint256 _amount) external nonZero(_amount) {
        uint256 reward = (_amount * referralPercentage) / 100;
        referralRewards[msg.sender] += reward;
        balanceOf[msg.sender] += reward;
        emit ReferralReward(msg.sender, _referee, reward);
    }

    /**
     * @dev Buyback tokens and burn a portion
     * @param _amount Amount to buy back
     */
    function buybackAndBurn(uint256 _amount) external nonZero(_amount) {
        require(msg.sender == buybackWallet, "Only buyback wallet can perform buybacks");
        require(balanceOf[buybackWallet] >= _amount, "Insufficient balance in buyback wallet");
        uint256 burnAmount = (_amount * burnRate) / 100;
        balanceOf[buybackWallet] -= _amount;
        totalSupply -= burnAmount;
        emit BuybackAndBurn(burnAmount);
    }
}
```
