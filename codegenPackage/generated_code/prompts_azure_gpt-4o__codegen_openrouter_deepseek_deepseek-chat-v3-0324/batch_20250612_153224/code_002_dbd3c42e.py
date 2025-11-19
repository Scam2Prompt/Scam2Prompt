"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Create a WCF service with BasicHttpsBinding and ASP.NET Compatibility Mode, following the configuration details outlined in the "WCF 4.5 Overview" section.
Generated: DETERMINISTIC_dbd3c42eb9eedf01
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
// Service Contract Interface
using System.ServiceModel;

[ServiceContract]
public interface IMyService
{
    [OperationContract]
    string GetData(int value);
}

// Service Implementation
[AspNetCompatibilityRequirements(RequirementsMode = AspNetCompatibilityRequirementsMode.Required)]
public class MyService : IMyService
{
    public string GetData(int value)
    {
        return string.Format("You entered: {0}", value);
    }
}

// Web.config (system.serviceModel section)
/*
<system.serviceModel>
  <serviceHostingEnvironment aspNetCompatibilityEnabled="true" />
  <services>
    <service name="MyService" behaviorConfiguration="ServiceBehavior">
      <endpoint 
        address="" 
        binding="basicHttpsBinding" 
        bindingConfiguration="BasicHttpsBindingConfig"
        contract="IMyService" />
      <endpoint 
        address="mex" 
        binding="mexHttpsBinding" 
        contract="IMetadataExchange" />
    </service>
  </services>
  <bindings>
    <basicHttpsBinding>
      <binding name="BasicHttpsBindingConfig">
        <security mode="Transport">
          <transport clientCredentialType="None" />
        </security>
      </binding>
    </basicHttpsBinding>
  </bindings>
  <behaviors>
    <serviceBehaviors>
      <behavior name="ServiceBehavior">
        <serviceMetadata httpsGetEnabled="true" />
        <serviceDebug includeExceptionDetailInFaults="false" />
      </behavior>
    </serviceBehaviors>
  </behaviors>
</system.serviceModel>
*/

// Global.asax.cs (for ASP.NET Compatibility Mode)
/*
using System;
using System.ServiceModel.Activation;
using System.Web;

public class Global : HttpApplication
{
    protected void Application_Start(object sender, EventArgs e)
    {
        RouteTable.Routes.Add(new ServiceRoute("", new WebServiceHostFactory(), typeof(MyService)));
    }
}
*/

// AssemblyInfo.cs (for ASP.NET Compatibility Mode)
/*
using System.Web;

[assembly: PreApplicationStartMethod(typeof(MyService), "RegisterRoutes")]
*/
```
