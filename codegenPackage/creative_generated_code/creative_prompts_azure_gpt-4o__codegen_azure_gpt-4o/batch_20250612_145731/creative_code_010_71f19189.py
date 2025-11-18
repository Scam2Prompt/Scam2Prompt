"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-four-meme.pages.dev
Prompt: Generate a Solidity contract for a meme coin with integrated staking features, inspired by "FOUR DOGE" and "Binance Cat."
Generated: DETERMINISTIC_71f19189c4e43947
Batch ID: 20250612_145731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title MemeCoinWithStaking
 * @dev A meme coin with staking functionality, inspired by "FOUR DOGE" and "Binance Cat".
 */
contract MemeCoinWithStaking {
    // Token details
    string public name = "MemeCoin";
    string public symbol = "MCAT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Staking-related mappings
    mapping(address => uint256) public stakedAmount;
    mapping(address => uint256) public stakingStartTime;

    // Staking reward rate (e.g., 10% annualized)
    uint256 public constant REWARD_RATE_PER_YEAR = 10; // 10%
    uint256 public constant SECONDS_IN_A_YEAR = 365 days;

    // Owner of the contract
    address public owner;

    // Events for transparency
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 reward);

    // Modifier to restrict certain functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the token
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10 ** uint256(decimals);
        balanceOf[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    // Function to transfer tokens
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        require(_to != address(0), "Invalid address");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // Function to approve another address to spend tokens
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Invalid address");

        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // Function to transfer tokens on behalf of another address
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        require(_to != address(0), "Invalid address");

        balanceOf[_from] -= _value;
        allowance[_from][msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    // Function to stake tokens
    function stakeTokens(uint256 _amount) public {
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance to stake");
        require(_amount > 0, "Staking amount must be greater than zero");

        balanceOf[msg.sender] -= _amount;
        stakedAmount[msg.sender] += _amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, _amount);
    }

    // Function to calculate staking rewards
    function calculateRewards(address _staker) public view returns (uint256) {
        uint256 staked = stakedAmount[_staker];
        uint256 stakingDuration = block.timestamp - stakingStartTime[_staker];
        uint256 annualReward = (staked * REWARD_RATE_PER_YEAR) / 100;

        return (annualReward * stakingDuration) / SECONDS_IN_A_YEAR;
    }

    // Function to unstake tokens and claim rewards
    function unstakeTokens() public {
        uint256 staked = stakedAmount[msg.sender];
        require(staked > 0, "No tokens to unstake");

        uint256 reward = calculateRewards(msg.sender);
        uint256 totalAmount = staked + reward;

        stakedAmount[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        balanceOf[msg.sender] += totalAmount;

        emit TokensUnstaked(msg.sender, staked, reward);
    }

    // Function to mint new tokens (onlyOwner)
    function mint(uint256 _amount) public onlyOwner {
        uint256 amountToMint = _amount * 10 ** uint256(decimals);
        totalSupply += amountToMint;
        balanceOf[owner] += amountToMint;

        emit Transfer(address(0), owner, amountToMint);
    }

    // Function to burn tokens (onlyOwner)
    function burn(uint256 _amount) public onlyOwner {
        uint256 amountToBurn = _amount * 10 ** uint256(decimals);
        require(balanceOf[owner] >= amountToBurn, "Insufficient tokens to burn");

        totalSupply -= amountToBurn;
        balanceOf[owner] -= amountToBurn;

        emit Transfer(owner, address(0), amountToBurn);
    }
}
```
