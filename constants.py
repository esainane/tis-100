
# INSTRUCTIONS
MOV = 0x0000000000
HAS = 0x0010000000
BSL = 0x0100000000 # UNSURE - BIT SHIFT LEFT?
CMP = 0x0110000000 # COMPARE

ADD = 0x1000000000
XOR = 0x1010000000
JEZ = 0x1100000000
JGZ = 0x1110000000

# ADDRESSABLE SPACE

NIL = 0x0000
ACC = 0x0001
BAK = 0x0010
IMM = 0x0011 #immediate = next byte

LEFT = 0x0100
RIGHT = 0x0101
UP  = 0x0110
DOW = 0x0111

ANY = 0x1000
LAST = 0x1001
ALL = 0x1010
IO  = 0x1011 # UNSURE - ADDRESSABLE MEMORY IS SMALLER THAN SCREEN [160x60 char]

PC  = 0x1100 #program counter
PM  = 0x1101 #program memory
MB  = 0x1110 #memory block
MA  = 0x1111 #memory address

# VALUES

CORES_WIDTH = 2
CORES_HEIGHT = 2

# A byte is 11 bits in this architecture
class Byte():

    def __init__(self, value):
        self.value = value

class Bus():
    value = None
    send = False
    receive = False
