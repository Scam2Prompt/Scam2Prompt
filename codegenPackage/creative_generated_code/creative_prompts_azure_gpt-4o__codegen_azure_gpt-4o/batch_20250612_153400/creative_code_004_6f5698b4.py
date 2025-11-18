"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://revolt-cultdaoio-migrate.vercel.app
Prompt: Develop a smart contract function to opt-in as a CULTmander and manage RVLT staking rewards with an APR of 6.31%.
Generated: DETERMINISTIC_6f5698b492c645fd
Batch ID: 20250612_153400
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
 * @title CULTmander Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to opt-in as a CULTmander and manage RVLT staking rewards
 * @dev APR is fixed at 6.31%. Ensure sufficient RVLT tokens are approved before staking.
 */
contract CULTmanderStaking {
    // State variables
    address public owner; // Address of the contract owner
    uint256 public constant APR = 631; // APR represented in basis points (6.31%)
    uint256 public constant BASIS_POINTS = 10000; // Basis points for APR calculations

    struct Stake {
        uint256 amount; // Amount of RVLT tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 rewardDebt; // Accumulated rewards owed to the staker
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stake details

    IERC20 public rvltToken; // Instance of the RVLT ERC20 token

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards, uint256 timestamp);

    /**
     * @dev Modifier to restrict access to contract owner only
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "CULTmanderStaking: Only owner can call this");
        _;
    }

    /**
     * @dev Constructor to set the RVLT token address and contract owner
     * @param _rvltToken Address of the RVLT ERC20 token
     */
    constructor(IERC20 _rvltToken) {
        rvltToken = _rvltToken;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake RVLT tokens and opt-in as a CULTmander
     * @param _amount Amount of RVLT tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "CULTmanderStaking: Cannot stake zero tokens");
        require(rvltToken.transferFrom(msg.sender, address(this), _amount), "CULTmanderStaking: Token transfer failed");

        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            // Calculate and update reward debt for previous stake before adding new amount
            userStake.rewardDebt += calculateRewards(msg.sender);
        }

        // Update stake details
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows users to unstake their RVLT tokens and claim rewards
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "CULTmanderStaking: No active stake found");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender) + userStake.rewardDebt;

        // Transfer staked tokens and rewards back to the user
        uint256 stakedAmount = userStake.amount;
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        require(rvltToken.transfer(msg.sender, stakedAmount + rewards), "CULTmanderStaking: Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, rewards, block.timestamp);
    }

    /**
     * @dev Calculates the staking rewards for a given user
     * @param _user Address of the user
     * @return Rewards amount based on staking duration and APR
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 annualRewards = (userStake.amount * APR) / BASIS_POINTS;

        // Calculate rewards proportional to staking duration (in seconds)
        return (annualRewards * stakingDuration) / (365 days);
    }

    /**
     * @dev Emergency function to allow the owner to withdraw tokens in case of unexpected issues
     * @param _amount Amount of RVLT tokens to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(rvltToken.transfer(owner, _amount), "CULTmanderStaking: Emergency withdrawal failed");
    }
}

/**
 * @dev Interface for the ERC20 token standard
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
