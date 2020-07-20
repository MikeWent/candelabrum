#!/usr/bin/env python3

import argparse

import pygatt

# get arguments from command line
p = argparse.ArgumentParser()
p.add_argument("--mac", "-m", help="Bluetooth MAC address of Yeelight Candela", type=str, nargs="*", required=True)
g = p.add_mutually_exclusive_group()
g.add_argument("--intensity", "-i", help="Light intensity (0-100)", type=int, required=False)
g.add_argument("--pulse", "-p", help="Enable pulse (flickering) mode", action="store_true", required=False)
args = p.parse_args()

for mac in args.mac:
    # init bluetooth adapter
    print(f"connecting to {mac}")
    try:
        adapter = pygatt.GATTToolBackend()
        adapter.start()
        device = adapter.connect(mac)
    except Exception as e:
        print(f"unable to connect: {e}")
        continue

    if args.intensity != None:
        if args.intensity > 0 and args.intensity <= 100:
            print(f"set intensity: {args.intensity}")
            # turn candela on
            device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x01]), wait_for_response=False)
            # set light intensity
            device.char_write_handle(0x001f, bytearray([0x43, 0x42, args.intensity]), wait_for_response=False)
        else:
            print("lamp off")
            # set zero light intensity
            device.char_write_handle(0x001f, bytearray([0x43, 0x42, 0]), wait_for_response=False)
            # turn candela off
            device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x02]), wait_for_response=False)

    if args.pulse:
        print("pulse on")
        # turn candela off
        device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x02]), wait_for_response=False)
        # turn candela on
        device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x01]), wait_for_response=False)
        # enable pulse mode
        device.char_write_handle(0x001f, bytearray([0x43, 0x67, 0x02]), wait_for_response=False)

    adapter.stop()