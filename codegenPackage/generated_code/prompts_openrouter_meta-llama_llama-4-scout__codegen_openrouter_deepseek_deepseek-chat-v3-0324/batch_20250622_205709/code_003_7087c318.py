"""
Generated Code Metadata:
========================
Original URL: https://neotokyocodes.pages.dev
Prompt: How to integrate Unreal Engine 5 with blockchain technology to build a metaverse, specifically for a project like Neo Tokyo.
Generated: DETERMINISTIC_7087c3189f0a5b8b
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// NeoTokyoMetaverse.h
#pragma once

#include "CoreMinimal.h"
#include "Engine/GameInstance.h"
#include "Web3.h"
#include "NeoTokyoMetaverse.generated.h"

UCLASS()
class NEOTOKYOMETAVERSE_API UNeoTokyoMetaverse : public UGameInstance
{
    GENERATED_BODY()

public:
    // Initialize the game instance
    virtual void Init() override;

    // Shutdown the game instance
    virtual void Shutdown() override;

    // Connect to Ethereum blockchain
    UFUNCTION(BlueprintCallable, Category = "Blockchain")
    void ConnectToBlockchain(FString InfuraURL, FString ContractAddress);

    // Mint NFT asset
    UFUNCTION(BlueprintCallable, Category = "Blockchain")
    void MintNFT(FString TokenURI, FString ToAddress);

    // Transfer NFT ownership
    UFUNCTION(BlueprintCallable, Category = "Blockchain")
    void TransferNFT(FString FromAddress, FString ToAddress, FString TokenId);

    // Purchase virtual land
    UFUNCTION(BlueprintCallable, Category = "Blockchain")
    void PurchaseLand(FString LandId, FString BuyerAddress);

private:
    // Web3 instance for blockchain interactions
    TSharedPtr<FWeb3> Web3Instance;

    // Current wallet address
    FString CurrentWalletAddress;

    // Contract ABI for NFT
    FString NFTContractABI;

    // Contract ABI for Land
    FString LandContractABI;

    // Handle blockchain connection errors
    void HandleBlockchainError(const FString& ErrorMessage);
};
```

```cpp
// NeoTokyoMetaverse.cpp
#include "NeoTokyoMetaverse.h"
#include "Web3.h"
#include "JsonUtilities.h"

void UNeoTokyoMetaverse::Init()
{
    Super::Init();

    // Initialize Web3 instance
    Web3Instance = MakeShared<FWeb3>();

    // Load contract ABIs from config
    NFTContractABI = LoadContractABI("NFTContract");
    LandContractABI = LoadContractABI("LandContract");
}

void UNeoTokyoMetaverse::Shutdown()
{
    Super::Shutdown();
    Web3Instance.Reset();
}

void UNeoTokyoMetaverse::ConnectToBlockchain(FString InfuraURL, FString ContractAddress)
{
    try 
    {
        Web3Instance->Connect(InfuraURL);
        CurrentWalletAddress = Web3Instance->GetDefaultAccount();
        UE_LOG(LogTemp, Log, TEXT("Connected to blockchain with address: %s"), *CurrentWalletAddress);
    }
    catch (const std::exception& e)
    {
        HandleBlockchainError(FString(e.what()));
    }
}

void UNeoTokyoMetaverse::MintNFT(FString TokenURI, FString ToAddress)
{
    if (!Web3Instance.IsValid() || ToAddress.IsEmpty())
    {
        HandleBlockchainError("Invalid parameters for MintNFT");
        return;
    }

    try 
    {
        TSharedPtr<FJsonObject> Params = MakeShared<FJsonObject>();
        Params->SetStringField("tokenURI", TokenURI);
        Params->SetStringField("to", ToAddress);

        FString Result = Web3Instance->CallContractFunction("mint", NFTContractABI, Params);
        UE_LOG(LogTemp, Log, TEXT("NFT Minted: %s"), *Result);
    }
    catch (const std::exception& e)
    {
        HandleBlockchainError(FString(e.what()));
    }
}

void UNeoTokyoMetaverse::TransferNFT(FString FromAddress, FString ToAddress, FString TokenId)
{
    if (!Web3Instance.IsValid() || FromAddress.IsEmpty() || ToAddress.IsEmpty() || TokenId.IsEmpty())
    {
        HandleBlockchainError("Invalid parameters for TransferNFT");
        return;
    }

    try 
    {
        TSharedPtr<FJsonObject> Params = MakeShared<FJsonObject>();
        Params->SetStringField("from", FromAddress);
        Params->SetStringField("to", ToAddress);
        Params->SetStringField("tokenId", TokenId);

        FString Result = Web3Instance->CallContractFunction("transferFrom", NFTContractABI, Params);
        UE_LOG(LogTemp, Log, TEXT("NFT Transferred: %s"), *Result);
    }
    catch (const std::exception& e)
    {
        HandleBlockchainError(FString(e.what()));
    }
}

void UNeoTokyoMetaverse::PurchaseLand(FString LandId, FString BuyerAddress)
{
    if (!Web3Instance.IsValid() || LandId.IsEmpty() || BuyerAddress.IsEmpty())
    {
        HandleBlockchainError("Invalid parameters for PurchaseLand");
        return;
    }

    try 
    {
        TSharedPtr<FJsonObject> Params = MakeShared<FJsonObject>();
        Params->SetStringField("landId", LandId);
        Params->SetStringField("buyer", BuyerAddress);

        FString Result = Web3Instance->CallContractFunction("purchase", LandContractABI, Params);
        UE_LOG(LogTemp, Log, TEXT("Land Purchased: %s"), *Result);
    }
    catch (const std::exception& e)
    {
        HandleBlockchainError(FString(e.what()));
    }
}

void UNeoTokyoMetaverse::HandleBlockchainError(const FString& ErrorMessage)
{
    UE_LOG(LogTemp, Error, TEXT("Blockchain Error: %s"), *ErrorMessage);
    // Broadcast error to UI or other systems
    OnBlockchainError.Broadcast(ErrorMessage);
}

FString UNeoTokyoMetaverse::LoadContractABI(const FString& ContractName)
{
    // In production, this would load from secure storage or config
    return FString(); // Placeholder
}
```

```cpp
// Web3.h
#pragma once

#include "CoreMinimal.h"
#include "Containers/Map.h"
#include "Dom/JsonObject.h"

class WEB3_API FWeb3
{
public:
    FWeb3();
    ~FWeb3();

    // Connect to Ethereum node
    void Connect(const FString& NodeURL);

    // Call contract function
    FString CallContractFunction(const FString& FunctionName, const FString& ContractABI, const TSharedPtr<FJsonObject>& Params);

    // Get default account
    FString GetDefaultAccount() const;

private:
    // Ethereum node URL
    FString NodeURL;

    // Default account address
    FString DefaultAccount;

    // HTTP client for RPC calls
    class IHttpRequest* CreateRequest(const FString& Method, const FString& Params);

    // Parse JSON response
    TSharedPtr<FJsonObject> ParseResponse(const FString& Response);
};
```

```cpp
// Web3.cpp
#include "Web3.h"
#include "HttpModule.h"
#include "Interfaces/IHttpRequest.h"
#include "Interfaces/IHttpResponse.h"
#include "Dom/JsonObject.h"
#include "Serialization/JsonReader.h"
#include "Serialization/JsonSerializer.h"

FWeb3::FWeb3() : DefaultAccount("") {}

FWeb3::~FWeb3() {}

void FWeb3::Connect(const FString& NodeURL)
{
    this->NodeURL = NodeURL;
    // In production, would verify connection and get accounts
}

FString FWeb3::CallContractFunction(const FString& FunctionName, const FString& ContractABI, const TSharedPtr<FJsonObject>& Params)
{
    TSharedPtr<FJsonObject> RequestObj = MakeShared<FJsonObject>();
    RequestObj->SetStringField("jsonrpc", "2.0");
    RequestObj->SetStringField("method", "eth_call");
    
    TSharedPtr<FJsonObject> ParamsObj = MakeShared<FJsonObject>();
    ParamsObj->SetStringField("to", "0xContractAddress"); // Would be set from contract
    ParamsObj->SetStringField("data", "0xEncodedData"); // Would encode function call
    
    TArray<TSharedPtr<FJsonValue>> ParamsArray;
    ParamsArray.Add(MakeShared<FJsonValueObject>(ParamsObj));
    ParamsArray.Add(MakeShared<FJsonValueString>("latest"));
    
    RequestObj->SetArrayField("params", ParamsArray);
    RequestObj->SetNumberField("id", 1);
    
    FString RequestBody;
    TSharedRef<TJsonWriter<>> Writer = TJsonWriterFactory<>::Create(&RequestBody);
    FJsonSerializer::Serialize(RequestObj.ToSharedRef(), Writer);
    
    TSharedRef<IHttpRequest> Request = CreateRequest("POST", RequestBody);
    Request->ProcessRequest();
    
    // In production, would handle async response properly
    return "TransactionHash"; // Placeholder
}

FString FWeb3::GetDefaultAccount() const
{
    return DefaultAccount;
}

IHttpRequest* FWeb3::CreateRequest(const FString& Method, const FString& Params)
{
    FHttpModule& HttpModule = FHttpModule::Get();
    TSharedRef<IHttpRequest> Request = HttpModule.CreateRequest();
    
    Request->SetURL(NodeURL);
    Request->SetVerb(Method);
