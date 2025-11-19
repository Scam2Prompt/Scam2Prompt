"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Write a smart contract on the Binance Smart Chain (BEP20) for the CRUDO token, including functions for token sale, staking, and reward distribution.
Generated: DETERMINISTIC_b47f1c7051bc2183
Batch ID: 20250622_212302
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
 * @title CRUDO Token Smart Contract
 * @dev Implements BEP20 token standard with token sale, staking, and reward distribution functionality.
 */
contract CRUDO {
    // Token details
    string public name = "CRUDO Token";
    string public symbol = "CRUDO";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals)); // 1 million tokens

    // Balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Staking details
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public stakingStartTime;
    uint256 public rewardRate = 10; // Reward rate in percentage per year

    // Token sale details
    uint256 public tokenPrice = 0.001 ether; // Price per token in BNB
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 reward);
    event TokensUnstaked(address indexed staker, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier hasEnoughBalance(address _from, uint256 _amount) {
        require(balanceOf[_from] >= _amount, "Insufficient balance");
        _;
    }

    modifier hasEnoughAllowance(address _spender, uint256 _amount) {
        require(allowance[_spender][msg.sender] >= _amount, "Allowance exceeded");
        _;
    }

    constructor() {
        owner = msg.sender;
        balanceOf[owner] = totalSupply; // Assign all tokens to the owner initially
    }

    // BEP20 Transfer function
    function transfer(address _to, uint256 _amount) public hasEnoughBalance(msg.sender, _amount) returns (bool) {
        balanceOf[msg.sender] -= _amount;
        balanceOf[_to] += _amount;
        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    // BEP20 Approve function
    function approve(address _spender, uint256 _amount) public returns (bool) {
        allowance[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    // BEP20 TransferFrom function
    function transferFrom(address _from, address _to, uint256 _amount)
        public
        hasEnoughBalance(_from, _amount)
        hasEnoughAllowance(_from, _amount)
        returns (bool)
    {
        balanceOf[_from] -= _amount;
        balanceOf[_to] += _amount;
        allowance[_from][msg.sender] -= _amount;
        emit Transfer(_from, _to, _amount);
        return true;
    }

    // Token sale function
    function buyTokens(uint256 _amount) public payable {
        require(msg.value == _amount * tokenPrice, "Incorrect BNB value sent");
        require(balanceOf[owner] >= _amount, "Not enough tokens available for sale");

        balanceOf[owner] -= _amount;
        balanceOf[msg.sender] += _amount;
        emit TokensPurchased(msg.sender, _amount);
    }

    // Staking function
    function stakeTokens(uint256 _amount) public hasEnoughBalance(msg.sender, _amount) {
        balanceOf[msg.sender] -= _amount;
        stakedBalance[msg.sender] += _amount;
        stakingStartTime[msg.sender] = block.timestamp;
        emit TokensStaked(msg.sender, _amount);
    }

    // Calculate staking rewards
    function calculateRewards(address _staker) public view returns (uint256) {
        uint256 stakingDuration = block.timestamp - stakingStartTime[_staker];
        uint256 reward = (stakedBalance[_staker] * rewardRate * stakingDuration) / (365 days * 100);
        return reward;
    }

    // Claim staking rewards
    function claimRewards() public {
        uint256 reward = calculateRewards(msg.sender);
        require(balanceOf[owner] >= reward, "Not enough tokens for rewards");

        stakingStartTime[msg.sender] = block.timestamp; // Reset staking start time
        balanceOf[owner] -= reward;
        balanceOf[msg.sender] += reward;
        emit RewardsClaimed(msg.sender, reward);
    }

    // Unstake tokens
    function unstakeTokens() public {
        uint256 stakedAmount = stakedBalance[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        uint256 reward = calculateRewards(msg.sender);
        require(balanceOf[owner] >= reward, "Not enough tokens for rewards");

        stakingStartTime[msg.sender] = 0;
        stakedBalance[msg.sender] = 0;

        balanceOf[owner] -= reward;
        balanceOf[msg.sender] += reward + stakedAmount;
        emit RewardsClaimed(msg.sender, reward);
        emit TokensUnstaked(msg.sender, stakedAmount);
    }

    // Withdraw BNB from contract (only owner)
    function withdrawBNB(uint256 _amount) public onlyOwner {
        require(address(this).balance >= _amount, "Insufficient BNB balance");
        payable(owner).transfer(_amount);
    }

    // Fallback function to accept BNB
    receive() external payable {}
}
```
