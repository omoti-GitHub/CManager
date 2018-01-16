#CManager
'''
これは顧客管理システムのプログラムを書いてみるの図です。
Auther: omoti
wxPython使いたいです。
'''

#インポートモジュール
import wx # wxpythonをインポート

app = wx.App() # アプリケーションを作成

frame = wx.Frame(None,-1) # ウィンドウ作成
frame.Show() # ウィンドウ表示

app.MainLoop() # ループを設定
