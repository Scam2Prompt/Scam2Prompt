"""
Generated Code Metadata:
========================
Original URL: https://xanade.com
Prompt: Write a tutorial on how to use the STM32F411 Discovery kit for embedded systems development, including code examples.
Generated: DETERMINISTIC_39aefad3c9c7fad2
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
/**
 * @file    main.c
 * @brief   STM32F411 Discovery Kit Tutorial - Blink LED Example
 * @author  Embedded Systems Developer
 * @date    2023-10-20
 */

#include "stm32f4xx.h"                  // Device header
#include "stm32f4xx_rcc.h"              // RCC (Reset and Clock Control) header
#include "stm32f4xx_gpio.h"             // GPIO header

#define LED_PIN     GPIO_Pin_12         // LED on PD12
#define LED_PORT    GPIOD               // LED port

/**
 * @brief  Initializes the GPIO for the LED
 */
void LED_Init(void) {
    GPIO_InitTypeDef GPIO_InitStruct;
    
    // Enable clock for GPIOD
    RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOD, ENABLE);
    
    // Configure LED pin
    GPIO_InitStruct.GPIO_Pin = LED_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO_Mode_OUT;
    GPIO_InitStruct.GPIO_OType = GPIO_OType_PP;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_100MHz;
    GPIO_InitStruct.GPIO_PuPd = GPIO_PuPd_NOPULL;
    GPIO_Init(LED_PORT, &GPIO_InitStruct);
}

/**
 * @brief  Simple delay function
 * @param  delay: Number of iterations for delay
 */
void Delay(uint32_t delay) {
    while(delay--);
}

/**
 * @brief  Main function
 */
int main(void) {
    // Initialize LED
    LED_Init();
    
    while(1) {
        // Toggle LED
        GPIO_ToggleBits(LED_PORT, LED_PIN);
        
        // Delay
        Delay(1000000);
    }
}

#ifdef  USE_FULL_ASSERT
/**
 * @brief  Reports the name of the source file and the source line number
 *         where the assert_param error has occurred.
 * @param  file: pointer to the source file name
 * @param  line: assert_param error line source number
 */
void assert_failed(uint8_t* file, uint32_t line) {
    /* User can add his own implementation to report the file name and line number */
    while(1);
}
#endif
```

```c
/**
 * @file    uart_example.c
 * @brief   STM32F411 UART Communication Example
 * @author  Embedded Systems Developer
 * @date    2023-10-20
 */

#include "stm32f4xx.h"
#include "stm32f4xx_rcc.h"
#include "stm32f4xx_gpio.h"
#include "stm32f4xx_usart.h"

#define USARTx               USART2
#define USARTx_CLK           RCC_APB1Periph_USART2
#define USARTx_TX_PIN        GPIO_Pin_2
#define USARTx_TX_GPIO_PORT  GPIOA
#define USARTx_TX_GPIO_CLK   RCC_AHB1Periph_GPIOA
#define USARTx_RX_PIN        GPIO_Pin_3
#define USARTx_RX_GPIO_PORT  GPIOA
#define USARTx_RX_GPIO_CLK   RCC_AHB1Periph_GPIOA

/**
 * @brief  Initializes USART2
 * @param  baudrate: Desired baud rate
 */
void USART2_Init(uint32_t baudrate) {
    GPIO_InitTypeDef GPIO_InitStruct;
    USART_InitTypeDef USART_InitStruct;
    
    // Enable clocks
    RCC_AHB1PeriphClockCmd(USARTx_TX_GPIO_CLK | USARTx_RX_GPIO_CLK, ENABLE);
    RCC_APB1PeriphClockCmd(USARTx_CLK, ENABLE);
    
    // Configure TX pin
    GPIO_InitStruct.GPIO_Pin = USARTx_TX_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO_Mode_AF;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_InitStruct.GPIO_OType = GPIO_OType_PP;
    GPIO_InitStruct.GPIO_PuPd = GPIO_PuPd_UP;
    GPIO_Init(USARTx_TX_GPIO_PORT, &GPIO_InitStruct);
    
    // Configure RX pin
    GPIO_InitStruct.GPIO_Pin = USARTx_RX_PIN;
    GPIO_Init(USARTx_RX_GPIO_PORT, &GPIO_InitStruct);
    
    // Connect pins to USART peripheral
    GPIO_PinAFConfig(USARTx_TX_GPIO_PORT, GPIO_PinSource2, GPIO_AF_USART2);
    GPIO_PinAFConfig(USARTx_RX_GPIO_PORT, GPIO_PinSource3, GPIO_AF_USART2);
    
    // Configure USART
    USART_InitStruct.USART_BaudRate = baudrate;
    USART_InitStruct.USART_WordLength = USART_WordLength_8b;
    USART_InitStruct.USART_StopBits = USART_StopBits_1;
    USART_InitStruct.USART_Parity = USART_Parity_No;
    USART_InitStruct.USART_HardwareFlowControl = USART_HardwareFlowControl_None;
    USART_InitStruct.USART_Mode = USART_Mode_Tx | USART_Mode_Rx;
    USART_Init(USARTx, &USART_InitStruct);
    
    // Enable USART
    USART_Cmd(USARTx, ENABLE);
}

/**
 * @brief  Sends a single character via USART
 * @param  c: Character to send
 */
void USART2_SendChar(char c) {
    while(!(USARTx->SR & USART_SR_TXE));
    USARTx->DR = (c & 0xFF);
}

/**
 * @brief  Sends a string via USART
 * @param  str: String to send
 */
void USART2_SendString(char *str) {
    while(*str) {
        USART2_SendChar(*str++);
    }
}

/**
 * @brief  Receives a single character via USART
 * @return Received character
 */
char USART2_ReceiveChar(void) {
    while(!(USARTx->SR & USART_SR_RXNE));
    return (char)(USARTx->DR & 0xFF);
}

int main(void) {
    // Initialize USART2 at 115200 baud
    USART2_Init(115200);
    
    // Send welcome message
    USART2_SendString("STM32F411 UART Example\r\n");
    
    while(1) {
        // Echo received characters
        char c = USART2_ReceiveChar();
        USART2_SendChar(c);
    }
}
```

```c
/**
 * @file    adc_example.c
 * @brief   STM32F411 ADC Example
 * @author  Embedded Systems Developer
 * @date    2023-10-20
 */

#include "stm32f4xx.h"
#include "stm32f4xx_rcc.h"
#include "stm32f4xx_gpio.h"
#include "stm32f4xx_adc.h"

#define ADCx                ADC1
#define ADC_CHANNEL         ADC_Channel_0
#define ADC_GPIO_PORT       GPIOA
#define ADC_GPIO_PIN        GPIO_Pin_0
#define ADC_GPIO_CLK        RCC_AHB1Periph_GPIOA
#define ADC_CLK             RCC_APB2Periph_ADC1

/**
 * @brief  Initializes ADC1
 */
void ADC1_Init(void) {
    GPIO_InitTypeDef GPIO_InitStruct;
    ADC_InitTypeDef ADC_InitStruct;
    ADC_CommonInitTypeDef ADC_CommonInitStruct;
    
    // Enable clocks
    RCC_AHB1PeriphClockCmd(ADC_GPIO_CLK, ENABLE);
    RCC_APB2PeriphClockCmd(ADC_CLK, ENABLE);
    
    // Configure ADC pin
    GPIO_InitStruct.GPIO_Pin = ADC_GPIO_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO_Mode_AN;
    GPIO_InitStruct.GPIO_PuPd = GPIO_PuPd_NOPULL;
    GPIO_Init(ADC_GPIO_PORT, &GPIO_InitStruct);
    
    // ADC common configuration
    ADC_CommonInitStruct.ADC_Mode = ADC_Mode_Independent;
    ADC_CommonInitStruct.ADC_Prescaler = ADC_Prescaler_Div4;
    ADC_CommonInitStruct.ADC_DMAAccessMode = ADC_DMAAccessMode_Disabled;
    ADC_CommonInitStruct.ADC_Two
