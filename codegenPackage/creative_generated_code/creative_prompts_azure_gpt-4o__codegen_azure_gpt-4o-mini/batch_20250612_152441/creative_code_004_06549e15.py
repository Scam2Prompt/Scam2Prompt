"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr2.pages.dev
Prompt: Create a smart contract for farming syASSET/ASSET LP tokens and earning SYNTH rewards, leveraging SYNTHR's liquidity provider benefits.
Generated: DETERMINISTIC_06549e1575c63478
Batch ID: 20250612_152441
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the SYNTH token
interface ISYNTH {
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
}

// Liquidity Farming Contract
contract FarmingContract is Ownable {
    using SafeMath for uint256;

    // Token addresses
    address public syAsset; // Address of the syASSET token
    address public asset; // Address of the ASSET token
    address public synth; // Address of the SYNTH token

    // LP Token structure
    struct UserInfo {
        uint256 amount; // Amount of LP tokens staked
        uint256 rewardDebt; // Reward debt
    }
    
    // Mapping of user addresses to their info
    mapping(address => UserInfo) public userInfo;

    // Total staked LP tokens
    uint256 public totalStaked;
    
    // Reward per block
    uint256 public rewardPerBlock;

    // Event for staking LP tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event for unstaking LP tokens
    event Unstaked(address indexed user, uint256 amount);
    
    // Event for claiming rewards
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _syAsset, address _asset, address _synth, uint256 _rewardPerBlock) {
        syAsset = _syAsset;
        asset = _asset;
        synth = _synth;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake LP tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer LP tokens from user to contract
        IERC20(syAsset).transferFrom(msg.sender, address(this), amount);
        
        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.amount = user.amount.add(amount);
        user.rewardDebt = user.rewardDebt.add(amount.mul(rewardPerBlock));
        
        // Update total staked
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake LP tokens
    function unstake(uint256 amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Insufficient staked amount");
        
        // Claim rewards before unstaking
        _claimRewards();

        // Update user info
        user.amount = user.amount.sub(amount);
        user.rewardDebt = user.rewardDebt.sub(amount.mul(rewardPerBlock));

        // Transfer LP tokens back to user
        IERC20(syAsset).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim SYNTH rewards
    function claimRewards() external {
        _claimRewards();
    }

    // Internal function to manage reward claiming
    function _claimRewards() internal {
        UserInfo storage user = userInfo[msg.sender];
        uint256 pendingRewards = user.rewardDebt;
        
        require(pendingRewards > 0, "No rewards to claim");

        // Reset user's reward debt
        user.rewardDebt = 0;

        // Mint SYNTH tokens to user
        ISYNTH(synth).mint(msg.sender, pendingRewards);

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    // Function to set reward per block (only owner)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to withdraw tokens in case of an emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        IERC20(syAsset).transfer(msg.sender, amount);
    }
}
```
