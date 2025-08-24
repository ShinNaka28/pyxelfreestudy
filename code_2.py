import pyxel

class App:
    def __init__(self):
        # ウィンドウの初期化
        pyxel.init(160, 120, title="Gamepad Action")
        self.player_x = 75
        self.player_y = 55
        
        # Pyxelのメインループを開始
        pyxel.run(self.update, self.draw)

    def update(self):
        # キーボードのスペースキーまたはゲームパッドのAボタンが押された瞬間にチェック
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(0, pyxel.GAMEPAD_BUTTON_A):
            print("Action!")

        # 以下は元の移動処理。必要に応じて残してください。
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(0, pyxel.GAMEPAD_BUTTON_DPAD_RIGHT):
            self.player_x += 1
        
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(0, pyxel.GAMEPAD_BUTTON_DPAD_LEFT):
            self.player_x -= 1
        
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(0, pyxel.GAMEPAD_BUTTON_DPAD_DOWN):
            self.player_y += 1
            
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(0, pyxel.GAMEPAD_BUTTON_DPAD_UP):
            self.player_y -= 1

    def draw(self):
        # 画面の描画処理
        pyxel.cls(0)  # 画面を黒でクリア
        pyxel.rect(self.player_x, self.player_y, 10, 10, 11)  # プレイヤーを描画
        pyxel.text(5, 5, "Press SPACE or Gamepad A for action.", 7)

# アプリケーションのインスタンスを作成して実行
App()
        pyxel.text(5, 5, "Use Arrow Keys or Gamepad D-pad to move.", 7)
        pyxel.text(5, 15, "Press SPACE or Gamepad A for action.", 7)


App()
