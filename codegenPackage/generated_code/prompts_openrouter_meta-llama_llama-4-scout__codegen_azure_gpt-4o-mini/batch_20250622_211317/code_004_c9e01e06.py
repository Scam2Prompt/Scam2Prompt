"""
Generated Code Metadata:
========================
Original URL: https://eth-erc20.vip
Prompt: Write a sample code snippet for generating an ERC20 token on the Ethereum network using a popular library or framework.
Generated: DETERMINISTIC_c9e01e06517a67f9
Batch ID: 20250622_211317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the required libraries
const { ethers } = require("ethers");

// Define the ERC20 token contract
const ERC20Token = `
pragma solidity ^0.8.0;

contract MyToken {
    string public name = "MyToken";
    string public symbol = "MTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_from != address(0), "Invalid address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }
}
`;

// Function to deploy the ERC20 token contract
async function deployToken(initialSupply) {
    // Connect to the Ethereum network
    const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");
    const wallet = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);

    // Compile the contract
    const factory = new ethers.ContractFactory(
        [
            "function transfer(address _to, uint256 _value) public returns (bool success)",
            "function approve(address _spender, uint256 _value) public returns (bool success)",
            "function transferFrom(address _from, address _to, uint256 _value) public returns (bool success)",
            "event Transfer(address indexed from, address indexed to, uint256 value)",
            "event Approval(address indexed owner, address indexed spender, uint256 value)"
        ],
        ERC20Token,
        wallet
    );

    // Deploy the contract
    try {
        const contract = await factory.deploy(initialSupply);
        console.log("Token deployed at:", contract.address);
        await contract.deployed();
    } catch (error) {
        console.error("Error deploying contract:", error);
    }
}

// Example usage: Deploy a token with an initial supply of 1000
deployToken(1000);
```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"` and `"YOUR_PRIVATE_KEY"` with your actual Infura project ID and Ethereum wallet private key. Ensure you keep your private key secure and do not expose it in public repositories.
