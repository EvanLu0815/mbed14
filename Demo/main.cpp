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
            if (recv == '\n')
                pc.printf("\r\n");
        }
    }
}

void send_thread()
{
    while (1) {
        if (button == 0) {
            char s[21];
            sprintf(s, "QRcode_decoding");
            uart.puts(s);
            pc.printf("send\r\n");
            wait(0.5);
        }
    }
}

int main()
{
    uart.baud(9600);
    thread1.start(send_thread);
    thread2.start(receive_thread);
}