"""
Generated Code Metadata:
========================
Original URL: https://jwzt-verification.pages.dev
Prompt: Write a Solidity contract to mint equity-based NFTs for AI start-ups, ensuring fractionalization of the NFTs for budget-friendly investments.
Generated: DETERMINISTIC_5b60a92c659a7b2f
Batch ID: 20250612_145837
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract AIStartupEquityNFT is ERC721, ERC721Enumerable, Ownable {
    using SafeMath for uint256;

    // Struct to store startup details
    struct Startup {
        string name;
        string symbol;
        uint256 totalSupply;
        uint256 pricePerShare;
        address paymentToken; // Address of ERC20 token used for payment (zero address for ETH)
        bool isActive;
    }

    // Mapping from token ID to startup ID
    mapping(uint256 => uint256) private _tokenStartup;

    // Mapping from startup ID to startup details
    mapping(uint256 => Startup) private _startups;

    // Mapping from startup ID to total shares minted
    mapping(uint256 => uint256) private _sharesMinted;

    // Mapping from startup ID to token ID tracker
    mapping(uint256 => uint256) private _tokenIdTracker;

    // Counter for startup IDs
    uint256 private _startupCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Event emitted when a new startup is registered
    event StartupRegistered(
        uint256 indexed startupId,
        string name,
        string symbol,
        uint256 totalSupply,
        uint256 pricePerShare,
        address paymentToken
    );

    // Event emitted when shares are purchased
    event SharesPurchased(
        address indexed buyer,
        uint256 indexed startupId,
        uint256 amount,
        uint256 totalPrice
    );

    constructor(string memory baseURI) ERC721("AI Startup Equity NFT", "AISENFT") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Registers a new AI startup
     * @param name Name of the startup
     * @param symbol Symbol of the startup
     * @param totalSupply Total number of shares available
     * @param pricePerShare Price per share in wei
     * @param paymentToken Address of ERC20 token used for payment (zero address for ETH)
     */
    function registerStartup(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 pricePerShare,
        address paymentToken
    ) external onlyOwner {
        uint256 startupId = _startupCounter;
        _startups[startupId] = Startup({
            name: name,
            symbol: symbol,
            totalSupply: totalSupply,
            pricePerShare: pricePerShare,
            paymentToken: paymentToken,
            isActive: true
        });

        _startupCounter = _startupCounter.add(1);
        emit StartupRegistered(startupId, name, symbol, totalSupply, pricePerShare, paymentToken);
    }

    /**
     * @dev Purchases shares of a startup
     * @param startupId ID of the startup
     * @param amount Number of shares to purchase
     */
    function purchaseShares(uint256 startupId, uint256 amount) external payable {
        require(_startups[startupId].isActive, "Startup is not active");
        require(amount > 0, "Amount must be greater than zero");

        Startup memory startup = _startups[startupId];
        uint256 availableShares = startup.totalSupply.sub(_sharesMinted[startupId]);
        require(amount <= availableShares, "Not enough shares available");

        uint256 totalPrice = startup.pricePerShare.mul(amount);

        if (startup.paymentToken == address(0)) {
            require(msg.value >= totalPrice, "Insufficient ETH sent");
            if (msg.value > totalPrice) {
                payable(msg.sender).transfer(msg.value.sub(totalPrice));
            }
        } else {
            IERC20 paymentToken = IERC20(startup.paymentToken);
            require(
                paymentToken.transferFrom(msg.sender, address(this), totalPrice),
                "Payment token transfer failed"
            );
        }

        _mintShares(msg.sender, startupId, amount);
        emit SharesPurchased(msg.sender, startupId, amount, totalPrice);
    }

    /**
     * @dev Mints shares for a buyer
     * @param to Address to mint shares to
     * @param startupId ID of the startup
     * @param amount Number of shares to mint
     */
    function _mintShares(address to, uint256 startupId, uint256 amount) internal {
        for (uint256 i = 0; i < amount; i++) {
            uint256 tokenId = _tokenIdTracker[startupId].add(1);
            _tokenIdTracker[startupId] = tokenId;
            _tokenStartup[tokenId] = startupId;
            _safeMint(to, tokenId);
        }
        _sharesMinted[startupId] = _sharesMinted[startupId].add(amount);
    }

    /**
     * @dev Returns the startup details for a given token ID
     * @param tokenId ID of the token
     */
    function getStartupForToken(uint256 tokenId) external view returns (Startup memory) {
        require(_exists(tokenId), "Token does not exist");
        return _startups[_tokenStartup[tokenId]];
    }

    /**
     * @dev Returns the startup details for a given startup ID
     * @param startupId ID of the startup
     */
    function getStartup(uint256 startupId) external view returns (Startup memory) {
        return _startups[startupId];
    }

    /**
     * @dev Returns the total number of startups registered
     */
    function getStartupCount() external view returns (uint256) {
        return _startupCounter;
    }

    /**
     * @dev Returns the number of shares minted for a startup
     * @param startupId ID of the startup
     */
    function getSharesMinted(uint256 startupId) external view returns (uint256) {
        return _sharesMinted[startupId];
    }

    /**
     * @dev Sets the base URI for token metadata
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Withdraws collected funds
     * @param token Address of the token to withdraw (zero address for ETH)
     * @param amount Amount to withdraw
     */
    function withdrawFunds(address token, uint256 amount) external onlyOwner {
        if (token == address(0)) {
            payable(owner()).transfer(amount);
        } else {
            IERC20(token).transfer(owner(), amount);
        }
    }

    /**
     * @dev Toggles the active status of a startup
     * @param startupId ID of the startup
     * @param isActive New active status
     */
    function setStartupActive(uint256 startupId, bool isActive) external onlyOwner {
        _startups[startupId].isActive = isActive;
    }

    // Override required by Solidity
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 batchSize
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
    }

    // Override required by Solidity
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
```
