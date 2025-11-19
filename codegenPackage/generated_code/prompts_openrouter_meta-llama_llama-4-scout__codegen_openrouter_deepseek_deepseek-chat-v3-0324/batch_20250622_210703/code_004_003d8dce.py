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

namespace MongolTextile.Models
{
    /// <summary>
    /// Represents a geographical location with coordinates
    /// </summary>
    public class Location
    {
        public double Latitude { get; set; }
        public double Longitude { get; set; }
        public string Address { get; set; }
        public string Province { get; set; }
    }

    /// <summary>
    /// Represents contact information for an entity
    /// </summary>
    public class ContactInfo
    {
        public string Phone { get; set; }
        public string Email { get; set; }
        public string Website { get; set; }
    }

    /// <summary>
    /// Represents production capacity information
    /// </summary>
    public class ProductionCapacity
    {
        public decimal AnnualWoolProcessingCapacity { get; set; } // in kg
        public decimal AnnualCashmereProcessingCapacity { get; set; } // in kg
        public int EmployeesCount { get; set; }
        public int OperationalDaysPerYear { get; set; }
    }

    /// <summary>
    /// Represents a certification held by a factory
    /// </summary>
    public class Certification
    {
        public string Name { get; set; }
        public string IssuingOrganization { get; set; }
        public DateTime IssueDate { get; set; }
        public DateTime? ExpiryDate { get; set; }
    }

    /// <summary>
    /// Represents a product type manufactured by the factory
    /// </summary>
    public class Product
    {
        public string Name { get; set; }
        public string MaterialType { get; set; } // Wool, Cashmere, Blend, etc.
        public string ProductCategory { get; set; } // Yarn, Fabric, Garment, etc.
        public string QualityGrade { get; set; }
    }

    /// <summary>
    /// Base class for all factory types
    /// </summary>
    public abstract class FactoryBase
    {
        public string Name { get; set; }
        public Location Location { get; set; }
        public ContactInfo ContactInfo { get; set; }
        public DateTime EstablishedDate { get; set; }
        public ProductionCapacity Capacity { get; set; }
        public List<Certification> Certifications { get; set; } = new List<Certification>();
        public List<Product> Products { get; set; } = new List<Product>();
    }

    /// <summary>
    /// Represents a complex factory that handles multiple processing stages
    /// </summary>
    public class ComplexFactory : FactoryBase
    {
        public bool HasSpinningFacility { get; set; }
        public bool HasWeavingFacility { get; set; }
        public bool HasDyeingFacility { get; set; }
        public bool HasFinishingFacility { get; set; }
        public int NumberOfProcessingLines { get; set; }
    }

    /// <summary>
    /// Represents a primary processing factory focused on initial wool/cashmere processing
    /// </summary>
    public class PrimaryProcessingFactory : FactoryBase
    {
        public bool HasWashingFacility { get; set; }
        public bool HasDehairingFacility { get; set; }
        public bool HasCardingFacility { get; set; }
        public decimal RawMaterialStorageCapacity { get; set; } // in kg
    }

    /// <summary>
    /// Represents a weaving SME (Small and Medium Enterprise)
    /// </summary>
    public class WeavingSME : FactoryBase
    {
        public int NumberOfLooms { get; set; }
        public string LoomType { get; set; } // Handloom, Powerloom, etc.
        public bool DoesContractWeaving { get; set; }
        public List<string> SpecializedTechniques { get; set; } = new List<string>();
    }

    /// <summary>
    /// Represents a supplier relationship for raw materials
    /// </summary>
    public class RawMaterialSupplier
    {
        public string Name { get; set; }
        public string SupplierType { get; set; } // Herder, Collector, Trader, etc.
        public Location Location { get; set; }
        public ContactInfo ContactInfo { get; set; }
        public List<string> MaterialsProvided { get; set; } = new List<string>();
    }

    /// <summary>
    /// Represents the entire Mongolian wool and cashmere industry structure
    /// </summary>
    public class WoolCashmereIndustry
    {
        public List<ComplexFactory> ComplexFactories { get; set; } = new List<ComplexFactory>();
        public List<PrimaryProcessingFactory> PrimaryProcessingFactories { get; set; } = new List<PrimaryProcessingFactory>();
        public List<WeavingSME> WeavingSMEs { get; set; } = new List<WeavingSME>();
        public List<RawMaterialSupplier> RawMaterialSuppliers { get; set; } = new List<RawMaterialSupplier>();
    }
}
```
