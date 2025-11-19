"""
Generated Code Metadata:
========================
Original URL: https://earnm-io.web.app
Prompt: "Generate a smart contract code for distributing $EARNM coins and Mystery Boxes to users based on their online activities, using a vesting and distribution mechanism."
Generated: DETERMINISTIC_06b0fde8d5b89321
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title EarnMDistributor
 * @dev Smart contract for distributing $EARNM tokens and Mystery Boxes based on user activities.
 * Implements a vesting mechanism for token distribution.
 */
contract EarnMDistributor {
    // Token interface
    IERC20 public earnMToken;

    // Owner of the contract
    address public owner;

    // Struct to store user distribution details
    struct Distribution {
        uint256 totalTokens; // Total tokens allocated
        uint256 claimedTokens; // Tokens already claimed
        uint256 startTime; // Vesting start time
        uint256 endTime; // Vesting end time
        bool mysteryBoxClaimed; // Whether the Mystery Box is claimed
    }

    // Mapping of user addresses to their distribution details
    mapping(address => Distribution) public distributions;

    // Events
    event TokensClaimed(address indexed user, uint256 amount);
    event MysteryBoxClaimed(address indexed user);
    event DistributionAdded(address indexed user, uint256 totalTokens, uint256 startTime, uint256 endTime);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _earnMToken Address of the $EARNM token contract.
     */
    constructor(address _earnMToken) {
        require(_earnMToken != address(0), "Invalid token address");
        earnMToken = IERC20(_earnMToken);
        owner = msg.sender;
    }

    /**
     * @dev Add a new distribution for a user.
     * @param _user Address of the user.
     * @param _totalTokens Total tokens allocated to the user.
     * @param _startTime Vesting start time.
     * @param _endTime Vesting end time.
     */
    function addDistribution(
        address _user,
        uint256 _totalTokens,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_totalTokens > 0, "Total tokens must be greater than zero");
        require(_startTime < _endTime, "Start time must be before end time");

        distributions[_user] = Distribution({
            totalTokens: _totalTokens,
            claimedTokens: 0,
            startTime: _startTime,
            endTime: _endTime,
            mysteryBoxClaimed: false
        });

        emit DistributionAdded(_user, _totalTokens, _startTime, _endTime);
    }

    /**
     * @dev Claim vested tokens.
     */
    function claimTokens() external {
        Distribution storage userDistribution = distributions[msg.sender];
        require(userDistribution.totalTokens > 0, "No distribution found");
        require(block.timestamp > userDistribution.startTime, "Vesting not started");

        uint256 vestedAmount = _calculateVestedAmount(userDistribution);
        uint256 claimableAmount = vestedAmount - userDistribution.claimedTokens;

        require(claimableAmount > 0, "No tokens available for claim");

        userDistribution.claimedTokens += claimableAmount;
        earnMToken.transfer(msg.sender, claimableAmount);

        emit TokensClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Claim the Mystery Box.
     */
    function claimMysteryBox() external {
        Distribution storage userDistribution = distributions[msg.sender];
        require(userDistribution.totalTokens > 0, "No distribution found");
        require(!userDistribution.mysteryBoxClaimed, "Mystery Box already claimed");

        userDistribution.mysteryBoxClaimed = true;

        emit MysteryBoxClaimed(msg.sender);
    }

    /**
     * @dev Calculate the vested amount of tokens for a user.
     * @param userDistribution Distribution details of the user.
     * @return Vested amount of tokens.
     */
    function _calculateVestedAmount(Distribution memory userDistribution) internal view returns (uint256) {
        if (block.timestamp >= userDistribution.endTime) {
            return userDistribution.totalTokens; // Fully vested
        } else {
            uint256 vestingDuration = userDistribution.endTime - userDistribution.startTime;
            uint256 timeElapsed = block.timestamp - userDistribution.startTime;
            return (userDistribution.totalTokens * timeElapsed) / vestingDuration;
        }
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        earnMToken.transfer(owner, _amount);
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
