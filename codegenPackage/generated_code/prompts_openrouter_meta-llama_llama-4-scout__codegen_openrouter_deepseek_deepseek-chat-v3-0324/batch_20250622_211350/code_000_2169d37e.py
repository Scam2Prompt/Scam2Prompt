"""
Generated Code Metadata:
========================
Original URL: https://bankless.pages.dev
Prompt: Write a smart contract function in Solidity to redeem a Base, Introduced NFT for $BASED tokens on the Base blockchain, considering the redemption phases and token allocation.
Generated: DETERMINISTIC_2169d37e451b8d72
Batch ID: 20250622_211350
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract BasedNFTRedeemer is Ownable, ReentrancyGuard {
    IERC721 public nftContract;
    IERC20 public basedToken;

    // Redemption phases
    enum RedemptionPhase {
        NOT_ACTIVE,
        EARLY,
        GENERAL,
        COMPLETED
    }

    RedemptionPhase public currentPhase = RedemptionPhase.NOT_ACTIVE;

    // Token allocation per phase
    uint256 public constant EARLY_PHASE_ALLOCATION = 1000 * 10**18; // 1000 $BASED tokens
    uint256 public constant GENERAL_PHASE_ALLOCATION = 500 * 10**18; // 500 $BASED tokens

    // Track redeemed tokens
    mapping(uint256 => bool) public redeemedTokens;
    mapping(address => uint256) public earlyPhaseRedemptions;

    // Events
    event NFTReedemed(address indexed user, uint256 tokenId, uint256 amount);
    event PhaseChanged(RedemptionPhase newPhase);

    constructor(address _nftContract, address _basedToken) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        require(_basedToken != address(0), "Invalid token contract address");
        
        nftContract = IERC721(_nftContract);
        basedToken = IERC20(_basedToken);
    }

    /**
     * @dev Set the current redemption phase
     * @param _phase The new phase to set
     */
    function setRedemptionPhase(RedemptionPhase _phase) external onlyOwner {
        require(_phase != currentPhase, "Phase already set");
        require(
            _phase == RedemptionPhase.NOT_ACTIVE || 
            _phase == RedemptionPhase.EARLY || 
            _phase == RedemptionPhase.GENERAL || 
            _phase == RedemptionPhase.COMPLETED,
            "Invalid phase"
        );

        currentPhase = _phase;
        emit PhaseChanged(_phase);
    }

    /**
     * @dev Redeem NFT for $BASED tokens
     * @param tokenId The NFT token ID to redeem
     */
    function redeemNFT(uint256 tokenId) external nonReentrant {
        require(currentPhase != RedemptionPhase.NOT_ACTIVE, "Redemption not active");
        require(currentPhase != RedemptionPhase.COMPLETED, "Redemption completed");
        require(nftContract.ownerOf(tokenId) == msg.sender, "Not NFT owner");
        require(!redeemedTokens[tokenId], "NFT already redeemed");

        uint256 redemptionAmount;
        
        if (currentPhase == RedemptionPhase.EARLY) {
            require(
                earlyPhaseRedemptions[msg.sender] < EARLY_PHASE_ALLOCATION,
                "Early phase limit reached"
            );
            redemptionAmount = EARLY_PHASE_ALLOCATION;
            earlyPhaseRedemptions[msg.sender] += redemptionAmount;
        } else {
            redemptionAmount = GENERAL_PHASE_ALLOCATION;
        }

        require(
            basedToken.balanceOf(address(this)) >= redemptionAmount,
            "Insufficient contract balance"
        );

        redeemedTokens[tokenId] = true;

        // Transfer tokens to redeemer
        bool success = basedToken.transfer(msg.sender, redemptionAmount);
        require(success, "Token transfer failed");

        emit NFTReedemed(msg.sender, tokenId, redemptionAmount);
    }

    /**
     * @dev Withdraw remaining $BASED tokens
     */
    function withdrawTokens() external onlyOwner {
        require(
            currentPhase == RedemptionPhase.COMPLETED,
            "Redemption not completed"
        );
        
        uint256 balance = basedToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        bool success = basedToken.transfer(owner(), balance);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Emergency withdraw NFTs (in case of issues)
     * @param tokenId The NFT token ID to withdraw
     */
    function emergencyWithdrawNFT(uint256 tokenId) external onlyOwner {
        require(nftContract.ownerOf(tokenId) == address(this), "NFT not owned by contract");
        nftContract.transferFrom(address(this), owner(), tokenId);
    }
}
```
