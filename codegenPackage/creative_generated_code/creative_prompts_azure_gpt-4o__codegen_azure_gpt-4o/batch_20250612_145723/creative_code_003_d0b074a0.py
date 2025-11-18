"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-pepecoin-io.pages.dev
Prompt: Write a Solidity smart contract for staking PepeCoin and earning BasedAI rewards. Include functionality for farming and bridging as described in the PepeOS staking application.
Generated: DETERMINISTIC_d0b074a009a42d4e
Batch ID: 20250612_145723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title PepeStake
 * @dev A staking smart contract for PepeCoin to earn BasedAI rewards, with farming and bridging functionality.
 */
contract PepeStake {
    // ERC20-compatible token interfaces for PepeCoin and BasedAI
    IERC20 public immutable pepeCoin;
    IERC20 public immutable basedAI;

    // Owner of the contract
    address public owner;

    // Staking data structure
    struct Stake {
        uint256 amount;
        uint256 timestamp; // Time when tokens were staked
    }

    // Mapping from user address to their staking details
    mapping(address => Stake) public stakes;

    // Reward rate (e.g., 100 BasedAI tokens per staked PepeCoin per second)
    uint256 public immutable rewardRate;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event Unstaked(address indexed user, uint256 amount);
    event BridgeActivated(address indexed user, uint256 amount);

    /**
     * @dev Sets the PepeCoin and BasedAI token addresses and the reward rate. Sets the contract deployer as the owner.
     * @param _pepeCoin Address of the PepeCoin token contract
     * @param _basedAI Address of the BasedAI token contract
     * @param _rewardRate Reward rate for staking
     */
    constructor(
        address _pepeCoin,
        address _basedAI,
        uint256 _rewardRate
    ) {
        require(_pepeCoin != address(0), "Invalid PepeCoin address");
        require(_basedAI != address(0), "Invalid BasedAI address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        pepeCoin = IERC20(_pepeCoin);
        basedAI = IERC20(_basedAI);
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Stake PepeCoin tokens to earn BasedAI rewards.
     * @param amount Amount of PepeCoin tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer the PepeCoin tokens to the contract
        require(
            pepeCoin.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update the user's stake details
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            // Claim rewards for the previous stake
            uint256 rewards = calculateRewards(msg.sender);
            basedAI.transfer(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }

        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake PepeCoin tokens and claim any outstanding BasedAI rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards and transfer them to the user
        uint256 rewards = calculateRewards(msg.sender);
        basedAI.transfer(msg.sender, rewards);
        emit RewardsClaimed(msg.sender, rewards);

        // Return staked PepeCoin tokens to the user
        uint256 stakedAmount = userStake.amount;
        pepeCoin.transfer(msg.sender, stakedAmount);

        // Reset the user's stake
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Calculate the BasedAI rewards for a user based on their staked amount and staking duration.
     * @param user Address of the user
     * @return rewards Amount of BasedAI rewards earned
     */
    function calculateRewards(address user) public view returns (uint256 rewards) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        rewards = userStake.amount * stakingDuration * rewardRate;
    }

    /**
     * @dev Allow the owner to activate bridging functionality for a user.
     * Simulates bridging tokens to another blockchain.
     * @param user Address of the user
     * @param amount Amount of tokens to bridge
     */
    function activateBridge(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        // Simulate bridging by sending tokens to the user
        basedAI.transfer(user, amount);

        emit BridgeActivated(user, amount);
    }
}

/**
 * @dev ERC20 interface to interact with the PepeCoin and BasedAI tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
