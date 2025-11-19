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

```asm
; Simple Atari ST Cracktro
; Inspired by Overlanders' Fantasy Cracktro Challenge
; Assembled with Devpac 2

    OPT O+,OW-

    SECTION TEXT

START:
    clr.l   -(sp)           ; Supervisor mode
    move.w  #$20,-(sp)
    trap    #1
    addq.l  #6,sp
    move.l  d0,SAVE_STACK

    move.w  #4,-(sp)        ; Get resolution
    trap    #14
    addq.l  #2,sp
    move.w  d0,OLD_RES

    move.w  #2,-(sp)        ; Get screen address
    trap    #14
    addq.l  #2,sp
    move.l  d0,OLD_SCREEN

    move.w  #0,-(sp)        ; Set low resolution
    move.l  #-1,-(sp)
    move.l  #-1,-(sp)
    move.w  #5,-(sp)
    trap    #14
    lea     12(sp),sp

    move.b  #0,$ffff8260.w  ; Ensure low res

    ; Set up palette
    move.l  #PALETTE,a0
    move.w  #15,d0
    lea     $ffff8240.w,a1
SET_PAL:
    move.w  (a0)+,(a1)+
    dbf     d0,SET_PAL

    ; Clear screen
    move.l  $44e.w,a0
    move.w  #8000-1,d0
    moveq   #0,d1
CLEAR:
    move.l  d1,(a0)+
    dbf     d0,CLEAR

    ; Display scroller text
    move.l  $44e.w,a0
    add.l   #160*100,a0     ; Position for scroller
    lea     SCROLL_TEXT,a1
    move.w  #40-1,d0        ; Width in words
DRAW_TEXT:
    move.w  (a1)+,(a0)+
    dbf     d0,DRAW_TEXT

MAIN_LOOP:
    ; Simple scroller logic
    lea     SCROLL_BUFFER,a0
    move.l  $44e.w,a1
    add.l   #160*100+152,a1 ; Scroller position
    move.w  #20-1,d0        ; Height
SCROLL_LINE:
    roxl.w  152(a0)         ; Scroll one pixel
    roxl.w  144(a0)
    roxl.w  136(a0)
    roxl.w  128(a0)
    roxl.w  120(a0)
    roxl.w  112(a0)
    roxl.w  104(a0)
    roxl.w  96(a0)
    roxl.w  88(a0)
    roxl.w  80(a0)
    roxl.w  72(a0)
    roxl.w  64(a0)
    roxl.w  56(a0)
    roxl.w  48(a0)
    roxl.w  40(a0)
    roxl.w  32(a0)
    roxl.w  24(a0)
    roxl.w  16(a0)
    roxl.w  8(a0)
    roxl.w  (a0)
    lea     160(a0),a0
    lea     160(a1),a1
    dbf     d0,SCROLL_LINE

    ; Check for space key to exit
    move.b  $fffffc02.w,d0
    cmp.b   #$39,d0         ; Space key
    bne     MAIN_LOOP

EXIT:
    move.w  OLD_RES,-(sp)   ; Restore resolution
    move.l  OLD_SCREEN,-(sp)
    move.l  OLD_SCREEN,-(sp)
    move.w  #5,-(sp)
    trap    #14
    lea     12(sp),sp

    move.l  SAVE_STACK,-(sp) ; User mode
    move.w  #$20,-(sp)
    trap    #1
    addq.l  #6,sp

    clr.l   -(sp)           ; Terminate
    trap    #1

    SECTION DATA

PALETTE:
    dc.w $0000,$0777,$0700,$0070,$0007,$0770,$0707,$0077
    dc.w $0555,$0333,$0F00,$00F0,$000F,$0FF0,$0F0F,$00FF

SCROLL_TEXT:
    dc.b "GREETINGS TO THE ATARI SCENE! THIS IS A SIMPLE CRACKTRO.  ",0

    SECTION BSS

OLD_RES:    ds.w 1
OLD_SCREEN: ds.l 1
SAVE_STACK: ds.l 1
SCROLL_BUFFER: ds.b 160*20

    END
```
