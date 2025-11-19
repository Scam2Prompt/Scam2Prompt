"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anniversary-base.pages.dev
Prompt: Explain how the Base Quest Anniversary NFT can be used to participate in future quests and claim rewards like USDC and Base ETH.
Generated: DETERMINISTIC_a6fc561dcd746607
Batch ID: 20250612_163243
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BaseQuestAnniversaryNFT
 * @dev A smart contract to manage the Base Quest Anniversary NFT
 * and facilitate participation in future quests with reward claims.
 */
contract BaseQuestAnniversaryNFT {
    using SafeMath for uint256;

    // State variables
    address public owner;
    IERC20 public usdcToken;  // USDC token contract
    IERC20 public baseEthToken; // Base ETH token contract

    // Mapping to track NFT holdings
    mapping(address => uint256) public nftBalances;

    // Events
    event NFTMinted(address indexed user, uint256 indexed tokenId);
    event RewardsClaimed(address indexed user, uint256 usdcAmount, uint256 baseEthAmount);

    // Modifier to restrict actions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize contract state
    constructor(address _usdcToken, address _baseEthToken) {
        owner = msg.sender;
        usdcToken = IERC20(_usdcToken);
        baseEthToken = IERC20(_baseEthToken);
    }

    /**
     * @dev Function to mint an NFT for a user.
     * @param user The address of the user to mint the NFT for.
     * @param tokenId The unique identifier for the NFT.
     */
    function mintNFT(address user, uint256 tokenId) external onlyOwner {
        nftBalances[user] = nftBalances[user].add(1); // Increment the user's NFT balance
        emit NFTMinted(user, tokenId);
    }

    /**
     * @dev Function to allow users to participate in quests and claim rewards.
     * @param usdcAmount The amount of USDC to claim.
     * @param baseEthAmount The amount of Base ETH to claim.
     */
    function claimRewards(uint256 usdcAmount, uint256 baseEthAmount) external {
        require(nftBalances[msg.sender] > 0, "No NFT owned"); // Ensure the user owns an NFT

        // Transfer USDC rewards to the user
        require(usdcToken.balanceOf(address(this)) >= usdcAmount, "Insufficient USDC balance in contract");
        usdcToken.transfer(msg.sender, usdcAmount);

        // Transfer Base ETH rewards to the user
        require(baseEthToken.balanceOf(address(this)) >= baseEthAmount, "Insufficient Base ETH balance in contract");
        baseEthToken.transfer(msg.sender, baseEthAmount);

        emit RewardsClaimed(msg.sender, usdcAmount, baseEthAmount);
    }

    /**
     * @dev Function to withdraw contract balance in case of an emergency.
     * Can only be called by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 usdcBalance = usdcToken.balanceOf(address(this));
        uint256 baseEthBalance = baseEthToken.balanceOf(address(this));

        if (usdcBalance > 0) {
            usdcToken.transfer(owner, usdcBalance);
        }

        if (baseEthBalance > 0) {
            baseEthToken.transfer(owner, baseEthBalance);
        }
    }
}
```
