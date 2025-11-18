"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogodoges.pages.dev
Prompt: Write a smart contract in Solidity for an ERC-20 token similar to $DOGO, including features for staking and governance as described in the Dogodoge ecosystem.
Generated: DETERMINISTIC_f7f09a60c420b2fa
Batch ID: 20250612_153648
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
 * @title ERC-20 Token with Staking and Governance
 * @dev Implements an ERC-20 token with staking functionality and governance features
 */
contract DogoToken {
    // ERC-20 standard variables
    string public name = "DogoToken";
    string public symbol = "DOGO";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for token balances
    mapping(address => uint256) public balances;

    // Mapping for allowances
    mapping(address => mapping(address => uint256)) public allowances;

    // Governance variables
    mapping(address => uint256) public votingPower;

    // Staking variables
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public stakingStartTime;
    uint256 public stakingRewardRate = 10; // Reward rate in percentage

    // Events for ERC-20 functionality
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Events for staking functionality
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount, uint256 reward);

    // Governance events
    event VotingPowerChanged(address indexed voter, uint256 newVotingPower);

    // Modifier to ensure valid address
    modifier validAddress(address addr) {
        require(addr != address(0), "Invalid address");
        _;
    }

    // Constructor to initialize total supply
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // ERC-20 transfer function
    function transfer(address _to, uint256 _amount)
        external
        validAddress(_to)
        returns (bool)
    {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] -= _amount;
        balances[_to] += _amount;
        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    // ERC-20 approve function
    function approve(address _spender, uint256 _amount)
        external
        validAddress(_spender)
        returns (bool)
    {
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    // ERC-20 transferFrom function
    function transferFrom(
        address _from,
        address _to,
        uint256 _amount
    ) external validAddress(_to) returns (bool) {
        require(allowances[_from][msg.sender] >= _amount, "Allowance exceeded");
        require(balances[_from] >= _amount, "Insufficient balance");

        allowances[_from][msg.sender] -= _amount;
        balances[_from] -= _amount;
        balances[_to] += _amount;

        emit Transfer(_from, _to, _amount);
        return true;
    }

    // ERC-20 balanceOf function
    function balanceOf(address _owner) external view returns (uint256) {
        return balances[_owner];
    }

    // ERC-20 allowance function
    function allowance(address _owner, address _spender)
        external
        view
        returns (uint256)
    {
        return allowances[_owner][_spender];
    }

    // Stake tokens to earn rewards
    function stake(uint256 _amount) external {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] -= _amount;
        stakedBalances[msg.sender] += _amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens and claim rewards
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked balance");

        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 reward = (stakedAmount * stakingRewardRate * stakingDuration) /
            (100 * 365 * 24 * 60 * 60); // Annualized rewards

        stakedBalances[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        balances[msg.sender] += stakedAmount + reward;

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    // Adjust voting power based on staked balance
    function adjustVotingPower(address _voter) external {
        uint256 stakedAmount = stakedBalances[_voter];
        votingPower[_voter] = stakedAmount / (10 ** decimals);
        emit VotingPowerChanged(_voter, votingPower[_voter]);
    }

    // Get voting power of an address
    function getVotingPower(address _voter) external view returns (uint256) {
        return votingPower[_voter];
    }
}
```
