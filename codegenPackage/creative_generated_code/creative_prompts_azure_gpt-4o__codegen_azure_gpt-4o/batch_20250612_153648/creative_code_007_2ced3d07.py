"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimgift-x44.web.app
Prompt: Generate a smart contract snippet to validate NFT ownership before allowing a wallet to claim DUST tokens from the airdrop pool.
Generated: DETERMINISTIC_2ced3d07f3e7ea30
Batch ID: 20250612_153648
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
 * @title NFT Ownership Validation and DUST Token Airdrop Smart Contract
 * @dev This contract validates NFT ownership before allowing wallet to claim DUST tokens
 */
contract DustAirdrop {
    // Address of the ERC721 NFT contract
    address public immutable nftContract;

    // Address of the ERC20 DUST token contract
    address public immutable dustToken;

    // Amount of DUST tokens to distribute per claim
    uint256 public immutable dustPerClaim;

    // Mapping to track claimed wallets
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are claimed
    event DustClaimed(address indexed wallet, uint256 amount);

    /**
     * @dev Constructor to initialize contract parameters
     * @param _nftContract Address of the NFT (ERC721) contract
     * @param _dustToken Address of the DUST (ERC20) token contract
     * @param _dustPerClaim Amount of DUST tokens to distribute per claim
     */
    constructor(address _nftContract, address _dustToken, uint256 _dustPerClaim) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        require(_dustToken != address(0), "Invalid DUST token contract address");
        require(_dustPerClaim > 0, "DUST per claim must be greater than zero");

        nftContract = _nftContract;
        dustToken = _dustToken;
        dustPerClaim = _dustPerClaim;
    }

    /**
     * @dev Function to claim DUST tokens after verifying NFT ownership
     */
    function claimDust() external {
        require(!hasClaimed[msg.sender], "Already claimed");
        
        // Interface for ERC721 contract
        IERC721 nft = IERC721(nftContract);

        // Check if caller owns at least one NFT
        require(nft.balanceOf(msg.sender) > 0, "No NFT ownership detected");

        // Interface for ERC20 contract
        IERC20 dust = IERC20(dustToken);

        // Check if contract has sufficient DUST tokens for transfer
        require(dust.balanceOf(address(this)) >= dustPerClaim, "Insufficient DUST tokens in airdrop pool");

        // Mark caller as having claimed
        hasClaimed[msg.sender] = true;

        // Transfer DUST tokens to caller
        dust.transfer(msg.sender, dustPerClaim);

        // Emit event for successful claim
        emit DustClaimed(msg.sender, dustPerClaim);
    }
}

/**
 * @dev Minimal ERC721 interface for checking NFT ownership
 */
interface IERC721 {
    function balanceOf(address owner) external view returns (uint256);
}

/**
 * @dev Minimal ERC20 interface for token transfer
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
