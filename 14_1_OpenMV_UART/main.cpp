#include "mbed.h"

Thread thread1;
Thread thread2;

Serial pc(USBTX, USBRX);    // tx, rx
Serial uart(D1, D0);      // tx, rx
DigitalIn button(SW2);

void receive_thread()
{
    while (1) {
        if (uart.readable()) {
            char recv = uart.getc();
            pc.putc(recv);
            pc.printf("\r\n");
        }
    }
}

void send_thread()
{
    while (1) {
        if (button == 0) {
            char s[21];
            sprintf(s, "image_classification");
            uart.puts(s);
            pc.printf("send\r\n");
            wait(0.5);
        }
    }
}

int main()
{
    uart.baud(9600);
    /*while (1) {
        send_thread();
        receive_thread();
    }*/
    thread1.start(send_thread);
    thread2.start(receive_thread);
}