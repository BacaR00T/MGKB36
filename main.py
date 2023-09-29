print("mgkb36_handwired")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
layers_ext = Layers()
                    #LEFT              MMVVEE      VVVVCXSS  CCCC FFRV                               #RIGHT
keyboard.col_pins = (board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP21, board.GP20,board.GP19,board.GP18,board.GP17) # Cols
keyboard.row_pins = (board.GP5, board.GP4, board.GP3,board.GP2 ) # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)

#from kmk.extensions.RGB import RGB
#rgb = RGB(
#    pixel_pin=board.GP27, 
#    num_pixels=2, 
#    hue_default =100, 
#    sat_default=255, 
#    val_default=10,	
#    )
#keyboard.extensions.append(rgb)

# Keymap
keyboard.keymap = [
    #KEYS
    [  
        KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,       KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,
        KC.A,   KC.S,   KC.D,   KC.F,   KC.G,       KC.H,   KC.J,   KC.K,   KC.L,   KC.SCOLON,
        KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,       KC.N,   KC.M,   KC.COMMA, KC.DOT , KC.SLASH,
        XXXXXXX,XXXXXXX,RAISE, KC.BSPC, KC.SPC,     KC.ENT, KC.LCTRL, LOWER, XXXXXXX, XXXXXXX,
    ],
    #LOWER
    [   
        KC.TAB,    KC.N1,   KC.N2,   KC.N3,   KC.N4,       KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,
        KC.CAPS,     KC.N5,   KC.N6,   KC.N7,   KC.N8,       KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,
        KC.LSHIFT,    KC.N9,   KC.N0,   KC.MINUS,   KC.EQL,   KC.F11,   KC.F12,   KC.QUOT, KC.LBRC , KC.RBRC,
        XXXXXXX,XXXXXXX,RAISE, KC.BSC, KC.SPC,              KC.ENT, KC.ESC, LOWER, XXXXXXX, XXXXXXX,
    ],
    #RAISE/MOUSE
    [  
        XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,            XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,
        XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,KC.MW_UP,	        KC.LEFT,   KC.UP,   KC.DOWN,   KC.RGHT, XXXXXXX,
        XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,KC.MW_DN,           KC.MB_MMB,   XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,
        XXXXXXX,XXXXXXX,RAISE, KC.BSPACE, KC.LGUI,        KC.ENT, KC.ESC, LOWER, XXXXXXX, XXXXXXX,
    ],

]





keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()


    
    