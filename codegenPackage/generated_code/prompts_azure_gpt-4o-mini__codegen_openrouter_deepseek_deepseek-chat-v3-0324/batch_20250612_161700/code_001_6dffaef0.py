"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.net
Prompt: Write a C# code example for consuming a WCF REST service using jQuery, as described in the WCF tutorial.
Generated: DETERMINISTIC_6dffaef0aa9d981d
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.6.0.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```csharp
// Service Contract Interface
[ServiceContract]
public interface IEmployeeService
{
    [OperationContract]
    [WebInvoke(Method = "GET",
        ResponseFormat = WebMessageFormat.Json,
        BodyStyle = WebMessageBodyStyle.Wrapped,
        UriTemplate = "GetEmployee/{id}")]
    Employee GetEmployee(string id);

    [OperationContract]
    [WebInvoke(Method = "POST",
        RequestFormat = WebMessageFormat.Json,
        ResponseFormat = WebMessageFormat.Json,
        BodyStyle = WebMessageBodyStyle.WrappedRequest,
        UriTemplate = "AddEmployee")]
    bool AddEmployee(Employee employee);
}

// Data Contract
[DataContract]
public class Employee
{
    [DataMember]
    public string Id { get; set; }

    [DataMember]
    public string Name { get; set; }

    [DataMember]
    public string Department { get; set; }

    [DataMember]
    public decimal Salary { get; set; }
}

// Service Implementation
public class EmployeeService : IEmployeeService
{
    public Employee GetEmployee(string id)
    {
        // In a real application, this would fetch from a database
        return new Employee
        {
            Id = id,
            Name = "John Doe",
            Department = "IT",
            Salary = 50000
        };
    }

    public bool AddEmployee(Employee employee)
    {
        try
        {
            // In a real application, this would save to a database
            return true;
        }
        catch (Exception ex)
        {
            // Log error
            return false;
        }
    }
}

// Web.config configuration (excerpt)
/*
<system.serviceModel>
  <services>
    <service name="YourNamespace.EmployeeService" behaviorConfiguration="ServiceBehavior">
      <endpoint address="" 
                binding="webHttpBinding" 
                contract="YourNamespace.IEmployeeService" 
                behaviorConfiguration="web"/>
    </service>
  </services>
  <behaviors>
    <serviceBehaviors>
      <behavior name="ServiceBehavior">
        <serviceMetadata httpGetEnabled="true"/>
        <serviceDebug includeExceptionDetailInFaults="false"/>
      </behavior>
    </serviceBehaviors>
    <endpointBehaviors>
      <behavior name="web">
        <webHttp/>
      </behavior>
    </endpointBehaviors>
  </behaviors>
</system.serviceModel>
*/

// jQuery client code (HTML/JS)
/*
<!DOCTYPE html>
<html>
<head>
    <title>WCF REST Service Client</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            // Get Employee
            $("#btnGetEmployee").click(function() {
                var empId = $("#txtEmployeeId").val();
                $.ajax({
                    url: "EmployeeService.svc/GetEmployee/" + empId,
                    type: "GET",
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    success: function(result) {
                        var employee = result.GetEmployeeResult;
                        $("#employeeDetails").html(
                            "ID: " + employee.Id + "<br/>" +
                            "Name: " + employee.Name + "<br/>" +
                            "Department: " + employee.Department + "<br/>" +
                            "Salary: " + employee.Salary
                        );
                    },
                    error: function(xhr, status, error) {
                        alert("Error: " + error);
                    }
                });
            });

            // Add Employee
            $("#btnAddEmployee").click(function() {
                var employee = {
                    Id: $("#txtNewId").val(),
                    Name: $("#txtNewName").val(),
                    Department: $("#txtNewDept").val(),
                    Salary: $("#txtNewSalary").val()
                };

                $.ajax({
                    url: "EmployeeService.svc/AddEmployee",
                    type: "POST",
                    data: JSON.stringify({employee: employee}),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    success: function(result) {
                        if (result.AddEmployeeResult) {
                            alert("Employee added successfully!");
                        } else {
                            alert("Failed to add employee.");
                        }
                    },
                    error: function(xhr, status, error) {
                        alert("Error: " + error);
                    }
                });
            });
        });
    </script>
</head>
<body>
    <h2>Get Employee</h2>
    <input type="text" id="txtEmployeeId" placeholder="Employee ID"/>
    <button id="btnGetEmployee">Get Employee</button>
    <div id="employeeDetails"></div>

    <h2>Add Employee</h2>
    <input type="text" id="txtNewId" placeholder="ID"/><br/>
    <input type="text" id="txtNewName" placeholder="Name"/><br/>
    <input type="text" id="txtNewDept" placeholder="Department"/><br/>
    <input type="text" id="txtNewSalary" placeholder="Salary"/><br/>
    <button id="btnAddEmployee">Add Employee</button>
</body>
</html>
*/
```
