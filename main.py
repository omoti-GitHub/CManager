#main.py
#CManager
# -*- coding:utf-8 -*-
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
import variable as V # variableの変数読み込みんでV.(変数)で代入できるようにした


'''
画面のクラスを作る #CMFrame
'''
class CMFrame(wx.Frame): # ウィンドウ表示させるためのwx.FrameをつかってCMAppを定義していく

    def __init__(self, *args, **kw):
        super(CMFrame,self).__init__(*args, **kw) # オーバーライドって言う奴の設定らしい

        self.init_ui() # 次の画面の初期設定の関数を実行するためのもの

    def init_ui(self):

        """""""""""""""""""""""""""""""""
        本体の設定
        """""""""""""""""""""""""""""""""
        self.SetTitle('CManager') # タイトル
        self.SetSize(V.w_size) # 横、縦の幅設定
        self.SetBackgroundColour(V.w_BK_color) # 背景色設定RGBの時は(255,255,255)って()の中に入れる
        self.Center() # 表示位置を中央に

        # iconの設定
        icon = wx.Icon(V.w_icon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        # メニューの設置
        self.SetMenuBar(CMMenu())


        """""""""""""""""""""""""""""""""
        複数パネルの設定
        """""""""""""""""""""""""""""""""
        #
        # 親パネルをつくる
        #
        notebook = wx.Notebook(self,-1, style=wx.NB_FLAT) # パネルを重ねるためのノートブックを作る(親,ID,pos,size,style,name)


        #
        # 子パネルを複数作る
        #
        Panel_start = wx.Panel(notebook, -1) # start時のパネル
        Panel_register = wx.Panel(notebook, -1)  #  顧客登録のパネル
        Panel_search = wx.Panel(notebook, -1) # 顧客検索のパネル

        # パネルのサイズを定義


        # パネルをノートブックに追加
        notebook.InsertPage(0, Panel_start, 'スタート画面') #親タブ.InsertPage(タブインデックス, 追加するパネルの名前,　名称)
        notebook.InsertPage(1, Panel_register, '顧客登録')
        notebook.InsertPage(2, Panel_search, '検索')

        # 背景色を全部画面のデフォルトと一緒にする
        notebook.SetBackgroundColour(V.w_BK_color)
        Panel_start.SetBackgroundColour(V.w_BK_color)
        Panel_register.SetBackgroundColour(V.w_BK_color)
        Panel_search.SetBackgroundColour(V.w_BK_color)

        # タブの文字色をデフォルトと一緒にする
        notebook.SetForegroundColour(V.w_FT_color)

        # タブのアイコンを設定する
        image_list = wx.ImageList(30,30) # ImageListの初期化

        # 画像の呼び出し
        icon_start = wx.Icon(V.n_start, wx.BITMAP_TYPE_PNG)
        icon_register = wx.Icon(V.n_register, wx.BITMAP_TYPE_PNG)
        icon_search = wx.Icon(V.n_search, wx.BITMAP_TYPE_PNG)


        # 画像をリストに追加
        image_list.Add(icon_start)
        image_list.Add(icon_register)
        image_list.Add(icon_search)

        notebook.AssignImageList(image_list) # ?

        # アイコンを適用
        notebook.SetPageImage(0,0)
        notebook.SetPageImage(1,1)
        notebook.SetPageImage(2,2)


        """""""""""""""""""""""""""""""""
         スタート画面の設定
        """""""""""""""""""""""""""""""""
        #
        # ロゴとボタンの設置
        #
        # 画像の呼び出し
        bmp_logo = wx.Bitmap(V.logo, wx.BITMAP_TYPE_PNG) # ロゴ
        bmp_btn_start = wx.Bitmap(V.b_start, wx.BITMAP_TYPE_PNG) # スタートボタン

        # ロゴの設置
        st_logo = wx.StaticBitmap(Panel_start, -1, bmp_logo, size=bmp_logo.GetSize()) # wx.StaticBitmap(親, ID, 表示する画像をコンバートしたもの, pos, size)

        #ボタン作成
        st_btn_start = wx.BitmapButton(Panel_start, -1, bmp_btn_start,style=wx.NO_BORDER)
        st_btn_start.SetBackgroundColour(V.w_BK_color)


        # レイアウト
        layout_start = wx.BoxSizer(wx.VERTICAL)
        layout_start.AddStretchSpacer()
        layout_start.Add(st_logo, proportion=0, flag= wx.ALIGN_CENTER)
        layout_start.Add(st_btn_start, proportion=0, flag=wx.ALIGN_CENTER)
        layout_start.AddStretchSpacer()
        Panel_start.SetSizer(layout_start)


        """""""""""""""""""""""""""""""""
         顧客登録画面の設定
        """""""""""""""""""""""""""""""""
        # 入力エリア
        panel_register_input = CMPanel_R(Panel_register)
        # ボタン
        st_btn_register = CMPanel_B(Panel_register)

        # レイアウトの設定
        layout_register = wx.BoxSizer(wx.VERTICAL)
        layout_register.AddStretchSpacer()
        layout_register.Add(panel_register_input, proportion=0, flag=wx.ALL, border=100)
        layout_register.AddStretchSpacer()
        layout_register.Add(st_btn_register, proportion=0, flag=wx.ALL, border=500)
        layout_register.AddStretchSpacer()
        layout_register.Fit(Panel_register)


        # セットレイアウト
        Panel_register.SetSizer(layout_register)



#
#入力パネルの設定
#

class CMPanel_R(wx.Panel):
    def __init__(self,a):
        super().__init__()
        self = a


        # テキストボックスの上のテキスト
        txt_company = wx.StaticText(self, -1, '会社名')
        txt_name = wx.StaticText(self, -1, '担当者名')
        txt_startday = wx.StaticText(self, -1, '取引開始時期')
        txt_tag = wx.StaticText(self, -1, '検索用のタグ')
        txt_job = wx.StaticText(self, -1, '業務内容')
        txt_url = wx.StaticText(self, -1, '会社URL')


        #
        # テキストボックスを作る
        #(company)・担当者名(name)・取引開始時期(start)・検索用のタグ(tag)・業務内容(job)
        box_company = wx.TextCtrl(self, -1)
        box_name = wx.TextCtrl(self, -1)
        box_startday = wx.TextCtrl(self, -1)
        box_tag = wx.TextCtrl(self, -1)
        box_job = wx.TextCtrl(self, -1)
        box_url = wx.TextCtrl(self, -1)

        # 背景色

        # list
        List = [txt_company,txt_name,box_company,box_name,txt_startday,txt_tag,box_startday,box_tag,txt_job,txt_url,box_job,box_url]




        # テキストボックスのレイアウト
        layout = wx.GridSizer(6, 2,0,0)
        for i in List:
            layout.Add(i, proportion=1)

        # セット
        self.SetSizer(layout)


#        self.Show() # ウィンドウ表示命令

#
# ボタンパネル
#

class CMPanel_B(wx.Panel):
    def __init__(self,b):
        super().__init__()
        self = b
        bmp_btn_register = wx.Bitmap(V.b_register, wx.BITMAP_TYPE_PNG) # スタートボタン

        # ロゴの設置
        btn_register = wx.BitmapButton(self, -1, bmp_btn_register,style=wx.NO_BORDER)
        # テキストボックスのレイアウト
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(btn_register)

        # セット
        self.SetSizer(layout)



"""""""""""""""""""""""""""""""""
の設定
"""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""
メニューの作成
"""""""""""""""""""""""""""""""""
class CMMenu(wx.MenuBar):
    def __init__(self):

        super().__init__()

        menubar = wx.MenuBar(wx.MB_DOCKABLE)

        #
        #　親メニューの作成
        #
        menu_file = wx.Menu() # ファイルメヌーの作成
        menu_help = wx.Menu() # ヘルプメニューの作成


        #
        #　子メニューの作成
        #

        # ファイルメヌーにメニュー追加
        menu_file_open = wx.Menu() # 開くメニューの作成
        menu_file_open = wx.MenuItem(menu_file, -1, '&開く\tCtrl+Q') # 開くメニューの設定で、ファイルメニューに開くって名前のメニューつけてショートカットキーも設定したよっていうやつ
        menu_file_open.SetBitmap(wx.Bitmap(V.m_open)) # 開くメニューにアイコンつけてみた
        menu_file.Append(menu_file_open) # ファイルメニューに開くメニューをついかする

        menu_file.Append(-1, '&保存') # 保存メニューの追加



        # ヘルプメヌーにメニュー追加
        menu_help_help = wx.Menu()
        menu_help_help = wx.MenuItem(menu_help,-1, '&ヘルプ')
        menu_file_open.SetBitmap(wx.Bitmap(V.m_help)) # 開くメニューにアイコンつけてみた
        menu_help.Append(menu_help_help)


        #
        # menubarにメニューさんたちをついか
        #
        menubar.Append(menu_file,'&ファイル')
        menubar.Append(menu_help,'&ヘルプ')



'''
最後においておくコード
'''
app = wx.App() # アプリケーションを作成
CMFrame(None).Show() # インスタンスってのを作るらしい
app.MainLoop() # ループを設定
