import os
import split_files_in_dir.util as util
import datetime

'''
读取文件夹中的全部文件，以4:1的比例做train集和test集
:param path 存放全部数据集的文件夹路径
:return all_file_dir 返回文件夹中存储的各中分类文件夹
'''
part = 6


def get_all_data(path):
    files_dir_name = os.listdir(path)
    all_file_dir = []
    for file_dir in files_dir_name:
        # file_dir_entire = os.path.join(path, file_dir)
        all_file_dir.append(file_dir)
    return all_file_dir


'''
:param file_dir 分类文件夹路径
:param test_file_path 测试内容文件夹路径
按3:1的比例分出测试集和训练集
'''


def segmentation_file(file_dir, init):
    files_dir = os.path.join(init.src_path, file_dir)
    files_name = os.listdir(files_dir)
    files_num = len(files_name)
    test_len = files_num * (1 / part)
    for file_name_index in range(int(test_len)):
        file_path = os.path.join(files_dir, files_name[file_name_index])
        util.util.copy_move(init, file_path, init.dest_path)


'''
:param path 总文件路径
:param test_dir_path 测试集文件路径
分割数据集流程
'''


def run(init):
    all_file_dir = get_all_data(init.src_path)
    print("读出了" + str(len(all_file_dir)) + "个种类新闻数据")
    for index, file_dir in enumerate(all_file_dir):
        if check_index(index):
            break
        print("开始按" + str(part) + ":1比例分割文件" + file_dir)
        segmentation_file(file_dir, init)


def check_index(index):
    if index == 3:
        return True
    return False


def segmentation_file_dev(file_dir, init):
    files_dir = os.path.join(init.src_path, file_dir)
    files_name = os.listdir(files_dir)
    files_num = len(files_name)
    test_len = files_num * (1 / part)
    for file_name_index in range(int(test_len)):
        dest_dir = os.path.join(init.dest_path, file_dir)
        file_path = os.path.join(files_dir, files_name[file_name_index])
        util.util.copy_move(init, file_path, dest_dir)


def run_dev(init):
    all_file_dir = get_all_data(init.src_path)
    print("读出了" + str(len(all_file_dir)) + "个种类新闻数据")
    for index, file_dir in enumerate(all_file_dir):
        # if check_index(index):
        #     break
        print("开始按" + str(part) + ":1比例分割文件" + file_dir)
        segmentation_file_dev(file_dir, init)


if __name__ == "__main__":
    # run("F:/实验数据暂存/THUCNews/THUCNews", "F:/实验数据暂存/THUCNews/testNews")
    init = util.util("F:/实验数据暂存/THUCNews/THUCNews", "F:/实验数据暂存/tempNews")
    start_time = init.start_time
    print(start_time)
    run_dev(init)
    end_time = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    end_timestamps = datetime.datetime.now()
    spend_time = end_timestamps - init.start_timestamp
    print(end_time)
    print("花费时间" + str(spend_time) + "秒")
