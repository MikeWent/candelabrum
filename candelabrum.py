#!/usr/bin/env python3

import argparse

import pygatt

# get arguments from command line
p = argparse.ArgumentParser()
p.add_argument("--mac", "-m", type=str, help="Bluetooth MAC address of Yeelight Candela", action="extend", nargs="+", required=True)
g = p.add_mutually_exclusive_group()
g.add_argument("--intensity", "-i", type=int, help="Light intensity (0-100)", required=False)
g.add_argument("--pulse", "-p", action="store_true", required=False)
args = p.parse_args()

for mac in args.mac:
    # init bluetooth adapter
    adapter = pygatt.GATTToolBackend()
    adapter.start()
    print(f"connecting to {mac}")
    try:
        device = adapter.connect(mac)
    except Exception as e:
        print(f"unable to connect: {e}")
        continue
    
    try:
        if args.intensity != None:
            if args.intensity > 0 and args.intensity <= 100:
                print(f"set intensity: {args.intensity}")
                # turn candela on
                device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x01]))
                # set light intensity
                device.char_write_handle(0x001f, bytearray([0x43, 0x42, args.intensity]))
            else:
                print("lamp off")
                # set zero light intensity
                device.char_write_handle(0x001f, bytearray([0x43, 0x42, 0]))
                # turn candela off
                device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x02]))

        if args.pulse:
            print("pulse on")
            # turn candela on
            device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x01]))
            # # set 1/100 light intensity
            # device.char_write_handle(0x001f, bytearray([0x43, 0x42, 1]))
            # enable pulse mode
            device.char_write_handle(0x001f, bytearray([0x43, 0x67, 0x02]))
    finally:
        adapter.stop()
