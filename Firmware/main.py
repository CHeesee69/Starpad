import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DirectPins

keyboard = KMKKeyboard()

keyboard.matrix = DirectPins(
    pins=[
        board.D8,   # UP
        board.D9,   # LEFT
        board.D10,  # DOWN
        board.D11,  # RIGHT
    ]
)

encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = ((board.D4, board.D3, board.D2),)
encoder.map = [
    ((KC.VOLD, KC.VOLU), KC.MUTE)
]

keyboard.keymap = [
    [
        KC.LGUI,           # UP
        KC.LCTRL(KC.C),    # LEFT
        KC.F11,            # DOWN
        KC.LCTRL(KC.V),    # RIGHT
    ]
]

if __name__ == "__main__":
    keyboard.go()