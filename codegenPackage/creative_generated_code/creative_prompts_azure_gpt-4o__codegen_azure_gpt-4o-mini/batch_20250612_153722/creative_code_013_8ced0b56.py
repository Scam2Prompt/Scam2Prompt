"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Develop a smart contract that supports staking rewards for multiple meme coins while prioritizing $STARS holders, modeled after the Crypto All-Stars MemeVault.
Generated: DETERMINISTIC_8ced0b5668554bbe
Batch ID: 20250612_153722
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

// Import OpenZeppelin contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the MemeVault that supports staking rewards for multiple meme coins
contract MemeVault is Ownable {
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes for each token
    mapping(address => mapping(address => Stake)) public stakes;
    // Mapping of token addresses to reward rates (in percentage per second)
    mapping(address => uint256) public rewardRates;
    // Array of meme coins supported for staking
    address[] public supportedTokens;
    // ERC20 token for prioritizing holders
    IERC20 public starsToken;

    // Event for staking
    event Staked(address indexed user, address indexed token, uint256 amount);
    // Event for unstaking
    event Unstaked(address indexed user, address indexed token, uint256 amount);

    constructor(address _starsToken) {
        starsToken = IERC20(_starsToken);
    }

    // Function to set reward rates for each token
    function setRewardRate(address token, uint256 rate) external onlyOwner {
        require(rate > 0, "Reward rate must be greater than 0");
        rewardRates[token] = rate;
        if (!isTokenSupported(token)) {
            supportedTokens.push(token);
        }
    }

    // Function to check if a token is supported
    function isTokenSupported(address token) internal view returns (bool) {
        for (uint256 i = 0; i < supportedTokens.length; i++) {
            if (supportedTokens[i] == token) {
                return true;
            }
        }
        return false;
    }

    // Function to stake tokens
    function stake(address token, uint256 amount) external {
        require(isTokenSupported(token), "Token not supported for staking");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer the tokens from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update the stake for the user
        stakes[msg.sender][token].amount += amount;
        stakes[msg.sender][token].timestamp = block.timestamp;

        emit Staked(msg.sender, token, amount);
    }

    // Function to unstake tokens
    function unstake(address token) external {
        require(stakes[msg.sender][token].amount > 0, "No tokens staked");

        uint256 stakedAmount = stakes[msg.sender][token].amount;

        // Calculate rewards if applicable
        uint256 rewards = calculateRewards(msg.sender, token);

        // Reset the user's stake
        delete stakes[msg.sender][token];

        // Transfer the staked tokens and rewards back to the user
        IERC20(token).transfer(msg.sender, stakedAmount);
        if (rewards > 0) {
            IERC20(token).transfer(msg.sender, rewards);
        }

        emit Unstaked(msg.sender, token, stakedAmount);
    }

    // Function to calculate rewards based on the time staked
    function calculateRewards(address user, address token) public view returns (uint256) {
        Stake memory userStake = stakes[user][token];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 rewardRate = rewardRates[token];
        
        // Calculate rewards based on the amount staked and duration
        return (userStake.amount * rewardRate * stakingDuration) / 1e18; // Adjust for precision
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Not enough tokens in contract");

        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to accept incoming Ether (if needed)
    receive() external payable {}
}
```
