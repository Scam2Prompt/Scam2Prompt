"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-claim.pages.dev
Prompt: Generate a Solidity smart contract for a token similar to $KANG, ensuring it includes features for staking and rewards as described in the Kangamoon documentation.
Generated: DETERMINISTIC_67390ea1dcc52fb2
Batch ID: 20250612_163848
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
 * @title KangToken
 * @dev A token contract with staking and reward functionality.
 */
contract KangToken {
    // ERC20 token properties
    string public name = "KangToken";
    string public symbol = "KANG";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) public balances;

    // Allowance mapping
    mapping(address => mapping(address => uint256)) public allowances;

    // Staking properties
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public stakingStartTimes;

    // Reward rate per second (e.g., 0.0001 tokens per second)
    uint256 public rewardRatePerSecond = 1e15; // 0.001 tokens per second

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 value);
    event Unstaked(address indexed staker, uint256 value);
    event RewardClaimed(address indexed staker, uint256 reward);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize token supply
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        balances[owner] = _initialSupply;
    }

    /**
     * @dev Transfers tokens from sender to recipient.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_value > 0, "Transfer value must be greater than zero");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);

        return true;
    }

    /**
     * @dev Approves spender to spend tokens on behalf of owner.
     * @param _spender Address of the spender.
     * @param _value Amount to be approved.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);

        return true;
    }

    /**
     * @dev Transfers tokens from one account to another using allowance.
     * @param _from Source address.
     * @param _to Destination address.
     * @param _value Amount to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(_value > 0, "Transfer value must be greater than zero");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);

        return true;
    }

    /**
     * @dev Stakes tokens to earn rewards.
     * @param _value Amount of tokens to stake.
     */
    function stake(uint256 _value) external {
        require(_value > 0, "Stake value must be greater than zero");
        require(balances[msg.sender] >= _value, "Insufficient balance to stake");

        // Transfer tokens to staking balance
        balances[msg.sender] -= _value;
        stakedBalances[msg.sender] += _value;
        
        // Record the staking start time
        stakingStartTimes[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _value);
    }

    /**
     * @dev Unstakes tokens and claims rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        uint256 stakingDuration = block.timestamp - stakingStartTimes[msg.sender];
        uint256 reward = stakingDuration * rewardRatePerSecond;

        // Update balances
        stakedBalances[msg.sender] = 0;
        stakingStartTimes[msg.sender] = 0;
        balances[msg.sender] += stakedAmount + reward;

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates reward for staker.
     * @param _staker Address of the staker.
     */
    function calculateReward(address _staker) external view returns (uint256) {
        uint256 stakingDuration = block.timestamp - stakingStartTimes[_staker];
        return stakingDuration * rewardRatePerSecond;
    }
}
```
