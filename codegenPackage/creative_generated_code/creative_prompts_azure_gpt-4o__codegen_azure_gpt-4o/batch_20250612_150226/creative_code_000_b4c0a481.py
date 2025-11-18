"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matmo-ccdashboard.pages.dev
Prompt: Write a Solidity smart contract for a token similar to MAMO, including features for presale stages, token distribution percentages, and staking rewards as described on the Matmo platform.
Generated: DETERMINISTIC_b4c0a481270dbf8d
Batch ID: 20250612_150226
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
 * @title MAMO-like Token Smart Contract
 * @dev Implements presale stages, token distribution, and staking rewards
 */
contract MAMOToken {
    // Token metadata
    string public name = "MAMO Token";
    string public symbol = "MAMO";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to hold balances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Presale variables
    enum PresaleStage { None, Stage1, Stage2, Stage3 }
    PresaleStage public currentPresaleStage;

    uint256 public totalTokensForPresale = 5000000 * 10 ** uint256(decimals); // 5M tokens
    uint256 public tokensSoldDuringPresale;

    uint256 public tokenPrice; // Price per token during presale stages
    bool public presaleActive;

    // Token distribution percentages
    uint256 public teamPercentage = 10; // 10% for the team
    uint256 public marketingPercentage = 5; // 5% for marketing
    uint256 public stakingRewardsPercentage = 15; // 15% for staking rewards
    uint256 public publicSalePercentage = 70; // 70% for public sale

    // Staking variables
    struct Staker {
        uint256 amountStaked;
        uint256 stakingStartTime;
        bool isStaking;
    }
    mapping(address => Staker) public stakers;
    uint256 public annualStakingRewardRate = 10; // 10% annual reward rate

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event PresalePurchase(address indexed buyer, uint256 amount);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount, uint256 reward);

    // Modifier to check presale stage
    modifier onlyDuringPresale() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Constructor to initialize token supply
    constructor(uint256 _totalSupply) {
        totalSupply = _totalSupply * 10 ** uint256(decimals);
        balanceOf[address(this)] = totalSupply; // Assign all tokens to contract initially
    }

    // Function to start presale
    function startPresale(PresaleStage stage, uint256 pricePerToken) external {
        require(stage != PresaleStage.None, "Invalid presale stage");
        require(!presaleActive, "Presale already active");
        currentPresaleStage = stage;
        tokenPrice = pricePerToken;
        presaleActive = true;
    }

    // Function to end presale
    function endPresale() external {
        presaleActive = false;
        currentPresaleStage = PresaleStage.None;
    }

    // Function for presale token purchase
    function buyTokensDuringPresale(uint256 amount) external payable onlyDuringPresale {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value >= amount * tokenPrice, "Insufficient Ether sent");
        require(tokensSoldDuringPresale + amount <= totalTokensForPresale, "Exceeds presale allocation");

        balanceOf[msg.sender] += amount;
        balanceOf[address(this)] -= amount;
        tokensSoldDuringPresale += amount;

        emit PresalePurchase(msg.sender, amount);
    }

    // Function to transfer tokens
    function transfer(address to, uint256 value) external returns (bool) {
        require(to != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= value, "Insufficient balance");

        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;

        emit Transfer(msg.sender, to, value);
        return true;
    }

    // Function to approve tokens
    function approve(address spender, uint256 value) external returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    // Function to transfer from approved allowance
    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        require(to != address(0), "Invalid address");
        require(balanceOf[from] >= value, "Insufficient balance");
        require(allowance[from][msg.sender] >= value, "Allowance exceeded");

        balanceOf[from] -= value;
        balanceOf[to] += value;
        allowance[from][msg.sender] -= value;

        emit Transfer(from, to, value);
        return true;
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        balanceOf[msg.sender] -= amount;
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].stakingStartTime = block.timestamp;
        stakers[msg.sender].isStaking = true;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstakeTokens() external {
        require(stakers[msg.sender].isStaking, "Not currently staking");
        uint256 stakedAmount = stakers[msg.sender].amountStaked;
        uint256 stakingDuration = block.timestamp - stakers[msg.sender].stakingStartTime;
        uint256 reward = (stakedAmount * annualStakingRewardRate * stakingDuration / 365 days) / 100;

        stakers[msg.sender].amountStaked = 0;
        stakers[msg.sender].stakingStartTime = 0;
        stakers[msg.sender].isStaking = false;

        balanceOf[msg.sender] += stakedAmount + reward;

        emit Unstaked(msg.sender, stakedAmount, reward);
    }
}
```
