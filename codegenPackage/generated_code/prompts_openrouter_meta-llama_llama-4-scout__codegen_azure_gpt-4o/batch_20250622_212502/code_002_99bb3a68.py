"""
Generated Code Metadata:
========================
Original URL: https://defiprot.pages.dev
Prompt: Generate a code example for a whitelist/presale process in a DeFi protocol, using a blockchain-based platform and incorporating features like claim reward and claim airdrop.
Generated: DETERMINISTIC_99bb3a68251f616f
Batch ID: 20250622_212502
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
 * @title WhitelistPresale
 * @dev A contract for managing a whitelist-based presale process in a DeFi protocol.
 * Includes functionality for claiming rewards and airdrops.
 */
contract WhitelistPresale {
    // Owner of the contract
    address public owner;

    // Token address for rewards and airdrops
    address public rewardToken;

    // Presale start and end timestamps
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Mapping to track whitelisted addresses
    mapping(address => bool) public whitelist;

    // Mapping to track claimed rewards
    mapping(address => bool) public rewardClaimed;

    // Mapping to track claimed airdrops
    mapping(address => bool) public airdropClaimed;

    // Events
    event Whitelisted(address indexed user);
    event RewardClaimed(address indexed user, uint256 amount);
    event AirdropClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Modifier to check if presale is active
    modifier presaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _rewardToken, uint256 _presaleStart, uint256 _presaleEnd) {
        require(_rewardToken != address(0), "Invalid token address");
        require(_presaleStart < _presaleEnd, "Invalid presale period");

        owner = msg.sender;
        rewardToken = _rewardToken;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
    }

    /**
     * @dev Add an address to the whitelist.
     * @param _user Address to be whitelisted.
     */
    function addToWhitelist(address _user) external onlyOwner {
        require(_user != address(0), "Invalid address");
        require(!whitelist[_user], "Already whitelisted");

        whitelist[_user] = true;
        emit Whitelisted(_user);
    }

    /**
     * @dev Claim reward during the presale.
     */
    function claimReward() external presaleActive {
        require(whitelist[msg.sender], "Not whitelisted");
        require(!rewardClaimed[msg.sender], "Reward already claimed");

        uint256 rewardAmount = calculateReward(msg.sender);
        rewardClaimed[msg.sender] = true;

        // Transfer reward tokens to the user
        require(ERC20(rewardToken).transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Claim airdrop after the presale ends.
     */
    function claimAirdrop() external {
        require(block.timestamp > presaleEnd, "Airdrop not available yet");
        require(whitelist[msg.sender], "Not whitelisted");
        require(!airdropClaimed[msg.sender], "Airdrop already claimed");

        uint256 airdropAmount = calculateAirdrop(msg.sender);
        airdropClaimed[msg.sender] = true;

        // Transfer airdrop tokens to the user
        require(ERC20(rewardToken).transfer(msg.sender, airdropAmount), "Airdrop transfer failed");

        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    /**
     * @dev Calculate reward amount for a user.
     * @param _user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address _user) internal view returns (uint256) {
        // Example logic for reward calculation
        return 100 * 10**18; // Fixed reward of 100 tokens
    }

    /**
     * @dev Calculate airdrop amount for a user.
     * @param _user Address of the user.
     * @return Airdrop amount.
     */
    function calculateAirdrop(address _user) internal view returns (uint256) {
        // Example logic for airdrop calculation
        return 50 * 10**18; // Fixed airdrop of 50 tokens
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(ERC20(_token).transfer(owner, _amount), "Withdraw failed");
    }
}

// Interface for ERC20 token
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
