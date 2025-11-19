"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.net
Prompt: How do I set up a WCF service with ASP.NET compatibility mode and utilize basic HTTPS binding?
Generated: DETERMINISTIC_0d9154f296d3ba3b
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
// Service Contract Interface
[ServiceContract]
public interface IMyService
{
    [OperationContract]
    string GetData(int value);
}

// Service Implementation with ASP.NET Compatibility Mode
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
    <service name="MyNamespace.MyService" behaviorConfiguration="ServiceBehavior">
      <endpoint 
        address="" 
        binding="basicHttpsBinding" 
        contract="MyNamespace.IMyService" />
      <endpoint 
        address="mex" 
        binding="mexHttpsBinding" 
        contract="IMetadataExchange" />
    </service>
  </services>
  <behaviors>
    <serviceBehaviors>
      <behavior name="ServiceBehavior">
        <serviceMetadata httpsGetEnabled="true" />
        <serviceDebug includeExceptionDetailInFaults="false" />
      </behavior>
    </serviceBehaviors>
  </behaviors>
  <bindings>
    <basicHttpsBinding>
      <binding name="BasicHttpsBindingConfig">
        <security mode="Transport">
          <transport clientCredentialType="None" />
        </security>
      </binding>
    </basicHttpsBinding>
  </bindings>
</system.serviceModel>
*/

// Global.asax.cs (for IIS hosting)
/*
public class Global : System.Web.HttpApplication
{
    protected void Application_Start(object sender, EventArgs e)
    {
        RouteTable.Routes.Add(new ServiceRoute("", new WebServiceHostFactory(), typeof(MyService)));
    }
}
*/

// SSL Configuration (in IIS)
/*
1. Create or obtain an SSL certificate
2. Bind the certificate to your website in IIS
3. Ensure the site is configured to require HTTPS
*/
```
