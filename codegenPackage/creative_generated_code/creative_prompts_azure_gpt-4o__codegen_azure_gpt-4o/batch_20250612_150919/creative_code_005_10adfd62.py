"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mazza.pages.dev
Prompt: Develop a smart contract in Solidity to enable staking on the Mazze blockchain, incorporating a 3X APR multiplier for early registrants.
Generated: DETERMINISTIC_10adfd625a4dcfac
Batch ID: 20250612_150919
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
 * @title StakingContract
 * @dev A smart contract for staking tokens on the Mazze blockchain with a 3X APR multiplier for early registrants.
 */
contract StakingContract {
    // Token-related declarations
    IERC20 public stakingToken;

    // APR-related constants
    uint256 public constant BASE_APR = 10; // Base APR (10% annual rate)
    uint256 public constant EARLY_MULTIPLIER = 3; // Early registrants get a 3X multiplier

    // Time-related constants
    uint256 public constant EARLY_REGISTRATION_PERIOD = 30 days; 
    uint256 public immutable deploymentTime;

    // User stakes
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 timestamp;     // Timestamp of staking
        bool isEarlyUser;      // Whether the user is an early registrant
    }

    // Mapping of user stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, bool isEarlyUser);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Modifier to check for zero address
    modifier nonZeroAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to initialize staking contract deployment time and staking token.
     * @param _stakingToken Token to be staked in this contract.
     */
    constructor(IERC20 _stakingToken) nonZeroAddress(address(_stakingToken)) {
        stakingToken = _stakingToken;
        deploymentTime = block.timestamp;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid staking amount");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Staking transfer failed");

        bool isEarlyUser = block.timestamp <= deploymentTime + EARLY_REGISTRATION_PERIOD;

        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + _amount, 
            timestamp: block.timestamp,
            isEarlyUser: isEarlyUser
        });

        emit Staked(msg.sender, _amount, isEarlyUser);
    }

    /**
     * @dev Allows users to withdraw their stake along with rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount found");

        // Calculate staking duration
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Calculate APR based on user type
        uint256 applicableAPR = userStake.isEarlyUser ? BASE_APR * EARLY_MULTIPLIER : BASE_APR;

        // Calculate reward (simplified reward formula)
        uint256 reward = (userStake.amount * applicableAPR * stakingDuration) / (365 days * 100);

        // Transfer staked amount and reward back to the user
        uint256 totalAmount = userStake.amount + reward;
        require(stakingToken.transfer(msg.sender, totalAmount), "Withdraw transfer failed");

        // Clear user's stake
        userStake.amount = 0;

        emit Withdrawn(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Fetches the staking details of a user.
     * @param _user Address of the user to fetch staking details.
     * @return Stake details including amount, timestamp, and early user status.
     */
    function getStakeDetails(address _user) external view returns (uint256, uint256, bool) {
        Stake storage userStake = stakes[_user];
        return (userStake.amount, userStake.timestamp, userStake.isEarlyUser);
    }
}

// Minimal IERC20 interface for token interactions
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
