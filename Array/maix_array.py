# Hello World Example
#
# Welcome to the MaixPy IDE!
# 1. Conenct board to computer
# 2. Select board at the top of MaixPy IDE: `tools->Select Board`
# 3. Click the connect buttion below to connect board
# 4. Click on the green run arrow button below to run the script!

from Maix import MIC_ARRAY as mic
import lcd

lcd.init()
mic.init()

while True:
    imga = mic.get_map()
    print(imga)
    b = mic.get_dir(imga)
    print(b)
    a = mic.set_led(b,(0,0,200))
    imgb = imga.resize(320,240)
    imgc = imgb.to_rainbow(1)
    a = lcd.display(imgc)
mic.deinit()
