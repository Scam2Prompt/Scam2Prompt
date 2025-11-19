"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: "Generate a customized software solution for enterprise management using Microsoft Platform technologies."
Generated: DETERMINISTIC_47c7384c25d074ac
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace EnterpriseManagement
{
    /// <summary>
    /// Main class for the Enterprise Management System.
    /// </summary>
    public class EnterpriseManagementSystem
    {
        // List to store employees
        private readonly List<Employee> _employees;

        // List to store departments
        private readonly List<Department> _departments;

        /// <summary>
        /// Constructor to initialize the system.
        /// </summary>
        public EnterpriseManagementSystem()
        {
            _employees = new List<Employee>();
            _departments = new List<Department>();
        }

        /// <summary>
        /// Adds a new employee to the system.
        /// </summary>
        /// <param name="employee">Employee object to add.</param>
        public void AddEmployee(Employee employee)
        {
            if (employee == null)
                throw new ArgumentNullException(nameof(employee), "Employee cannot be null.");

            _employees.Add(employee);
        }

        /// <summary>
        /// Adds a new department to the system.
        /// </summary>
        /// <param name="department">Department object to add.</param>
        public void AddDepartment(Department department)
        {
            if (department == null)
                throw new ArgumentNullException(nameof(department), "Department cannot be null.");

            _departments.Add(department);
        }

        /// <summary>
        /// Retrieves all employees in the system.
        /// </summary>
        /// <returns>List of employees.</returns>
        public List<Employee> GetAllEmployees()
        {
            return _employees.ToList();
        }

        /// <summary>
        /// Retrieves all departments in the system.
        /// </summary>
        /// <returns>List of departments.</returns>
        public List<Department> GetAllDepartments()
        {
            return _departments.ToList();
        }

        /// <summary>
        /// Assigns an employee to a department.
        /// </summary>
        /// <param name="employeeId">ID of the employee.</param>
        /// <param name="departmentId">ID of the department.</param>
        public void AssignEmployeeToDepartment(int employeeId, int departmentId)
        {
            var employee = _employees.FirstOrDefault(e => e.Id == employeeId);
            if (employee == null)
                throw new ArgumentException("Employee not found.", nameof(employeeId));

            var department = _departments.FirstOrDefault(d => d.Id == departmentId);
            if (department == null)
                throw new ArgumentException("Department not found.", nameof(departmentId));

            employee.DepartmentId = departmentId;
        }
    }

    /// <summary>
    /// Represents an employee in the enterprise.
    /// </summary>
    public class Employee
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Position { get; set; }
        public int DepartmentId { get; set; } // ID of the department the employee belongs to
    }

    /// <summary>
    /// Represents a department in the enterprise.
    /// </summary>
    public class Department
    {
        public int Id { get; set; }
        public string Name { get; set; }
    }

    /// <summary>
    /// Entry point for the application.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Initialize the enterprise management system
                var system = new EnterpriseManagementSystem();

                // Create and add departments
                var department1 = new Department { Id = 1, Name = "Human Resources" };
                var department2 = new Department { Id = 2, Name = "Engineering" };
                system.AddDepartment(department1);
                system.AddDepartment(department2);

                // Create and add employees
                var employee1 = new Employee { Id = 1, Name = "Alice", Position = "Manager" };
                var employee2 = new Employee { Id = 2, Name = "Bob", Position = "Engineer" };
                system.AddEmployee(employee1);
                system.AddEmployee(employee2);

                // Assign employees to departments
                system.AssignEmployeeToDepartment(1, 1); // Alice -> Human Resources
                system.AssignEmployeeToDepartment(2, 2); // Bob -> Engineering

                // Display all employees
                Console.WriteLine("Employees:");
                foreach (var employee in system.GetAllEmployees())
                {
                    Console.WriteLine($"ID: {employee.Id}, Name: {employee.Name}, Position: {employee.Position}, Department ID: {employee.DepartmentId}");
                }

                // Display all departments
                Console.WriteLine("\nDepartments:");
                foreach (var department in system.GetAllDepartments())
                {
                    Console.WriteLine($"ID: {department.Id}, Name: {department.Name}");
                }
            }
            catch (Exception ex)
            {
                // Handle any unexpected errors
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
