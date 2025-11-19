"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Generate Unreal Engine code to implement a "jetpack" feature in a multiplayer game, allowing players to fly until their energy indicator reaches zero, as described in the Artyfact metaverse.
Generated: DETERMINISTIC_fe13a8ecd2a95b9d
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**JetpackComponent.h**
```cpp
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/ActorComponent.h"
#include "JetpackComponent.generated.h"

UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class YOURGAME_API UJetpackComponent : public UActorComponent
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

    // Function to activate the jetpack
    UFUNCTION(BlueprintCallable, Category = "Jetpack")
    void ActivateJetpack();

    // Function to deactivate the jetpack
    UFUNCTION(BlueprintCallable, Category = "Jetpack")
    void DeactivateJetpack();

    // Function to get the current energy level
    UFUNCTION(BlueprintCallable, Category = "Jetpack")
    float GetEnergyLevel() const;

private:
    // Jetpack properties
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Jetpack")
    float MaxEnergy;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Jetpack")
    float EnergyDrainRate;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Jetpack")
    float JetpackSpeed;

    // Current energy level
    float CurrentEnergy;

    // Is the jetpack active?
    bool IsJetpackActive;

    // Reference to the owning actor
    AActor* OwningActor;

    // Movement component
    UPROPERTY()
    class UCharacterMovementComponent* MovementComponent;
};
```

**JetpackComponent.cpp**
```cpp
#include "JetpackComponent.h"
#include "GameFramework/Character.h"
#include "GameFramework/CharacterMovementComponent.h"

UJetpackComponent::UJetpackComponent()
{
    // Set this component to call TickComponent() every frame.  You can turn this off to improve performance if you don't need it.
    PrimaryComponentTick.bCanEverTick = true;

    // Initialize jetpack properties
    MaxEnergy = 100.0f;
    EnergyDrainRate = 5.0f;
    JetpackSpeed = 500.0f;

    // Initialize current energy level and jetpack state
    CurrentEnergy = MaxEnergy;
    IsJetpackActive = false;
}

void UJetpackComponent::BeginPlay()
{
    Super::BeginPlay();

    // Get the owning actor
    OwningActor = GetOwner();

    // Get the movement component
    MovementComponent = OwningActor->FindComponentByClass<UCharacterMovementComponent>();
}

void UJetpackComponent::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
    Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

    // If the jetpack is active, drain energy and apply movement
    if (IsJetpackActive)
    {
        // Drain energy
        CurrentEnergy -= EnergyDrainRate * DeltaTime;

        // Check if energy is depleted
        if (CurrentEnergy <= 0.0f)
        {
            DeactivateJetpack();
            CurrentEnergy = 0.0f;
        }

        // Apply movement
        if (MovementComponent)
        {
            MovementComponent->AddImpulse(OwningActor->GetActorUpVector() * JetpackSpeed * DeltaTime, true);
        }
    }
}

void UJetpackComponent::ActivateJetpack()
{
    // Check if the jetpack is not already active
    if (!IsJetpackActive)
    {
        IsJetpackActive = true;
    }
}

void UJetpackComponent::DeactivateJetpack()
{
    // Check if the jetpack is active
    if (IsJetpackActive)
    {
        IsJetpackActive = false;
    }
}

float UJetpackComponent::GetEnergyLevel() const
{
    return CurrentEnergy;
}
```

**JetpackUsageExample.h**
```cpp
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "JetpackUsageExample.generated.h"

UCLASS()
class YOURGAME_API AJetpackUsageExample : public ACharacter
{
    GENERATED_BODY()

public:
    // Sets default values for this character's properties
    AJetpackUsageExample();

protected:
    // Called when the game starts
    virtual void BeginPlay() override;

public:
    // Called every frame
    virtual void Tick(float DeltaTime) override;

    // Function to handle jetpack activation
    UFUNCTION()
    void ActivateJetpack();

    // Function to handle jetpack deactivation
    UFUNCTION()
    void DeactivateJetpack();

private:
    // Jetpack component
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Jetpack", meta = (AllowPrivateAccess = "true"))
    class UJetpackComponent* JetpackComponent;
};
```

**JetpackUsageExample.cpp**
```cpp
#include "JetpackUsageExample.h"
#include "JetpackComponent.h"

AJetpackUsageExample::AJetpackUsageExample()
{
    // Create and attach jetpack component
    JetpackComponent = CreateDefaultSubobject<UJetpackComponent>(TEXT("JetpackComponent"));
    RootComponent = JetpackComponent;
}

void AJetpackUsageExample::BeginPlay()
{
    Super::BeginPlay();
}

void AJetpackUsageExample::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
}

void AJetpackUsageExample::ActivateJetpack()
{
    if (JetpackComponent)
    {
        JetpackComponent->ActivateJetpack();
    }
}

void AJetpackUsageExample::DeactivateJetpack()
{
    if (JetpackComponent)
    {
        JetpackComponent->DeactivateJetpack();
    }
}
```
