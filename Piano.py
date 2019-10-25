import winsound
import msvcrt

piano_notes = {'c': 262, 'd': 294, 'e': 330, 'f': 350, 'g': 392, 'a': 440, 'b': 494}
yes = True
while yes:
    u_keys = msvcrt.getwche()
    if u_keys == 'q':
        yes = False
    else:
        winsound.Beep(piano_notes.get(u_keys), 700)
