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
import java.util.List;
import java.util.Scanner;

/**
 * Simulates a Scrum master's task assignment and tracking system.
 */
public class ScrumMasterTaskSystem {

    // Enum for task status
    enum TaskStatus {
        TO_DO,
        IN_PROGRESS,
        DONE
    }

    // Class representing a task
    static class Task {
        private String id;
        private String name;
        private String assignee;
        private TaskStatus status;

        public Task(String id, String name) {
            this.id = id;
            this.name = name;
            this.assignee = null;
            this.status = TaskStatus.TO_DO;
        }

        // Getters and setters
        public String getId() { return id; }
        public String getName() { return name; }
        public String getAssignee() { return assignee; }
        public void setAssignee(String assignee) { this.assignee = assignee; }
        public TaskStatus getStatus() { return status; }
        public void setStatus(TaskStatus status) { this.status = status; }
    }

    // Class representing the Scrum master's task system
    static class TaskSystem {
        private List<Task> tasks;
        private int taskIdCounter;

        public TaskSystem() {
            this.tasks = new ArrayList<>();
            this.taskIdCounter = 1;
        }

        // Create a new task
        public Task createTask(String name) {
            String taskId = "T" + taskIdCounter++;
            Task task = new Task(taskId, name);
            tasks.add(task);
            return task;
        }

        // Assign a task to a team member
        public void assignTask(String taskId, String assignee) {
            Task task = findTask(taskId);
            if (task != null) {
                task.setAssignee(assignee);
                System.out.println("Task " + taskId + " assigned to " + assignee);
            } else {
                System.out.println("Task not found");
            }
        }

        // Update task status
        public void updateTaskStatus(String taskId, TaskStatus status) {
            Task task = findTask(taskId);
            if (task != null) {
                task.setStatus(status);
                System.out.println("Task " + taskId + " status updated to " + status);
            } else {
                System.out.println("Task not found");
            }
        }

        // Find a task by ID
        private Task findTask(String taskId) {
            for (Task task : tasks) {
                if (task.getId().equals(taskId)) {
                    return task;
                }
            }
            return null;
        }

        // Display all tasks
        public void displayTasks() {
            System.out.println("Tasks:");
            for (Task task : tasks) {
                System.out.println("ID: " + task.getId() +
                                   ", Name: " + task.getName() +
                                   ", Assignee: " + task.getAssignee() +
                                   ", Status: " + task.getStatus());
            }
        }
    }

    public static void main(String[] args) {
        TaskSystem taskSystem = new TaskSystem();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Create Task");
            System.out.println("2. Assign Task");
            System.out.println("3. Update Task Status");
            System.out.println("4. Display Tasks");
            System.out.println("5. Exit");

            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    System.out.print("Enter task name: ");
                    String taskName = scanner.nextLine();
                    Task task = taskSystem.createTask(taskName);
                    System.out.println("Task created: " + task.getId() + " - " + task.getName());
                    break;
                case 2:
                    System.out.print("Enter task ID: ");
                    String taskId = scanner.nextLine();
                    System.out.print("Enter assignee: ");
                    String assignee = scanner.nextLine();
                    taskSystem.assignTask(taskId, assignee);
                    break;
                case 3:
                    System.out.print("Enter task ID: ");
                    taskId = scanner.nextLine();
                    System.out.println("Select status:");
                    System.out.println("1. TO_DO");
                    System.out.println("2. IN_PROGRESS");
                    System.out.println("3. DONE");
                    System.out.print("Choose an option: ");
                    int statusOption = scanner.nextInt();
                    scanner.nextLine(); // Consume newline left-over
                    TaskStatus status = switch (statusOption) {
                        case 1 -> TaskStatus.TO_DO;
                        case 2 -> TaskStatus.IN_PROGRESS;
                        case 3 -> TaskStatus.DONE;
                        default -> TaskStatus.TO_DO;
                    };
                    taskSystem.updateTaskStatus(taskId, status);
                    break;
                case 4:
                    taskSystem.displayTasks();
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid option");
            }
        }
    }
}
```
