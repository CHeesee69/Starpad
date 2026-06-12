import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DirectPins

keyboard = KMKKeyboard()

# Direct pin switches
keyboard.matrix = DirectPins(
    pins=[
        board.D8,   # UP
        board.D9,   # LEFT
        board.D10,  # DOWN
        board.D11,   # RIGHT
    ]
)
# Encoder setup
encoder = EncoderHandler()
keyboard.modules.append(encoder)

# Encoder pins: A = D4, B = D3, Button = D2
encoder.pins = ((board.D4, board.D3, board.D2),)

# Custom behavior: brightness when button held
def encoder_handler(index, clockwise):
    button_pressed = not keyboard.io.pins[board.D2].value

    if button_pressed:
        # Brightness mode
        return KC.BRIGHTNESS_UP if clockwise else KC.BRIGHTNESS_DOWN
    else:
        # Normal volume mode
        return KC.VOLU if clockwise else KC.VOLD

encoder.map = [encoder_handler]

# Keymap
keyboard.keymap = [
    [
        KC.LGUI,            # UP
        KC.LCTRL(KC.C),    # LEFT
        KC.F11,           # DOWN
        KC.LCTRL(KC.V),    # RIGHT
    ]
]

if __name__ == "__main__":
    keyboard.go()
    