"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Implement a lexical analyzer in C that builds a symbol table for variables and their types, as described in the LEX ANALYSER AND SYMBOL TABLE example.
Generated: DETERMINISTIC_9e377dcde960549f
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_IDENT_LEN 32
#define MAX_SYMBOLS 100

// Token types
typedef enum {
    TOKEN_IDENTIFIER,
    TOKEN_NUMBER,
    TOKEN_KEYWORD,
    TOKEN_OPERATOR,
    TOKEN_DELIMITER,
    TOKEN_UNKNOWN,
    TOKEN_EOF
} TokenType;

// Symbol table entry
typedef struct {
    char name[MAX_IDENT_LEN];
    char type[20];
    int scope;
    int line_no;
} SymbolEntry;

// Symbol table
SymbolEntry symbol_table[MAX_SYMBOLS];
int symbol_count = 0;

// Keywords
const char *keywords[] = {
    "int", "float", "char", "double", "void",
    "if", "else", "while", "for", "return"
};
const int num_keywords = sizeof(keywords) / sizeof(keywords[0]);

// Current token information
typedef struct {
    TokenType type;
    char lexeme[MAX_IDENT_LEN];
    int line_no;
} Token;

// Function prototypes
Token get_next_token(FILE *src);
void add_to_symbol_table(const char *name, const char *type, int line_no);
void print_symbol_table();
int is_keyword(const char *str);
void lexical_error(int line_no, const char *msg);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <source_file>\n", argv[0]);
        return 1;
    }

    FILE *src = fopen(argv[1], "r");
    if (!src) {
        perror("Error opening source file");
        return 1;
    }

    Token token;
    char current_type[20] = ""; // To track variable declarations
    
    printf("Starting lexical analysis...\n");
    
    while (1) {
        token = get_next_token(src);
        
        if (token.type == TOKEN_EOF) {
            break;
        }
        
        // Check if this is a type keyword (variable declaration)
        if (strcmp(token.lexeme, "int") == 0 || strcmp(token.lexeme, "float") == 0 ||
            strcmp(token.lexeme, "char") == 0 || strcmp(token.lexeme, "double") == 0) {
            strcpy(current_type, token.lexeme);
        }
        // If we have a type and next token is identifier, add to symbol table
        else if (current_type[0] != '\0' && token.type == TOKEN_IDENTIFIER) {
            add_to_symbol_table(token.lexeme, current_type, token.line_no);
            current_type[0] = '\0'; // Reset type
        }
        else {
            current_type[0] = '\0'; // Reset type if not followed by identifier
        }
    }
    
    fclose(src);
    
    printf("\nLexical analysis completed.\n");
    print_symbol_table();
    
    return 0;
}

Token get_next_token(FILE *src) {
    Token token;
    token.type = TOKEN_UNKNOWN;
    token.lexeme[0] = '\0';
    static int line_no = 1;
    
    int c = fgetc(src);
    
    // Skip whitespace
    while (isspace(c)) {
        if (c == '\n') line_no++;
        c = fgetc(src);
    }
    
    if (c == EOF) {
        token.type = TOKEN_EOF;
        token.line_no = line_no;
        return token;
    }
    
    token.line_no = line_no;
    
    // Handle identifiers and keywords
    if (isalpha(c) || c == '_') {
        int i = 0;
        token.lexeme[i++] = c;
        
        while ((c = fgetc(src)) != EOF && (isalnum(c) || c == '_')) {
            if (i < MAX_IDENT_LEN - 1) {
                token.lexeme[i++] = c;
            }
        }
        token.lexeme[i] = '\0';
        
        ungetc(c, src); // Put back the non-identifier character
        
        if (is_keyword(token.lexeme)) {
            token.type = TOKEN_KEYWORD;
        } else {
            token.type = TOKEN_IDENTIFIER;
        }
    }
    // Handle numbers
    else if (isdigit(c)) {
        int i = 0;
        token.lexeme[i++] = c;
        
        while ((c = fgetc(src)) != EOF && isdigit(c)) {
            if (i < MAX_IDENT_LEN - 1) {
                token.lexeme[i++] = c;
            }
        }
        
        // Check for floating point
        if (c == '.') {
            if (i < MAX_IDENT_LEN - 1) {
                token.lexeme[i++] = c;
            }
            while ((c = fgetc(src)) != EOF && isdigit(c)) {
                if (i < MAX_IDENT_LEN - 1) {
                    token.lexeme[i++] = c;
                }
            }
        }
        
        token.lexeme[i] = '\0';
        ungetc(c, src);
        token.type = TOKEN_NUMBER;
    }
    // Handle operators and delimiters
    else {
        token.lexeme[0] = c;
        token.lexeme[1] = '\0';
        
        switch (c) {
            case '+': case '-': case '*': case '/': 
            case '=': case '<': case '>': case '!':
                token.type = TOKEN_OPERATOR;
                break;
            case ';': case ',': case '(': case ')': 
            case '{': case '}': case '[': case ']':
                token.type = TOKEN_DELIMITER;
                break;
            default:
                lexical_error(line_no, "Unknown character");
                token.type = TOKEN_UNKNOWN;
        }
    }
    
    return token;
}

void add_to_symbol_table(const char *name, const char *type, int line_no) {
    if (symbol_count >= MAX_SYMBOLS) {
        fprintf(stderr, "Symbol table overflow at line %d\n", line_no);
        return;
    }
    
    // Check if symbol already exists
    for (int i = 0; i < symbol_count; i++) {
        if (strcmp(symbol_table[i].name, name) == 0) {
            fprintf(stderr, "Warning: Redeclaration of '%s' at line %d\n", name, line_no);
            return;
        }
    }
    
    // Add new symbol
    strncpy(symbol_table[symbol_count].name, name, MAX_IDENT_LEN);
    strncpy(symbol_table[symbol_count].type, type, 20);
    symbol_table[symbol_count].scope = 0; // Global scope for now
    symbol_table[symbol_count].line_no = line_no;
    symbol_count++;
}

void print_symbol_table() {
    printf("\nSymbol Table:\n");
    printf("-------------------------------------------------\n");
    printf("| %-20s | %-10s | %-5s | %-7s |\n", "Name", "Type", "Scope", "Line No");
    printf("-------------------------------------------------\n");
    
    for (int i = 0; i < symbol_count; i++) {
        printf("| %-20s | %-10s | %-5d | %-7d |\n", 
               symbol_table[i].name, 
               symbol_table[i].type, 
               symbol_table[i].scope, 
               symbol_table[i].line_no);
    }
    
    printf("-------------------------------------------------\n");
    printf("Total symbols: %d\n", symbol_count);
}

int is_keyword(const char *str) {
    for (int i = 0; i < num_keywords; i++) {
        if (strcmp(str, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

void lexical_error(int line_no, const char *msg) {
    fprintf(stderr, "Lexical error at line %d: %s\n", line_no, msg);
}
```
