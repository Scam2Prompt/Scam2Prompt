"""
Generated Code Metadata:
========================
Original URL: https://peaptoken.fun
Prompt: "Draft a smart contract for the PEPE Pump Pad, enabling two-click launches of meme coins with anti-rug security features."
Generated: DETERMINISTIC_eb8bf56c0b33671c
Batch ID: 20250622_212724
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
 * @title PEPE Pump Pad Smart Contract
 * @dev Enables two-click launches of meme coins with anti-rug security features.
 */
contract PEPEPumpPad {
    // Struct to store token details
    struct Token {
        string name;
        string symbol;
        uint256 totalSupply;
        address creator;
        bool antiRugEnabled;
    }

    // Mapping to store launched tokens
    mapping(address => Token) public launchedTokens;

    // Event emitted when a new token is launched
    event TokenLaunched(
        address indexed tokenAddress,
        string name,
        string symbol,
        uint256 totalSupply,
        address indexed creator,
        bool antiRugEnabled
    );

    // Modifier to ensure only the creator can call certain functions
    modifier onlyCreator(address tokenAddress) {
        require(
            launchedTokens[tokenAddress].creator == msg.sender,
            "Only the creator can perform this action"
        );
        _;
    }

    /**
     * @dev Launches a new meme coin with anti-rug security features.
     * @param name Name of the token.
     * @param symbol Symbol of the token.
     * @param totalSupply Total supply of the token.
     * @param antiRugEnabled Whether anti-rug features are enabled.
     */
    function launchToken(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        bool antiRugEnabled
    ) external {
        // Create a new ERC20 token contract
        address newToken = address(new ERC20Token(name, symbol, totalSupply, msg.sender));

        // Store token details
        launchedTokens[newToken] = Token({
            name: name,
            symbol: symbol,
            totalSupply: totalSupply,
            creator: msg.sender,
            antiRugEnabled: antiRugEnabled
        });

        // Emit event
        emit TokenLaunched(newToken, name, symbol, totalSupply, msg.sender, antiRugEnabled);
    }

    /**
     * @dev Enables anti-rug security features for a token.
     * @param tokenAddress Address of the token.
     */
    function enableAntiRug(address tokenAddress) external onlyCreator(tokenAddress) {
        require(!launchedTokens[tokenAddress].antiRugEnabled, "Anti-rug already enabled");
        launchedTokens[tokenAddress].antiRugEnabled = true;
    }

    /**
     * @dev Disables anti-rug security features for a token.
     * @param tokenAddress Address of the token.
     */
    function disableAntiRug(address tokenAddress) external onlyCreator(tokenAddress) {
        require(launchedTokens[tokenAddress].antiRugEnabled, "Anti-rug already disabled");
        launchedTokens[tokenAddress].antiRugEnabled = false;
    }
}

/**
 * @title ERC20Token
 * @dev Basic ERC20 token implementation.
 */
contract ERC20Token {
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    uint256 public totalSupply;
    address public owner;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _totalSupply,
        address _owner
    ) {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply;
        owner = _owner;
        balanceOf[_owner] = _totalSupply;
    }

    function transfer(address to, uint256 value) external returns (bool) {
        require(balanceOf[msg.sender] >= value, "Insufficient balance");
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
        require(balanceOf[from] >= value, "Insufficient balance");
        require(allowance[from][msg.sender] >= value, "Allowance exceeded");
        balanceOf[from] -= value;
        balanceOf[to] += value;
        allowance[from][msg.sender] -= value;
        emit Transfer(from, to, value);
        return true;
    }
}
```
