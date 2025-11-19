"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koalamemecoin.pages.dev
Prompt: Generate a code snippet for a smart contract that includes tokenomics similar to KoalaKash, including presale and staking rewards.
Generated: DETERMINISTIC_b33c7edaafca188e
Batch ID: 20250612_160946
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
 * @title KoalaKashToken
 * @dev Smart contract implementing tokenomics with presale and staking rewards.
 */
contract KoalaKashToken {
    // Token details
    string public name = "KoalaKash";
    string public symbol = "KKASH";
    uint8 public decimals = 18;
    uint256 public totalSupply = 10_000_000 * 10**decimals;

    // Balances mapping
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Presale variables
    address public owner;
    uint256 public presaleRate = 1000; // Tokens per ETH
    uint256 public presaleCap = 2_000_000 * 10**decimals;
    uint256 public presaleSold = 0;

    // Staking variables
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    mapping(address => Stake) public stakes;
    uint256 public stakingRewardRate = 10; // 10% annual rate
    uint256 public stakingLockPeriod = 30 days;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 ethSpent);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier hasSufficientBalance(address _account, uint256 _amount) {
        require(balanceOf[_account] >= _amount, "Insufficient balance");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
        balanceOf[owner] = totalSupply;
    }

    // ERC20 transfer function
    function transfer(address _to, uint256 _amount) public hasSufficientBalance(msg.sender, _amount) returns (bool success) {
        balanceOf[msg.sender] -= _amount;
        balanceOf[_to] += _amount;
        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    // ERC20 approve function
    function approve(address _spender, uint256 _amount) public returns (bool success) {
        allowance[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    // ERC20 transferFrom function
    function transferFrom(address _from, address _to, uint256 _amount) public hasSufficientBalance(_from, _amount) returns (bool success) {
        require(allowance[_from][msg.sender] >= _amount, "Allowance exceeded");
        balanceOf[_from] -= _amount;
        balanceOf[_to] += _amount;
        allowance[_from][msg.sender] -= _amount;
        emit Transfer(_from, _to, _amount);
        return true;
    }

    // Presale purchase function
    function buyTokens() public payable {
        require(presaleSold < presaleCap, "Presale cap reached");
        uint256 tokensToBuy = msg.value * presaleRate;
        require(presaleSold + tokensToBuy <= presaleCap, "Exceeds presale cap");

        balanceOf[msg.sender] += tokensToBuy;
        balanceOf[owner] -= tokensToBuy;
        presaleSold += tokensToBuy;

        emit TokensPurchased(msg.sender, tokensToBuy, msg.value);
    }

    // Stake tokens
    function stakeTokens(uint256 _amount) public hasSufficientBalance(msg.sender, _amount) {
        balanceOf[msg.sender] -= _amount;
        stakes[msg.sender] = Stake({
            amount: _amount,
            timestamp: block.timestamp
        });

        emit TokensStaked(msg.sender, _amount);
    }

    // Unstake tokens and claim rewards
    function unstakeTokens() public {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= userStake.timestamp + stakingLockPeriod, "Stake lock period not reached");

        uint256 reward = (userStake.amount * stakingRewardRate * (block.timestamp - userStake.timestamp)) / (365 days * 100);
        uint256 totalAmount = userStake.amount + reward;

        balanceOf[msg.sender] += totalAmount;
        stakes[msg.sender] = Stake({amount: 0, timestamp: 0});

        emit TokensUnstaked(msg.sender, userStake.amount, reward);
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Withdraw ETH from contract
    function withdrawETH(uint256 _amount) public onlyOwner {
        require(address(this).balance >= _amount, "Insufficient contract balance");
        payable(msg.sender).transfer(_amount);
    }
}
```
