import os
import tensorflow as tf
from PIL import Image  #注意Image,后面会用到
import matplotlib.pyplot as plt
import numpy as np
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"]="0"


def get_classes(path):
    '''列出所有类别的路径
    :param path 数据集总路径
    :return 所有类别路径'''
    classes = os.listdir(path)
    return classes

def write_tfrecord(path, classes, mode):
    '''将类别以及对应图片转存成tfrecord格式
    :param path 所有类别路径
    :param classes 所有类别组成的列表
    :param mode tfrecord的文件名'''
    tfrecord_path = os.path.join(path, mode + ".tfrecords")
    with tf.python_io.TFRecordWriter(tfrecord_path) as writer:
        for index, name in enumerate(classes):
            print(name + "   文件正在转换")
            class_path = os.path.join(path, name)
            for imag_name in os.listdir(class_path):
                imag_path = os.path.join(class_path, imag_name)
                img = Image.open(imag_path)
                img = img.resize((112, 112))
                img_raw = img.tobytes()
                example = tf.train.Example(features=tf.train.Features(feature={
            "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[index])),
            'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw]))
        }))
                writer.write(example.SerializeToString())

def read_tfrecord(path):
    filename_queue = tf.train.string_input_producer([path], num_epochs=1)
    reader = tf.TFRecordReader()
    # 从文件中读出一个样例
    _, serialized_example = reader.read(filename_queue)
    print("")

def run(path, mode):
    '''将总路径下的mode文件夹里的图片转换为tfrecord格式
    :param path 总路径
    :param mode 总路径下需要全部被转换为tfrecord格式的数据集文件夹'''
    entire_path = os.path.join(path, mode)
    classes = get_classes(entire_path)
    write_tfrecord(entire_path, classes, mode)

if __name__=="__main__":
    run("F:/temp python workplace/data/hand_write_output_result", "tst")
    # run("F:/temp python workplace/data/hand_write_output_result", "dev")
    # read_tfrecord("F:/temp python workplace/data/hand_write_output_result/trn/train.tfrecords")
