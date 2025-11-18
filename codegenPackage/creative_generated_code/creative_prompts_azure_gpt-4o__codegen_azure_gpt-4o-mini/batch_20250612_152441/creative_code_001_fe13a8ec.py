"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Generate Unreal Engine code to implement a "jetpack" feature in a multiplayer game, allowing players to fly until their energy indicator reaches zero, as described in the Artyfact metaverse.
Generated: DETERMINISTIC_fe13a8ecd2a95b9d
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
// JetpackComponent.h

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "JetpackComponent.generated.h"

// Delegate for notifying when jetpack energy changes
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnJetpackEnergyChanged, float, NewEnergyLevel);

/**
 * UJetpackComponent allows the player to fly using a jetpack until energy is depleted.
 */
UCLASS(ClassGroup=(Custom), meta=(BlueprintSpawnableComponent))
class ARTYFACT_API UJetpackComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    // Sets default values for this component's properties
    UJetpackComponent();

protected:
    // Called when the game starts
    virtual void BeginPlay() override;

public:
    // Called every frame
    virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

    // Activate the jetpack
    void ActivateJetpack();

    // Deactivate the jetpack
    void DeactivateJetpack();

    // Check if jetpack is currently active
    bool IsJetpackActive() const;

    // Event triggered when energy level changes
    UPROPERTY(BlueprintAssignable)
    FOnJetpackEnergyChanged OnJetpackEnergyChanged;

private:
    // Jetpack energy level
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Jetpack", meta = (AllowPrivateAccess = "true"))
    float MaxEnergy;

    // Current energy level
    float CurrentEnergy;

    // Jetpack flying thrust
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Jetpack", meta = (AllowPrivateAccess = "true"))
    float ThrustForce;

    // Duration for jetpack usage
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Jetpack", meta = (AllowPrivateAccess = "true"))
    float EnergyConsumptionRate;

    // Flag to track jetpack activation
    bool bIsJetpackActive;

    // Handles jetpack functionality
    void HandleJetpackMovement(float DeltaTime);

    // Update current energy level
    void UpdateEnergy(float DeltaTime);
};
```

```cpp
// JetpackComponent.cpp

#include "JetpackComponent.h"
#include "GameFramework/Actor.h"
#include "GameFramework/Character.h"
#include "GameFramework/CharacterMovementComponent.h"

// Sets default values for this component's properties
UJetpackComponent::UJetpackComponent()
{
    PrimaryComponentTick.bCanEverTick = true;
    MaxEnergy = 100.0f;
    CurrentEnergy = MaxEnergy;
    ThrustForce = 1000.0f;
    EnergyConsumptionRate = 20.0f;
    bIsJetpackActive = false;
}

// Called when the game starts
void UJetpackComponent::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void UJetpackComponent::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
    Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

    // Handle jetpack movement if active
    if (bIsJetpackActive)
    {
        HandleJetpackMovement(DeltaTime);
        UpdateEnergy(DeltaTime);
    }
}

// Activate the jetpack
void UJetpackComponent::ActivateJetpack()
{
    if (!bIsJetpackActive && CurrentEnergy > 0)
    {
        bIsJetpackActive = true;
        UE_LOG(LogTemp, Warning, TEXT("Jetpack activated!"));
    }
}

// Deactivate the jetpack
void UJetpackComponent::DeactivateJetpack()
{
    if (bIsJetpackActive)
    {
        bIsJetpackActive = false;
        UE_LOG(LogTemp, Warning, TEXT("Jetpack deactivated!"));
    }
}

// Check if jetpack is currently active
bool UJetpackComponent::IsJetpackActive() const
{
    return bIsJetpackActive;
}

// Handles jetpack functionality
void UJetpackComponent::HandleJetpackMovement(float DeltaTime)
{
    ACharacter* CharacterOwner = Cast<ACharacter>(GetOwner());
    if (CharacterOwner)
    {
        FVector UpwardThrust = FVector::UpVector * ThrustForce;
        CharacterOwner->GetCharacterMovement()->AddForce(UpwardThrust);
    }
}

// Update current energy level
void UJetpackComponent::UpdateEnergy(float DeltaTime)
{
    if (CurrentEnergy > 0)
    {
        CurrentEnergy -= EnergyConsumptionRate * DeltaTime;
        CurrentEnergy = FMath::Max(CurrentEnergy, 0.0f); // Ensure energy doesn't go below 0
        OnJetpackEnergyChanged.Broadcast(CurrentEnergy); // Notify listeners

        // Deactivate jetpack if energy is depleted
        if (CurrentEnergy <= 0)
        {
            DeactivateJetpack();
        }
    }
}
```

```cpp
// Example usage in a character class

// MyCharacter.h

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "MyCharacter.generated.h"

UCLASS()
class ARTYFACT_API AMyCharacter : public ACharacter
{
    GENERATED_BODY()

public:
    AMyCharacter();

protected:
    virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;

private:
    UPROPERTY(VisibleAnywhere)
    UJetpackComponent* JetpackComponent;

    void ToggleJetpack();
};
```

```cpp
// MyCharacter.cpp

#include "MyCharacter.h"
#include "JetpackComponent.h"

AMyCharacter::AMyCharacter()
{
    // Create the Jetpack component
    JetpackComponent = CreateDefaultSubobject<UJetpackComponent>(TEXT("JetpackComponent"));
}

// Setup input bindings
void AMyCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
    Super::SetupPlayerInputComponent(PlayerInputComponent);
    
    // Bind jetpack toggle to an input action
    PlayerInputComponent->BindAction("ToggleJetpack", IE_Pressed, this, &AMyCharacter::ToggleJetpack);
}

// Toggle jetpack activation
void AMyCharacter::ToggleJetpack()
{
    if (JetpackComponent)
    {
        if (JetpackComponent->IsJetpackActive())
        {
            JetpackComponent->DeactivateJetpack();
        }
        else
        {
            JetpackComponent->ActivateJetpack();
        }
    }
}
```

**Note:** Remember to create an input action named "ToggleJetpack" in your project settings to test the jetpack functionality.
