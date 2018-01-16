#main.py
#CManager
'''
これは顧客管理システムのプログラムを書いてみるの図です。
Auther: omoti
wxPython使いたいです。

顧客の会社名(company)・担当者名(name)・取引開始時期(start)・検索用のタグ(tag)・業務内容(job)
以上を入力し、CSVに出力できるようにしてみる
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


        # メニューの作成
        menubar = wx.MenuBar(wx.MB_DOCKABLE)

        # ファイルメヌーの作成
        fil = wx.Menu()

        fil.Append(-1, '&開く')
        fil.Append(-1, '&保存')

        # 顧客管理メニューの作成
        rgt = wx.Menu()

        # 検索メニューの作成
        sch = wx.Menu()

        menubar.Append(fil,'&ファイル')
        menubar.Append(rgt,'&顧客管理')
        menubar.Append(sch,'&検索')

        self.SetMenuBar(menubar)
        self.Center()
        self.Show(True)



'''
最後においておくコード
'''
app = wx.App() # アプリケーションを作成
CMApp(None) # インスタンスってのを作るらしい
app.MainLoop() # ループを設定
