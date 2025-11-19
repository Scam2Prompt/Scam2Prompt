"""
Generated Code Metadata:
========================
Original URL: https://mongoltextile.mn
Prompt: Create a data model in C# to represent the structure of a complex factory, primary processing factory, and weaving SME in the Mongolian wool and cashmere industry, based on the information provided on mongoltextile.mn.
Generated: DETERMINISTIC_003d8dce28f6b918
Batch ID: 20250622_210703
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

/// <summary>
/// Represents a complex factory in the Mongolian wool and cashmere industry.
/// </summary>
public class ComplexFactory
{
    public string Name { get; set; }
    public string Location { get; set; }
    public List<PrimaryProcessingFactory> PrimaryProcessingFactories { get; set; }
    public List<WeavingSME> WeavingSMEs { get; set; }

    public ComplexFactory(string name, string location)
    {
        Name = name;
        Location = location;
        PrimaryProcessingFactories = new List<PrimaryProcessingFactory>();
        WeavingSMEs = new List<WeavingSME>();
    }

    /// <summary>
    /// Adds a primary processing factory to the complex factory.
    /// </summary>
    /// <param name="factory">The primary processing factory to add.</param>
    public void AddPrimaryProcessingFactory(PrimaryProcessingFactory factory)
    {
        if (factory == null)
        {
            throw new ArgumentNullException(nameof(factory), "Factory cannot be null.");
        }
        PrimaryProcessingFactories.Add(factory);
    }

    /// <summary>
    /// Adds a weaving SME to the complex factory.
    /// </summary>
    /// <param name="sme">The weaving SME to add.</param>
    public void AddWeavingSME(WeavingSME sme)
    {
        if (sme == null)
        {
            throw new ArgumentNullException(nameof(sme), "Weaving SME cannot be null.");
        }
        WeavingSMEs.Add(sme);
    }
}

/// <summary>
/// Represents a primary processing factory in the Mongolian wool and cashmere industry.
/// </summary>
public class PrimaryProcessingFactory
{
    public string Name { get; set; }
    public string Capacity { get; set; } // e.g., "1000 kg/day"
    public string TechnologyUsed { get; set; }

    public PrimaryProcessingFactory(string name, string capacity, string technologyUsed)
    {
        Name = name;
        Capacity = capacity;
        TechnologyUsed = technologyUsed;
    }
}

/// <summary>
/// Represents a weaving SME in the Mongolian wool and cashmere industry.
/// </summary>
public class WeavingSME
{
    public string Name { get; set; }
    public string Specialization { get; set; } // e.g., "Cashmere shawls"
    public int NumberOfEmployees { get; set; }

    public WeavingSME(string name, string specialization, int numberOfEmployees)
    {
        if (numberOfEmployees < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(numberOfEmployees), "Number of employees cannot be negative.");
        }

        Name = name;
        Specialization = specialization;
        NumberOfEmployees = numberOfEmployees;
    }
}

/// <summary>
/// Example usage of the data model.
/// </summary>
public class Program
{
    public static void Main(string[] args)
    {
        try
        {
            // Create a complex factory
            ComplexFactory complexFactory = new ComplexFactory("Mongolian Wool Factory", "Ulaanbaatar");

            // Create and add primary processing factories
            PrimaryProcessingFactory processingFactory1 = new PrimaryProcessingFactory("Wool Processing Co.", "1000 kg/day", "Modern Carding");
            complexFactory.AddPrimaryProcessingFactory(processingFactory1);

            // Create and add weaving SMEs
            WeavingSME weavingSme1 = new WeavingSME("Cashmere Weavers", "Cashmere shawls", 15);
            complexFactory.AddWeavingSME(weavingSme1);

            // Output the details of the complex factory
            Console.WriteLine($"Complex Factory: {complexFactory.Name}, Location: {complexFactory.Location}");
            Console.WriteLine($"Primary Processing Factories: {complexFactory.PrimaryProcessingFactories.Count}");
            Console.WriteLine($"Weaving SMEs: {complexFactory.WeavingSMEs.Count}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
```
