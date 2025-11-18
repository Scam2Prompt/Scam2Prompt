"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenbursts.com
Prompt: Create a smart contract in Solidity that supports staking for $ETH, $BNB, and $POL, with functionality to calculate rewards based on Tokenbursts' APY values.
Generated: DETERMINISTIC_14c6025e4f0fd563
Batch ID: 20250612_152920
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

// Importing OpenZeppelin's Context and Ownable for ownership management
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// A smart contract for staking with reward calculation based on APY
contract Staking is Ownable {
    // Token interfaces for staking
    IERC20 public ethToken;
    IERC20 public bnbToken;
    IERC20 public polToken;

    // APY values for each token in basis points (i.e., 100 basis points = 1%)
    uint256 public ethAPY; // APY for ETH
    uint256 public bnbAPY; // APY for BNB
    uint256 public polAPY; // APY for POL

    // Staker's information
    struct Staker {
        uint256 amount; // Amount staked
        uint256 lastRewardTime; // Last time rewards were calculated
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount, address token);
    event Unstaked(address indexed user, uint256 amount, address token);
    event RewardsClaimed(address indexed user, uint256 reward, address token);

    // Constructor to set initial token addresses and APYs
    constructor(
        address _ethToken,
        address _bnbToken,
        address _polToken,
        uint256 _ethAPY,
        uint256 _bnbAPY,
        uint256 _polAPY
    ) {
        ethToken = IERC20(_ethToken);
        bnbToken = IERC20(_bnbToken);
        polToken = IERC20(_polToken);
        ethAPY = _ethAPY;
        bnbAPY = _bnbAPY;
        polAPY = _polAPY;
    }

    // Function to stake tokens
    function stake(uint256 amount, address token) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token == address(ethToken) || token == address(bnbToken) || token == address(polToken), "Invalid token");

        // Transfer tokens from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.lastRewardTime = block.timestamp;

        emit Staked(msg.sender, amount, token);
    }

    // Function to unstake tokens
    function unstake(uint256 amount, address token) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");
        require(token == address(ethToken) || token == address(bnbToken) || token == address(polToken), "Invalid token");

        // Calculate and transfer rewards before unstaking
        uint256 reward = calculateReward(msg.sender, token);
        if (reward > 0) {
            // Transfer rewards to the user
            IERC20(token).transfer(msg.sender, reward);
            emit RewardsClaimed(msg.sender, reward, token);
        }

        // Update staker information
        staker.amount -= amount;
        staker.lastRewardTime = block.timestamp;

        // Transfer the staked tokens back to the user
        IERC20(token).transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount, token);
    }

    // Function to calculate rewards based on time staked and APY
    function calculateReward(address stakerAddress, address token) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 stakedTime = block.timestamp - staker.lastRewardTime;

        // Compute the APY based on the token
        uint256 apy;
        if (token == address(ethToken)) {
            apy = ethAPY;
        } else if (token == address(bnbToken)) {
            apy = bnbAPY;
        } else {
            apy = polAPY;
        }

        // Calculate reward
        uint256 reward = (staker.amount * apy * stakedTime) / (365 days * 10000);
        return reward;
    }

    // Admin function to update APY values
    function updateAPY(uint256 _ethAPY, uint256 _bnbAPY, uint256 _polAPY) external onlyOwner {
        ethAPY = _ethAPY;
        bnbAPY = _bnbAPY;
        polAPY = _polAPY;
    }
}
```
