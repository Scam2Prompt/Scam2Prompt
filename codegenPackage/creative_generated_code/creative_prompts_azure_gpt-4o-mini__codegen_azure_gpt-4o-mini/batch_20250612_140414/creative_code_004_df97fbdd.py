"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.nfts2.me
Prompt: How can I promote an NFT collection effectively while integrating a referral program that rewards users with ETH on the Arbitrum blockchain?
Generated: DETERMINISTIC_df97fbdd0ee0943a
Batch ID: 20250612_140414
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTCollection is ERC721, Ownable {
    // ERC20 token used for rewards (ETH in this case will be wrapped in WETH)
    IERC20 public rewardToken;
    
    // Mapping of NFT owners to their referral addresses
    mapping(address => address) public referrals;

    // Mapping to track rewards for each referrer
    mapping(address => uint256) public referralRewards;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    // Event emitted when a referral reward is claimed
    event ReferralRewardClaimed(address indexed referrer, uint256 amount);

    // Current token ID counter
    uint256 private _currentTokenId;

    constructor(string memory name, string memory symbol, address _rewardToken) 
        ERC721(name, symbol) {
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @notice Mint a new NFT and set a referral if provided
     * @param referrer The address of the referrer
     */
    function mintNFT(address referrer) external {
        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT to the caller
        _mint(msg.sender, _currentTokenId);
        
        // If a valid referrer is provided, set the referral
        if (referrer != address(0) && referrer != msg.sender) {
            referrals[msg.sender] = referrer;
            // Reward the referrer with a fixed amount (e.g., 0.1 WETH)
            uint256 rewardAmount = 0.1 ether; // Adjust based on your requirement
            referralRewards[referrer] += rewardAmount;
        }

        emit NFTMinted(msg.sender, _currentTokenId);
    }

    /**
     * @notice Claim referral rewards
     */
    function claimReferralReward() external {
        uint256 rewardAmount = referralRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the reward balance for this referrer
        referralRewards[msg.sender] = 0;

        // Transfer the reward to the referrer
        require(rewardToken.transfer(msg.sender, rewardAmount), "Transfer failed");
        
        emit ReferralRewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Set a new reward token
     * @param newRewardToken The address of the new reward token
     */
    function setRewardToken(address newRewardToken) external onlyOwner {
        rewardToken = IERC20(newRewardToken);
    }

    /**
     * @notice Withdraw any ERC20 tokens from the contract
     * @param token The address of the token to withdraw
     * @param amount The amount to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(msg.sender, amount), "Withdrawal failed");
    }
    
    // Override any additional functions as necessary
}
```
