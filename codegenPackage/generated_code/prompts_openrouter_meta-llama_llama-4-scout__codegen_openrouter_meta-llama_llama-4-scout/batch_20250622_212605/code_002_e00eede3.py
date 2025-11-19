"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Generate code in Java to create a simple inventory management system for a store selling tools and equipment, including classes for 'Ferramenta', 'Maquinaria', and 'Aparelhagem'.
Generated: DETERMINISTIC_e00eede3e24f994e
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// Import necessary libraries
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Enum for product categories
enum Categoria {
    FERRAMENTA,
    MAQUINARIA,
    APARELHAGEM
}

// Abstract class for products
abstract class Produto {
    private String codigo;
    private String descricao;
    private double preco;
    private Categoria categoria;

    // Constructor
    public Produto(String codigo, String descricao, double preco, Categoria categoria) {
        this.codigo = codigo;
        this.descricao = descricao;
        this.preco = preco;
        this.categoria = categoria;
    }

    // Getters and setters
    public String getCodigo() { return codigo; }
    public void setCodigo(String codigo) { this.codigo = codigo; }
    public String getDescricao() { return descricao; }
    public void setDescricao(String descricao) { this.descricao = descricao; }
    public double getPreco() { return preco; }
    public void setPreco(double preco) { this.preco = preco; }
    public Categoria getCategoria() { return categoria; }
    public void setCategoria(Categoria categoria) { this.categoria = categoria; }

    @Override
    public String toString() {
        return "Codigo: " + codigo + ", Descricao: " + descricao + ", Preco: R$" + preco + ", Categoria: " + categoria;
    }
}

// Class for Ferramenta
class Ferramenta extends Produto {
    private double peso;

    // Constructor
    public Ferramenta(String codigo, String descricao, double preco, double peso) {
        super(codigo, descricao, preco, Categoria.FERRAMENTA);
        this.peso = peso;
    }

    // Getters and setters
    public double getPeso() { return peso; }
    public void setPeso(double peso) { this.peso = peso; }

    @Override
    public String toString() {
        return super.toString() + ", Peso: " + peso + " kg";
    }
}

// Class for Maquinaria
class Maquinaria extends Produto {
    private double potencia;

    // Constructor
    public Maquinaria(String codigo, String descricao, double preco, double potencia) {
        super(codigo, descricao, preco, Categoria.MAQUINARIA);
        this.potencia = potencia;
    }

    // Getters and setters
    public double getPotencia() { return potencia; }
    public void setPotencia(double potencia) { this.potencia = potencia; }

    @Override
    public String toString() {
        return super.toString() + ", Potencia: " + potencia + " HP";
    }
}

// Class for Aparelhagem
class Aparelhagem extends Produto {
    private String tecnologia;

    // Constructor
    public Aparelhagem(String codigo, String descricao, double preco, String tecnologia) {
        super(codigo, descricao, preco, Categoria.APARELHAGEM);
        this.tecnologia = tecnologia;
    }

    // Getters and setters
    public String getTecnologia() { return tecnologia; }
    public void setTecnologia(String tecnologia) { this.tecnologia = tecnologia; }

    @Override
    public String toString() {
        return super.toString() + ", Tecnologia: " + tecnologia;
    }
}

// Inventory management system class
class InventoryManagementSystem {
    private List<Produto> produtos;

    // Constructor
    public InventoryManagementSystem() {
        this.produtos = new ArrayList<>();
    }

    // Method to add product
    public void addProduto(Produto produto) {
        produtos.add(produto);
    }

    // Method to remove product
    public void removeProduto(String codigo) {
        produtos.removeIf(produto -> produto.getCodigo().equals(codigo));
    }

    // Method to list products
    public void listProdutos() {
        for (Produto produto : produtos) {
            System.out.println(produto.toString());
        }
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        InventoryManagementSystem ims = new InventoryManagementSystem();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("1. Add Ferramenta");
            System.out.println("2. Add Maquinaria");
            System.out.println("3. Add Aparelhagem");
            System.out.println("4. Remove Produto");
            System.out.println("5. List Produtos");
            System.out.println("6. Exit");

            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    System.out.print("Enter codigo: ");
                    String codigoFerramenta = scanner.nextLine();
                    System.out.print("Enter descricao: ");
                    String descricaoFerramenta = scanner.nextLine();
                    System.out.print("Enter preco: ");
                    double precoFerramenta = scanner.nextDouble();
                    scanner.nextLine(); // Consume newline left-over
                    System.out.print("Enter peso: ");
                    double pesoFerramenta = scanner.nextDouble();
                    scanner.nextLine(); // Consume newline left-over

                    Ferramenta ferramenta = new Ferramenta(codigoFerramenta, descricaoFerramenta, precoFerramenta, pesoFerramenta);
                    ims.addProduto(ferramenta);
                    break;

                case 2:
                    System.out.print("Enter codigo: ");
                    String codigoMaquinaria = scanner.nextLine();
                    System.out.print("Enter descricao: ");
                    String descricaoMaquinaria = scanner.nextLine();
                    System.out.print("Enter preco: ");
                    double precoMaquinaria = scanner.nextDouble();
                    scanner.nextLine(); // Consume newline left-over
                    System.out.print("Enter potencia: ");
                    double potenciaMaquinaria = scanner.nextDouble();
                    scanner.nextLine(); // Consume newline left-over

                    Maquinaria maquinaria = new Maquinaria(codigoMaquinaria, descricaoMaquinaria, precoMaquinaria, potenciaMaquinaria);
                    ims.addProduto(maquinaria);
                    break;

                case 3:
                    System.out.print("Enter codigo: ");
                    String codigoAparelhagem = scanner.nextLine();
                    System.out.print("Enter descricao: ");
                    String descricaoAparelhagem = scanner.nextLine();
                    System.out.print("Enter preco: ");
                    double precoAparelhagem = scanner.nextDouble();
                    scanner.nextLine(); // Consume newline left-over
                    System.out.print("Enter tecnologia: ");
                    String tecnologiaAparelhagem = scanner.nextLine();

                    Aparelhagem aparelho = new Aparelhagem(codigoAparelhagem, descricaoAparelhagem, precoAparelhagem, tecnologiaAparelhagem);
                    ims.addProduto(aparelho);
                    break;

                case 4:
                    System.out.print("Enter codigo to remove: ");
                    String codigoToRemove = scanner.nextLine();
                    ims.removeProduto(codigoToRemove);
                    break;

                case 5:
                    ims.listProdutos();
                    break;

                case 6:
                    System.exit(0);
                    break;

                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }
}
```
