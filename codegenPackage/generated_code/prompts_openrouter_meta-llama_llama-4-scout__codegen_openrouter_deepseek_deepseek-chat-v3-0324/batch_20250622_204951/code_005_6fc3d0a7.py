"""
Generated Code Metadata:
========================
Original URL: https://reef-io.pages.dev
Prompt: "Develop a guide for porting an existing Ethereum-based Solidity project to Reef chain, ensuring compatibility and minimal code modifications."
Generated: DETERMINISTIC_6fc3d0a743afb3e0
Batch ID: 20250622_204951
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

/**
 * @title ReefPortingGuide
 * @dev A collection of modifications and best practices for porting Ethereum projects to Reef chain
 */
contract ReefPortingGuide {
    // Address of the wrapped ETH equivalent on Reef (REEF20)
    address public constant REEF_WETH = 0x0000000000000000000000000000000000001000;
    
    // Gas price considerations (Reef has different gas economics)
    uint256 public constant REEF_TARGET_GAS_PRICE = 1 gwei;
    
    /**
     * @dev Modifier to ensure functions are only called with appropriate gas price
     */
    modifier reefGasPrice() {
        require(tx.gasprice <= REEF_TARGET_GAS_PRICE, "ReefPortingGuide: Gas price too high");
        _;
    }
    
    /**
     * @notice Convert ETH addresses to REEF20 equivalent
     * @dev Replace ETH addresses with REEF_WETH for token handling
     * @param tokenAddress Original token address
     * @return address The equivalent REEF20 address if input was ETH
     */
    function convertEthToReefWeth(address tokenAddress) public pure returns (address) {
        return tokenAddress == address(0) ? REEF_WETH : tokenAddress;
    }
    
    /**
     * @notice Adjust block.timestamp dependent logic
     * @dev Reef has faster block times (~6s vs Ethereum's ~13s)
     * @param ethereumDuration Duration calculated for Ethereum
     * @return uint256 Adjusted duration for Reef
     */
    function adjustDurationForReef(uint256 ethereumDuration) public pure returns (uint256) {
        // Adjust timing by approximately half for Reef's faster blocks
        return ethereumDuration / 2;
    }
    
    /**
     * @notice Handle chain-specific address formats
     * @dev Reef uses the same address format as Ethereum, but this can be extended
     * for other potential differences
     * @param addr The address to validate
     */
    function validateReefAddress(address addr) public pure {
        require(addr != address(0), "ReefPortingGuide: Zero address not allowed");
        // Additional Reef-specific validation if needed
    }
    
    /**
     * @notice Check if running on Reef chain
     * @dev Uses chain ID (REEF mainnet: 13939, testnet: 13938)
     * @return bool True if on Reef chain
     */
    function isReefChain() public view returns (bool) {
        uint256 chainId;
        assembly {
            chainId := chainid()
        }
        return chainId == 13939 || chainId == 13938;
    }
    
    /**
     * @notice Example of gas optimization for Reef
     * @dev Reef has different gas costs, optimize accordingly
     */
    function reefOptimizedFunction() external reefGasPrice {
        // Function implementation optimized for Reef's gas costs
    }
}

/**
 * @title ReefCompatibleToken
 * @dev Example ERC20 implementation with Reef-specific adjustments
 */
contract ReefCompatibleToken {
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;
    
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _initialSupply
    ) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply;
        balanceOf[msg.sender] = _initialSupply;
    }
    
    function transfer(address to, uint256 value) external returns (bool) {
        require(to != address(0), "ReefCompatibleToken: Invalid address");
        require(balanceOf[msg.sender] >= value, "ReefCompatibleToken: Insufficient balance");
        
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }
    
    function approve(address spender, uint256 value) external returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }
    
    function transferFrom(
        address from,
        address to,
        uint256 value
    ) external returns (bool) {
        require(to != address(0), "ReefCompatibleToken: Invalid address");
        require(balanceOf[from] >= value, "ReefCompatibleToken: Insufficient balance");
        require(allowance[from][msg.sender] >= value, "ReefCompatibleToken: Insufficient allowance");
        
        balanceOf[from] -= value;
        balanceOf[to] += value;
        allowance[from][msg.sender] -= value;
        emit Transfer(from, to, value);
        return true;
    }
}

/**
 * @title ReefDeployer
 * @dev Helper contract for deploying to Reef chain
 */
contract ReefDeployer {
    /**
     * @notice Deploy a contract with Reef-specific optimizations
     * @param salt The salt for create2 deployment
     * @param creationCode The contract creation code
     * @return addr The deployed contract address
     */
    function deployOnReef(bytes32 salt, bytes memory creationCode) public returns (address addr) {
        assembly {
            addr := create2(0, add(creationCode, 0x20), mload(creationCode), salt)
            if iszero(extcodesize(addr)) {
                revert(0, 0)
            }
        }
        return addr;
    }
}
```
