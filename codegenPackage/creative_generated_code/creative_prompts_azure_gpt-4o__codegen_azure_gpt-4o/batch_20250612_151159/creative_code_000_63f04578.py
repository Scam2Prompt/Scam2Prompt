"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-wienerdog.pages.dev
Prompt: Write a smart contract in Solidity that mimics the tokenomics of WienerAI ($WAI), including presale allocation, staking rewards, and community rewards distribution.
Generated: DETERMINISTIC_63f045785716ec70
Batch ID: 20250612_151159
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
 * @title WienerAI ($WAI) Token Contract
 * @dev A token contract with presale allocation, staking rewards, and community rewards distribution.
 */
contract WienerAIToken {
    // ERC20-like variables
    string public name = "WienerAI";
    string public symbol = "WAI";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Token allocation
    uint256 public presaleAllocation;
    uint256 public stakingRewardsAllocation;
    uint256 public communityRewardsAllocation;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Staking data
    mapping(address => uint256) public stakingBalances;
    mapping(address => uint256) public stakingTimestamp;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event PresaleClaim(address indexed claimant, uint256 value);
    event Staked(address indexed staker, uint256 value);
    event RewardDistributed(address indexed recipient, uint256 value);

    // Owner address
    address public owner;

    // Error definitions
    error OnlyOwner();
    error InsufficientBalance();
    error InvalidAmount();

    // Constructor: initializes the contract
    constructor(
        uint256 _totalSupply,
        uint256 _presaleAllocation,
        uint256 _stakingRewardsAllocation,
        uint256 _communityRewardsAllocation
    ) {
        require(
            _totalSupply == _presaleAllocation + _stakingRewardsAllocation + _communityRewardsAllocation,
            "Total supply must match allocations"
        );

        owner = msg.sender;
        totalSupply = _totalSupply;
        presaleAllocation = _presaleAllocation;
        stakingRewardsAllocation = _stakingRewardsAllocation;
        communityRewardsAllocation = _communityRewardsAllocation;

        balances[owner] = _totalSupply;
    }

    /**
     * @dev Modifier to restrict functions to the owner.
     */
    modifier onlyOwner() {
        if (msg.sender != owner) {
            revert OnlyOwner();
        }
        _;
    }

    /**
     * @dev Transfer tokens between users.
     * @param to The address of the recipient.
     * @param value The amount of tokens to transfer.
     */
    function transfer(address to, uint256 value) external {
        if (balances[msg.sender] < value) {
            revert InsufficientBalance();
        }
        balances[msg.sender] -= value;
        balances[to] += value;
        emit Transfer(msg.sender, to, value);
    }

    /**
     * @dev Claim presale allocation tokens.
     * @param value The amount of tokens to claim.
     */
    function claimPresale(uint256 value) external {
        if (presaleAllocation < value) {
            revert InvalidAmount();
        }
        presaleAllocation -= value;
        balances[msg.sender] += value;
        emit PresaleClaim(msg.sender, value);
    }

    /**
     * @dev Stake tokens for rewards.
     * @param value The amount of tokens to stake.
     */
    function stake(uint256 value) external {
        if (balances[msg.sender] < value) {
            revert InsufficientBalance();
        }
        balances[msg.sender] -= value;
        stakingBalances[msg.sender] += value;
        stakingTimestamp[msg.sender] = block.timestamp;
        emit Staked(msg.sender, value);
    }

    /**
     * @dev Distribute rewards to stakers based on staking duration.
     */
    function distributeRewards() external onlyOwner {
        uint256 totalRewardsDistributed = 0;

        for (uint256 i = 0; i < stakingBalances.length; i++) {
            uint256 stakedAmount = stakingBalances[address(i)];
            uint256 stakingDuration = block.timestamp - stakingTimestamp[address(i)];
            
            // Calculate rewards based on a simple formula (e.g., 1% per day staked)
            uint256 reward = (stakedAmount * stakingDuration * 1) / (100 * 1 days);
            if (stakingRewardsAllocation >= reward) {
                stakingRewardsAllocation -= reward;
                balances[address(i)] += reward;
                totalRewardsDistributed += reward;
                emit RewardDistributed(address(i), reward);
            }
        }
    }

    /**
     * @dev Distribute community rewards to addresses in bulk.
     * @param recipients Array of recipient addresses.
     * @param values Array of reward values corresponding to recipients.
     */
    function distributeCommunityRewards(address[] calldata recipients, uint256[] calldata values) external onlyOwner {
        require(recipients.length == values.length, "Data length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            if (communityRewardsAllocation < values[i]) {
                revert InvalidAmount();
            }
            communityRewardsAllocation -= values[i];
            balances[recipients[i]] += values[i];
            emit RewardDistributed(recipients[i], values[i]);
        }
    }

    /**
     * @dev Get the balance of an address.
     * @param account The address to query.
     * @return The balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
