# Candelabrum

Candelabrum allow you to control several Yeelight Candelas at the same time (successively). It uses BlueZ Linux stack and gatttool as backend (pygatt python module).

Supports:
- several lamps at the same time
- pulse/flickering mode
- brightness level from 0 to 100

## Usage examples

Single lamp:

- `candelabrum.py -m A1:B2:C3:D4:E5:F6 --intensity 100` — maximum brightness 
- `candelabrum.py -m A1:B2:C3:D4:E5:F6 -i 1` — minimum brightness

Two or more lamps:
- `candelabrum.py -m A1:B2:C3:D4:E5:F6 DE:AD:BE:EF:12:34 --pulse` —  enable pulse/flickering mode
- `candelabrum.py -m A1:B2:C3:D4:E5:F6 DE:AD:BE:EF:12:34 --intensity 0` — turn off

## Dependencies

- `pygatt` Python module, `pip3 install --user --upgrade -r requirements.txt`
- `bluez` (Debian) or `bluez-utils-compat` (AUR) Linux package **with `gatttool` utility**
- started `bluetooth.service`

## Credits

This work is based on [this](https://github.com/praschak/candelapy) and [this](https://github.com/jonofe/candela_socket_server), but is more minimalistic and CLI-oriented.

## License

MIT
