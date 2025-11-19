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

// Enum for token types
typedef enum {
    TOKEN_EOF,
    TOKEN_IDENTIFIER,
    TOKEN_KEYWORD,
    TOKEN_OPERATOR,
    TOKEN_INTEGER,
    TOKEN_ERROR
} token_type;

// Enum for data types
typedef enum {
    DATA_TYPE_INT,
    DATA_TYPE_FLOAT,
    DATA_TYPE_CHAR,
    DATA_TYPE_UNKNOWN
} data_type;

// Structure for symbol table entries
typedef struct symbol_table_entry {
    char* name;
    data_type type;
    struct symbol_table_entry* next;
} symbol_table_entry;

// Structure for tokens
typedef struct token {
    token_type type;
    char* value;
    data_type data_type;
} token;

// Lexical analyzer structure
typedef struct lexical_analyzer {
    char* input;
    int position;
    symbol_table_entry* symbol_table;
} lexical_analyzer;

// Function to create a new lexical analyzer
lexical_analyzer* create_lexical_analyzer(char* input) {
    lexical_analyzer* analyzer = malloc(sizeof(lexical_analyzer));
    analyzer->input = input;
    analyzer->position = 0;
    analyzer->symbol_table = NULL;
    return analyzer;
}

// Function to create a new symbol table entry
symbol_table_entry* create_symbol_table_entry(char* name, data_type type) {
    symbol_table_entry* entry = malloc(sizeof(symbol_table_entry));
    entry->name = strdup(name);
    entry->type = type;
    entry->next = NULL;
    return entry;
}

// Function to add an entry to the symbol table
void add_symbol(lexical_analyzer* analyzer, char* name, data_type type) {
    symbol_table_entry* entry = create_symbol_table_entry(name, type);
    entry->next = analyzer->symbol_table;
    analyzer->symbol_table = entry;
}

// Function to get the data type of a symbol
data_type get_symbol_type(lexical_analyzer* analyzer, char* name) {
    symbol_table_entry* entry = analyzer->symbol_table;
    while (entry != NULL) {
        if (strcmp(entry->name, name) == 0) {
            return entry->type;
        }
        entry = entry->next;
    }
    return DATA_TYPE_UNKNOWN;
}

// Function to tokenize the input
token* tokenize(lexical_analyzer* analyzer) {
    // Skip whitespace
    while (analyzer->position < strlen(analyzer->input) && isspace(analyzer->input[analyzer->position])) {
        analyzer->position++;
    }

    // Check for end of input
    if (analyzer->position >= strlen(analyzer->input)) {
        token* token = malloc(sizeof(token));
        token->type = TOKEN_EOF;
        token->value = NULL;
        token->data_type = DATA_TYPE_UNKNOWN;
        return token;
    }

    // Check for identifier
    if (isalpha(analyzer->input[analyzer->position])) {
        int start = analyzer->position;
        while (analyzer->position < strlen(analyzer->input) && (isalnum(analyzer->input[analyzer->position]) || analyzer->input[analyzer->position] == '_')) {
            analyzer->position++;
        }
        char* value = strndup(analyzer->input + start, analyzer->position - start);
        token* token = malloc(sizeof(token));
        token->type = TOKEN_IDENTIFIER;
        token->value = value;
        token->data_type = get_symbol_type(analyzer, value);
        return token;
    }

    // Check for integer
    if (isdigit(analyzer->input[analyzer->position])) {
        int start = analyzer->position;
        while (analyzer->position < strlen(analyzer->input) && isdigit(analyzer->input[analyzer->position])) {
            analyzer->position++;
        }
        char* value = strndup(analyzer->input + start, analyzer->position - start);
        token* token = malloc(sizeof(token));
        token->type = TOKEN_INTEGER;
        token->value = value;
        token->data_type = DATA_TYPE_INT;
        return token;
    }

    // Check for operator
    if (analyzer->input[analyzer->position] == '+' || analyzer->input[analyzer->position] == '-' ||
        analyzer->input[analyzer->position] == '*' || analyzer->input[analyzer->position] == '/' ||
        analyzer->input[analyzer->position] == '=' || analyzer->input[analyzer->position] == ';') {
        char* value = malloc(2);
        value[0] = analyzer->input[analyzer->position];
        value[1] = '\0';
        analyzer->position++;
        token* token = malloc(sizeof(token));
        token->type = TOKEN_OPERATOR;
        token->value = value;
        token->data_type = DATA_TYPE_UNKNOWN;
        return token;
    }

    // Error handling
    token* token = malloc(sizeof(token));
    token->type = TOKEN_ERROR;
    token->value = NULL;
    token->data_type = DATA_TYPE_UNKNOWN;
    return token;
}

// Function to free the lexical analyzer
void free_lexical_analyzer(lexical_analyzer* analyzer) {
    symbol_table_entry* entry = analyzer->symbol_table;
    while (entry != NULL) {
        symbol_table_entry* next = entry->next;
        free(entry->name);
        free(entry);
        entry = next;
    }
    free(analyzer);
}

int main() {
    char* input = "int x; x = 5; y = x + 3;";
    lexical_analyzer* analyzer = create_lexical_analyzer(input);
    add_symbol(analyzer, "int", DATA_TYPE_INT);
    add_symbol(analyzer, "float", DATA_TYPE_FLOAT);
    add_symbol(analyzer, "char", DATA_TYPE_CHAR);

    token* token;
    while ((token = tokenize(analyzer))->type != TOKEN_EOF) {
        switch (token->type) {
            case TOKEN_IDENTIFIER:
                printf("Identifier: %s, Type: %d\n", token->value, token->data_type);
                break;
            case TOKEN_INTEGER:
                printf("Integer: %s, Type: %d\n", token->value, token->data_type);
                break;
            case TOKEN_OPERATOR:
                printf("Operator: %s\n", token->value);
                break;
            case TOKEN_ERROR:
                printf("Error\n");
                break;
        }
        free(token->value);
        free(token);
    }

    free(token);
    free_lexical_analyzer(analyzer);
    return 0;
}
```
