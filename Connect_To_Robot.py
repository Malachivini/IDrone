import serial
import time

ser = serial.Serial(port='COM4', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS, timeout=0)

print("Connected to: " + ser.portstr)

# This will store the line
seq = []
count = 1

# Get the current timestamp
current_time = time.strftime("%Y%m%d-%H%M%S")

# Create a new text file with the timestamp as the name
file_name = current_time + ".txt"
file = open(file_name, "w")

while True:
    for c in ser.read():
        seq.append(chr(c))  # Convert from ASCII
        joined_seq = ''.join(str(v) for v in seq)  # Make a string from the array

        if chr(c) == '\n':
            line = joined_seq + "\n"
            print(line)
            file.write(line)
            seq = []
            count += 1
            break

ser.close()
file.close()
