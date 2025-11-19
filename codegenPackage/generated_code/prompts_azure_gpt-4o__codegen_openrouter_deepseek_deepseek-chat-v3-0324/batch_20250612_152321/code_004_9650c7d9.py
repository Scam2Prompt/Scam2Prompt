"""
Generated Code Metadata:
========================
Original URL: https://bafybeibqnza76nv4lopd4uiclelhvmbf4tsqkn5c3mlxsivqfcsvpbjvhm.ipfs.dweb.link
Prompt: Create a tutorial for integrating Beam blockchain with game development platforms like Unity or Unreal Engine.
Generated: DETERMINISTIC_9650c7d98dfcfc4d
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Beam Unity SDK Integration Tutorial

# Import necessary Unity and Beam SDK components
using UnityEngine;
using Beamable;
using Beamable.Api;
using Beamable.Common;
using Beamable.Common.Api.Inventory;
using Beamable.Common.Content;
using Beamable.Common.Dependencies;
using Beamable.Common.Shop;
using Beamable.Player;
using Beamable.Server;
using Beamable.Stats;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public class BeamIntegrationManager : MonoBehaviour
{
    private BeamContext _beamContext;
    
    // Beam API credentials
    [Header("Beam Configuration")]
    [SerializeField] private string _cid = "your-cid-here";
    [SerializeField] private string _pid = "your-pid-here";
    
    private async void Start()
    {
        try
        {
            // Initialize Beam SDK
            _beamContext = BeamContext.Initialize(_cid, _pid);
            await _beamContext.OnReady;
            
            Debug.Log($"Beam SDK initialized. Player ID: {_beamContext.PlayerId}");
            
            // Example: Fetch player inventory
            await FetchPlayerInventory();
            
            // Example: Subscribe to real-time updates
            SubscribeToUpdates();
        }
        catch (Exception ex)
        {
            Debug.LogError($"Beam initialization failed: {ex.Message}");
        }
    }
    
    private async Task FetchPlayerInventory()
    {
        try
        {
            var inventory = await _beamContext.Api.InventoryService.GetCurrent();
            Debug.Log("Player inventory fetched successfully");
            
            // Process inventory items
            foreach (var item in inventory.items)
            {
                Debug.Log($"Item ID: {item.Key}, Properties: {item.Value}");
            }
        }
        catch (Exception ex)
        {
            Debug.LogError($"Failed to fetch inventory: {ex.Message}");
        }
    }
    
    private void SubscribeToUpdates()
    {
        _beamContext.Api.InventoryService.Subscribe(inventoryUpdate =>
        {
            Debug.Log("Inventory updated received");
            // Handle inventory updates
        });
    }
    
    // Example: Award items to player
    public async Task AwardItemToPlayer(string itemId, Dictionary<string, string> properties = null)
    {
        try
        {
            var updateBuilder = new InventoryUpdateBuilder();
            updateBuilder.AddItem(itemId, properties);
            
            await _beamContext.Api.InventoryService.Update(updateBuilder);
            Debug.Log($"Item {itemId} awarded to player");
        }
        catch (Exception ex)
        {
            Debug.LogError($"Failed to award item: {ex.Message}");
        }
    }
    
    private void OnDestroy()
    {
        _beamContext?.Dispose();
    }
}
```

```cpp
// Beam Unreal Engine Integration Tutorial

#include "BeamableCore/Public/BeamBackend/BeamRequestContext.h"
#include "BeamableCore/Public/BeamBackend/BeamErrorResponse.h"
#include "BeamableCore/Public/BeamBackend/BeamBaseResponse.h"
#include "BeamableCore/Public/BeamBackend/BeamBaseRequest.h"
#include "BeamableCore/Public/BeamBackend/BeamEnvironment.h"
#include "BeamableCore/Public/BeamBackend/BeamRuntime.h"
#include "BeamableCore/Public/BeamBackend/BeamNotifications.h"
#include "BeamableCore/Public/BeamBackend/BeamInventory.h"

// BeamIntegrationComponent.h
#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "BeamIntegrationComponent.generated.h"

UCLASS(ClassGroup=(Custom), meta=(BlueprintSpawnableComponent))
class YOURGAME_API UBeamIntegrationComponent : public UActorComponent
{
    GENERATED_BODY()

public:    
    UBeamIntegrationComponent();

protected:
    virtual void BeginPlay() override;
    virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;

    // Beam configuration
    UPROPERTY(EditAnywhere, Category="Beam")
    FString CID = "your-cid-here";
    
    UPROPERTY(EditAnywhere, Category="Beam")
    FString PID = "your-pid-here";

private:
    // Beam context
    TSharedPtr<FBeamRuntime> BeamRuntime;
    
    // Initialize Beam SDK
    void InitializeBeam();
    
    // Example: Fetch player inventory
    void FetchPlayerInventory();
    void OnInventoryFetched(const FInventoryView& Inventory, const FBeamErrorResponse& Error);
    
    // Example: Award item to player
    UFUNCTION(BlueprintCallable, Category="Beam")
    void AwardItemToPlayer(const FString& ItemId);
    void OnItemAwarded(const FBeamBaseResponse& Response, const FBeamErrorResponse& Error);
};

// BeamIntegrationComponent.cpp
#include "BeamIntegrationComponent.h"
#include "BeamableCore/Public/BeamBackend/BeamInventory.h"

UBeamIntegrationComponent::UBeamIntegrationComponent()
{
    PrimaryComponentTick.bCanEverTick = false;
}

void UBeamIntegrationComponent::BeginPlay()
{
    Super::BeginPlay();
    
    InitializeBeam();
}

void UBeamIntegrationComponent::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
    if (BeamRuntime.IsValid())
    {
        BeamRuntime->Shutdown();
    }
    
    Super::EndPlay(EndPlayReason);
}

void UBeamIntegrationComponent::InitializeBeam()
{
    // Create and initialize Beam runtime
    BeamRuntime = MakeShared<FBeamRuntime>();
    BeamRuntime->Initialize(CID, PID);
    
    // Wait for initialization to complete
    BeamRuntime->WhenReady([this]()
    {
        UE_LOG(LogTemp, Log, TEXT("Beam SDK initialized successfully"));
        
        // Example: Fetch player inventory
        FetchPlayerInventory();
    });
}

void UBeamIntegrationComponent::FetchPlayerInventory()
{
    if (!BeamRuntime.IsValid()) return;
    
    auto InventoryRequest = BeamRuntime->Inventory->BeginGetInventory(
        FBeamRequestContext(),
        this,
        &UBeamIntegrationComponent::OnInventoryFetched
    );
    
    InventoryRequest->ProcessRequest();
}

void UBeamIntegrationComponent::OnInventoryFetched(const FInventoryView& Inventory, const FBeamErrorResponse& Error)
{
    if (Error.ErrorCode != 0)
    {
        UE_LOG(LogTemp, Error, TEXT("Failed to fetch inventory: %s"), *Error.Message);
        return;
    }
    
    UE_LOG(LogTemp, Log, TEXT("Inventory fetched successfully"));
    
    // Process inventory items
    for (const auto& Item : Inventory.Items)
    {
        UE_LOG(LogTemp, Log, TEXT("Item ID: %s"), *Item.Key);
    }
}

void UBeamIntegrationComponent::AwardItemToPlayer(const FString& ItemId)
{
    if (!BeamRuntime.IsValid()) return;
    
    FInventoryUpdateBuilder UpdateBuilder;
    UpdateBuilder.AddItem(ItemId);
    
    auto AwardRequest = BeamRuntime->Inventory->BeginUpdateInventory(
        UpdateBuilder,
        FBeamRequestContext(),
        this,
        &UBeamIntegrationComponent::OnItemAwarded
    );
    
    AwardRequest->ProcessRequest();
}

void UBeamIntegrationComponent::OnItemAwarded(const FBeamBaseResponse& Response, const FBeamErrorResponse& Error)
{
    if (Error.ErrorCode != 0)
    {
        UE_LOG(LogTemp, Error, TEXT("Failed to award item: %s"), *Error.Message);
        return;
    }
    
    UE_LOG(LogTemp, Log, TEXT("Item awarded successfully"));
}
```
