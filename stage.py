
ACTIVITI_METER_MAC = "ee:f9:5c:6b:d9:73"

UUID_battery = "0000-180F-0000-1000-8000-00805F9B34FB"

Handle_Blevel = "0x1E"


from bluepy.btle import Scanner, DefaultDelegate, Peripheral, UUID
import binascii

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)


def scan():
    scanner = Scanner()
    devices = scanner.scan(10)


    for dev in devices:
        print ("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
            print ("  %s = %s" % (desc, value))



#ACTIVITI_MET = Peripheral(ACTIVITI_METER_MAC, "public")

##descriptors=ACTIVITI_MET.getDescriptors() #Bug if no limt is specified the function wil hang 
##				      # (go in a endless loop and not return anything)
##print("UUID                                  Handle UUID by name")
##for descriptor in descriptors:
##    print ( " "+ str(descriptor.uuid) + "  0x" + format(descriptor.handle,"02X") +"   "+ str(descriptor) )
# binascii.b2a_hex(val).decode('utf-8')

def battery_level():
    print("\nBATTERY LEVEL")
    dev_name_uuid = UUID(0x2a19)
    bat_lev = ACTIVITI_MET.getCharacteristics(uuid=dev_name_uuid)[0]
    if (bat_lev.supportsRead()):
        val = binascii.b2a_hex(bat_lev.read())
        val = str(val)[2:-1]
        val = int(val, 16)
        print(val)

def hextodec(hexa):
    hexa = str(hexa)[2:-1]
    hexa = int(hexa, 16)
    return(hexa)

import struct
def test(cara):
    
    for  a in range(255):
        cara.write(struct.pack('<B',a))

#cara1 = ACTIVITI_MET.getCharacteristics(uuid="351cf040-457b-11e5-9a37-0002a5d5c51b")
##    Characteristic <351cf040-457b-11e5-9a37-0002a5d5c51b>
##Characteristic <351cf041-457b-11e5-9a37-0002a5d5c51b>
##Characteristic <351cf030-457b-11e5-9a37-0002a5d5c51b>
##Characteristic <351cf021-457b-11e5-9a37-0002a5d5c51b>


#ACTIVITI_MET.writeCharacteristic(34,bytes,True)

    

#r = int(str(binascii.b2a_hex(gg.read()))[2:-1],16) gg = ACTIVITI_MET.getCharacteristics()[-2] hexTodec(r)
#ACTIVITI_MET.getCharacteristics(uuid=UUID(0x2904)[0].read() f021


#42004c000551...3030 serial number
