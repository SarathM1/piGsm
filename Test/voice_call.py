"""
Voice call using AT commands
Calls the at_cmds class definitions - version v3
"""
## The packges below must be installed in advance
## sudo apt-get install python-setuptools
## easy_install pyserial

import serial
import time
import sys
from at_cmds import ATcommands
from at_cmds import VoiceCall


if len(sys.argv) > 1:
	phoneNumber = sys.argv[1]
	callPhone = VoiceCall(phoneNumber)
else:
	callPhone = VoiceCall()

usb_serial = ATcommands()

usb_serial.connectPhone()
callPhone.dialNumber()
usb_serial.disconnectPhone()

#Main function that calls other functions - Makes script reusable
def main():
	pass

if __name__ == "__main__":
	main()
