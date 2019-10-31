from docx import Document
import os
import shutil

# 标签内容
dict_txt = {'1':"unknown",'2':"标题单方解除合同",
            '3':"不可抗力免责",'4':"出示证明",
            '5':"房屋面积+位置", '6':"房屋维修处理",
            '7':"非法活动",'8':"甲方",
            '9':"其他费用",'10':"签约日期",
            '11':"擅自改动房屋结构",'12':"擅自改动房屋用途",
            '13':"擅自转租",'14':"市政改造",
            '15':"损坏赔偿",'16':"提前中止合同",
            '17':"拖欠房租累计时间",'18':"未尽事项",
            '19':"协商转租",'20':"一式多份",
            '21':"乙方",'22':"逾期交房租",
            '23':"约定房屋装饰",'24':"争议解决",
            '25':"自愿订立",'26':"租金及付款方式",
            '27':"租赁期满",'28':"租赁日期"
            }

# 读取docx文件分段内容，并打印出来供选择存入对应的标签
def read_docx(contract_file_path,label_file_name_header):
    contract_document = Document(contract_file_path)
    for para in contract_document.paragraphs:
        print(para.text)
        num = input("放入第几个txt文件中：")
        try:
            if(len(num) == 0 or int(num) == 0):
                continue
            label_file_name = label_file_name_header +'/'+ dict_txt[num] + '.txt'
            save(label_file_name,para.text)
        except:
            continue

# 将对应条款内容存储进入对应的标签中
def save(label_file_name,para):
    check_is_exit(label_file_name)
    with open(label_file_name,'a', encoding= 'UTF-8') as f:
        f.write(para)
        f.write("\n\n")

# 检查文件夹是否存在，不存在则创建
def check_is_exit(label_file_name):
    if not os.path.exists(label_file_name):
        os.makedirs(label_file_name)

# 读取文件夹中的文件数据
def read_dir_file(dir_file_path):
    try:
        contract_file_path = os.listdir(dir_file_path)
    except:
        print("文档位置异常，请检查")
    return contract_file_path

# 把已经处理完的文件转移到另一个文件夹中
def move_file_to_other_dir(contract_file_path,new_dir):
    # check_is_exit(new_dir)
    shutil.move(contract_file_path,new_dir)

if __name__ == "__main__":
    # 待处理合同文件的文件夹位置
    dir_file_path = "F:/毕业设计涉及论文/合同文本数据"
    # 标签文件存放位置
    label_file_name_header = "G:/tim照片消息缓存聚集地/消息缓存/794182811/FileRecv/real2"
    # 处理完成的合同文件转移存放位置
    new_dir = "F:/毕业设计涉及论文/temp"
    for contract_file_path in read_dir_file(dir_file_path):
        contract_file_path = dir_file_path + "/" + contract_file_path
        # 进入下一个合同文件处理
        print('\033[0;31;40m\t'+contract_file_path+'\033[0m')
        read_docx(contract_file_path,label_file_name_header)
        move_file_to_other_dir(contract_file_path,new_dir)





