"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: What are some strategies for implementing a sustainable, interactive farming system in a game, and how might this be achieved using a game engine like Unity or Unreal Engine?
Generated: DETERMINISTIC_486381b164c422a0
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
// SustainableFarmingSystem.cs
using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Represents a crop that can be planted and harvested
/// </summary>
[System.Serializable]
public class Crop
{
    public string name;
    public GameObject prefab;
    public float growthTime; // in seconds
    public int yieldAmount;
    public int waterRequirement; // per growth stage
    public bool isHarvestable;
    public int currentGrowthStage;
    public int maxGrowthStages = 4;
    public float currentWater;
    public bool isWilted;

    public void WaterCrop(int amount)
    {
        currentWater += amount;
        if (currentWater >= waterRequirement)
        {
            currentWater = 0;
            AdvanceGrowthStage();
        }
    }

    public void AdvanceGrowthStage()
    {
        if (currentGrowthStage < maxGrowthStages)
        {
            currentGrowthStage++;
            if (currentGrowthStage == maxGrowthStages)
            {
                isHarvestable = true;
            }
        }
    }

    public void CheckWiltStatus()
    {
        if (currentWater <= 0 && currentGrowthStage > 0)
        {
            isWilted = true;
            isHarvestable = false;
        }
    }
}

/// <summary>
/// Manages the farming system including planting, growing, and harvesting crops
/// </summary>
public class SustainableFarmingSystem : MonoBehaviour
{
    public List<Crop> availableCrops = new List<Crop>();
    public Dictionary<Vector3Int, Crop> plantedCrops = new Dictionary<Vector3Int, Crop>();
    public GameObject farmingGrid;
    public float timeScale = 1f; // For speeding up time for testing

    private float growthTimer;

    private void Update()
    {
        // Update growth timer
        growthTimer += Time.deltaTime * timeScale;

        // Check growth every second (game time)
        if (growthTimer >= 1f)
        {
            growthTimer = 0f;
            UpdateCropGrowth();
        }
    }

    /// <summary>
    /// Plants a crop at the specified grid position
    /// </summary>
    public bool PlantCrop(Vector3Int gridPosition, int cropIndex)
    {
        if (plantedCrops.ContainsKey(gridPosition) || cropIndex < 0 || cropIndex >= availableCrops.Count)
        {
            return false;
        }

        Crop newCrop = new Crop
        {
            name = availableCrops[cropIndex].name,
            prefab = availableCrops[cropIndex].prefab,
            growthTime = availableCrops[cropIndex].growthTime,
            yieldAmount = availableCrops[cropIndex].yieldAmount,
            waterRequirement = availableCrops[cropIndex].waterRequirement,
            currentGrowthStage = 0,
            currentWater = 0,
            isHarvestable = false,
            isWilted = false
        };

        GameObject cropInstance = Instantiate(newCrop.prefab, gridPosition, Quaternion.identity, farmingGrid.transform);
        plantedCrops.Add(gridPosition, newCrop);
        return true;
    }

    /// <summary>
    /// Waters the crop at the specified position
    /// </summary>
    public bool WaterCrop(Vector3Int gridPosition, int waterAmount)
    {
        if (!plantedCrops.ContainsKey(gridPosition)) return false;

        Crop crop = plantedCrops[gridPosition];
        crop.WaterCrop(waterAmount);
        return true;
    }

    /// <summary>
    /// Harvests the crop at the specified position if it's ready
    /// </summary>
    public bool HarvestCrop(Vector3Int gridPosition, out int yield)
    {
        yield = 0;
        if (!plantedCrops.ContainsKey(gridPosition)) return false;

        Crop crop = plantedCrops[gridPosition];
        if (!crop.isHarvestable) return false;

        yield = crop.yieldAmount;
        plantedCrops.Remove(gridPosition);
        // Destroy the crop GameObject here (implementation depends on your setup)
        return true;
    }

