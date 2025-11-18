"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://satoshivmsquad.army
Prompt: Create a smart contract in Solidity for staking tokens and distributing airdrops, inspired by the SatoshiVM Squad staking model.
Generated: DETERMINISTIC_72e24defdb3dad2e
Batch ID: 20250612_152526
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
 * @title Staking and Airdrop Contract
 * @dev This contract allows users to stake ERC20 tokens and receive rewards via airdrops.
 */
contract TokenStaking {
    // ERC20 token interface
    IERC20 public stakingToken;
    address public owner;

    // Struct to store staking details of each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 stakingStartTime; // Timestamp of staking start
    }

    // Mapping to track stakes for each user
    mapping(address => Stake) public stakes;
    // Total staked tokens across all users
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event AirdropDistributed(address indexed user, uint256 reward);

    // Modifier to restrict function calls to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the staking token and owner.
     * @param _stakingToken Address of the ERC20 token used for staking.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Transfer tokens from the sender to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update user's stake details
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].stakingStartTime = block.timestamp;

        // Update total staked tokens
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake their tokens.
     */
    function unstake() external {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens to unstake");

        // Reset stake details
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].stakingStartTime = 0;

        // Update total staked tokens
        totalStaked -= stakedAmount;

        // Transfer tokens back to the user
        require(
            stakingToken.transfer(msg.sender, stakedAmount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Distributes an airdrop reward to all stakers proportionally.
     * @param _airdropAmount Total amount of tokens to distribute as airdrop.
     */
    function distributeAirdrop(uint256 _airdropAmount) external onlyOwner {
        require(_airdropAmount > 0, "Airdrop amount must be greater than zero");
        require(totalStaked > 0, "No staked tokens to distribute rewards");

        // Transfer airdrop tokens to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _airdropAmount),
            "Token transfer failed"
        );

        // Distribute rewards proportionally to all stakers
        for (address staker in getAllStakers()) {
            uint256 reward = (_airdropAmount * stakes[staker].amount) /
                totalStaked;
            require(
                stakingToken.transfer(staker, reward),
                "Reward transfer failed"
            );
            emit AirdropDistributed(staker, reward);
        }
    }

    /**
     * @dev Helper function to get a list of all stakers.
     * @return An array of addresses representing all stakers.
     */
    function getAllStakers() public view returns (address[] memory) {
        // To be implemented: Logic for retrieving all staker addresses
    }
}

// ERC20 Interface
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
