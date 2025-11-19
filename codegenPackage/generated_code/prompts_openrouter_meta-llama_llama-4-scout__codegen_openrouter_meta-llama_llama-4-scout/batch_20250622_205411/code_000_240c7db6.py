"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Write a code for a simple cracktro intro for the Atari ST demoscene, similar to the one released by Overlanders for the "Fantasy Cracktro Challenge".
Generated: DETERMINISTIC_240c7db6e2a35b4c
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```assembly
; Overlanders Fantasy Cracktro Challenge-inspired intro for Atari ST

; Screen dimensions
SCREEN_WIDTH equ 320
SCREEN_HEIGHT equ 200

; Color constants
WHITE equ $FFFFFF
BLACK equ $000000

; STOS constants
STOS_SCREEN equ $FF8000
STOS_PALETTE equ $FF8240

; Initialize screen and palette
    org $6000

start:
    move.l #STOS_SCREEN, a0
    move.w #SCREEN_WIDTH, d0
    move.w #SCREEN_HEIGHT, d1
    jsr $E0F0       ; STOS clear screen

    ; Set up palette
    move.l #STOS_PALETTE, a0
    move.l #WHITE, (a0)
    move.l #BLACK, 4(a0)

; Main loop
main_loop:
    ; Draw something (e.g., a bouncing ball)
    move.l #STOS_SCREEN, a0
    move.w #100, d0     ; X coordinate
    move.w #100, d1     ; Y coordinate
    move.w #10, d2      ; radius
    move.l #WHITE, d3   ; color
    jsr $E120       ; STOS plot circle

    ; Animate (e.g., move the ball)
    move.w #10, d0
animation_loop:
    ; Delay
    move.w #10000, d1
delay_loop:
    dbne d1, delay_loop

    ; Update ball position
    add.w #2, d0
    cmp.w #SCREEN_WIDTH - 10, d0
    blt animation_loop
    move.w #0, d0

    bra main_loop

; STOS jump table
    dc.l $E0F0       ; clear screen
    dc.l $E120       ; plot circle
    dc.l $E140       ; plot line
; End of STOS jump table

; IRQ handler (empty)
irq_handler:
    rte

; Exception vectors
    org $70
    dc.l start       ; Reset
    dc.l irq_handler ; IRQ
    dc.l irq_handler ; Emulation trap
    dc.l irq_handler ; Bus error
    dc.l irq_handler ; Address error
    dc.l irq_handler ; Illegal instruction
    dc.l irq_handler ; Divide by zero
    dc.l irq_handler ; NMI
    dc.l irq_handler ; Uninitialized interrupt
    dc.l irq_handler ; Spurious interrupt
    dc.l irq_handler ; TRAP #00
    dc.l irq_handler ; TRAP #01
    dc.l irq_handler ; TRAP #02
    dc.l irq_handler ; TRAP #03
    dc.l irq_handler ; TRAP #04
    dc.l irq_handler ; TRAP #05
    dc.l irq_handler ; TRAP #06
    dc.l irq_handler ; TRAP #07
    dc.l irq_handler ; TRAP #08
    dc.l irq_handler ; TRAP #09
    dc.l irq_handler ; TRAP #10
    dc.l irq_handler ; TRAP #11
    dc.l irq_handler ; TRAP #12
    dc.l irq_handler ; TRAP #13
    dc.l irq_handler ; TRAP #14
    dc.l irq_handler ; TRAP #15

; End of code
    end
```
