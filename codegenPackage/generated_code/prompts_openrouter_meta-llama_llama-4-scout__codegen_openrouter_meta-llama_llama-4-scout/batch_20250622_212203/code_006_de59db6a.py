"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Create a parser using YACC (yacc.y) that can parse a given arithmetic expression and compute its value.
Generated: DETERMINISTIC_de59db6a84193ff1
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**yacc.y**
```yacc
%{
#include <stdio.h>
#include <stdlib.h>

// Define the structure for the symbol table entry
typedef struct {
    int value;
} symbol_entry;

// Symbol table
symbol_entry symbol_table[100];
int symbol_table_size = 0;

// Function to add a symbol to the symbol table
void add_symbol(char *name, int value) {
    // Check if the symbol already exists
    for (int i = 0; i < symbol_table_size; i++) {
        if (strcmp(symbol_table[i].name, name) == 0) {
            symbol_table[i].value = value;
            return;
        }
    }
    // Add the symbol to the table
    symbol_table[symbol_table_size].name = strdup(name);
    symbol_table[symbol_table_size].value = value;
    symbol_table_size++;
}

// Function to get the value of a symbol
int get_symbol_value(char *name) {
    for (int i = 0; i < symbol_table_size; i++) {
        if (strcmp(symbol_table[i].name, name) == 0) {
            return symbol_table[i].value;
        }
    }
    // If the symbol is not found, return an error
    yyerror("Undefined symbol");
    exit(1);
}
%}

// Define the tokens
%token NUMBER
%token PLUS MINUS TIMES DIVIDE
%token LPAREN RPAREN
%token ID

// Define the precedence
%left PLUS MINUS
%left TIMES DIVIDE

// Define the grammar
%%

expression:
    NUMBER {
        $$ = $1;
    }
    | ID {
        $$ = get_symbol_value($1);
    }
    | expression PLUS expression {
        $$ = $1 + $3;
    }
    | expression MINUS expression {
        $$ = $1 - $3;
    }
    | expression TIMES expression {
        $$ = $1 * $3;
    }
    | expression DIVIDE expression {
        if ($3 == 0) {
            yyerror("Division by zero");
            exit(1);
        }
        $$ = $1 / $3;
    }
    | LPAREN expression RPAREN {
        $$ = $2;
    }
    ;

%%

// Error handling function
void yyerror(const char *message) {
    fprintf(stderr, "Error: %s\n", message);
}

// Main function
int main() {
    // Initialize the symbol table
    // ...

    // Parse the input
    yyparse();

    return 0;
}
```

**lex.l**
```lex
%{
#include "y.tab.h"
extern int yylval;
%}

%%
[0-9]+ {
    yylval = atoi(yytext);
    return NUMBER;
}

[ \t\n] {
    /* ignore whitespace */
}

"+" {
    return PLUS;
}

"-" {
    return MINUS;
}

"*" {
    return TIMES;
}

"/" {
    return DIVIDE;
}

"(" {
    return LPAREN;
}

")" {
    return RPAREN;
}

[a-zA-Z_][a-zA-Z_0-9]* {
    yylval = strdup(yytext);
    return ID;
}

. {
    printf("Invalid character: %c\n", *yytext);
    exit(1);
}
%%
```

**Makefile**
```makefile
y.tab.c: yacc.y
    yacc -d yacc.y

lex.yy.c: lex.l
    lex lex.l

parser: y.tab.c lex.yy.c
    gcc -o parser y.tab.c lex.yy.c -lfl

clean:
    rm -f y.tab.c lex.yy.c parser
```

To compile and run:
```bash
make
./parser
```
