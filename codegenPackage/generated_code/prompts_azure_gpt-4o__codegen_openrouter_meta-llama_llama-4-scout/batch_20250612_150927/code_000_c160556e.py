"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Write a smart contract interface in Código Interface Description Language (CIDL) for a decentralized finance application that enables token exchange across multiple platforms. Include boilerplate code generation using Código's platform.
Generated: DETERMINISTIC_c160556e2bfcacad
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cidl
// TokenExchange.cidl

/**
 * @title Token Exchange Interface
 * @author [Your Name]
 * @notice This interface enables token exchange across multiple platforms.
 */

pragma solidity ^0.8.0;

interface ITokenExchange {
    /**
     * @dev Event emitted when a token exchange occurs.
     * @param from The platform from which the token is being exchanged.
     * @param to The platform to which the token is being exchanged.
     * @param token The token being exchanged.
     * @param amount The amount of tokens being exchanged.
     */
    event TokenExchange(address indexed from, address indexed to, address token, uint256 amount);

    /**
     * @dev Function to exchange tokens across platforms.
     * @param fromPlatform The platform from which to exchange tokens.
     * @param toPlatform The platform to which to exchange tokens.
     * @param token The token to exchange.
     * @param amount The amount of tokens to exchange.
     * @param data Additional data for the exchange.
     */
    function exchangeTokens(
        address fromPlatform,
        address toPlatform,
        address token,
        uint256 amount,
        bytes calldata data
    ) external;

    /**
     * @dev Function to get the supported platforms.
     * @return An array of supported platforms.
     */
    function getSupportedPlatforms() external view returns (address[] memory);

    /**
     * @dev Function to get the supported tokens for a platform.
     * @param platform The platform for which to get supported tokens.
     * @return An array of supported tokens.
     */
    function getSupportedTokens(address platform) external view returns (address[] memory);

    /**
     * @dev Function to check if a platform is supported.
     * @param platform The platform to check.
     * @return True if the platform is supported, false otherwise.
     */
    function isPlatformSupported(address platform) external view returns (bool);

    /**
     * @dev Function to check if a token is supported on a platform.
     * @param platform The platform to check.
     * @param token The token to check.
     * @return True if the token is supported, false otherwise.
     */
    function isTokenSupported(address platform, address token) external view returns (bool);
}

// Boilerplate code generation using Código's platform

contract TokenExchange is ITokenExchange {
    // Mapping of supported platforms to their respective tokens
    mapping(address => mapping(address => bool)) public supportedTokens;

    // Mapping of supported platforms
    mapping(address => bool) public supportedPlatforms;

    // Array of supported platforms
    address[] public platforms;

    /**
     * @dev Constructor to initialize the contract.
     * @param _platforms An array of supported platforms.
     */
    constructor(address[] memory _platforms) {
        // Initialize supported platforms
        for (uint256 i = 0; i < _platforms.length; i++) {
            supportedPlatforms[_platforms[i]] = true;
            platforms.push(_platforms[i]);
        }
    }

    /**
     * @dev Function to add a supported platform.
     * @param platform The platform to add.
     */
    function addPlatform(address platform) public onlyOwner {
        // Check if platform is not already supported
        require(!supportedPlatforms[platform], "Platform already supported");

        // Add platform to supported platforms
        supportedPlatforms[platform] = true;
        platforms.push(platform);
    }

    /**
     * @dev Function to add a supported token for a platform.
     * @param platform The platform for which to add the token.
     * @param token The token to add.
     */
    function addToken(address platform, address token) public onlyOwner {
        // Check if platform is supported
        require(supportedPlatforms[platform], "Platform not supported");

        // Add token to supported tokens for platform
        supportedTokens[platform][token] = true;
    }

    /**
     * @dev Function to exchange tokens across platforms.
     * @param fromPlatform The platform from which to exchange tokens.
     * @param toPlatform The platform to which to exchange tokens.
     * @param token The token to exchange.
     * @param amount The amount of tokens to exchange.
     * @param data Additional data for the exchange.
     */
    function exchangeTokens(
        address fromPlatform,
        address toPlatform,
        address token,
        uint256 amount,
        bytes calldata data
    ) external override {
        // Check if from and to platforms are supported
        require(supportedPlatforms[fromPlatform], "From platform not supported");
        require(supportedPlatforms[toPlatform], "To platform not supported");

        // Check if token is supported on from and to platforms
        require(supportedTokens[fromPlatform][token], "Token not supported on from platform");
        require(supportedTokens[toPlatform][token], "Token not supported on to platform");

        // Emit TokenExchange event
        emit TokenExchange(fromPlatform, toPlatform, token, amount);

        // Perform token exchange logic
        // NOTE: This is a placeholder, implement actual exchange logic here
    }

    /**
     * @dev Function to get the supported platforms.
     * @return An array of supported platforms.
     */
    function getSupportedPlatforms() external view override returns (address[] memory) {
        return platforms;
    }

    /**
     * @dev Function to get the supported tokens for a platform.
     * @param platform The platform for which to get supported tokens.
     * @return An array of supported tokens.
     */
    function getSupportedTokens(address platform) external view override returns (address[] memory) {
        // NOTE: This is a placeholder, implement actual logic to get supported tokens here
        return new address[](0);
    }

    /**
     * @dev Function to check if a platform is supported.
     * @param platform The platform to check.
     * @return True if the platform is supported, false otherwise.
     */
    function isPlatformSupported(address platform) external view override returns (bool) {
        return supportedPlatforms[platform];
    }

    /**
     * @dev Function to check if a token is supported on a platform.
     * @param platform The platform to check.
     * @param token The token to check.
     * @return True if the token is supported, false otherwise.
     */
    function isTokenSupported(address platform, address token) external view override returns (bool) {
        return supportedTokens[platform][token];
    }

    // Modifier to restrict functions to only the owner
    address private owner;

    modifier onlyOwner {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }
}
```
