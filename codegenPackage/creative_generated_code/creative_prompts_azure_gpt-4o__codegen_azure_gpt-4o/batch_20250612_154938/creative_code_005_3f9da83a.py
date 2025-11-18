"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riarus.ru
Prompt: Create a smart contract in Solidity that interacts with Perpetual Protocol's staking mechanism to automate staking and reward distribution for PERP token holders.
Generated: DETERMINISTIC_3f9da83a2804e99a
Batch ID: 20250612_154938
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
 * @title Automated PERP Staking and Reward Distribution Contract
 * @dev This contract interacts with Perpetual Protocol's staking mechanism
 * to automate staking and reward distribution for PERP token holders.
 */
interface IPerpetualStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
    function balanceOf(address account) external view returns (uint256);
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AutomatedPERPStaking {
    // Address of the PERP token
    IERC20 public immutable perpToken;

    // Address of the Perpetual Protocol staking contract
    IPerpetualStaking public immutable stakingContract;

    // Owner of the contract
    address public owner;

    // Struct to track user deposits
    struct UserInfo {
        uint256 stakedAmount;
        uint256 pendingRewards;
    }

    // Mapping of user address to their staking info
    mapping(address => UserInfo) public userInfo;

    // Events
    event Stake(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    modifier onlyPositiveAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    constructor(address _perpToken, address _stakingContract) {
        require(_perpToken != address(0), "Invalid PERP token address");
        require(_stakingContract != address(0), "Invalid staking contract address");
        
        perpToken = IERC20(_perpToken);
        stakingContract = IPerpetualStaking(_stakingContract);
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake PERP tokens.
     * @param amount Amount of PERP tokens to stake.
     */
    function stake(uint256 amount) external onlyPositiveAmount(amount) {
        // Transfer PERP tokens from the user to this contract
        perpToken.transferFrom(msg.sender, address(this), amount);

        // Approve staking contract to spend the tokens
        perpToken.approve(address(stakingContract), amount);

        // Stake tokens in the Perpetual Protocol staking contract
        stakingContract.stake(amount);

        // Update user info
        userInfo[msg.sender].stakedAmount += amount;

        emit Stake(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw staked PERP tokens.
     * @param amount Amount of PERP tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyPositiveAmount(amount) {
        require(userInfo[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        // Withdraw tokens from the staking contract
        stakingContract.withdraw(amount);

        // Transfer tokens back to the user
        perpToken.transfer(msg.sender, amount);

        // Update user info
        userInfo[msg.sender].stakedAmount -= amount;

        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim staking rewards.
     */
    function claimRewards() external {
        // Claim rewards from the staking contract
        stakingContract.claimRewards();

        // Calculate the rewards available for the user
        uint256 rewards = perpToken.balanceOf(address(this)) - getTotalStaked();
        userInfo[msg.sender].pendingRewards += rewards;

        // Transfer claimed rewards to the user
        perpToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Returns the total amount of PERP tokens staked in the contract.
     */
    function getTotalStaked() public view returns (uint256) {
        return stakingContract.balanceOf(address(this));
    }

    /**
     * @dev Allows the contract owner to withdraw excess tokens (if any).
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).transfer(owner, amount);
    }
}
```
