"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeskombat.pages.dev
Prompt: Develop a Solidity contract for distributing community rewards, ensuring that 10% of the $MK token supply is allocated fairly among active participants in Meme Kombat battles.
Generated: DETERMINISTIC_50ad4d94d0231b05
Batch ID: 20250612_152410
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
 * @title CommunityRewards
 * @dev This contract handles the distribution of 10% of the $MK token supply
 *      among active participants in Meme Kombat battles.
 */
contract CommunityRewards {
    // Address of the $MK token contract
    IERC20 public mkToken;

    // Total rewards allocated (10% of $MK token supply)
    uint256 public totalRewards;

    // Mapping to track active participants and their reward shares
    mapping(address => uint256) public rewards;

    // Owner of the contract
    address public owner;

    // Event to track reward distribution
    event RewardsDistributed(address indexed participant, uint256 rewardAmount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to certain functions to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _mkToken Address of the $MK token contract.
     * @param _totalSupply Total supply of the $MK token.
     */
    constructor(address _mkToken, uint256 _totalSupply) {
        require(_mkToken != address(0), "Invalid token address");
        mkToken = IERC20(_mkToken);
        totalRewards = (_totalSupply * 10) / 100; // Calculating 10% of token supply
        owner = msg.sender; // Assigning contract deployer as owner
    }

    /**
     * @dev Function to distribute rewards to active participants.
     * @param participants Array of participant addresses.
     * @param rewardShares Array of reward shares corresponding to participants.
     */
    function distributeRewards(address[] memory participants, uint256[] memory rewardShares)
        external
        onlyOwner
    {
        require(participants.length == rewardShares.length, "Invalid input lengths");

        uint256 totalDistributed = 0;

        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            uint256 reward = rewardShares[i];

            require(participant != address(0), "Invalid participant address");
            require(reward > 0, "Reward must be greater than zero");

            // Ensure sufficient rewards remain for distribution
            totalDistributed += reward;
            require(totalDistributed <= totalRewards, "Insufficient rewards");

            // Update rewards mapping and perform transfer
            rewards[participant] += reward;
            mkToken.transfer(participant, reward);

            emit RewardsDistributed(participant, reward);
        }

        // Deduct the distributed rewards from totalRewards
        totalRewards -= totalDistributed;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
