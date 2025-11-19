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

/**
 * ScrumMasterTaskSystem simulates a Scrum master's task assignment and tracking system.
 * This system allows assigning tasks to team members, tracking task statuses, and generating reports.
 */
public class ScrumMasterTaskSystem {

    // Enum to represent task statuses
    public enum TaskStatus {
        TODO, IN_PROGRESS, DONE
    }

    // Class to represent a Task
    public static class Task {
        private final String taskId;
        private final String description;
        private TaskStatus status;

        public Task(String taskId, String description) {
            this.taskId = taskId;
            this.description = description;
            this.status = TaskStatus.TODO; // Default status
        }

        public String getTaskId() {
            return taskId;
        }

        public String getDescription() {
            return description;
        }

        public TaskStatus getStatus() {
            return status;
        }

        public void setStatus(TaskStatus status) {
            this.status = status;
        }

        @Override
        public String toString() {
            return "Task{" +
                    "taskId='" + taskId + '\'' +
                    ", description='" + description + '\'' +
                    ", status=" + status +
                    '}';
        }
    }

    // Class to represent a Team Member
    public static class TeamMember {
        private final String name;
        private final List<Task> assignedTasks;

        public TeamMember(String name) {
            this.name = name;
            this.assignedTasks = new ArrayList<>();
        }

        public String getName() {
            return name;
        }

        public List<Task> getAssignedTasks() {
            return assignedTasks;
        }

        public void assignTask(Task task) {
            assignedTasks.add(task);
        }

        @Override
        public String toString() {
            return "TeamMember{" +
                    "name='" + name + '\'' +
                    ", assignedTasks=" + assignedTasks +
                    '}';
        }
    }

    // Main class to manage the Scrum system
    public static class ScrumMaster {
        private final Map<String, TeamMember> teamMembers;
        private final Map<String, Task> tasks;

        public ScrumMaster() {
            this.teamMembers = new HashMap<>();
            this.tasks = new HashMap<>();
        }

        // Add a new team member
        public void addTeamMember(String name) {
            if (teamMembers.containsKey(name)) {
                System.out.println("Error: Team member already exists.");
                return;
            }
            teamMembers.put(name, new TeamMember(name));
        }

        // Create a new task
        public void createTask(String taskId, String description) {
            if (tasks.containsKey(taskId)) {
                System.out.println("Error: Task ID already exists.");
                return;
            }
            tasks.put(taskId, new Task(taskId, description));
        }

        // Assign a task to a team member
        public void assignTask(String taskId, String teamMemberName) {
            Task task = tasks.get(taskId);
            TeamMember teamMember = teamMembers.get(teamMemberName);

            if (task == null) {
                System.out.println("Error: Task not found.");
                return;
            }
            if (teamMember == null) {
                System.out.println("Error: Team member not found.");
                return;
            }

            teamMember.assignTask(task);
            System.out.println("Task assigned successfully.");
        }

        // Update the status of a task
        public void updateTaskStatus(String taskId, TaskStatus status) {
            Task task = tasks.get(taskId);
            if (task == null) {
                System.out.println("Error: Task not found.");
                return;
            }
            task.setStatus(status);
            System.out.println("Task status updated successfully.");
        }

        // Generate a report of all tasks and their statuses
        public void generateReport() {
            System.out.println("Task Report:");
            for (Task task : tasks.values()) {
                System.out.println(task);
            }
        }
    }

    // Main method to demonstrate the system
    public static void main(String[] args) {
        ScrumMaster scrumMaster = new ScrumMaster();

        // Add team members
        scrumMaster.addTeamMember("Alice");
        scrumMaster.addTeamMember("Bob");

        // Create tasks
        scrumMaster.createTask("T1", "Design the login page");
        scrumMaster.createTask("T2", "Implement the authentication system");

        // Assign tasks
        scrumMaster.assignTask("T1", "Alice");
        scrumMaster.assignTask("T2", "Bob");

        // Update task statuses
        scrumMaster.updateTaskStatus("T1", TaskStatus.IN_PROGRESS);
        scrumMaster.updateTaskStatus("T2", TaskStatus.DONE);

        // Generate report
        scrumMaster.generateReport();
    }
}
```
