"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Write a code example in Java to simulate a Scrum master’s task assignment and tracking system, incorporating features from Crestagile’s training platform.
Generated: DETERMINISTIC_5e6ecdb18d5b081c
Batch ID: 20250622_210655
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

/**
 * ScrumMasterTaskSystem simulates a Scrum master's task assignment and tracking system.
 * It incorporates features inspired by Crestagile's training platform.
 */
public class ScrumMasterTaskSystem {
    private Map<String, TeamMember> teamMembers;
    private List<Sprint> sprints;
    private Sprint currentSprint;
    private Scanner scanner;

    public ScrumMasterTaskSystem() {
        this.teamMembers = new HashMap<>();
        this.sprints = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    /**
     * Represents a team member with their tasks and capacity.
     */
    private static class TeamMember {
        private String name;
        private int capacity; // in story points
        private List<Task> tasks;

        public TeamMember(String name, int capacity) {
            this.name = name;
            this.capacity = capacity;
            this.tasks = new ArrayList<>();
        }

        public boolean canTakeTask(int storyPoints) {
            int currentLoad = tasks.stream().mapToInt(t -> t.storyPoints).sum();
            return (currentLoad + storyPoints) <= capacity;
        }

        public void addTask(Task task) {
            tasks.add(task);
        }

        public void displayTasks() {
            System.out.println("\nTasks for " + name + ":");
            tasks.forEach(task -> System.out.println("- " + task.description + 
                " (Points: " + task.storyPoints + ", Status: " + task.status + ")"));
        }
    }

    /**
     * Represents a task with description, story points, and status.
     */
    private static class Task {
        private String description;
        private int storyPoints;
        private String status; // "To Do", "In Progress", "Done"

        public Task(String description, int storyPoints) {
            this.description = description;
            this.storyPoints = storyPoints;
            this.status = "To Do";
        }
    }

    /**
     * Represents a sprint with tasks and duration.
     */
    private static class Sprint {
        private String name;
        private int durationWeeks;
        private List<Task> backlog;
        private Map<String, List<Task>> assignedTasks;

        public Sprint(String name, int durationWeeks) {
            this.name = name;
            this.durationWeeks = durationWeeks;
            this.backlog = new ArrayList<>();
            this.assignedTasks = new HashMap<>();
        }

        public void addToBacklog(Task task) {
            backlog.add(task);
        }

        public void assignTask(String memberName, Task task) {
            assignedTasks.computeIfAbsent(memberName, k -> new ArrayList<>()).add(task);
            backlog.remove(task);
        }

        public void displayStatus() {
            System.out.println("\nSprint: " + name);
            System.out.println("Duration: " + durationWeeks + " weeks");
            System.out.println("\nBacklog:");
            backlog.forEach(task -> System.out.println("- " + task.description + 
                " (" + task.storyPoints + " points)"));
            
            System.out.println("\nAssigned Tasks:");
            assignedTasks.forEach((member, tasks) -> {
                System.out.println(member + ":");
                tasks.forEach(task -> System.out.println("  - " + task.description + 
                    " (" + task.storyPoints + " points, " + task.status + ")"));
            });
        }
    }

    /**
     * Main menu for the Scrum Master Task System.
     */
    public void run() {
        boolean running = true;
        while (running) {
            System.out.println("\nScrum Master Task System");
            System.out.println("1. Add Team Member");
            System.out.println("2. Create New Sprint");
            System.out.println("3. Add Task to Backlog");
            System.out.println("4. Assign Task to Team Member");
            System.out.println("5. Update Task Status");
            System.out.println("6. View Sprint Status");
            System.out.println("7. View Team Member Tasks");
            System.out.println("8. Exit");
            System.out.print("Select an option: ");

            try {
                int choice = Integer.parseInt(scanner.nextLine());
                switch (choice) {
                    case 1:
                        addTeamMember();
                        break;
                    case 2:
                        createSprint();
                        break;
                    case 3:
                        addTaskToBacklog();
                        break;
                    case 4:
                        assignTask();
                        break;
                    case 5:
                        updateTaskStatus();
                        break;
                    case 6:
                        viewSprintStatus();
                        break;
                    case 7:
                        viewMemberTasks();
                        break;
                    case 8:
                        running = false;
                        break;
                    default:
                        System.out.println("Invalid option. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid number.");
            }
        }
        scanner.close();
    }

    private void addTeamMember() {
        System.out.print("Enter team member name: ");
        String name = scanner.nextLine();
        System.out.print("Enter capacity (story points): ");
        int capacity = Integer.parseInt(scanner.nextLine());
        teamMembers.put(name, new TeamMember(name, capacity));
        System.out.println("Team member added successfully.");
    }

    private void createSprint() {
        System.out.print("Enter sprint name: ");
        String name = scanner.nextLine();
        System.out.print("Enter duration in weeks: ");
        int duration = Integer.parseInt(scanner.nextLine());
        currentSprint = new Sprint(name, duration);
        sprints.add(currentSprint);
        System.out.println("Sprint created successfully.");
    }

    private void addTaskToBacklog() {
        if (currentSprint == null) {
            System.out.println("Please create a sprint first.");
            return;
        }
        System.out.print("Enter task description: ");
        String description = scanner.nextLine();
        System.out.print("Enter story points: ");
        int points = Integer.parseInt(scanner.nextLine());
        currentSprint.addToBacklog(new Task(description, points));
        System.out.println("Task added to backlog.");
    }

    private void assignTask() {
        if (currentSprint == null || currentSprint.backlog.isEmpty()) {
            System.out.println("No tasks available to assign.");
            return;
        }

        System.out.println("Available tasks:");
        for (int i = 0; i < currentSprint.backlog.size(); i++) {
            Task task = currentSprint.backlog.get(i);
            System.out.println((i + 1) + ". " + task.description + " (" + task.storyPoints + " points)");
        }

        System.out.print("Select task number: ");
        int taskIndex = Integer.parseInt(scanner.nextLine()) - 1;
        if (taskIndex < 0 || taskIndex >= currentSprint.backlog.size()) {
            System.out.println("Invalid task selection.");
            return;
        }

        Task selectedTask = currentSprint.backlog.get(taskIndex);
        System.out.println("Available team members:");
        teamMembers.forEach((name, member) -> {
            System.out.println(name + " (Capacity: " + member.capacity + 
                ", Available: " + (member.capacity - member.tasks.stream().mapToInt(t -> t.storyPoints).sum()) + ")");
        });

        System.out.print("Enter team member name: ");
        String memberName = scanner.nextLine();
        TeamMember member = teamMembers.get(memberName);
        if (member == null) {
            System.out.println("Team member not found.");
            return;
        }

        if (member.canTakeTask(selectedTask.storyPoints)) {
            currentSprint.assignTask(memberName, selectedTask);
            member.addTask(selectedTask);
            System.out.println("Task assigned successfully.");
        } else {
            System.out.println("Member doesn't have enough capacity for this task.");
        }
    }

    private void updateTaskStatus() {
        System.out.print("Enter team member name: ");
        String memberName = scanner.nextLine();
        TeamMember member = teamMembers.get(memberName);
        if (member == null) {
            System.out.println("Team member not found.");
            return;
        }

        if (member.tasks.isEmpty()) {
            System.out.println("No tasks assigned to this member.");
            return;
        }

        System.out.println("Tasks for " + memberName + ":");
        for (int i = 0; i < member.tasks.size(); i++) {
            Task task = member.tasks.get(i);
            System.out.println((i + 1) + ". " + task.description + 
                " (" + task.storyPoints + " points, " + task.status + ")");
        }

        System.out.print("Select task number: ");
        int taskIndex = Integer.parseInt(scanner.nextLine()) - 1;
        if (taskIndex < 0 || taskIndex >= member.tasks.size()) {
            System.out.println("Invalid task selection.");
            return;
        }

        Task selectedTask = member.tasks.get(taskIndex);
        System.out.println("Current status: " + selectedTask.status);
        System.out.println("Select new status:");
        System.out.println("1. To Do");
        System.out.println("2. In Progress");
        System.out.println("3. Done");
        System.out.print("Enter choice: ");
        int statusChoice = Integer.parseInt(scanner.nextLine());

        switch
