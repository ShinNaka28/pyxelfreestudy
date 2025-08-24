import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Gamepad Test")
        self.player_x = 75
        self.player_y = 55
        pyxel.run(self.update, self.draw)

    def update(self):
        # Pyxel 1.x系のコードに修正
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.player_x += 1
        
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.player_x -= 1
        
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.player_y += 1
            
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.player_y -= 1
            
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or \
           pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) or \
           pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y):
            print("Action!")




    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.player_x, self.player_y, 10, 10, 11)
        pyxel.text(5, 5, "Use Arrow Keys or Gamepad D-pad to move.", 7)
        pyxel.text(5, 15, "Press SPACE or Gamepad A for action.", 7)


App()