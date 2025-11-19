"""
Generated Code Metadata:
========================
Original URL: https://anyinumult.pages.dev
Prompt: Write a script to deploy and manage Any Inu's token on a new EVM chain, using permissionless bridge providers and Axelar's Interchain token service.
Generated: DETERMINISTIC_a639ce21cc12e17e
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@axelar-network/axelar-gmp-sdk-solidity/contracts/interfaces/IAxelarGateway.sol";
import "@axelar-network/axelar-gmp-sdk-solidity/contracts/interfaces/IAxelarGasService.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AnyInuToken
 * @dev ERC20 token with Axelar interchain capabilities
 */
contract AnyInuToken is ERC20, Ownable {
    IAxelarGateway public gateway;
    IAxelarGasService public gasService;
    string public chainName;

    /**
     * @dev Constructor to initialize the token
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _initialSupply Initial token supply
     * @param _gateway Axelar gateway address
     * @param _gasService Axelar gas service address
     * @param _chainName Name of the current chain
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        address _gateway,
        address _gasService,
        string memory _chainName
    ) ERC20(_name, _symbol) {
        _mint(msg.sender, _initialSupply);
        gateway = IAxelarGateway(_gateway);
        gasService = IAxelarGasService(_gasService);
        chainName = _chainName;
    }

    /**
     * @dev Mint new tokens (owner only)
     * @param to Address to receive tokens
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens (owner only)
     * @param from Address to burn from
     * @param amount Amount to burn
     */
    function burn(address from, uint256 amount) public onlyOwner {
        _burn(from, amount);
    }

    /**
     * @dev Send tokens to another chain via Axelar
     * @param destinationChain Name of destination chain
     * @param destinationAddress Address on destination chain
     * @param symbol Token symbol
     * @param amount Amount to send
     */
    function sendToChain(
        string calldata destinationChain,
        string calldata destinationAddress,
        string calldata symbol,
        uint256 amount
    ) external payable {
        require(msg.value > 0, "Gas payment required");
        require(amount > 0, "Amount must be positive");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _burn(msg.sender, amount);

        bytes memory payload = abi.encode(destinationAddress, amount);
        gasService.payNativeGasForContractCall{value: msg.value}(
            address(this),
            destinationChain,
            destinationAddress,
            payload,
            msg.sender
        );

        gateway.callContract(
            destinationChain,
            destinationAddress,
            payload
        );
    }

    /**
     * @dev Execute token reception from another chain
     * @param sourceChain Name of source chain
     * @param sourceAddress Address on source chain
     * @param payload Encoded (destinationAddress, amount)
     */
    function execute(
        string calldata sourceChain,
        string calldata sourceAddress,
        bytes calldata payload
    ) external {
        require(msg.sender == address(gateway), "Only gateway can call");
        
        (address recipient, uint256 amount) = abi.decode(payload, (address, uint256));
        _mint(recipient, amount);
    }
}

/**
 * @title AnyInuDeployer
 * @dev Helper contract to deploy and manage AnyInuToken across chains
 */
contract AnyInuDeployer {
    address public owner;
    mapping(string => address) public deployedTokens;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call");
        _;
    }

    /**
     * @dev Deploy token on current chain
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     * @param gateway Axelar gateway address
     * @param gasService Axelar gas service address
     * @param chainName Name of the current chain
     */
    function deployToken(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address gateway,
        address gasService,
        string memory chainName
    ) external onlyOwner returns (address) {
        require(deployedTokens[chainName] == address(0), "Token already deployed on this chain");

        AnyInuToken token = new AnyInuToken(
            name,
            symbol,
            initialSupply,
            gateway,
            gasService,
            chainName
        );

        deployedTokens[chainName] = address(token);
        return address(token);
    }

    /**
     * @dev Get token address for a chain
     * @param chainName Name of the chain
     */
    function getTokenAddress(string memory chainName) external view returns (address) {
        return deployedTokens[chainName];
    }
}
```
