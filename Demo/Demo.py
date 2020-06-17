import pyb
import sensor, image, time, math

uart = pyb.UART(3,9600,timeout_char=1000)
uart.init(9600,bits=8,parity = None, stop=1, timeout_char=1000)

#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time = 2000)
#sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
#sensor.set_auto_whitebal(False)  # must turn this off to prevent image washout...
#clock = time.clock()
tmp = ""

#while(True):
    #a = uart.readline()
    #if a is not None:
        #tmp += a.decode()
        #print(a.decode())

    #if tmp == "QRcode_decoding":
        #clock.tick()
        #img = sensor.snapshot()
        #img.lens_corr(1.8) # strength of 1.8 is good for the 2.8mm lens.

        #matrices = img.find_datamatrices()
        #for matrix in matrices:
            #img.draw_rectangle(matrix.rect(), color = (255, 0, 0))
            #print_args = (matrix.rows(), matrix.columns(), matrix.payload(), (180 * matrix.rotation()) / math.pi, clock.fps())
            #uart.write(("Matrix [%d:%d], Payload \"%s\", rotation %f (degrees), FPS %f\r\n" % print_args).encode())
        ## if not matrices:
        ##    uart.write(("FPS %f\r\n" % clock.fps()).encode())

#import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must turn this off to prevent image washout...
clock = time.clock()

while(True):
    a = uart.readline()
    if a is not None:
        tmp += a.decode()
        print(a.decode())

    if tmp == "QRcode_decoding":
        clock.tick()
        img = sensor.snapshot()
        img.lens_corr(1.8) # strength of 1.8 is good for the 2.8mm lens.
        for code in img.find_qrcodes():
            img.draw_rectangle(code.rect(), color = (255, 0, 0))
            uart.write(code[4].encode())
            uart.write("\n")
        # print(clock.fps())
