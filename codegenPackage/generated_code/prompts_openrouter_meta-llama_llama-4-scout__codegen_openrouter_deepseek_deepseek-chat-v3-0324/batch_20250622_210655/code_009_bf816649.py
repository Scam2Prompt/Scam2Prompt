"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Implement a WCF service that uses transactions and provides a task-based programming model.
Generated: DETERMINISTIC_bf816649b11adbc0
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
using System.ServiceModel;
using System.ServiceModel.Channels;
using System.Transactions;
using System.Threading.Tasks;

namespace TaskBasedWcfService
{
    [ServiceContract]
    public interface ITaskService
    {
        [OperationContract]
        [TransactionFlow(TransactionFlowOption.Mandatory)]
        Task<string> PerformTaskAsync(int taskId);

        [OperationContract]
        [TransactionFlow(TransactionFlowOption.Mandatory)]
        Task<bool> CompleteTaskAsync(int taskId);
    }

    [ServiceBehavior(
        InstanceContextMode = InstanceContextMode.PerCall,
        ConcurrencyMode = ConcurrencyMode.Multiple,
        ReleaseServiceInstanceOnTransactionComplete = false)]
    public class TaskService : ITaskService
    {
        [OperationBehavior(TransactionScopeRequired = true, TransactionAutoComplete = true)]
        public async Task<string> PerformTaskAsync(int taskId)
        {
            try
            {
                // Simulate async work
                await Task.Delay(100);

                if (taskId < 0)
                {
                    throw new ArgumentException("Task ID cannot be negative", nameof(taskId));
                }

                return $"Task {taskId} performed successfully";
            }
            catch (Exception ex)
            {
                throw new FaultException(ex.Message);
            }
        }

        [OperationBehavior(TransactionScopeRequired = true, TransactionAutoComplete = true)]
        public async Task<bool> CompleteTaskAsync(int taskId)
        {
            try
            {
                // Simulate async work
                await Task.Delay(100);

                if (taskId == 0)
                {
                    throw new ArgumentException("Invalid task ID", nameof(taskId));
                }

                return true;
            }
            catch (Exception ex)
            {
                throw new FaultException(ex.Message);
            }
        }
    }

    public class ServiceHostFactory
    {
        public static ServiceHost CreateServiceHost()
        {
            var binding = new NetTcpBinding
            {
                TransactionFlow = true,
                MaxReceivedMessageSize = 65536,
                TransferMode = TransferMode.Buffered
            };

            var host = new ServiceHost(typeof(TaskService));
            host.AddServiceEndpoint(typeof(ITaskService), binding, "net.tcp://localhost:8000/TaskService");

            return host;
        }
    }

    public class Program
    {
        public static async Task Main(string[] args)
        {
            using (var host = ServiceHostFactory.CreateServiceHost())
            {
                host.Open();
                Console.WriteLine("Service is running. Press any key to exit...");
                Console.ReadKey();
                host.Close();
            }
        }
    }
}
```
