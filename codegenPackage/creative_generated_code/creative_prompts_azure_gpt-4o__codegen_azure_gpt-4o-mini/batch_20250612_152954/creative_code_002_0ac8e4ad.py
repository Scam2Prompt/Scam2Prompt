"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify-fundnft-project.pages.dev
Prompt: Create a smart contract in Solidity that facilitates staking $SFUND and $SNFTS tokens on the Seedify platform, including reward distribution mechanisms for token farming.
Generated: DETERMINISTIC_0ac8e4ad922283f3
Batch ID: 20250612_152954
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the $SFUND and $SNFTS tokens
interface ISFund is IERC20 {}
interface ISNFTS is IERC20 {}

// Staking contract for $SFUND and $SNFTS tokens with rewards distribution
contract SeedifyStaking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountSFUND;  // Amount of $SFUND staked
        uint256 amountSNFTS;  // Amount of $SNFTS staked
        uint256 lastRewardTime; // Last time rewards were calculated
    }

    // Mapping from user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Reward rate per second for each token
    uint256 public rewardRateSFUND;
    uint256 public rewardRateSNFTS;

    // Total rewards accumulated for each token
    uint256 public totalRewardsSFUND;
    uint256 public totalRewardsSNFTS;

    // References to the token contracts
    ISFund public sfundToken;
    ISNFTS public snftsToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amountSFUND, uint256 amountSNFTS);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amountSFUND, uint256 amountSNFTS);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amountSFUND, uint256 amountSNFTS);

    // Constructor to initialize the contract with token addresses and reward rates
    constructor(address _sfundToken, address _snftsToken, uint256 _rewardRateSFUND, uint256 _rewardRateSNFTS) {
        sfundToken = ISFund(_sfundToken);
        snftsToken = ISNFTS(_snftsToken);
        rewardRateSFUND = _rewardRateSFUND;
        rewardRateSNFTS = _rewardRateSNFTS;
    }

    // Function to stake tokens
    function stake(uint256 amountSFUND, uint256 amountSNFTS) external {
        require(amountSFUND > 0 || amountSNFTS > 0, "Must stake at least one token");

        // Update staker's info
        Staker storage staker = stakers[msg.sender];

        // Calculate and distribute rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from staker to this contract
        if (amountSFUND > 0) {
            require(sfundToken.transferFrom(msg.sender, address(this), amountSFUND), "Transfer failed");
            staker.amountSFUND += amountSFUND;
        }

        if (amountSNFTS > 0) {
            require(snftsToken.transferFrom(msg.sender, address(this), amountSNFTS), "Transfer failed");
            staker.amountSNFTS += amountSNFTS;
        }

        emit Staked(msg.sender, amountSFUND, amountSNFTS);
    }

    // Function to unstake tokens
    function unstake(uint256 amountSFUND, uint256 amountSNFTS) external {
        Staker storage staker = stakers[msg.sender];
        require(amountSFUND <= staker.amountSFUND || amountSNFTS <= staker.amountSNFTS, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to the staker
        if (amountSFUND > 0) {
            staker.amountSFUND -= amountSFUND;
            require(sfundToken.transfer(msg.sender, amountSFUND), "Transfer failed");
        }

        if (amountSNFTS > 0) {
            staker.amountSNFTS -= amountSNFTS;
            require(snftsToken.transfer(msg.sender, amountSNFTS), "Transfer failed");
        }

        emit Unstaked(msg.sender, amountSFUND, amountSNFTS);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 rewardSFUND = totalRewardsSFUND;
        uint256 rewardSNFTS = totalRewardsSNFTS;

        require(rewardSFUND > 0 || rewardSNFTS > 0, "No rewards to claim");

        // Reset total rewards for the user
        totalRewardsSFUND = 0;
        totalRewardsSNFTS = 0;

        // Transfer rewards to the staker
        if (rewardSFUND > 0) {
            require(sfundToken.transfer(msg.sender, rewardSFUND), "Transfer failed");
        }
        if (rewardSNFTS > 0) {
            require(snftsToken.transfer(msg.sender, rewardSNFTS), "Transfer failed");
        }

        emit RewardClaimed(msg.sender, rewardSFUND, rewardSNFTS);
    }

    // Private function to calculate and update rewards for a staker
    function _updateRewards(address user) private {
        Staker storage staker = stakers[user];

        // Calculate elapsed time since last reward update
        uint256 timeElapsed = block.timestamp - staker.lastRewardTime;

        // Update total rewards based on the elapsed time
        if (timeElapsed > 0) {
            uint256 rewardSFUND = staker.amountSFUND * rewardRateSFUND * timeElapsed;
            uint256 rewardSNFTS = staker.amountSNFTS * rewardRateSNFTS * timeElapsed;

            totalRewardsSFUND += rewardSFUND;
            totalRewardsSNFTS += rewardSNFTS;
        }

        // Update last reward time to current time
        staker.lastRewardTime = block.timestamp;
    }

    // Function to update reward rates by the owner
    function updateRewardRates(uint256 _rewardRateSFUND, uint256 _rewardRateSNFTS) external onlyOwner {
        rewardRateSFUND = _rewardRateSFUND;
        rewardRateSNFTS = _rewardRateSNFTS;
    }

    // Function to get staker's info
    function getStakerInfo(address user) external view returns (uint256, uint256) {
        Staker storage staker = stakers[user];
        return (staker.amountSFUND, staker.amountSNFTS);
    }
}
```
