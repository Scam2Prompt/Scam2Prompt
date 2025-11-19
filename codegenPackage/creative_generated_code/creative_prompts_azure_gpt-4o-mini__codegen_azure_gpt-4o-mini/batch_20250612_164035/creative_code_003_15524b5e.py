"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doglibretoken.web.app
Prompt: Develop a smart contract for a staking mechanism that allows users to stake their $DOGL tokens and earn rewards, referencing DogLibre's tokenomics.
Generated: DETERMINISTIC_15524b5e0318dc0e
Batch ID: 20250612_164035
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

// Importing the interface for the ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $DOGL tokens
contract DogLibreStaking is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 timestamp;    // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // The ERC20 token that users will stake
    IERC20 public doglToken;
    // Reward rate per second (in wei)
    uint256 public rewardRate;
    // Total rewards distributed
    uint256 public totalRewards;

    // Constructor to initialize the token and reward rate
    constructor(IERC20 _doglToken, uint256 _rewardRate) {
        doglToken = _doglToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");
        require(doglToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        
        // Transfer tokens from user to contract
        doglToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens along with rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer staked tokens back to the user
        uint256 amountToReturn = userStake.amount;
        userStake.amount = 0; // Resetting user's stake

        // Transfer rewards
        totalRewards -= rewards; // Deduct from total rewards pool
        doglToken.transfer(msg.sender, amountToReturn + rewards);

        emit Unstaked(msg.sender, amountToReturn);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) return 0;
        
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        return (stakingDuration * rewardRate * userStake.amount) / 1e18; // Assuming rewardRate is in wei
    }

    // Function to adjust the reward rate (onlyOwner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to withdraw any ERC20 tokens accidentally sent to this contract (onlyOwner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != doglToken, "Cannot withdraw staked token");
        token.transfer(msg.sender, amount);
    }

    // Function to withdraw any ETH accidentally sent to this contract (onlyOwner)
    function withdrawEther(uint256 amount) external onlyOwner {
        payable(owner()).transfer(amount);
    }

    // Receive function to accept ETH
    receive() external payable {}
}
```
