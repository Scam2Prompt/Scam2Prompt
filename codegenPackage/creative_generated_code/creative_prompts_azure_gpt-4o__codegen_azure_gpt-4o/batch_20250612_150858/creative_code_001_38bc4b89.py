"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealyi.github.io
Prompt: Generate Solidity code for a smart contract that allows users to stake ORB tokens on the Zealy platform and earn rewards in Ethereum and stablecoins.
Generated: DETERMINISTIC_38bc4b8943107539
Batch ID: 20250612_150858
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
 * @title ORB Staking Contract
 * @dev Allows users to stake ORB tokens on the Zealy platform and earn rewards in Ethereum and stablecoins.
 *      Rewards distribution and staking logic are implemented with security and best practices.
 */
contract ORBStaking {
    // ERC20 interface for interacting with stablecoins and the ORB token
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the ORB token contract
    IERC20 public immutable orbToken;

    // Address of the stablecoin reward token contract (example: USDC)
    IERC20 public immutable stablecoinReward;

    // Mapping to track staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping to track reward balances for each user
    mapping(address => uint256) public ethRewards; // Rewards in ETH
    mapping(address => uint256) public stablecoinRewards; // Rewards in stablecoins

    // Event declarations for logging key actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 ethAmount, uint256 stablecoinAmount);

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize token addresses and contract owner
    constructor(address _orbToken, address _stablecoinReward) {
        require(_orbToken != address(0), "Invalid ORB token address");
        require(_stablecoinReward != address(0), "Invalid stablecoin address");
        orbToken = IERC20(_orbToken);
        stablecoinReward = IERC20(_stablecoinReward);
        owner = msg.sender;
    }

    /**
     * @dev Stake ORB tokens in the contract.
     * @param amount Amount of ORB tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");

        // Transfer ORB tokens from the user to the contract
        bool success = orbToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake ORB tokens from the contract.
     * @param amount Amount of ORB tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstaking amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer ORB tokens back to the user
        bool success = orbToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards in ETH and stablecoins.
     */
    function claimRewards() external {
        uint256 ethReward = ethRewards[msg.sender];
        uint256 stablecoinRewardAmount = stablecoinRewards[msg.sender];

        require(ethReward > 0 || stablecoinRewardAmount > 0, "No rewards available");

        // Reset rewards
        ethRewards[msg.sender] = 0;
        stablecoinRewards[msg.sender] = 0;

        // Transfer ETH rewards
        if (ethReward > 0) {
            (bool sent, ) = msg.sender.call{value: ethReward}("");
            require(sent, "ETH transfer failed");
        }

        // Transfer stablecoin rewards
        if (stablecoinRewardAmount > 0) {
            bool success = stablecoinReward.transfer(msg.sender, stablecoinRewardAmount);
            require(success, "Stablecoin transfer failed");
        }

        emit RewardsClaimed(msg.sender, ethReward, stablecoinRewardAmount);
    }

    /**
     * @dev Distribute rewards to a user. Can only be called by the owner.
     * @param user Address of the user to distribute rewards to.
     * @param ethAmount Amount of ETH rewards.
     * @param stablecoinAmount Amount of stablecoin rewards.
     */
    function distributeRewards(address user, uint256 ethAmount, uint256 stablecoinAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(ethAmount > 0 || stablecoinAmount > 0, "Rewards must be greater than zero");

        ethRewards[user] += ethAmount;
        stablecoinRewards[user] += stablecoinAmount;
    }

    /**
     * @dev Withdraw ETH from the contract. Only owner can call this.
     * @param amount Amount of ETH to withdraw.
     */
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient ETH balance");

        (bool sent, ) = owner.call{value: amount}("");
        require(sent, "ETH transfer failed");
    }

    /**
     * @dev Withdraw stablecoins from the contract. Only owner can call this.
     * @param amount Amount of stablecoins to withdraw.
     */
    function withdrawStablecoins(uint256 amount) external onlyOwner {
        require(stablecoinReward.balanceOf(address(this)) >= amount, "Insufficient stablecoin balance");

        bool success = stablecoinReward.transfer(owner, amount);
        require(success, "Stablecoin transfer failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Function to receive plain ETH transfers
    fallback() external payable {}
}
```
