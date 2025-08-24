import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Gamepad Action")
        # 「Action!」表示のフラグ
        self.show_action = False
        pyxel.run(self.update, self.draw)

    def update(self):
        # A, B, C, Dボタンのいずれかが押された瞬間にフラグをTrueにする
        # pyxel 1.x系の場合は pyxel.GAMEPAD1_BUTTON_B のように修正が必要
        if pyxel.btnp(pyxel.GAMEPAD_BUTTON_A) or \
           pyxel.btnp(pyxel.GAMEPAD_BUTTON_B) or \
           pyxel.btnp(pyxel.GAMEPAD_BUTTON_C) or \
           pyxel.btnp(pyxel.GAMEPAD_BUTTON_D):
            self.show_action = True
            
        # 画面がクリックされたらリセットする (確認用)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.show_action = False

    def draw(self):
        pyxel.cls(0)  # 画面を黒でクリア
        
        if self.show_action:
            # 画面中央に「Action!」と表示
            # 文字列の幅を計算して中央揃えにする
            text = "Action!"
            text_x = pyxel.width / 2 - pyxel.text_width(text) / 2
            text_y = pyxel.height / 2 - pyxel.FONT_HEIGHT / 2
            pyxel.text(text_x, text_y, text, 7) # 7は文字の色番号

App()
