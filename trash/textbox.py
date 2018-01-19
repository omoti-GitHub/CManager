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

        panel_ui = wx.Panel(self, -1, pos=(50, 50),size=(300, 200)) # panel_uiをつくる

        self.label = wx.StaticText(panel_ui, -1, '', pos=(10, 10))

        self.box = wx.TextCtrl(panel_ui, -1, pos=(10,50)) # テキストボックスを作る

        btn = wx.Button(panel_ui,-1,'コピー', pos=(10, 90))
        btn.Bind(wx.EVT_BUTTON, self.clicked)

    def clicked(self, event):
        text = self.box.GetValue()
        self.box.Clear()
        self.label.SetLabel(text)

'''
最後においておくコード
'''
app = wx.App() # アプリケーションを作成
CMApp(None) # インスタンスってのを作るらしい
app.MainLoop() # ループを設定
