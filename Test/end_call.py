"""
Terminate voice call using AT commands
Calls the at_cmds class definitions - version v4
"""
## The packges below must be installed in advance
## sudo apt-get install python-setuptools
## easy_install pyserial

import serial
import time
import sys
from at_cmds import ATcommands
from at_cmds import VoiceCall

currentCall = VoiceCall()
usb_serial = ATcommands()

usb_serial.connectPhone()
currentCall.endCall()
usb_serial.disconnectPhone()

#Main function that calls other functions - Makes script reusable
def main():
	pass

if __name__ == "__main__":
main() 
