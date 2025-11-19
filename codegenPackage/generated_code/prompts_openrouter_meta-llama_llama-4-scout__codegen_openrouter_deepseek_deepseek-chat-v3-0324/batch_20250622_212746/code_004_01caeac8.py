"""
Generated Code Metadata:
========================
Original URL: https://kaaia.io
Prompt: "Design a Kaia-based RWA (Real-World Asset) tokenization platform, including smart contract code and ecosystem integration."
Generated: DETERMINISTIC_01caeac8c2e92506
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RWAToken
 * @dev ERC20 token representing ownership of a real-world asset
 */
contract RWAToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    struct Asset {
        string assetId;
        string description;
        uint256 value;
        string location;
        bool verified;
    }

    mapping(string => Asset) public assets;
    mapping(address => bool) public verifiedMinters;
    mapping(address => mapping(string => uint256)) public assetBalances;

    event AssetRegistered(string assetId, string description, uint256 value);
    event AssetVerified(string assetId);
    event MinterAdded(address minter);
    event MinterRemoved(address minter);

    constructor() ERC20("RWA Token", "RWA") {}

    /**
     * @dev Register a new real-world asset
     * @param assetId Unique identifier for the asset
     * @param description Description of the asset
     * @param value Estimated value of the asset
     * @param location Physical location of the asset
     */
    function registerAsset(
        string memory assetId,
        string memory description,
        uint256 value,
        string memory location
    ) external onlyOwner {
        require(bytes(assetId).length > 0, "Asset ID cannot be empty");
        require(bytes(assets[assetId].assetId).length == 0, "Asset already registered");
        
        assets[assetId] = Asset(assetId, description, value, location, false);
        emit AssetRegistered(assetId, description, value);
    }

    /**
     * @dev Verify a registered asset
     * @param assetId Unique identifier for the asset
     */
    function verifyAsset(string memory assetId) external onlyOwner {
        require(bytes(assets[assetId].assetId).length > 0, "Asset not registered");
        require(!assets[assetId].verified, "Asset already verified");
        
        assets[assetId].verified = true;
        emit AssetVerified(assetId);
    }

    /**
     * @dev Add a verified minter address
     * @param minter Address to be added as minter
     */
    function addMinter(address minter) external onlyOwner {
        require(minter != address(0), "Invalid address");
        require(!verifiedMinters[minter], "Already a minter");
        
        verifiedMinters[minter] = true;
        emit MinterAdded(minter);
    }

    /**
     * @dev Remove a verified minter address
     * @param minter Address to be removed as minter
     */
    function removeMinter(address minter) external onlyOwner {
        require(verifiedMinters[minter], "Not a minter");
        
        verifiedMinters[minter] = false;
        emit MinterRemoved(minter);
    }

    /**
     * @dev Mint tokens representing ownership of an asset
     * @param to Address to receive the tokens
     * @param assetId Asset ID being tokenized
     * @param amount Number of tokens to mint
     */
    function mint(
        address to,
        string memory assetId,
        uint256 amount
    ) external whenNotPaused {
        require(verifiedMinters[msg.sender], "Not authorized to mint");
        require(assets[assetId].verified, "Asset not verified");
        require(to != address(0), "Cannot mint to zero address");
        require(amount > 0, "Amount must be positive");
        
        _mint(to, amount);
        assetBalances[to][assetId] = assetBalances[to][assetId].add(amount);
    }

    /**
     * @dev Burn tokens to redeem underlying asset
     * @param from Address burning tokens
     * @param assetId Asset ID being redeemed
     * @param amount Number of tokens to burn
     */
    function burn(
        address from,
        string memory assetId,
        uint256 amount
    ) external whenNotPaused {
        require(verifiedMinters[msg.sender], "Not authorized to burn");
        require(assets[assetId].verified, "Asset not verified");
        require(assetBalances[from][assetId] >= amount, "Insufficient balance");
        
        _burn(from, amount);
        assetBalances[from][assetId] = assetBalances[from][assetId].sub(amount);
    }

    /**
     * @dev Pause all token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause all token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Override ERC20 transfer to include pausable functionality
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}

/**
 * @title RWATokenizationPlatform
 * @dev Main platform contract for RWA tokenization
 */
contract RWATokenizationPlatform is Ownable {
    mapping(address => bool) public registeredTokens;
    mapping(string => address) public assetToToken;

    event TokenRegistered(address tokenAddress, string assetId);
    event TokenUnregistered(address tokenAddress);

    /**
     * @dev Register a new RWA token contract
     * @param tokenAddress Address of the token contract
     * @param assetId Asset ID being tokenized
     */
    function registerToken(address tokenAddress, string memory assetId) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(!registeredTokens[tokenAddress], "Token already registered");
        require(bytes(assetId).length > 0, "Asset ID cannot be empty");
        
        registeredTokens[tokenAddress] = true;
        assetToToken[assetId] = tokenAddress;
        emit TokenRegistered(tokenAddress, assetId);
    }

    /**
     * @dev Unregister a token contract
     * @param tokenAddress Address of the token contract
     */
    function unregisterToken(address tokenAddress) external onlyOwner {
        require(registeredTokens[tokenAddress], "Token not registered");
        
        registeredTokens[tokenAddress] = false;
        emit TokenUnregistered(tokenAddress);
    }

    /**
     * @dev Get token address for a specific asset
     * @param assetId Asset ID to look up
     * @return Address of the token contract
     */
    function getTokenForAsset(string memory assetId) external view returns (address) {
        return assetToToken[assetId];
    }
}

// Integration with Chainlink Oracle for price feeds
interface IChainlinkOracle {
    function latestAnswer() external view returns (int256);
}

/**
 * @title RWAPriceFeed
 * @dev Contract to get price feeds for RWA tokens
 */
contract RWAPriceFeed {
    mapping(address => address) public tokenPriceFeeds;
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    /**
     * @dev Set price feed for a token
     * @param tokenAddress Address of the token
     * @param priceFeed Address of Chainlink price feed
     */
    function setPriceFeed(address tokenAddress, address priceFeed) external onlyOwner {
        tokenPriceFeeds[tokenAddress] = priceFeed;
    }

    /**
     * @dev Get current price for a token
     * @param tokenAddress Address of the token
     * @return Current price (scaled to 8 decimals)
     */
    function getTokenPrice(address tokenAddress) external view returns (uint256) {
        address feedAddress = tokenPriceFeeds[tokenAddress];
        require(feedAddress != address(0), "Price feed not set");
        
        int256 price = IChainlinkOracle(feedAddress).latestAnswer();
        require(price > 0, "Invalid price");
        
        return uint256(price);
    }
}

/**
 * @title RWATokenizationUI
 * @dev Mock contract representing frontend integration
 */
contract RWATokenizationUI {
    RWATokenizationPlatform public platform;
    RWAPriceFeed public priceFeed;

    constructor(address _platform, address _priceFeed) {
        platform = RWATokenizationPlatform(_platform);
        priceFeed = RWAPriceFeed(_priceFeed);
    }

    /**
     * @dev Get token details for display
     * @param assetId Asset ID to query
     * @return tokenAddress Address of the token contract
     * @return price Current price of the token
     */
    function getTokenDetails(string memory assetId) external view returns (address tokenAddress, uint256 price) {
        tokenAddress = platform.getTokenForAsset(assetId);
        if (tokenAddress != address(0)) {
            price =
