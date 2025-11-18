"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testai-qhn.pages.dev
Prompt: Implement an NFT-based reward boost mechanism in a staking smart contract for AITECH tokens, referencing the "NFT Boost" feature described on the Solidus AI Tech webpage.
Generated: DETERMINISTIC_87089bac3cf2392e
Batch ID: 20250612_152656
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
 * @title StakingContractWithNFTBoost
 * @dev This contract allows users to stake AITECH tokens and receive rewards.
 *      NFT holders receive bonus rewards based on their NFT Boost multiplier.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContractWithNFTBoost is Ownable {
    IERC20 public immutable aitechToken; // AITECH token contract
    IERC721 public immutable boostNFT; // The NFT contract providing reward boost

    uint256 public constant REWARD_RATE = 1 ether; // Reward rate per second
    uint256 public immutable BOOST_MULTIPLIER = 20; // Boost percentage for NFT holders (20%)

    struct Stake {
        uint256 stakedAmount;
        uint256 lastRewardCalculation;
        uint256 pendingRewards;
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _aitechToken, IERC721 _boostNFT) {
        require(address(_aitechToken) != address(0), "Invalid token address");
        require(address(_boostNFT) != address(0), "Invalid NFT address");

        aitechToken = _aitechToken;
        boostNFT = _boostNFT;
    }

    /**
     * @dev Modifier to ensure non-zero token amounts.
     * @param _amount The token amount being validated.
     */
    modifier nonZeroAmount(uint256 _amount) {
        require(_amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Stake AITECH tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonZeroAmount(_amount) {
        updateRewards(msg.sender);

        require(aitechToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakes[msg.sender].stakedAmount += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked AITECH tokens from the contract.
     */
    function withdraw() external {
        updateRewards(msg.sender);

        uint256 stakedAmount = stakes[msg.sender].stakedAmount;
        require(stakedAmount > 0, "No staked tokens to withdraw");

        stakes[msg.sender].stakedAmount = 0;
        require(aitechToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim pending rewards.
     */
    function claimRewards() external {
        updateRewards(msg.sender);

        uint256 rewards = stakes[msg.sender].pendingRewards;
        require(rewards > 0, "No rewards to claim");

        stakes[msg.sender].pendingRewards = 0;
        require(aitechToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate and update the user's rewards.
     *      If the user holds an NFT, apply the boost multiplier.
     * @param _user The address of the user.
     */
    function updateRewards(address _user) internal {
        Stake storage stakeData = stakes[_user];

        if (stakeData.stakedAmount == 0) {
            return;
        }

        uint256 timeElapsed = block.timestamp - stakeData.lastRewardCalculation;
        uint256 baseRewards = timeElapsed * stakeData.stakedAmount * REWARD_RATE / 1 ether;

        bool hasNFT = boostNFT.balanceOf(_user) > 0;
        uint256 finalRewards = hasNFT ? baseRewards + (baseRewards * BOOST_MULTIPLIER / 100) : baseRewards;

        stakeData.pendingRewards += finalRewards;
        stakeData.lastRewardCalculation = block.timestamp;
    }

    /**
     * @dev Allows the owner to withdraw tokens accidentally sent to the contract.
     * @param _token Address of the token contract.
     * @param _amount Number of tokens to withdraw.
     */
    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        require(IERC20(_token).transfer(owner(), _amount), "Token transfer failed");
    }
}
```
