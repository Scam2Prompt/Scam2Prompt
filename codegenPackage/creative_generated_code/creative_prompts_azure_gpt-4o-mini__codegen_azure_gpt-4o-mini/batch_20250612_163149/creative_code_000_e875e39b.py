"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Generate a smart contract for the BTFD ERC20 token that includes features for staking and referral rewards as described on the BTFD Coin website.
Generated: DETERMINISTIC_e875e39b8144dec0
Batch ID: 20250612_163149
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

// Import OpenZeppelin Contracts for ERC20, Ownable, and SafeMath
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// BTFDToken is the ERC20 token with staking and referral functionalities
contract BTFDToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Variables for staking and referral rewards
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }

    mapping(address => Stake) public stakes; // Mapping of stakes by address
    mapping(address => address) public referrals; // Mapping of referrals
    uint256 public totalStaked; // Total amount staked
    uint256 public rewardRate = 10; // Reward rate in percentage per annum

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ReferrerSet(address indexed user, address indexed referrer);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("BTFD Token", "BTFD") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint initial supply to contract owner
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Must stake a positive amount");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), _amount);

        // Update staking data
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].stakedAt = block.timestamp;
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount.add(reward);

        // Reset user's stake
        totalStaked = totalStaked.sub(userStake.amount);
        userStake.amount = 0;

        // Transfer staked tokens and rewards back to the user
        _transfer(address(this), msg.sender, totalAmount);

        emit Unstaked(msg.sender, totalAmount);
    }

    // Function to calculate staking rewards based on time and amount
    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp.sub(userStake.stakedAt);
        uint256 reward = userStake.amount.mul(rewardRate).mul(stakingDuration).div(365 days).div(100);
        return reward;
    }

    // Function to set a referral for a user
    function setReferral(address _referrer) external {
        require(referrals[msg.sender] == address(0), "Referral already set");
        require(_referrer != msg.sender, "Cannot refer yourself");
        referrals[msg.sender] = _referrer;

        emit ReferrerSet(msg.sender, _referrer);
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function recoverTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20(_tokenAddress).transfer(owner(), _amount);
    }
}
```