    /// <summary>
    /// Updates all crops' growth status
    /// </summary>
    private void UpdateCropGrowth()
    {
        List<Vector3Int> positionsToRemove = new List<Vector3Int>();

        foreach (KeyValuePair<Vector3Int, Crop> entry in plantedCrops)
        {
            Crop crop = entry.Value;
            crop.CheckWiltStatus();

            if (crop.isWilted)
            {
                positionsToRemove.Add(entry.Key);
                continue;
            }

            // Natural growth over time
            if (Random.Range(0f, 1f) < 0.1f) // 10% chance per second to grow naturally
            {
                crop.AdvanceGrowthStage();
            }
        }

        // Remove wilted crops
        foreach (Vector3Int position in positionsToRemove)
        {
            plantedCrops.Remove(position);
            // Destroy the crop GameObject here
        }
    }

    /// <summary>
    /// Rotates crops to maintain soil health
    /// </summary>
    public void RotateCrops()
    {
        // Implementation would track crop types planted in each position
        // and enforce rotation rules to prevent soil depletion
    }

    /// <summary>
    /// Gets soil quality at position (for future soil health system)
    /// </summary>
    public float GetSoilQuality(Vector3Int position)
    {
        // Base implementation - would be enhanced with soil tracking
        return 1f;
    }
}
```

```cpp
// SustainableFarmingSystem.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "SustainableFarmingSystem.generated.h"

USTRUCT(BlueprintType)
struct FCropData
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString Name;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    UClass* CropClass;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float GrowthTime;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    int32 YieldAmount;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    int32 WaterRequirement;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    int32 CurrentGrowthStage;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    float CurrentWater;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    bool bIsHarvestable;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    bool bIsWilted;

    void WaterCrop(int32 Amount);
    void AdvanceGrowthStage();
    void CheckWiltStatus();
};

UCLASS()
class FARMINGSIM_API ASustainableFarmingSystem : public AActor
{
    GENERATED_BODY()

public:
    ASustainableFarmingSystem();

protected:
    virtual void BeginPlay() override;
    virtual void Tick(float DeltaTime) override;

public:
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Farming")
    TArray<FCropData> AvailableCrops;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Farming")
    float TimeScale = 1.0f;

    UFUNCTION(BlueprintCallable, Category = "Farming")
    bool PlantCrop(FVector Location, int32 CropIndex);

    UFUNCTION(BlueprintCallable, Category = "Farming")
    bool WaterCrop(FVector Location, int32 WaterAmount);

    UFUNCTION(BlueprintCallable, Category = "Farming")
    bool HarvestCrop(FVector Location, int32& Yield);

private:
    TMap<FVector, FCropData> PlantedCrops;
    float GrowthTimer;

    void UpdateCropGrowth(float DeltaTime);
    void RotateCrops();
    float GetSoilQuality(FVector Location) const;
};

// SustainableFarmingSystem.cpp
#include "SustainableFarmingSystem.h"

void FCropData::WaterCrop(int32 Amount)
{
    CurrentWater += Amount;
    if (CurrentWater >= WaterRequirement)
    {
        CurrentWater = 0;
        AdvanceGrowthStage();
    }
}

void FCropData::AdvanceGrowthStage()
{
    if (CurrentGrowthStage < 4) // Assuming 4 growth stages
    {
        CurrentGrowthStage++;
        if (CurrentGrowthStage == 4)
        {
            bIsHarvestable = true;
        }
    }
}

void FCropData::CheckWiltStatus()
{
    if (CurrentWater <= 0 && CurrentGrowthStage > 0)
    {
        bIsWilted = true;
        bIsHarvestable = false;
    }
}

ASustainableFarmingSystem::ASustainableFarmingSystem()
{
    PrimaryActorTick.bCanEverTick = true;
}

void ASustainableFarmingSystem::BeginPlay()
{
    Super::BeginPlay();
    GrowthTimer = 0.0f;
}

void ASustainableFarmingSystem::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
    UpdateCropGrowth(DeltaTime);
}

bool ASustainableFarmingSystem::PlantCrop(FVector Location
