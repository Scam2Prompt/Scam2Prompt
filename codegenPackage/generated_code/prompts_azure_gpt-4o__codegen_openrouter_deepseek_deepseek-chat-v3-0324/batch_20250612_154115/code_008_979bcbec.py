"""
Generated Code Metadata:
========================
Original URL: https://debridge-finance.org
Prompt: Generate a technical overview of how deBridge utilizes Chainlink oracles for cross-chain transfers, with an example implementation in a DeFi protocol.
Generated: DETERMINISTIC_979bcbeccd496405
Batch ID: 20250612_154115
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

// Import Chainlink and deBridge interfaces
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@debridge-finance/contracts/contracts/interfaces/IDeBridgeGate.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CrossChainDeFiProtocol
 * @dev A DeFi protocol that uses deBridge and Chainlink for cross-chain transfers
 * and price feeds. Implements deposit/withdraw functionality with cross-chain support.
 */
contract CrossChainDeFiProtocol is Ownable, ReentrancyGuard {
    // Chainlink price feed for asset pricing
    AggregatorV3Interface public priceFeed;
    
    // deBridge gate contract
    IDeBridgeGate public deBridgeGate;
    
    // Supported tokens
    mapping(address => bool) public supportedTokens;
    
    // User balances
    mapping(address => mapping(address => uint256)) public userBalances;
    
    // Chainlink price feed decimals
    uint8 public constant PRICE_FEED_DECIMALS = 8;
    
    // Events
    event Deposit(
        address indexed user,
        address indexed token,
        uint256 amount,
        uint256 timestamp
    );
    
    event Withdraw(
        address indexed user,
        address indexed token,
        uint256 amount,
        uint256 timestamp
    );
    
    event CrossChainTransferInitiated(
        address indexed user,
        uint256 chainId,
        address indexed token,
        uint256 amount,
        uint256 timestamp
    );
    
    /**
     * @dev Constructor initializes the contract with deBridge and Chainlink
     * @param _priceFeed Chainlink price feed address
     * @param _deBridgeGate deBridge gate contract address
     */
    constructor(address _priceFeed, address _deBridgeGate) {
        require(_priceFeed != address(0), "Invalid price feed address");
        require(_deBridgeGate != address(0), "Invalid deBridge address");
        
        priceFeed = AggregatorV3Interface(_priceFeed);
        deBridgeGate = IDeBridgeGate(_deBridgeGate);
    }
    
    /**
     * @dev Add a supported token
     * @param token Address of the token to support
     */
    function addSupportedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = true;
    }
    
    /**
     * @dev Deposit tokens into the protocol
     * @param token Address of the token to deposit
     * @param amount Amount to deposit
     */
    function deposit(address token, uint256 amount) external nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        userBalances[msg.sender][token] += amount;
        
        emit Deposit(msg.sender, token, amount, block.timestamp);
    }
    
    /**
     * @dev Withdraw tokens from the protocol
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdraw(address token, uint256 amount) external nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender][token] >= amount, "Insufficient balance");
        
        userBalances[msg.sender][token] -= amount;
        IERC20(token).transfer(msg.sender, amount);
        
        emit Withdraw(msg.sender, token, amount, block.timestamp);
    }
    
    /**
     * @dev Initiate cross-chain transfer using deBridge and Chainlink for price validation
     * @param token Address of the token to transfer
     * @param amount Amount to transfer
     * @param targetChainId Destination chain ID
     * @param targetAddress Destination address
     * @param executionFee Execution fee for deBridge
     */
    function initiateCrossChainTransfer(
        address token,
        uint256 amount,
        uint256 targetChainId,
        bytes32 targetAddress,
        uint256 executionFee
    ) external payable nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender][token] >= amount, "Insufficient balance");
        
        // Get current price from Chainlink
        (, int256 price, , , ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price");
        
        // Convert price to 18 decimals
        uint256 normalizedPrice = uint256(price) * (10 ** (18 - PRICE_FEED_DECIMALS));
        
        // Validate price is within acceptable range (example: must be > $1)
        require(normalizedPrice > 1 ether, "Price too low");
        
        // Update user balance
        userBalances[msg.sender][token] -= amount;
        
        // Approve deBridge to spend tokens
        IERC20(token).approve(address(deBridgeGate), amount);
        
        // Prepare submission data
        bytes memory submissionData = abi.encode(
            targetAddress,
            abi.encode(amount, normalizedPrice, block.timestamp)
        );
        
        // Send cross-chain transfer via deBridge
        deBridgeGate.send{value: msg.value}(
            token,
            amount,
            targetChainId,
            submissionData,
            false, // useAssetFee
            executionFee,
            msg.sender
        );
        
        emit CrossChainTransferInitiated(msg.sender, targetChainId, token, amount, block.timestamp);
    }
    
    /**
     * @dev Receive cross-chain transfer (to be called by deBridge)
     * @param _token Address of the token received
     * @param _amount Amount received
     * @param _chainId Source chain ID
     * @param _data Additional data (decoded as (address, uint256, uint256))
     */
    function receiveCrossChainTransfer(
        address _token,
        uint256 _amount,
        uint256 _chainId,
        bytes calldata _data
    ) external {
        require(msg.sender == address(deBridgeGate), "Only deBridge can call");
        require(supportedTokens[_token], "Token not supported");
        
        (bytes32 targetAddress, bytes memory innerData) = abi.decode(_data, (bytes32, bytes));
        (uint256 amount, uint256 price, uint256 timestamp) = abi.decode(innerData, (uint256, uint256, uint256));
        
        // Convert bytes32 target address to address type
        address receiver = address(uint160(uint256(targetAddress)));
        
        // Update user balance
        userBalances[receiver][_token] += amount;
        
        emit Deposit(receiver, _token, amount, timestamp);
    }
    
    /**
     * @dev Get the latest price from Chainlink
     * @return Current price with 18 decimals
     */
    function getLatestPrice() public view returns (uint256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return uint256(price) * (10 ** (18 - PRICE_FEED_DECIMALS));
    }
}
```
