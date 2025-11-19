"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Write a C program that identifies keywords, operators, separators, and delimiters in a given code snippet using the logic described in the TOKEN SEP example from the CD Lab Code Snippets EX 1 section.
Generated: DETERMINISTIC_4fd1b953d16512fb
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
#include <ctype.h>
#include <string.h>

// Token types
typedef enum {
    KEYWORD,
    OPERATOR,
    SEPARATOR,
    DELIMITER,
    IDENTIFIER,
    UNKNOWN
} token_type;

// Structure to represent a token
typedef struct {
    char* token;
    token_type type;
} token;

// Function to check if a string is a keyword
int is_keyword(char* str) {
    // List of C keywords
    char* keywords[] = {"auto", "break", "case", "char", "const", "continue", 
                        "default", "do", "double", "else", "enum", "extern", 
                        "float", "for", "goto", "if", "int", "long", "register", 
                        "return", "short", "signed", "sizeof", "static", "struct", 
                        "switch", "typedef", "union", "unsigned", "void", "volatile", 
                        "while"};
    int i;
    for (i = 0; i < 32; i++) {
        if (strcmp(str, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

// Function to get token type
token_type get_token_type(char* token) {
    // Check for keywords
    if (is_keyword(token)) {
        return KEYWORD;
    }

    // Check for operators
    char* operators[] = {"+", "-", "*", "/", "%", "=", "==", "!=", "<", ">", 
                         "<=", ">=", "&&", "||", "!", "~", "&", "|", "^", "<<", 
                         ">>", "++", "--", "->", "."};
    int i;
    for (i = 0; i < 25; i++) {
        if (strcmp(token, operators[i]) == 0) {
            return OPERATOR;
        }
    }

    // Check for separators
    char* separators[] = {"(", ")", "{", "}", "[", "]"};
    for (i = 0; i < 5; i++) {
        if (strcmp(token, separators[i]) == 0) {
            return SEPARATOR;
        }
    }

    // Check for delimiters
    char* delimiters[] = {",", ";", ":"};
    for (i = 0; i < 3; i++) {
        if (strcmp(token, delimiters[i]) == 0) {
            return DELIMITER;
        }
    }

    // If none of the above, it's an identifier
    if (isalpha(token[0]) || token[0] == '_') {
        int i;
        for (i = 0; i < strlen(token); i++) {
            if (!isalnum(token[i]) && token[i] != '_') {
                return UNKNOWN;
            }
        }
        return IDENTIFIER;
    }

    return UNKNOWN;
}

// Function to tokenize code
void tokenize_code(char* code) {
    char token[1024];
    int token_index = 0;

    int i;
    for (i = 0; i < strlen(code); i++) {
        // Skip whitespace
        if (isspace(code[i])) {
            if (token_index > 0) {
                token[token_index] = '\0';
                token_type type = get_token_type(token);
                printf("Token: %s, Type: ", token);
                switch (type) {
                    case KEYWORD:
                        printf("Keyword\n");
                        break;
                    case OPERATOR:
                        printf("Operator\n");
                        break;
                    case SEPARATOR:
                        printf("Separator\n");
                        break;
                    case DELIMITER:
                        printf("Delimiter\n");
                        break;
                    case IDENTIFIER:
                        printf("Identifier\n");
                        break;
                    default:
                        printf("Unknown\n");
                }
                token_index = 0;
            }
            continue;
        }

        // Check for multi-character operators
        if (code[i] == '/' && i + 1 < strlen(code) && code[i + 1] == '/') {
            if (token_index > 0) {
                token[token_index] = '\0';
                token_type type = get_token_type(token);
                printf("Token: %s, Type: ", token);
                switch (type) {
                    case KEYWORD:
                        printf("Keyword\n");
                        break;
                    case OPERATOR:
                        printf("Operator\n");
                        break;
                    case SEPARATOR:
                        printf("Separator\n");
                        break;
                    case DELIMITER:
                        printf("Delimiter\n");
                        break;
                    case IDENTIFIER:
                        printf("Identifier\n");
                        break;
                    default:
                        printf("Unknown\n");
                }
                token_index = 0;
            }
            // Skip comment
            while (i < strlen(code) && code[i] != '\n') {
                i++;
            }
            continue;
        }

        if (token_index < 1023) {
            token[token_index++] = code[i];
        }
    }

    // Handle last token
    if (token_index > 0) {
        token[token_index] = '\0';
        token_type type = get_token_type(token);
        printf("Token: %s, Type: ", token);
        switch (type) {
            case KEYWORD:
                printf("Keyword\n");
                break;
            case OPERATOR:
                printf("Operator\n");
                break;
            case SEPARATOR:
                printf("Separator\n");
                break;
            case DELIMITER:
                printf("Delimiter\n");
                break;
            case IDENTIFIER:
                printf("Identifier\n");
                break;
            default:
                printf("Unknown\n");
        }
    }
}

int main() {
    char code[] = "int main() { int x = 5; // This is a comment\n"
                  "if (x > 10) {\n"
                  "   printf(\"Hello World\");\n"
                  "}\n"
                  "return 0;\n"
                  "}";
    tokenize_code(code);
    return 0;
}
```
