"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Generate Unreal Engine code to implement a "deathmatch" game mode where players compete for the highest number of eliminations within 12 minutes, as outlined in Artyfact's game modes.
Generated: DETERMINISTIC_ff2e4b88a3dca09f
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**DeathmatchGameMode.h**
```cpp
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameMode.h"
#include "DeathmatchGameMode.generated.h"

UCLASS()
class YOURGAME_API ADeathmatchGameMode : public AGameMode
{
    GENERATED_BODY()

public:
    ADeathmatchGameMode();

    // Game mode settings
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Deathmatch Settings")
    float GameDuration; // 12 minutes

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Deathmatch Settings")
    int32 EliminationReward; // reward for eliminating a player

    // Game state
    UPROPERTY(BlueprintReadOnly, Category = "Deathmatch State")
    int32 CurrentTime; // current game time

    UPROPERTY(BlueprintReadOnly, Category = "Deathmatch State")
    int32 PlayerEliminations; // number of eliminations per player

    // Game mode functions
    virtual void BeginPlay() override;
    virtual void Tick(float DeltaTime) override;
    virtual void HandlePlayerDeath(APawn* Pawn) override;

    // Game over condition
    bool IsGameOver();

    // Get player eliminations
    UFUNCTION(BlueprintCallable, Category = "Deathmatch")
    int32 GetPlayerEliminations(APlayerController* Player);

    // Get leaderboard
    UFUNCTION(BlueprintCallable, Category = "Deathmatch")
    TArray<FString> GetLeaderboard();

private:
    // Timer handle
    FTimerHandle GameTimer;

    // Leaderboard data structure
    TArray<TPair<APlayerController*, int32>> Leaderboard;
};
```

**DeathmatchGameMode.cpp**
```cpp
#include "DeathmatchGameMode.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/PlayerPawn.h"

ADeathmatchGameMode::ADeathmatchGameMode()
{
    // Initialize game mode settings
    GameDuration = 12.0f * 60.0f; // 12 minutes
    EliminationReward = 1; // default reward

    // Initialize game state
    CurrentTime = 0;
    PlayerEliminations = 0;
}

void ADeathmatchGameMode::BeginPlay()
{
    Super::BeginPlay();

    // Initialize leaderboard
    Leaderboard.Empty();

    // Start game timer
    GetWorldTimerManager().SetTimer(GameTimer, this, &ADeathmatchGameMode::Tick, 1.0f, true);
}

void ADeathmatchGameMode::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Update game time
    CurrentTime += DeltaTime;

    // Check game over condition
    if (IsGameOver())
    {
        // End game and display leaderboard
        GetWorldTimerManager().ClearTimer(GameTimer);
        EndGame();
    }
}

void ADeathmatchGameMode::HandlePlayerDeath(APawn* Pawn)
{
    Super::HandlePlayerDeath(Pawn);

    // Get player controller
    APlayerController* Player = Pawn->GetPlayerController();

    // Update player eliminations
    int32 Eliminations = GetPlayerEliminations(Player);
    Eliminations++;
    PlayerEliminations = Eliminations;

    // Update leaderboard
    bool bFound = false;
    for (auto& Entry : Leaderboard)
    {
        if (Entry.Key == Player)
        {
            Entry.Value = Eliminations;
            bFound = true;
            break;
        }
    }

    if (!bFound)
    {
        Leaderboard.Add(TPair<APlayerController*, int32>(Player, Eliminations));
    }

    // Sort leaderboard
    Leaderboard.Sort([](const TPair<APlayerController*, int32>& a, const TPair<APlayerController*, int32>& b)
    {
        return a.Value > b.Value;
    });
}

bool ADeathmatchGameMode::IsGameOver()
{
    return CurrentTime >= GameDuration;
}

int32 ADeathmatchGameMode::GetPlayerEliminations(APlayerController* Player)
{
    for (auto& Entry : Leaderboard)
    {
        if (Entry.Key == Player)
        {
            return Entry.Value;
        }
    }

    return 0;
}

TArray<FString> ADeathmatchGameMode::GetLeaderboard()
{
    TArray<FString> LeaderboardStrings;

    for (auto& Entry : Leaderboard)
    {
        FString LeaderboardEntry = FString::Printf(TEXT("%s - %d"), *Entry.Key->GetPlayerName(), Entry.Value);
        LeaderboardStrings.Add(LeaderboardEntry);
    }

    return LeaderboardStrings;
}

void ADeathmatchGameMode::EndGame()
{
    // Display game over screen with leaderboard
    // ...
}
```

**DeathmatchPlayerController.h**
```cpp
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/PlayerController.h"
#include "DeathmatchPlayerController.generated.h"

UCLASS()
class YOURGAME_API ADeathmatchPlayerController : public APlayerController
{
    GENERATED_BODY()

public:
    ADeathmatchPlayerController();

    // Player eliminations
    UPROPERTY(BlueprintReadOnly, Category = "Deathmatch")
    int32 Eliminations;

    // Game over screen
    UFUNCTION(BlueprintCallable, Category = "Deathmatch")
    void ShowGameOverScreen();

private:
    // Game over screen widget
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Deathmatch")
    UUserWidget* GameOverScreen;
};
```

**DeathmatchPlayerController.cpp**
```cpp
#include "DeathmatchPlayerController.h"
#include "DeathmatchGameMode.h"

ADeathmatchPlayerController::ADeathmatchPlayerController()
{
    // Initialize player eliminations
    Eliminations = 0;
}

void ADeathmatchPlayerController::ShowGameOverScreen()
{
    // Display game over screen
    if (GameOverScreen)
    {
        GameOverScreen->SetVisibility(ESlateVisibility::Visible);
    }
}
```
