"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spacex-airdrop-1f381.web.app
Prompt: Generate code to create a staking portal for $SpaceX tokens on the Binance Smart Chain network, including functionality to qualify users for vintage NFTs.
Generated: DETERMINISTIC_a72515f9bd04d5f2
Batch ID: 20250612_151624
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

// Importing required interfaces from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking contract for $SpaceX tokens
contract StakingPortal is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public spaceXToken;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when a user qualifies for NFT
    event QualifiedForNFT(address indexed user);

    // Minimum staking duration in seconds
    uint256 public constant MIN_STAKE_DURATION = 30 days;

    // Constructor to initialize the token
    constructor(address _spaceXToken) {
        require(_spaceXToken != address(0), "Invalid token address");
        spaceXToken = IERC20(_spaceXToken);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(spaceXToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");
        
        // Transfer tokens from user to contract
        spaceXToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= userStake.timestamp.add(MIN_STAKE_DURATION), "Stake is still locked");

        uint256 amountToWithdraw = userStake.amount;
        
        // Reset user's stake
        userStake.amount = 0;

        // Transfer tokens back to user
        spaceXToken.transfer(msg.sender, amountToWithdraw);

        emit Unstaked(msg.sender, amountToWithdraw);
    }

    // Function to check if the user qualifies for a vintage NFT
    function checkNFTQualification() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stakes found");

        // Check if the user qualifies (has staked for at least the minimum duration)
        require(block.timestamp >= userStake.timestamp.add(MIN_STAKE_DURATION), "Not qualified yet");

        emit QualifiedForNFT(msg.sender);
    }

    // Function to withdraw tokens in case of emergency (only owner can call)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(spaceXToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        // Transfer tokens to owner
        spaceXToken.transfer(msg.sender, _amount);
    }
}
```
