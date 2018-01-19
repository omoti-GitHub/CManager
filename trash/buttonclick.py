#main.py
#CManager
'''
これは顧客管理システムのプログラムを書いてみるの図です。
Auther: omoti
wxPython使いたいです
'''

'''
インポートモジュール
'''
import wx # wxpythonをインポート



'''
画面のクラスを作る #CMApp
'''
class CMApp(wx.Frame): # ウィンドウ表示させるためのwx.FrameをつかってCMAppを定義していく

    def __init__(self, *args, **kw):
        super(CMApp,self).__init__(*args, **kw) # オーバーライドって言う奴の設定らしい

        self.init_ui() # 次の画面の初期設定の関数を実行するためのもの

    def init_ui(self):
        self.SetTitle('CManager') # タイトル
        self.SetBackgroundColour((40,175,148)) # 背景色設定
        self.SetPosition((200,200)) # 表示位置
        self.SetSize((800,600)) # 横、縦の幅設定
        self.Show() # ウィンドウ表示命令

        panel_ui = wx.Panel(self, -1, pos=(50,10), size=(300,600)) # panel_uiというパネルを作る



        self.label = wx.StaticText(panel_ui, -1, 'こんちゃ', pos=(10,10)) # 日本語でこんちゃと表示させる

        btn = wx.Button(panel_ui, -1, 'ぼたんっふー！', pos=(10,50)) # ボタンを作る
        btn.Bind(wx.EVT_BUTTON, self.clicked) # wx.EVT_BUTTON（ボタンクリック）という動作がされたら、self.clicked()関数を呼び出す

        panel_A = wx.Panel(panel_ui, -1, pos=(0,100), size= (300,500)) # panel_A
        panel_A.SetBackgroundColour((239,117,152))

        panel_ui.label = wx.StaticText(panel_A, -1, 'wawawa', pos=(10,10))
        '''
        親親.label = wx.StaticText(親, -1, 'wawawa', pos=(10,10))

        '''

        def click_buttun(event):
            panel_ui.label.SetLabel('まじか')

        btn_A = wx.Button(panel_A, -1, 'saaosunodesu', pos=(20,50))
        btn_A.Bind(wx.EVT_BUTTON, click_buttun)


        panel_ux = wx.Panel(self, -1, pos=(400,10), size=(300,600)) # panel_uiというパネルを作る
        panel_ux.SetBackgroundColour((255,195,76))

    def clicked(self, event):
        self.label.SetLabel('くりっくしたじゃん！')



'''
最後においておくコード
'''
app = wx.App() # アプリケーションを作成
CMApp(None) # インスタンスってのを作るらしい
app.MainLoop() # ループを設定
