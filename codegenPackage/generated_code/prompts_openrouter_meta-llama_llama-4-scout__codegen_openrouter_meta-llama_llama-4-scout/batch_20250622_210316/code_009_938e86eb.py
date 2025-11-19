"""
Generated Code Metadata:
========================
Original URL: https://web-tpad.pages.dev
Prompt: Write a Solidity contract for creating a token like TPAD, with features such as staking, rewards, and governance.
Generated: DETERMINISTIC_938e86eb208d17a5
Batch ID: 20250622_210316
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TPAD Token Contract
 * @author [Your Name]
 * @notice A token contract with staking, rewards, and governance features.
 */
contract TPADToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of reward distribution to stakers
    mapping(address => uint256) public rewards;

    // Total staked amount
    uint256 public totalStaked;

    // Staking reward rate (per block)
    uint256 public rewardRate;

    // Governance address
    address public governanceAddress;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when governance address is updated
    event GovernanceAddressUpdated(address indexed newAddress);

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 lastRewardedBlock;
    }

    /**
     * @dev Constructor for the TPAD token contract
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _initialSupply Initial supply of the token
     * @param _rewardRate Staking reward rate (per block)
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        uint256 _rewardRate
    ) ERC20(_name, _symbol) {
        _mint(msg.sender, _initialSupply);
        rewardRate = _rewardRate;
        governanceAddress = msg.sender;
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(_amount);
        stakers[msg.sender].lastRewardedBlock = block.number;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(_amount);

        // Update total staked amount
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens from contract to user
        _transfer(address(this), msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distribute rewards to stakers
     */
    function distributeRewards() public {
        // Calculate rewards for each staker
        for (address staker in stakers) {
            uint256 stakedAmount = stakers[staker].stakedAmount;
            uint256 blocksSinceLastReward = block.number.sub(stakers[staker].lastRewardedBlock);
            uint256 reward = stakedAmount.mul(rewardRate).mul(blocksSinceLastReward);

            // Update staker's rewards
            rewards[staker] = rewards[staker].add(reward);

            // Update staker's last rewarded block
            stakers[staker].lastRewardedBlock = block.number;

            emit RewardsDistributed(staker, reward);
        }
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() public {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards
        rewards[msg.sender] = 0;

        // Transfer rewards to user
        _transfer(address(this), msg.sender, reward);
    }

    /**
     * @dev Update governance address
     * @param _newAddress New governance address
     */
    function updateGovernanceAddress(address _newAddress) public {
        require(msg.sender == governanceAddress, "Only governance can update address");
        governanceAddress = _newAddress;

        emit GovernanceAddressUpdated(_newAddress);
    }

    /**
     * @dev Update reward rate
     * @param _newRate New reward rate (per block)
     */
    function updateRewardRate(uint256 _newRate) public {
        require(msg.sender == governanceAddress, "Only governance can update reward rate");
        rewardRate = _newRate;
    }
}
```
