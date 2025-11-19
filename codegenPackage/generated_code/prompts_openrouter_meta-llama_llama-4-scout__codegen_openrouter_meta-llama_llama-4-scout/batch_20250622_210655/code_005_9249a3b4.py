"""
Generated Code Metadata:
========================
Original URL: https://webservicesindia.info
Prompt: "Develop a .NET code snippet for a basic RESTful API using C# and ASP.NET Core, reflecting WebServicesIndia's expertise in .NET Development."
Generated: DETERMINISTIC_9249a3b4c9774ffd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;

// Model
public class Book
{
    public int Id { get; set; }
    [Required]
    public string Title { get; set; }
    [Required]
    public string Author { get; set; }
}

// DbContext
public class LibraryDbContext : DbContext
{
    public LibraryDbContext(DbContextOptions<LibraryDbContext> options) : base(options)
    {
    }

    public DbSet<Book> Books { get; set; }
}

// Controller
[ApiController]
[Route("api/[controller]")]
public class BooksController : ControllerBase
{
    private readonly LibraryDbContext _context;
    private readonly ILogger<BooksController> _logger;

    public BooksController(LibraryDbContext context, ILogger<BooksController> logger)
    {
        _context = context;
        _logger = logger;
    }

    // GET: api/books
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Book>>> GetBooks()
    {
        try
        {
            return await _context.Books.ToListAsync();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error getting books");
            return StatusCode(500, "Internal server error");
        }
    }

    // GET: api/books/5
    [HttpGet("{id}")]
    public async Task<ActionResult<Book>> GetBook(int id)
    {
        try
        {
            var book = await _context.Books.FindAsync(id);

            if (book == null)
            {
                return NotFound();
            }

            return book;
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error getting book");
            return StatusCode(500, "Internal server error");
        }
    }

    // POST: api/books
    [HttpPost]
    public async Task<ActionResult<Book>> PostBook(Book book)
    {
        try
        {
            _context.Books.Add(book);
            await _context.SaveChangesAsync();

            return CreatedAtAction(nameof(GetBook), new { id = book.Id }, book);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error creating book");
            return StatusCode(500, "Internal server error");
        }
    }

    // PUT: api/books/5
    [HttpPut("{id}")]
    public async Task<ActionResult> PutBook(int id, Book book)
    {
        try
        {
            if (id != book.Id)
            {
                return BadRequest();
            }

            _context.Entry(book).State = EntityState.Modified;
            await _context.SaveChangesAsync();

            return NoContent();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error updating book");
            return StatusCode(500, "Internal server error");
        }
    }

    // DELETE: api/books/5
    [HttpDelete("{id}")]
    public async Task<ActionResult> DeleteBook(int id)
    {
        try
        {
            var book = await _context.Books.FindAsync(id);
            if (book == null)
            {
                return NotFound();
            }

            _context.Books.Remove(book);
            await _context.SaveChangesAsync();

            return NoContent();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error deleting book");
            return StatusCode(500, "Internal server error");
        }
    }
}

// Startup
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddDbContext<LibraryDbContext>(options =>
            options.UseInMemoryDatabase(databaseName: "Library"));
        services.AddControllers();
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        app.UseRouting();
        app.UseEndpoints(endpoints =>
        {
            endpoints.MapControllers();
        });
    }
}

// Program
public class Program
{
    public static void Main(string[] args)
    {
        CreateHostBuilder(args).Build().Run();
    }

    public static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .ConfigureWebHostDefaults(webBuilder =>
            {
                webBuilder.UseStartup<Startup>();
            });
}
```
