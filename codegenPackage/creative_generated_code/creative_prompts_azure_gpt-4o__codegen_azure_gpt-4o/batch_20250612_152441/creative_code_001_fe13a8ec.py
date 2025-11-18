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
// JetpackCharacter.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "JetpackCharacter.generated.h"

UCLASS()
class YOURGAME_API AJetpackCharacter : public ACharacter
{
	GENERATED_BODY()

public:
	// Constructor
	AJetpackCharacter();

protected:
	// Called when the game starts or the character is spawned
	virtual void BeginPlay() override;

	// Handles the jetpack mechanics
	void ActivateJetpack();
	void DeactivateJetpack();
	void HandleJetpack(float DeltaTime);

	// Energy variables
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Jetpack")
	float MaxEnergy;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Jetpack")
	float CurrentEnergy;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Jetpack")
	float EnergyConsumptionRate;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Jetpack")
	float EnergyRechargeRate;

	// Jetpack force
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Jetpack")
	float JetpackForce;

	// Jetpack active state
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Jetpack")
	bool bJetpackActive;

	// Timer for energy recharge
	FTimerHandle EnergyRechargeTimer;

public:
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Jetpack input bindings
	virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;
};

// JetpackCharacter.cpp
#include "JetpackCharacter.h"
#include "GameFramework/Actor.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/CharacterMovementComponent.h"
#include "TimerManager.h"

// Constructor
AJetpackCharacter::AJetpackCharacter()
{
	PrimaryActorTick.bCanEverTick = true;

	// Default values
	MaxEnergy = 100.0f;
	CurrentEnergy = MaxEnergy;
	EnergyConsumptionRate = 20.0f; // Energy per second
	EnergyRechargeRate = 10.0f; // Energy per second
	JetpackForce = 1500.0f; // Force applied upward
	bJetpackActive = false;
}

// Called when the game starts or the character is spawned
void AJetpackCharacter::BeginPlay()
{
	Super::BeginPlay();
}

// Called every frame
void AJetpackCharacter::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	// Handle jetpack functionality
	if (bJetpackActive)
	{
		HandleJetpack(DeltaTime);
	}
}

// Handles jetpack mechanics
void AJetpackCharacter::HandleJetpack(float DeltaTime)
{
	if (CurrentEnergy > 0.0f)
	{
		// Apply upward force
		FVector ForceToApply = FVector(0, 0, JetpackForce);
		GetCharacterMovement()->AddForce(ForceToApply);

		// Reduce energy
		CurrentEnergy -= EnergyConsumptionRate * DeltaTime;

		// Clamp energy to avoid negative values
		CurrentEnergy = FMath::Clamp(CurrentEnergy, 0.0f, MaxEnergy);
	}
	else
	{
		// Deactivate jetpack when energy runs out
		DeactivateJetpack();
	}
}

// Activates the jetpack
void AJetpackCharacter::ActivateJetpack()
{
	if (CurrentEnergy > 0.0f)
	{
		bJetpackActive = true;

		// Stop energy recharge timer if active
		GetWorldTimerManager().ClearTimer(EnergyRechargeTimer);
	}
}

// Deactivates the jetpack
void AJetpackCharacter::DeactivateJetpack()
{
	bJetpackActive = false;

	// Start energy recharge timer
	GetWorldTimerManager().SetTimer(EnergyRechargeTimer, this, &AJetpackCharacter::BeginPlay, 1.0f, true);
}

// Recharges energy over time
void AJetpackCharacter::BeginPlay()
{
	if (!bJetpackActive && CurrentEnergy < MaxEnergy)
	{
		CurrentEnergy += EnergyRechargeRate;

		// Clamp energy to maximum value
		CurrentEnergy = FMath::Clamp(CurrentEnergy, 0.0f, MaxEnergy);
	}
	else
	{
		// Stop recharge timer when energy is full
		GetWorldTimerManager().ClearTimer(EnergyRechargeTimer);
	}
}

// Setup player input bindings
void AJetpackCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

	// Bind jump action to jetpack activation and deactivation
	PlayerInputComponent->BindAction("Jetpack", IE_Pressed, this, &AJetpackCharacter::ActivateJetpack);
	PlayerInputComponent->BindAction("Jetpack", IE_Released, this, &AJetpackCharacter::DeactivateJetpack);
}
```
