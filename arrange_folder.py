import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory  # filedialog是一个模块，不能直接在代码中用tk.filedialog，这样的.方法只能用于调用函数
import tkinter.messagebox as tkm  # 弹窗库


def GUI():
    def star():
        global src  # python的global有些特别
        src = askdirectory()
        text1.insert('insert', src)  # 第一个参数'insert',代表往指针处插入。如果没有指针，则在文字后面插入；如果没有文字，就在刚开始。

    def end():
        global dst
        dst = askdirectory()
        text2.insert('insert', dst)

    # 遍历出根目录下的所有文件路径
    def copy():

        for root, dirs, files in os.walk(src):  # 路径root、目录名dirs与文件名files
            for file in files:
                shutil.copy(os.path.join(root, file), dst)  # join方法就是讲其路径与目录名或者文件名连接起来，组成一个完整的目录
        tkm.showinfo('提示', '复制成功')  # 弹窗显示 操作成功

    windows = tk.Tk()  # 创建一个主窗口，用于容纳整个GUI程序
    windows.title("复制根目录下所有文件到指定文件夹的小工具")  # 设置主窗口对象的标题栏
    windows.geometry('500x125')  # 设置窗口大小

    lable1 = tk.Label(windows, text='   需要整理的根目录:')
    lable1.grid(row=0, column=0)
    lable2 = tk.Label(windows, text='   输出的目标文件夹路径:')
    lable2.grid(row=1, column=0)
    lable3 = tk.Label(windows, text='注意：输出的目标文件夹不能在根目录下', bg='red')
    lable3.grid(row=2, column=1)  # 作者github:WenjieZeng7
    lable4 = tk.Label(windows,text='复制时间与文件大小有关，请等待...')
    lable4.grid(row=3, column=1)

    text1 = tk.Text(windows, width=32, height=1)
    text1.grid(row=0, column=1)
    text2 = tk.Text(windows, width=32, height=1)
    text2.grid(row=1, column=1)

    button1 = tk.Button(windows, text='选择根目录', command=star, width=14)  # 进行操作
    button1.grid(row=0, column=2)
    button2 = tk.Button(windows, text='选择输出文件夹', command=end, width=14)  # 进行操作
    button2.grid(row=1, column=2)
    button3 = tk.Button(windows, text='开始复制', command=copy, width=14)  # 进行操作
    button3.grid(row=2, column=2)

    windows.mainloop()


if __name__ == '__main__':
    GUI()
