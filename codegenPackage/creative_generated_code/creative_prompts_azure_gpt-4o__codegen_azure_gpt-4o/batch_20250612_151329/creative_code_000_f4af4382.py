"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-shibashootout.pages.dev
Prompt: Write a smart contract in Solidity for staking $SHIBASHOOT tokens that visually represents rewards growing over time, similar to the 'Cactus Staking' concept described on the Shiba Shootout website.
Generated: DETERMINISTIC_f4af438206595fcb
Batch ID: 20250612_151329
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
 * @title ShibaShootStaking
 * @dev Smart contract for staking $SHIBASHOOT tokens and earning rewards over time.
 */
contract ShibaShootStaking {
    // ERC20 interface for $SHIBASHOOT token
    IERC20 public shibaShootToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;         // Staked amount
        uint256 reward;         // Accumulated reward
        uint256 lastUpdated;    // Timestamp of last update
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Annual percentage yield (APY) for staking rewards
    uint256 public constant APY = 10; // 10% annual return

    // Reward growth interval (in seconds)
    uint256 public constant REWARD_INTERVAL = 1 days;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of $SHIBASHOOT token contract.
     */
    constructor(address _token) {
        shibaShootToken = IERC20(_token);
        owner = msg.sender;
    }

    /**
     * @dev Stake $SHIBASHOOT tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards before modifying the stake
        updateReward(msg.sender);

        // Transfer tokens from the user to the contract
        require(shibaShootToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update rewards before modifying the stake
        updateReward(msg.sender);

        // Reduce staked amount
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the user
        require(shibaShootToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        updateReward(msg.sender);

        uint256 reward = stakes[msg.sender].reward;
        require(reward > 0, "No rewards to claim");

        // Reset reward balance
        stakes[msg.sender].reward = 0;

        // Transfer rewards to the user
        require(shibaShootToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function updateReward(address _user) internal {
        Stake storage stakeInfo = stakes[_user];

        if (stakeInfo.amount > 0) {
            // Calculate time passed since last update
            uint256 timeElapsed = block.timestamp - stakeInfo.lastUpdated;

            // Calculate rewards based on APY and time elapsed
            uint256 reward = (stakeInfo.amount * APY * timeElapsed) / (365 days * 100);

            // Update reward balance and last updated timestamp
            stakeInfo.reward += reward;
            stakeInfo.lastUpdated = block.timestamp;
        }
    }

    /**
     * @dev Retrieve staking details for a user.
     * @param _user Address of the user.
     * @return amount Staked amount.
     * @return reward Accumulated reward.
     * @return lastUpdated Timestamp of last update.
     */
    function getStakeInfo(address _user)
        external
        view
        returns (uint256 amount, uint256 reward, uint256 lastUpdated)
    {
        Stake memory stakeInfo = stakes[_user];
        return (stakeInfo.amount, stakeInfo.reward, stakeInfo.lastUpdated);
    }

    /**
     * @dev Allow the owner to recover ERC20 tokens accidentally sent to this contract.
     * @param _token Address of the ERC20 token.
     * @param _amount Amount of tokens to recover.
     */
    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        require(IERC20(_token).transfer(owner, _amount), "Token recovery failed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);

    function transfer(address to, uint256 amount) external returns (bool);
}
```
