"""
Generated Code Metadata:
========================
Original URL: https://steemit-monadscore.blogspot.com
Prompt: How can I implement a decentralized marketplace for AI solutions using blockchain technology as described in Anaphora AI?
Generated: DETERMINISTIC_df095445467fd3ac
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Decentralized Marketplace for AI Solutions - Smart Contract Implementation

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract AISolutionMarketplace is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Supported payment tokens
    mapping(address => bool) public supportedPaymentTokens;
    
    // Platform fee percentage (e.g., 250 = 2.5%)
    uint256 public platformFeePercentage;
    address public platformFeeRecipient;

    struct AISolution {
        uint256 tokenId;
        address creator;
        string metadataURI;
        uint256 price;
        address paymentToken; // Address of ERC20 token, or zero address for ETH
        bool isActive;
    }

    mapping(uint256 => AISolution) public aiSolutions;
    mapping(uint256 => address) public solutionOwners;

    event SolutionCreated(
        uint256 indexed tokenId,
        address indexed creator,
        string metadataURI,
        uint256 price,
        address paymentToken
    );

    event SolutionPurchased(
        uint256 indexed tokenId,
        address indexed buyer,
        address indexed seller,
        uint256 price,
        address paymentToken
    );

    event SolutionUpdated(
        uint256 indexed tokenId,
        uint256 newPrice,
        bool isActive
    );

    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _platformFeePercentage,
        address _platformFeeRecipient
    ) ERC721(_name, _symbol) {
        require(_platformFeePercentage <= 1000, "Fee cannot exceed 10%");
        platformFeePercentage = _platformFeePercentage;
        platformFeeRecipient = _platformFeeRecipient;
    }

    /**
     * @dev Add a supported payment token
     * @param _token Address of the ERC20 token
     */
    function addPaymentToken(address _token) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        supportedPaymentTokens[_token] = true;
    }

    /**
     * @dev Remove a supported payment token
     * @param _token Address of the ERC20 token
     */
    function removePaymentToken(address _token) external onlyOwner {
        supportedPaymentTokens[_token] = false;
    }

    /**
     * @dev Update platform fee percentage
     * @param _newFee New fee percentage (e.g., 250 = 2.5%)
     */
    function updatePlatformFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 1000, "Fee cannot exceed 10%");
        platformFeePercentage = _newFee;
    }

    /**
     * @dev Update platform fee recipient
     * @param _newRecipient Address of the new recipient
     */
    function updatePlatformFeeRecipient(address _newRecipient) external onlyOwner {
        require(_newRecipient != address(0), "Invalid recipient address");
        platformFeeRecipient = _newRecipient;
    }

    /**
     * @dev List a new AI solution on the marketplace
     * @param _metadataURI URI pointing to solution metadata
     * @param _price Price of the solution
     * @param _paymentToken Address of payment token (zero address for ETH)
     */
    function listSolution(
        string memory _metadataURI,
        uint256 _price,
        address _paymentToken
    ) external nonReentrant returns (uint256) {
        require(_price > 0, "Price must be greater than zero");
        
        if (_paymentToken != address(0)) {
            require(supportedPaymentTokens[_paymentToken], "Payment token not supported");
        }

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        _mint(msg.sender, newTokenId);
        
        aiSolutions[newTokenId] = AISolution({
            tokenId: newTokenId,
            creator: msg.sender,
            metadataURI: _metadataURI,
            price: _price,
            paymentToken: _paymentToken,
            isActive: true
        });

        solutionOwners[newTokenId] = msg.sender;

        emit SolutionCreated(newTokenId, msg.sender, _metadataURI, _price, _paymentToken);
        return newTokenId;
    }

    /**
     * @dev Update an existing AI solution listing
     * @param _tokenId ID of the solution to update
     * @param _newPrice New price of the solution
     * @param _isActive Whether the solution is active for sale
     */
    function updateSolution(
        uint256 _tokenId,
        uint256 _newPrice,
        bool _isActive
    ) external nonReentrant {
        require(_exists(_tokenId), "Solution does not exist");
        require(ownerOf(_tokenId) == msg.sender, "Not the solution owner");
        require(_newPrice > 0, "Price must be greater than zero");

        AISolution storage solution = aiSolutions[_tokenId];
        solution.price = _newPrice;
        solution.isActive = _isActive;

        emit SolutionUpdated(_tokenId, _newPrice, _isActive);
    }

    /**
     * @dev Purchase an AI solution
     * @param _tokenId ID of the solution to purchase
     */
    function purchaseSolution(uint256 _tokenId) external payable nonReentrant {
        require(_exists(_tokenId), "Solution does not exist");
        
        AISolution memory solution = aiSolutions[_tokenId];
        require(solution.isActive, "Solution is not active for sale");
        require(solutionOwners[_tokenId] != msg.sender, "Cannot purchase your own solution");

        uint256 totalPrice = solution.price;
        uint256 platformFee = (totalPrice * platformFeePercentage) / 10000;
        uint256 creatorAmount = totalPrice - platformFee;

        if (solution.paymentToken == address(0)) {
            // ETH payment
            require(msg.value == totalPrice, "Incorrect ETH amount sent");
            
            (bool success1, ) = solutionOwners[_tokenId].call{value: creatorAmount}("");
            (bool success2, ) = platformFeeRecipient.call{value: platformFee}("");
            
            require(success1 && success2, "ETH transfer failed");
        } else {
            // ERC20 payment
            require(msg.value == 0, "ETH sent for ERC20 payment");
            
            IERC20 paymentToken = IERC20(solution.paymentToken);
            require(
                paymentToken.transferFrom(msg.sender, solutionOwners[_tokenId], creatorAmount),
                "ERC20 transfer to creator failed"
            );
            require(
                paymentToken.transferFrom(msg.sender, platformFeeRecipient, platformFee),
                "ERC20 transfer to platform failed"
            );
        }

        // Transfer ownership
        _transfer(solutionOwners[_tokenId], msg.sender, _tokenId);
        solutionOwners[_tokenId] = msg.sender;

        emit SolutionPurchased(
            _tokenId,
            msg.sender,
            solution.creator,
            solution.price,
            solution.paymentToken
        );
    }

    /**
     * @dev Get solution details by token ID
     * @param _tokenId ID of the solution
     */
    function getSolution(uint256 _tokenId) external view returns (AISolution memory) {
        require(_exists(_tokenId), "Solution does not exist");
        return aiSolutions[_tokenId];
    }

    /**
     * @dev Override transfer functions to maintain solutionOwners mapping
     */
    function _transfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._transfer(from, to, tokenId);
        solutionOwners[tokenId] = to;
    }
}
```

```javascript
// Frontend Interaction (using ethers.js)
const marketplaceAbi = [
  // ABI definitions would go here
];

async function listSolution(provider, contractAddress, metadataURI, price, paymentToken) {
    try {
        const signer = provider.getSigner();
        const marketplace = new ethers.Contract(contractAddress, marketplaceAbi, signer);
        
        const tx = await marketplace.listSolution(
            metadataURI,
            ethers.utils.parseUnits(price.toString(), 18), // Assuming 18 decimals
            paymentToken
        );
        
        const receipt = await tx.wait();
        const event = receipt.events.find(e => e.event === 'SolutionCreated');
        return event.args.tokenId.toString();
    } catch (error) {
        console.error("Error listing solution:", error);
        throw error;
    }
}

async function purchaseSolution(provider, contractAddress, tokenId, paymentToken, price) {
    try {
        const signer = provider.getSigner();
        const marketplace = new ethers.Contract(contractAddress
