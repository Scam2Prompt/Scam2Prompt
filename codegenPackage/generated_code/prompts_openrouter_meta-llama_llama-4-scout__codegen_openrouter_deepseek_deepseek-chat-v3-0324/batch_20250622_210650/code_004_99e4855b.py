"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: "Create a Java library for simulating data center downtime scenarios, including UPS battery failure and cyber attacks, to test backup power systems."
Generated: DETERMINISTIC_99e4855b145c5ac9
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.time.Duration;
import java.time.LocalDateTime;
import java.util.Random;
import java.util.concurrent.TimeUnit;

/**
 * Simulates data center downtime scenarios for testing backup power systems.
 */
public class DataCenterDowntimeSimulator {

    private static final Random random = new Random();

    /**
     * Simulates a UPS battery failure scenario.
     * @param durationMinutes Duration of the power outage in minutes
     * @throws InterruptedException if the thread is interrupted during sleep
     */
    public static void simulateUPSFailure(int durationMinutes) throws InterruptedException {
        if (durationMinutes <= 0) {
            throw new IllegalArgumentException("Duration must be positive");
        }

        System.out.println("[SIMULATION] UPS Battery Failure Detected");
        System.out.println("[SIMULATION] Switching to backup power...");
        
        TimeUnit.SECONDS.sleep(2); // Simulate switchover delay
        
        System.out.printf("[SIMULATION] Backup power active. Simulating outage for %d minutes...\n", durationMinutes);
        TimeUnit.MINUTES.sleep(durationMinutes);
        
        System.out.println("[SIMULATION] Main power restored. Switching back...");
        TimeUnit.SECONDS.sleep(1);
        System.out.println("[SIMULATION] Simulation complete. System back to normal operation.");
    }

    /**
     * Simulates a cyber attack scenario with random outage duration.
     * @param maxOutageMinutes Maximum possible outage duration in minutes
     * @throws InterruptedException if the thread is interrupted during sleep
     */
    public static void simulateCyberAttack(int maxOutageMinutes) throws InterruptedException {
        if (maxOutageMinutes <= 0) {
            throw new IllegalArgumentException("Max outage duration must be positive");
        }

        int attackDuration = random.nextInt(maxOutageMinutes) + 1;
        
        System.out.println("[SIMULATION] Cyber Attack Detected!");
        System.out.println("[SIMULATION] Initiating emergency protocols...");
        
        TimeUnit.SECONDS.sleep(3); // Simulate detection and response delay
        
        System.out.printf("[SIMULATION] Systems compromised. Simulating outage for %d minutes...\n", attackDuration);
        TimeUnit.MINUTES.sleep(attackDuration);
        
        System.out.println("[SIMULATION] Attack mitigated. Restoring systems...");
        TimeUnit.SECONDS.sleep(2);
        System.out.println("[SIMULATION] Simulation complete. Systems secured.");
    }

    /**
     * Simulates a rolling blackout scenario with multiple short outages.
     * @param numberOfOutages Number of outages to simulate
     * @param maxOutageDurationSeconds Maximum duration of each outage in seconds
     * @throws InterruptedException if the thread is interrupted during sleep
     */
    public static void simulateRollingBlackout(int numberOfOutages, int maxOutageDurationSeconds) 
            throws InterruptedException {
        if (numberOfOutages <= 0 || maxOutageDurationSeconds <= 0) {
            throw new IllegalArgumentException("Parameters must be positive");
        }

        System.out.printf("[SIMULATION] Starting rolling blackout simulation with %d outages...\n", numberOfOutages);
        
        for (int i = 1; i <= numberOfOutages; i++) {
            int duration = random.nextInt(maxOutageDurationSeconds) + 1;
            System.out.printf("[SIMULATION] Outage #%d: %d seconds\n", i, duration);
            TimeUnit.SECONDS.sleep(duration);
            
            if (i < numberOfOutages) {
                int betweenOutages = random.nextInt(30) + 10; // 10-40 seconds between outages
                System.out.printf("[SIMULATION] Power restored. Next outage in %d seconds...\n", betweenOutages);
                TimeUnit.SECONDS.sleep(betweenOutages);
            }
        }
        
        System.out.println("[SIMULATION] Rolling blackout simulation complete.");
    }

    /**
     * Simulates a scheduled maintenance window with controlled downtime.
     * @param startTime Scheduled start time
     * @param duration Duration of the maintenance window
     */
    public static void simulateScheduledMaintenance(LocalDateTime startTime, Duration duration) {
        LocalDateTime now = LocalDateTime.now();
        
        if (now.isBefore(startTime)) {
            System.out.printf("[SIMULATION] Scheduled maintenance begins at %s\n", startTime);
            System.out.printf("[SIMULATION] Current time: %s\n", now);
            System.out.println("[SIMULATION] Waiting for scheduled time...");
        } else {
            System.out.println("[SIMULATION] Beginning scheduled maintenance now");
        }
        
        System.out.printf("[SIMULATION] Maintenance window duration: %s\n", duration);
        System.out.println("[SIMULATION] Systems will be unavailable during this window");
    }

    /**
     * Runs a comprehensive test of all simulation scenarios.
     * @throws InterruptedException if the thread is interrupted during sleep
     */
    public static void runFullTestSuite() throws InterruptedException {
        System.out.println("[TEST SUITE] Starting comprehensive data center downtime simulations");
        
        System.out.println("\n=== Testing UPS Battery Failure Scenario ===");
        simulateUPSFailure(5);
        
        System.out.println("\n=== Testing Cyber Attack Scenario ===");
        simulateCyberAttack(15);
        
        System.out.println("\n=== Testing Rolling Blackout Scenario ===");
        simulateRollingBlackout(3, 20);
        
        System.out.println("\n=== Testing Scheduled Maintenance Scenario ===");
        simulateScheduledMaintenance(LocalDateTime.now().plusMinutes(1), Duration.ofMinutes(30));
        
        System.out.println("\n[TEST SUITE] All simulations completed successfully");
    }
}
```
