import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Gamepad Test")
        self.player_x = 75
        self.player_y = 55
        # 「Action!」表示用のタイマー（0より大きいときに表示）
        self.action_display_timer = 0 
        pyxel.run(self.update, self.draw)

    def update(self):
        # プレイヤーの移動処理
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.player_x += 1
        
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.player_x -= 1
        
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.player_y += 1
            
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.player_y -= 1
            
        # スペースキー、またはゲームパッドのA, B, X, Yボタンのいずれかが押された瞬間に、
        # Action!表示タイマーを設定する
        if pyxel.btnp(pyxel.KEY_SPACE) or \
           pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or \
           pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or \
           pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) or \
           pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y):
            self.action_display_timer = 30  # 約0.5秒間表示 (30フレーム)

        # Action!表示タイマーが0より大きければカウントダウン
        if self.action_display_timer > 0:
            self.action_display_timer -= 1


    def draw(self):
        pyxel.cls(0) # 画面を黒でクリア
        pyxel.rect(self.player_x, self.player_y, 10, 10, 11) # プレイヤーを描画
        pyxel.text(5, 5, "Use Arrow Keys or Gamepad D-pad to move.", 7)
        pyxel.text(5, 15, "Press SPACE or Gamepad buttons A,B,X,Y for action.", 7)

        # Action!表示タイマーが0より大きい場合のみ「Action!」と表示
        if self.action_display_timer > 0:
            text = "Action!"
            # 画面中央に表示するためのX座標とY座標を計算
            # text_width() がないため、文字列の長さにFONT_WIDTHを掛けて幅を計算
            text_width_calculated = len(text) * pyxel.FONT_WIDTH
            text_x = pyxel.width / 2 - text_width_calculated / 2
            text_y = pyxel.height / 2 - pyxel.FONT_HEIGHT / 2
            pyxel.text(text_x, text_y, text, 8) # 8は明るい黄色 (文字色)
App()
