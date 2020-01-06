
import os
from win32com import client as wc

# 获得要转换doc文档的文件夹路径
def get_doc_file(path):
    files = []
    for file in os.listdir(path):
        if file.endswith(".doc"):  # 排除文件夹内的其它干扰文件，只获取".doc"后缀的word文件
            files.append(path + file)
    return files

# 转换为docx
def save_to_docx(files):
    word = wc.Dispatch("Word.Application")
    for file in files:
        try:
            print("现在在转存："+file)
            doc = word.Documents.Open(file) #打开word文件
            doc.SaveAs("{}x".format(file), 12)#另存为后缀为".docx"的文件，其中参数12指docx文件
            doc.Close() #关闭原来word文件
            dele_doc(file)
        except Exception as e:
            print("文件："+file +"转存失败，失败原因：", e)
            continue
    word.Quit()

# 删除已经转换完的doc文件
def dele_doc(file_path):
    os.remove(file_path)
    print("已删除：" + file_path + " 文件")

# 运行代码
def run(path):
    files_path = get_doc_file(path)
    save_to_docx(files_path)
    print("转换完成")


if __name__ == "__main__":
    path = "G:/律师-劳动/"  # 打开word文件
    run(path)
    path = "G:/律师-买卖/"  # 打开word文件
    run(path)

