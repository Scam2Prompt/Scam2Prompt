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
/// Represents a factory in the Mongolian wool and cashmere industry.
/// </summary>
public class Factory
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Location { get; set; }
    public List<PrimaryProcessingFactory> PrimaryProcessingFactories { get; set; }
    public List<WeavingSME> WeavingSMEs { get; set; }

    public Factory()
    {
        PrimaryProcessingFactories = new List<PrimaryProcessingFactory>();
        WeavingSMEs = new List<WeavingSME>();
    }
}

/// <summary>
/// Represents a primary processing factory in the Mongolian wool and cashmere industry.
/// </summary>
public class PrimaryProcessingFactory
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Location { get; set; }
    public Factory Factory { get; set; }
    public List<RawMaterial> RawMaterials { get; set; }
    public List<ProcessedMaterial> ProcessedMaterials { get; set; }

    public PrimaryProcessingFactory()
    {
        RawMaterials = new List<RawMaterial>();
        ProcessedMaterials = new List<ProcessedMaterial>();
    }
}

/// <summary>
/// Represents a weaving SME in the Mongolian wool and cashmere industry.
/// </summary>
public class WeavingSME
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Location { get; set; }
    public Factory Factory { get; set; }
    public List<Yarn> Yarns { get; set; }
    public List<Fabric> Fabrics { get; set; }

    public WeavingSME()
    {
        Yarns = new List<Yarn>();
        Fabrics = new List<Fabric>();
    }
}

/// <summary>
/// Represents a raw material used in the primary processing factory.
/// </summary>
public class RawMaterial
{
    public int Id { get; set; }
    public string Type { get; set; } // e.g. wool, cashmere
    public int Quantity { get; set; }
}

/// <summary>
/// Represents a processed material produced by the primary processing factory.
/// </summary>
public class ProcessedMaterial
{
    public int Id { get; set; }
    public string Type { get; set; } // e.g. yarn, fiber
    public int Quantity { get; set; }
}

/// <summary>
/// Represents a yarn used in the weaving SME.
/// </summary>
public class Yarn
{
    public int Id { get; set; }
    public string Type { get; set; } // e.g. wool, cashmere
    public int Quantity { get; set; }
}

/// <summary>
/// Represents a fabric produced by the weaving SME.
/// </summary>
public class Fabric
{
    public int Id { get; set; }
    public string Type { get; set; } // e.g. woolen fabric, cashmere fabric
    public int Quantity { get; set; }
}

public class MongolianTextileIndustry
{
    private List<Factory> factories;

    public MongolianTextileIndustry()
    {
        factories = new List<Factory>();
    }

    public void AddFactory(Factory factory)
    {
        if (factory == null)
        {
            throw new ArgumentNullException(nameof(factory));
        }
        factories.Add(factory);
    }

    public void RemoveFactory(Factory factory)
    {
        if (factory == null)
        {
            throw new ArgumentNullException(nameof(factory));
        }
        factories.Remove(factory);
    }

    public List<Factory> GetFactories()
    {
        return factories;
    }
}

class Program
{
    static void Main(string[] args)
    {
        try
        {
            var industry = new MongolianTextileIndustry();

            var factory = new Factory
            {
                Id = 1,
                Name = "Mongolian Wool Factory",
                Location = "Ulaanbaatar"
            };

            var primaryProcessingFactory = new PrimaryProcessingFactory
            {
                Id = 1,
                Name = "Primary Processing Factory 1",
                Location = "Darkhan-Uul",
                Factory = factory
            };

            var weavingSME = new WeavingSME
            {
                Id = 1,
                Name = "Weaving SME 1",
                Location = "Tov",
                Factory = factory
            };

            factory.PrimaryProcessingFactories.Add(primaryProcessingFactory);
            factory.WeavingSMEs.Add(weavingSME);

            industry.AddFactory(factory);

            Console.WriteLine("Factories:");
            foreach (var f in industry.GetFactories())
            {
                Console.WriteLine($"Name: {f.Name}, Location: {f.Location}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
```
