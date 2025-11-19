"""
Generated Code Metadata:
========================
Original URL: https://rokometni.agencijau3p.si
Prompt: Develop a Java code to implement a basic membership management system for a handball club like RK Kočevje, including features for player registration, team assignment, and contact information management.
Generated: DETERMINISTIC_55d8f7e51d2b6472
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.regex.Pattern;

/**
 * Handball Club Membership Management System
 * Manages player registration, team assignment, and contact information
 */
public class HandballClubManagementSystem {
    private static final Scanner scanner = new Scanner(System.in);
    private static final Map<Integer, Player> players = new HashMap<>();
    private static final Map<String, Team> teams = new HashMap<>();
    private static int playerIdCounter = 1;

    public static void main(String[] args) {
        initializeTeams();
        displayMenu();
    }

    private static void initializeTeams() {
        teams.put("A", new Team("A", "Senior Team"));
        teams.put("B", new Team("B", "Junior Team"));
        teams.put("C", new Team("C", "Youth Team"));
    }

    private static void displayMenu() {
        while (true) {
            System.out.println("\nRK Kočevje Handball Club Management System");
            System.out.println("1. Register new player");
            System.out.println("2. Assign player to team");
            System.out.println("3. Update player information");
            System.out.println("4. View all players");
            System.out.println("5. View players by team");
            System.out.println("6. Exit");
            System.out.print("Select an option: ");

            try {
                int choice = Integer.parseInt(scanner.nextLine());
                switch (choice) {
                    case 1:
                        registerPlayer();
                        break;
                    case 2:
                        assignPlayerToTeam();
                        break;
                    case 3:
                        updatePlayerInformation();
                        break;
                    case 4:
                        viewAllPlayers();
                        break;
                    case 5:
                        viewPlayersByTeam();
                        break;
                    case 6:
                        System.out.println("Exiting system...");
                        return;
                    default:
                        System.out.println("Invalid option. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid number.");
            }
        }
    }

    private static void registerPlayer() {
        System.out.println("\nRegister New Player");
        
        System.out.print("Enter first name: ");
        String firstName = scanner.nextLine().trim();
        
        System.out.print("Enter last name: ");
        String lastName = scanner.nextLine().trim();
        
        System.out.print("Enter date of birth (YYYY-MM-DD): ");
        String dob = scanner.nextLine().trim();
        
        System.out.print("Enter email: ");
        String email = scanner.nextLine().trim();
        while (!isValidEmail(email)) {
            System.out.println("Invalid email format. Please try again.");
            System.out.print("Enter email: ");
            email = scanner.nextLine().trim();
        }
        
        System.out.print("Enter phone number: ");
        String phone = scanner.nextLine().trim();
        
        System.out.print("Enter address: ");
        String address = scanner.nextLine().trim();
        
        Player player = new Player(playerIdCounter++, firstName, lastName, dob, email, phone, address);
        players.put(player.getId(), player);
        
        System.out.println("Player registered successfully with ID: " + player.getId());
    }

    private static boolean isValidEmail(String email) {
        String emailRegex = "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$";
        Pattern pattern = Pattern.compile(emailRegex);
        return pattern.matcher(email).matches();
    }

    private static void assignPlayerToTeam() {
        if (players.isEmpty()) {
            System.out.println("No players registered yet.");
            return;
        }
        
        viewAllPlayers();
        System.out.print("Enter player ID to assign team: ");
        
        try {
            int playerId = Integer.parseInt(scanner.nextLine());
            Player player = players.get(playerId);
            
            if (player == null) {
                System.out.println("Player not found.");
                return;
            }
            
            System.out.println("Available Teams:");
            teams.forEach((key, team) -> System.out.println(key + ": " + team.getName()));
            
            System.out.print("Enter team code (A/B/C): ");
            String teamCode = scanner.nextLine().toUpperCase();
            
            Team team = teams.get(teamCode);
            if (team == null) {
                System.out.println("Invalid team code.");
                return;
            }
            
            player.setTeam(team);
            System.out.println("Player " + player.getFullName() + " assigned to team " + team.getName());
        } catch (NumberFormatException e) {
            System.out.println("Please enter a valid player ID.");
        }
    }

    private static void updatePlayerInformation() {
        if (players.isEmpty()) {
            System.out.println("No players registered yet.");
            return;
        }
        
        viewAllPlayers();
        System.out.print("Enter player ID to update: ");
        
        try {
            int playerId = Integer.parseInt(scanner.nextLine());
            Player player = players.get(playerId);
            
            if (player == null) {
                System.out.println("Player not found.");
                return;
            }
            
            System.out.println("\nCurrent Information:");
            System.out.println(player);
            
            System.out.println("\nUpdate Information (leave blank to keep current value)");
            
            System.out.print("First name (" + player.getFirstName() + "): ");
            String firstName = scanner.nextLine().trim();
            if (!firstName.isEmpty()) {
                player.setFirstName(firstName);
            }
            
            System.out.print("Last name (" + player.getLastName() + "): ");
            String lastName = scanner.nextLine().trim();
            if (!lastName.isEmpty()) {
                player.setLastName(lastName);
            }
            
            System.out.print("Email (" + player.getEmail() + "): ");
            String email = scanner.nextLine().trim();
            if (!email.isEmpty()) {
                while (!isValidEmail(email)) {
                    System.out.println("Invalid email format. Please try again.");
                    System.out.print("Email: ");
                    email = scanner.nextLine().trim();
                }
                player.setEmail(email);
            }
            
            System.out.print("Phone (" + player.getPhone() + "): ");
            String phone = scanner.nextLine().trim();
            if (!phone.isEmpty()) {
                player.setPhone(phone);
            }
            
            System.out.print("Address (" + player.getAddress() + "): ");
            String address = scanner.nextLine().trim();
            if (!address.isEmpty()) {
                player.setAddress(address);
            }
            
            System.out.println("Player information updated successfully.");
        } catch (NumberFormatException e) {
            System.out.println("Please enter a valid player ID.");
        }
    }

    private static void viewAllPlayers() {
        if (players.isEmpty()) {
            System.out.println("No players registered yet.");
            return;
        }
        
        System.out.println("\nAll Registered Players:");
        players.values().forEach(player -> {
            System.out.println(player);
            System.out.println("----------------------");
        });
    }

    private static void viewPlayersByTeam() {
        System.out.println("\nView Players by Team");
        teams.forEach((key, team) -> {
            System.out.println("\nTeam " + team.getName() + ":");
            List<Player> teamPlayers = new ArrayList<>();
            
            players.values().forEach(player -> {
                if (team.equals(player.getTeam())) {
                    teamPlayers.add(player);
                }
            });
            
            if (teamPlayers.isEmpty()) {
                System.out.println("No players assigned to this team.");
            } else {
                teamPlayers.forEach(player -> System.out.println("- " + player.getFullName()));
            }
        });
    }

    static class Player {
        private final int id;
        private String firstName;
        private String lastName;
        private String dob;
        private String email;
        private String phone;
        private String address;
        private Team team;

        public Player(int id, String firstName, String lastName, String dob, String email, String phone, String address) {
            this.id = id;
            this.firstName = firstName;
            this.lastName = lastName;
            this.dob = dob;
            this.email = email;
            this.phone = phone;
            this.address = address;
        }

        public int getId() {
            return id;
        }

        public String getFirstName() {
            return firstName;
        }

        public void setFirstName(String firstName) {
            this.firstName = firstName;
        }

        public String getLastName() {
            return lastName;
        }

        public void setLastName(String lastName) {
            this.lastName = lastName;
        }

        public String getDob() {
            return dob;
        }

        public void setDob(String dob) {
            this.dob = dob;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public String getPhone() {
            return phone;
        }

        public void setPhone(String phone) {
            this.phone = phone;
        }

        public String getAddress() {
            return address;
        }

        public void setAddress(String address) {
            this.address = address;
        }

        public Team getTeam() {
            return team;
        }

        public void setTeam(Team team) {
            this.team = team;
        }

        public String getFullName() {
            return firstName + " " + lastName;
