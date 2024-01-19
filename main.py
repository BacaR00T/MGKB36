print("mgkb36_handwired")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.holdtap import HoldTap
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.modules = [HoldTap(), Layers(), TapDance()]

                    #LEFT                                           #RIGHT
keyboard.col_pins = (board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP21, board.GP20,board.GP19,board.GP18,board.GP17) # Cols
keyboard.row_pins = (board.GP5, board.GP4, board.GP3,board.GP2 ) # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
SPCLOW = KC.HT(KC.SPC, LOWER)
ENTRAI = KC.HT(KC.ENT, RAISE)
ESCALT = KC.HT(KC.ESC, KC.LALT)
TABCTRL = KC.HT(KC.TAB, KC.LCTRL)
SUPERSHIFT = KC.HT(KC.LGUI, KC.LSHIFT)
BSPDEL = KC.HT(KC.BSPC, KC.DEL)

# Keymap
keyboard.keymap = [
    #KEYS
    [  
        KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,       KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,
        KC.A,   KC.S,   KC.D,   KC.F,   KC.G,       KC.H,   KC.J,   KC.K,   KC.L,   KC.SCOLON,
        KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,       KC.N,   KC.M,   KC.COMMA, KC.DOT , KC.SLASH,
        XXXXXXX,XXXXXXX,ESCALT,BSPDEL, SPCLOW,     ENTRAI,SUPERSHIFT,TABCTRL, XXXXXXX, XXXXXXX,
    ],
    #LOWER
    [   
        KC.TAB,    KC.N1,   KC.N2,   KC.N3,   KC.N4,       KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,
        KC.CAPS,     KC.N5,   KC.N6,   KC.N7,   KC.N8,       KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,
        KC.LSHIFT,    KC.N9,   KC.N0,   KC.MINUS,   KC.EQL,   KC.F11,   KC.F12,   KC.QUOT, KC.LBRC , KC.RBRC,
        XXXXXXX,XXXXXXX,KC.TAB, KC.BSC, KC.SPC,              KC.ENT, KC.ESC, LOWER, XXXXXXX, XXXXXXX,
    ],
    #RAISE/MOUSE
    [  
        KC.TAB,XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,            XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,
        XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,KC.MW_UP,	        KC.LEFT,   KC.UP,   KC.DOWN,   KC.RGHT, XXXXXXX,
        XXXXXXX,XXXXXXX,KC.LALT,XXXXXXX,KC.MW_DN,           KC.MB_MMB,   XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,
        XXXXXXX,XXXXXXX,RAISE, KC.BSPACE, KC.LGUI,        KC.ENT, KC.ESC, LOWER, XXXXXXX, XXXXXXX,
    ],

]





keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()


    
    
