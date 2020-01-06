import shutil
import os
import datetime
class util(object):
    def __init__(self, src_path, dest_path):
        self.start_timestamp = datetime.datetime.now()
        self.start_time = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
        self.src_path = src_path
        self.dest_path = dest_path

    '''
    :param src_path 源文件
    :param dest_path 需要剪切到的路径
    将文件剪切到另一个文件夹
    '''
    def copy_move(self, src_path, dest_path):
        try:
            self.check_path(dest_path)
            shutil.copy(src_path, dest_path)
        except:
            pass

    '''
    :param path 被检查是否存在的路径
    :return 已经存在的路径（不存在则创建）
    检查路径是否存在，不存在则创建
    '''
    def check_path(self, path):
        if os.path.exists(path):
            return path
        else:
            os.makedirs(path)
            return path
