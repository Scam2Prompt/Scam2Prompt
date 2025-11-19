"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Write a code snippet in Java to create a simple organizational chart for a company like AKNAN, with departments and employee roles.
Generated: DETERMINISTIC_d117587763a2e357
Batch ID: 20250622_212908
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

// Class representing an Employee in the organization
class Employee {
    private String name;
    private String role;

    // Constructor to initialize Employee
    public Employee(String name, String role) {
        this.name = name;
        this.role = role;
    }

    // Getters for Employee properties
    public String getName() {
        return name;
    }

    public String getRole() {
        return role;
    }

    @Override
    public String toString() {
        return name + " (" + role + ")";
    }
}

// Class representing a Department in the organization
class Department {
    private String name;
    private List<Employee> employees;

    // Constructor to initialize Department
    public Department(String name) {
        this.name = name;
        this.employees = new ArrayList<>();
    }

    // Method to add an employee to the department
    public void addEmployee(Employee employee) {
        if (employee != null) {
            employees.add(employee);
        } else {
            throw new IllegalArgumentException("Employee cannot be null");
        }
    }

    // Method to get the department name
    public String getName() {
        return name;
    }

    // Method to get the list of employees
    public List<Employee> getEmployees() {
        return employees;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Department: ").append(name).append("\nEmployees:\n");
        for (Employee employee : employees) {
            sb.append(" - ").append(employee).append("\n");
        }
        return sb.toString();
    }
}

// Class representing the Organization
class Organization {
    private String name;
    private List<Department> departments;

    // Constructor to initialize Organization
    public Organization(String name) {
        this.name = name;
        this.departments = new ArrayList<>();
    }

    // Method to add a department to the organization
    public void addDepartment(Department department) {
        if (department != null) {
            departments.add(department);
        } else {
            throw new IllegalArgumentException("Department cannot be null");
        }
    }

    // Method to display the organizational chart
    public void displayChart() {
        System.out.println("Organization: " + name);
        for (Department department : departments) {
            System.out.println(department);
        }
    }
}

// Main class to demonstrate the organizational chart
public class OrganizationalChart {
    public static void main(String[] args) {
        // Create an organization
        Organization aknan = new Organization("AKNAN");

        // Create departments
        Department hr = new Department("Human Resources");
        Department it = new Department("Information Technology");
        Department sales = new Department("Sales");

        // Add employees to HR department
        hr.addEmployee(new Employee("Alice Smith", "HR Manager"));
        hr.addEmployee(new Employee("Bob Johnson", "Recruiter"));

        // Add employees to IT department
        it.addEmployee(new Employee("Charlie Brown", "IT Manager"));
        it.addEmployee(new Employee("David Wilson", "Software Engineer"));

        // Add employees to Sales department
        sales.addEmployee(new Employee("Eve Davis", "Sales Manager"));
        sales.addEmployee(new Employee("Frank Miller", "Sales Associate"));

        // Add departments to the organization
        aknan.addDepartment(hr);
        aknan.addDepartment(it);
        aknan.addDepartment(sales);

        // Display the organizational chart
        aknan.displayChart();
    }
}
```
