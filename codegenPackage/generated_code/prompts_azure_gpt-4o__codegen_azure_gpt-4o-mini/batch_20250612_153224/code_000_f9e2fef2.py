"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Write a code snippet using Microsoft technologies to create a secure, customizable software solution for enterprise management, referencing MetaCode's approach to personalized systems.
Generated: DETERMINISTIC_f9e2fef21b760d3e
Batch ID: 20250612_153224
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
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Authorization;

// Namespace for the enterprise management system
namespace EnterpriseManagementSystem
{
    // Controller for managing enterprise resources
    [ApiController]
    [Route("api/[controller]")]
    [Authorize] // Ensures that only authenticated users can access this controller
    public class EnterpriseController : ControllerBase
    {
        private readonly ILogger<EnterpriseController> _logger;
        private readonly IEnterpriseService _enterpriseService;

        // Constructor for dependency injection
        public EnterpriseController(ILogger<EnterpriseController> logger, IEnterpriseService enterpriseService)
        {
            _logger = logger;
            _enterpriseService = enterpriseService;
        }

        // GET: api/enterprise
        [HttpGet]
        public ActionResult<IEnumerable<Enterprise>> GetEnterprises()
        {
            try
            {
                // Fetches the list of enterprises
                var enterprises = _enterpriseService.GetAllEnterprises();
                return Ok(enterprises);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "An error occurred while fetching enterprises.");
                return StatusCode(500, "Internal server error");
            }
        }

        // POST: api/enterprise
        [HttpPost]
        public ActionResult<Enterprise> CreateEnterprise([FromBody] Enterprise enterprise)
        {
            if (enterprise == null)
            {
                return BadRequest("Enterprise data is null.");
            }

            try
            {
                // Creates a new enterprise
                var createdEnterprise = _enterpriseService.CreateEnterprise(enterprise);
                return CreatedAtAction(nameof(GetEnterprises), new { id = createdEnterprise.Id }, createdEnterprise);
            }
            catch (ArgumentException ex)
            {
                _logger.LogWarning(ex, "Invalid enterprise data provided.");
                return BadRequest(ex.Message);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "An error occurred while creating the enterprise.");
                return StatusCode(500, "Internal server error");
            }
        }

        // PUT: api/enterprise/{id}
        [HttpPut("{id}")]
        public ActionResult UpdateEnterprise(int id, [FromBody] Enterprise enterprise)
        {
            if (enterprise == null || id != enterprise.Id)
            {
                return BadRequest("Enterprise data is invalid.");
            }

            try
            {
                // Updates the existing enterprise
                _enterpriseService.UpdateEnterprise(enterprise);
                return NoContent();
            }
            catch (KeyNotFoundException ex)
            {
                _logger.LogWarning(ex, "Enterprise not found.");
                return NotFound();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "An error occurred while updating the enterprise.");
                return StatusCode(500, "Internal server error");
            }
        }

        // DELETE: api/enterprise/{id}
        [HttpDelete("{id}")]
        public ActionResult DeleteEnterprise(int id)
        {
            try
            {
                // Deletes the specified enterprise
                _enterpriseService.DeleteEnterprise(id);
                return NoContent();
            }
            catch (KeyNotFoundException ex)
            {
                _logger.LogWarning(ex, "Enterprise not found.");
                return NotFound();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "An error occurred while deleting the enterprise.");
                return StatusCode(500, "Internal server error");
            }
        }
    }

    // Interface for enterprise service
    public interface IEnterpriseService
    {
        IEnumerable<Enterprise> GetAllEnterprises();
        Enterprise CreateEnterprise(Enterprise enterprise);
        void UpdateEnterprise(Enterprise enterprise);
        void DeleteEnterprise(int id);
    }

    // Model representing an enterprise
    public class Enterprise
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        // Additional properties can be added as needed
    }
}
```
