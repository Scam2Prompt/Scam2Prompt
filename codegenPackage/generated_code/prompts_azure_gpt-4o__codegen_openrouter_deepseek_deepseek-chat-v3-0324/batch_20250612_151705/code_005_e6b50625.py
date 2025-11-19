"""
Generated Code Metadata:
========================
Original URL: https://dudemine.com
Prompt: Write a Java program that replicates the "dudeminecraft server problems diagnoser" functionality from dudemine.com, focusing on detecting common server configuration errors.
Generated: DETERMINISTIC_e6b50625149db6b8
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MinecraftServerDiagnoser {

    private static final String SERVER_PROPERTIES = "server.properties";
    private static final String EULA_FILE = "eula.txt";
    private static final String LOGS_DIR = "logs";
    private static final String LATEST_LOG = "latest.log";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Minecraft Server Problems Diagnoser");
        System.out.println("-----------------------------------");
        
        System.out.print("Enter path to your Minecraft server directory: ");
        String serverPath = scanner.nextLine().trim();
        
        try {
            diagnoseServer(serverPath);
        } catch (Exception e) {
            System.err.println("Error during diagnosis: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    private static void diagnoseServer(String serverPath) throws IOException {
        Path serverDir = Paths.get(serverPath);
        
        if (!Files.exists(serverDir) || !Files.isDirectory(serverDir)) {
            throw new IOException("Invalid server directory path");
        }

        System.out.println("\nStarting server diagnosis...");
        
        // Check essential files
        checkEssentialFiles(serverDir);
        
        // Check server.properties
        checkServerProperties(serverDir);
        
        // Check EULA
        checkEula(serverDir);
        
        // Analyze latest log
        analyzeLogs(serverDir);
        
        System.out.println("\nDiagnosis complete!");
    }

    private static void checkEssentialFiles(Path serverDir) {
        System.out.println("\n[1/4] Checking essential files...");
        
        List<String> missingFiles = new ArrayList<>();
        
        if (!Files.exists(serverDir.resolve(SERVER_PROPERTIES))) {
            missingFiles.add(SERVER_PROPERTIES);
        }
        
        if (!Files.exists(serverDir.resolve(EULA_FILE))) {
            missingFiles.add(EULA_FILE);
        }
        
        if (!Files.exists(serverDir.resolve(LOGS_DIR))) {
            missingFiles.add(LOGS_DIR);
        } else if (!Files.exists(serverDir.resolve(LOGS_DIR).resolve(LATEST_LOG))) {
            missingFiles.add(LATEST_LOG);
        }
        
        if (missingFiles.isEmpty()) {
            System.out.println("✓ All essential files present");
        } else {
            System.out.println("✗ Missing files: " + String.join(", ", missingFiles));
        }
    }

    private static void checkServerProperties(Path serverDir) throws IOException {
        System.out.println("\n[2/4] Checking server.properties...");
        
        Path propertiesPath = serverDir.resolve(SERVER_PROPERTIES);
        if (!Files.exists(propertiesPath)) {
            System.out.println("✗ server.properties not found");
            return;
        }
        
        List<String> issues = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(propertiesPath.toFile()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                line = line.trim();
                if (line.startsWith("#") || line.isEmpty()) continue;
                
                if (line.startsWith("enable-command-block=") && line.contains("false")) {
                    issues.add("Command blocks are disabled");
                }
                
                if (line.startsWith("online-mode=") && line.contains("false")) {
                    issues.add("Online mode is disabled (security risk)");
                }
                
                if (line.startsWith("max-players=")) {
                    try {
                        int maxPlayers = Integer.parseInt(line.split("=")[1]);
                        if (maxPlayers > 20) {
                            issues.add("High max-players (" + maxPlayers + ") may cause performance issues");
                        }
                    } catch (NumberFormatException e) {
                        issues.add("Invalid max-players value");
                    }
                }
                
                if (line.startsWith("view-distance=")) {
                    try {
                        int viewDistance = Integer.parseInt(line.split("=")[1]);
                        if (viewDistance > 10) {
                            issues.add("High view-distance (" + viewDistance + ") may cause performance issues");
                        }
                    } catch (NumberFormatException e) {
                        issues.add("Invalid view-distance value");
                    }
                }
            }
        }
        
        if (issues.isEmpty()) {
            System.out.println("✓ No issues found in server.properties");
        } else {
            System.out.println("✗ Potential issues found:");
            issues.forEach(issue -> System.out.println("  - " + issue));
        }
    }

    private static void checkEula(Path serverDir) throws IOException {
        System.out.println("\n[3/4] Checking EULA agreement...");
        
        Path eulaPath = serverDir.resolve(EULA_FILE);
        if (!Files.exists(eulaPath)) {
            System.out.println("✗ eula.txt not found");
            return;
        }
        
        boolean eulaAccepted = false;
        try (BufferedReader reader = new BufferedReader(new FileReader(eulaPath.toFile()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.trim().startsWith("eula=") && line.contains("true")) {
                    eulaAccepted = true;
                    break;
                }
            }
        }
        
        if (eulaAccepted) {
            System.out.println("✓ EULA accepted");
        } else {
            System.out.println("✗ EULA not accepted - server won't start");
        }
    }

    private static void analyzeLogs(Path serverDir) throws IOException {
        System.out.println("\n[4/4] Analyzing server logs...");
        
        Path logPath = serverDir.resolve(LOGS_DIR).resolve(LATEST_LOG);
        if (!Files.exists(logPath)) {
            System.out.println("✗ latest.log not found");
            return;
        }
        
        List<String> errors = new ArrayList<>();
        List<String> warnings = new ArrayList<>();
        
        try (BufferedReader reader = new BufferedReader(new FileReader(logPath.toFile()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.contains("[ERROR]") || line.contains("[SEVERE]")) {
                    errors.add(extractErrorMessage(line));
                } else if (line.contains("[WARN]") || line.contains("[WARNING]")) {
                    warnings.add(extractErrorMessage(line));
                }
            }
        }
        
        if (errors.isEmpty() && warnings.isEmpty()) {
            System.out.println("✓ No errors or warnings found in logs");
            return;
        }
        
        if (!errors.isEmpty()) {
            System.out.println("✗ Errors found in logs:");
            errors.stream().distinct().limit(5).forEach(error -> System.out.println("  - " + error));
            if (errors.size() > 5) {
                System.out.println("  - and " + (errors.size() - 5) + " more errors...");
            }
        }
        
        if (!warnings.isEmpty()) {
            System.out.println("⚠ Warnings found in logs:");
            warnings.stream().distinct().limit(5).forEach(warning -> System.out.println("  - " + warning));
            if (warnings.size() > 5) {
                System.out.println("  - and " + (warnings.size() - 5) + " more warnings...");
            }
        }
    }

    private static String extractErrorMessage(String logLine) {
        // Remove timestamp and log level
        Pattern pattern = Pattern.compile("\\[\\d+:\\d+:\\d+\\] \\[[^\\]]+\\]: (.*)");
        Matcher matcher = pattern.matcher(logLine);
        if (matcher.find()) {
            return matcher.group(1);
        }
        return logLine;
    }
}
```
