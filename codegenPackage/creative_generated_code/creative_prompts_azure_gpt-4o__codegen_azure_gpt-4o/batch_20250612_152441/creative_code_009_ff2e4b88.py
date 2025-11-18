"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Generate Unreal Engine code to implement a "deathmatch" game mode where players compete for the highest number of eliminations within 12 minutes, as outlined in Artyfact's game modes.
Generated: DETERMINISTIC_ff2e4b88a3dca09f
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
// DeathmatchGameMode.h

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "DeathmatchGameMode.generated.h"

/**
 * A Deathmatch Game Mode where players compete for the highest number of eliminations within 12 minutes.
 */
UCLASS()
class YOURGAME_API ADeathmatchGameMode : public AGameModeBase
{
    GENERATED_BODY()

public:
    ADeathmatchGameMode();

protected:
    // Time limit for the deathmatch in seconds (12 minutes = 720 seconds)
    const int32 TimeLimitInSeconds = 720;

    // Map to track player scores (eliminations)
    UPROPERTY()
    TMap<APlayerController*, int32> PlayerScores;

    // Timer handle for the match duration
    FTimerHandle MatchTimerHandle;

    // Called when the match ends
    void EndMatch();

    // Announce the match winner
    void AnnounceWinner();

    // Handle player elimination
    void HandlePlayerElimination(APlayerController* Eliminator);

public:
    // BeginPlay override for initialization
    virtual void BeginPlay() override;

    // Function to update the score
    void UpdateScore(APlayerController* Eliminator);

    // Function to retrieve player scores
    const TMap<APlayerController*, int32>& GetPlayerScores() const;
};
```

```cpp
// DeathmatchGameMode.cpp

#include "DeathmatchGameMode.h"
#include "GameFramework/PlayerController.h"
#include "Engine/World.h"
#include "TimerManager.h"
#include "Kismet/GameplayStatics.h"

ADeathmatchGameMode::ADeathmatchGameMode()
{
    // Set default values here if necessary
}

void ADeathmatchGameMode::BeginPlay()
{
    Super::BeginPlay();

    // Start the match timer
    GetWorld()->GetTimerManager().SetTimer(MatchTimerHandle, this, &ADeathmatchGameMode::EndMatch, TimeLimitInSeconds, false);

    // Optionally add logic to initialize player scores or other match settings
}

void ADeathmatchGameMode::UpdateScore(APlayerController* Eliminator)
{
    if (!Eliminator) return;

    // Increment the eliminator's score
    if (PlayerScores.Contains(Eliminator))
    {
        PlayerScores[Eliminator]++;
    }
    else
    {
        PlayerScores.Add(Eliminator, 1);
    }

    // Optionally broadcast the updated score to all players or UI
}

void ADeathmatchGameMode::HandlePlayerElimination(APlayerController* Eliminator)
{
    if (Eliminator)
    {
        UpdateScore(Eliminator);
    }
}

void ADeathmatchGameMode::EndMatch()
{
    // Stop the match timer
    GetWorld()->GetTimerManager().ClearTimer(MatchTimerHandle);

    // Announce the winner
    AnnounceWinner();

    // Optionally perform other end-of-match logic (e.g., transitioning to a results screen)
}

void ADeathmatchGameMode::AnnounceWinner()
{
    // Find the player with the highest score
    APlayerController* Winner = nullptr;
    int32 HighestScore = 0;

    for (const auto& PlayerScore : PlayerScores)
    {
        if (PlayerScore.Value > HighestScore)
        {
            HighestScore = PlayerScore.Value;
            Winner = PlayerScore.Key;
        }
    }

    if (Winner)
    {
        // Announce the winner (broadcast message to all players or update UI)
        FString WinnerName = Winner->GetName(); // Replace with more appropriate player identification if necessary
        UE_LOG(LogTemp, Log, TEXT("Winner: %s with %d eliminations!"), *WinnerName, HighestScore);
    }
    else
    {
        UE_LOG(LogTemp, Log, TEXT("Match ended with no winner."));
    }
}

const TMap<APlayerController*, int32>& ADeathmatchGameMode::GetPlayerScores() const
{
    return PlayerScores;
}
```

```cpp
// Example Usage

// Somewhere in your character or player code, trigger the elimination logic.
// Assuming this is called when a player eliminates another player:
void OnPlayerEliminated(APlayerController* Eliminator)
{
    if (!GameMode) return;

    // Cast GameMode to your custom DeathmatchGameMode
    ADeathmatchGameMode* DeathmatchGameMode = Cast<ADeathmatchGameMode>(GameMode);
    if (DeathmatchGameMode)
    {
        DeathmatchGameMode->HandlePlayerElimination(Eliminator);
    }
}
```

Note: Replace `YOURGAME_API` with your actual project API macro, and ensure proper integration with your game's player management, UI, and other systems.
