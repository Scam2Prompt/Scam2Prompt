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

```yacc
%{
#include <stdio.h>
#include <stdlib.h>

// Function prototypes
int yylex(void);
void yyerror(const char *s);
%}

%token NUMBER
%left '+' '-'
%left '*' '/'

// Grammar rules
%%
expression:
    expression '+' expression { $$ = $1 + $3; }
    | expression '-' expression { $$ = $1 - $3; }
    | expression '*' expression { $$ = $1 * $3; }
    | expression '/' expression {
        if ($3 == 0) {
            yyerror("Division by zero");
            YYABORT;
        }
        $$ = $1 / $3;
    }
    | '(' expression ')' { $$ = $2; }
    | NUMBER { $$ = $1; }
    ;

%%

// Error handling function
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

// Main function
int main(void) {
    printf("Enter an arithmetic expression: ");
    if (yyparse() == 0) {
        printf("Expression evaluated successfully.\n");
    } else {
        fprintf(stderr, "Failed to evaluate expression.\n");
    }
    return 0;
}
```

```lex
%{
#include "y.tab.h"
%}

%%

// Match numbers
[0-9]+  { yylval = atoi(yytext); return NUMBER; }

// Match operators and parentheses
"+"    { return '+'; }
"-"    { return '-'; }
"*"    { return '*'; }
"/"    { return '/'; }
"("    { return '('; }
")"    { return ')'; }

// Ignore whitespace
[ \t\n]  { /* ignore whitespace */ }

// Catch all for invalid characters
.       { yyerror("Invalid character"); }

%%

// Main function for the lexer
int main(void) {
    yylex();
    return 0;
}
```

### Instructions to Compile and Run
1. Save the YACC code in a file named `yacc.y`.
2. Save the LEX code in a file named `lex.l`.
3. Run the following commands in your terminal:
   ```bash
   yacc -d yacc.y
   lex lex.l
   gcc y.tab.c lex.yy.c -o parser -lm
   ```
4. Execute the parser:
   ```bash
   ./parser
   ```
