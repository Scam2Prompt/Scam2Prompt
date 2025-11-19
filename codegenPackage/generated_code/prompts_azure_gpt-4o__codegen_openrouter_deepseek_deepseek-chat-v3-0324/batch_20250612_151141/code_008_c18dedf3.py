"""
Generated Code Metadata:
========================
Original URL: https://airyd.pages.dev
Prompt: Provide code to implement permissionless token listings on a blockchain platform, inspired by Avalaunch's emphasis on permissionless fundraising.
Generated: DETERMINISTIC_c18dedf31668301a
Batch ID: 20250612_151141
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PermissionlessTokenListing
 * @dev A contract for permissionless token listings with basic validation
 */
contract PermissionlessTokenListing is Ownable, ReentrancyGuard {
    struct Listing {
        address tokenAddress;
        address creator;
        uint256 listingFee;
        uint256 timestamp;
        bool isActive;
    }

    uint256 public baseListingFee;
    uint256 public minLiquidityRequirement;
    uint256 public minLockPeriod;
    uint256 public totalListings;

    mapping(uint256 => Listing) public listings;
    mapping(address => bool) public isListed;

    event TokenListed(
        uint256 listingId,
        address indexed tokenAddress,
        address indexed creator,
        uint256 listingFee,
        uint256 timestamp
    );
    event ListingDeactivated(uint256 listingId);
    event FeesUpdated(uint256 newBaseFee, uint256 newMinLiquidity);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor initializes the contract with basic parameters
     * @param _baseListingFee Initial base fee for listing tokens
     * @param _minLiquidityRequirement Minimum liquidity required for tokens
     * @param _minLockPeriod Minimum lock period for listed tokens
     */
    constructor(
        uint256 _baseListingFee,
        uint256 _minLiquidityRequirement,
        uint256 _minLockPeriod
    ) {
        require(_baseListingFee > 0, "Fee must be greater than zero");
        baseListingFee = _baseListingFee;
        minLiquidityRequirement = _minLiquidityRequirement;
        minLockPeriod = _minLockPeriod;
    }

    /**
     * @dev Lists a new token with basic validation
     * @param _tokenAddress Address of the token to be listed
     */
    function listToken(address _tokenAddress) external payable nonReentrant {
        require(msg.value >= baseListingFee, "Insufficient listing fee");
        require(_tokenAddress != address(0), "Invalid token address");
        require(!isListed[_tokenAddress], "Token already listed");

        IERC20 token = IERC20(_tokenAddress);
        uint256 balance = token.balanceOf(_tokenAddress);
        require(
            balance >= minLiquidityRequirement,
            "Insufficient token liquidity"
        );

        uint256 listingId = totalListings++;
        listings[listingId] = Listing({
            tokenAddress: _tokenAddress,
            creator: msg.sender,
            listingFee: msg.value,
            timestamp: block.timestamp,
            isActive: true
        });

        isListed[_tokenAddress] = true;
        emit TokenListed(listingId, _tokenAddress, msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Deactivates a listing (only owner or creator)
     * @param _listingId ID of the listing to deactivate
     */
    function deactivateListing(uint256 _listingId) external {
        require(_listingId < totalListings, "Invalid listing ID");
        Listing storage listing = listings[_listingId];
        require(
            msg.sender == owner() || msg.sender == listing.creator,
            "Not authorized"
        );
        require(listing.isActive, "Listing already inactive");

        listing.isActive = false;
        isListed[listing.tokenAddress] = false;
        emit ListingDeactivated(_listingId);
    }

    /**
     * @dev Updates fee and liquidity parameters (only owner)
     * @param _newBaseFee New base listing fee
     * @param _newMinLiquidity New minimum liquidity requirement
     */
    function updateFees(
        uint256 _newBaseFee,
        uint256 _newMinLiquidity
    ) external onlyOwner {
        require(_newBaseFee > 0, "Fee must be greater than zero");
        baseListingFee = _newBaseFee;
        minLiquidityRequirement = _newMinLiquidity;
        emit FeesUpdated(_newBaseFee, _newMinLiquidity);
    }

    /**
     * @dev Withdraws collected fees (only owner)
     */
    function withdrawFees() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
        emit FundsWithdrawn(owner(), balance);
    }

    /**
     * @dev Checks if a token is currently listed and active
     * @param _tokenAddress Address of the token to check
     * @return bool Whether the token is listed and active
     */
    function isTokenListed(address _tokenAddress) external view returns (bool) {
        return isListed[_tokenAddress] && _isListingActive(_tokenAddress);
    }

    /**
     * @dev Internal function to check if a listing is active
     * @param _tokenAddress Address of the token to check
     * @return bool Whether the listing is active
     */
    function _isListingActive(address _tokenAddress) internal view returns (bool) {
        for (uint256 i = 0; i < totalListings; i++) {
            if (
                listings[i].tokenAddress == _tokenAddress &&
                listings[i].isActive &&
                block.timestamp >= listings[i].timestamp + minLockPeriod
            ) {
                return true;
            }
        }
        return false;
    }
}
```
