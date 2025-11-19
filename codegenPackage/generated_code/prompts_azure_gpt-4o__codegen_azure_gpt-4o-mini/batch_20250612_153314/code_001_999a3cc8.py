"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnfts.com
Prompt: Generate Unreal Engine 5 code snippets for creating customizable domes in the Cornucopias MMORPG, ensuring compatibility with player-driven economies and digital asset ownership.
Generated: DETERMINISTIC_999a3cc825e2b3ac
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// DomeActor.h

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "DomeActor.generated.h"

// Enum to define dome customization options
UENUM(BlueprintType)
enum class EDomeType : uint8
{
    DomeType_Small UMETA(DisplayName = "Small Dome"),
    DomeType_Medium UMETA(DisplayName = "Medium Dome"),
    DomeType_Large UMETA(DisplayName = "Large Dome"),
};

// Structure to hold dome customization properties
USTRUCT(BlueprintType)
struct FDomeCustomization
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Dome Customization")
    EDomeType DomeType;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Dome Customization")
    FColor DomeColor;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Dome Customization")
    float DomeHeight;

    FDomeCustomization()
        : DomeType(EDomeType::DomeType_Medium), DomeColor(FColor::White), DomeHeight(300.0f) {}
};

UCLASS()
class CORNUCOPIAS_API ADomeActor : public AActor
{
    GENERATED_BODY()

public:
    // Sets default values for this actor's properties
    ADomeActor();

protected:
    // Called when the game starts or when spawned
    virtual void BeginPlay() override;

public:
    // Called every frame
    virtual void Tick(float DeltaTime) override;

    // Function to customize the dome
    UFUNCTION(BlueprintCallable, Category = "Dome")
    void CustomizeDome(const FDomeCustomization& Customization);

private:
    // Mesh component for the dome
    UPROPERTY(VisibleAnywhere)
    UStaticMeshComponent* DomeMesh;

    // Function to apply customization to the dome mesh
    void ApplyCustomization(const FDomeCustomization& Customization);
};

// DomeActor.cpp

#include "DomeActor.h"

// Sets default values
ADomeActor::ADomeActor()
{
    PrimaryActorTick.bCanEverTick = true;

    // Create and initialize the dome mesh component
    DomeMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("DomeMesh"));
    RootComponent = DomeMesh;

    // Set a default mesh (ensure you have a valid mesh in your project)
    static ConstructorHelpers::FObjectFinder<UStaticMesh> DomeMeshAsset(TEXT("StaticMesh'/Game/Path/To/YourDomeMesh.YourDomeMesh'"));
    if (DomeMeshAsset.Succeeded())
    {
        DomeMesh->SetStaticMesh(DomeMeshAsset.Object);
    }
}

// Called when the game starts or when spawned
void ADomeActor::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void ADomeActor::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
}

// Customize the dome based on the provided customization struct
void ADomeActor::CustomizeDome(const FDomeCustomization& Customization)
{
    ApplyCustomization(Customization);
}

// Apply customization to the dome mesh
void ADomeActor::ApplyCustomization(const FDomeCustomization& Customization)
{
    // Set the dome color
    DomeMesh->SetMaterial(0, UMaterialInstanceDynamic::Create(DomeMesh->GetMaterial(0), this));
    DomeMesh->GetMaterial(0)->SetVectorParameterValue(FName("DomeColor"), Customization.DomeColor);

    // Adjust the scale based on dome type
    FVector NewScale;
    switch (Customization.DomeType)
    {
        case EDomeType::DomeType_Small:
            NewScale = FVector(0.5f, 0.5f, 0.5f);
            break;
        case EDomeType::DomeType_Medium:
            NewScale = FVector(1.0f, 1.0f, 1.0f);
            break;
        case EDomeType::DomeType_Large:
            NewScale = FVector(1.5f, 1.5f, 1.5f);
            break;
        default:
            NewScale = FVector(1.0f, 1.0f, 1.0f);
            break;
    }
    DomeMesh->SetWorldScale3D(NewScale);

    // Set the height of the dome (if applicable)
    FVector NewLocation = GetActorLocation();
    NewLocation.Z = Customization.DomeHeight;
    SetActorLocation(NewLocation);
}
```
