"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmnt.org
Prompt: Provide a smart contract example in Solidity for staking GMNTCoin that includes features like high APY rewards and daily profit generation, as described in the GMNT web3 staking platform.
Generated: DETERMINISTIC_083a095a8906d833
Batch ID: 20250612_151525
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
 * @title GMNTCoin Staking Contract
 * @dev This contract allows users to stake GMNT coins and earn rewards with high APY.
 * Rewards are calculated daily and distributed based on the staked amount.
 */
contract GMNTStaking {
    // Struct to keep track of each staker's information
    struct Staker {
        uint256 amountStaked;       // Amount of GMNT staked
        uint256 lastClaimedTime;    // Last time rewards were claimed
        uint256 unclaimedRewards;  // Rewards not yet claimed
    }

    // Mapping of staker's address to their staking information
    mapping(address => Staker) public stakers;

    // Address of the GMNT token contract (ERC20)
    address public gmntToken;

    // Annual Percentage Yield (APY) for staking (e.g., 20% APY -> set to 20)
    uint256 public apy;

    // Daily reward rate calculated based on the APY
    uint256 public dailyRewardRate;

    // Owner of the contract (for administrative functions)
    address public owner;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 amount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _gmntToken Address of the GMNT token contract
     * @param _apy Annual Percentage Yield for staking
     */
    constructor(address _gmntToken, uint256 _apy) {
        require(_gmntToken != address(0), "Invalid token address");
        require(_apy > 0, "APY must be greater than zero");

        gmntToken = _gmntToken;
        apy = _apy;
        dailyRewardRate = (_apy * 1e18) / 365; // Convert APY to daily reward rate in wei
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake GMNT tokens.
     * @param _amount Amount of GMNT tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer GMNT tokens from the user to the contract
        require(
            IERC20(gmntToken).transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking information
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        staker.amountStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake GMNT tokens and withdraw their staked amount.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        _updateRewards(msg.sender);

        uint256 amount = staker.amountStaked;
        staker.amountStaked = 0;

        // Transfer staked tokens back to the user
        require(
            IERC20(gmntToken).transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their staking rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        uint256 rewards = staker.unclaimedRewards;
        require(rewards > 0, "No rewards to claim");

        staker.unclaimedRewards = 0;

        // Transfer rewards to the user
        require(
            IERC20(gmntToken).transfer(msg.sender, rewards),
            "Token transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Updates the rewards for a staker based on their staked amount and time elapsed.
     * @param _staker Address of the staker
     */
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];

        if (staker.amountStaked > 0) {
            uint256 timeElapsed = block.timestamp - staker.lastClaimedTime;
            uint256 newRewards = (staker.amountStaked * dailyRewardRate * timeElapsed) / (1e18 * 1 days);

            staker.unclaimedRewards += newRewards;
        }

        staker.lastClaimedTime = block.timestamp;
    }

    /**
     * @dev Allows the contract owner to update the APY.
     * @param _newAPY New APY value
     */
    function updateAPY(uint256 _newAPY) external onlyOwner {
        require(_newAPY > 0, "APY must be greater than zero");

        apy = _newAPY;
        dailyRewardRate = (_newAPY * 1e18) / 365; // Update daily reward rate
    }
}

/**
 * @dev Minimal IERC20 interface for interacting with GMNT token.
 */
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
