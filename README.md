# 脚本清单

## doc_to_docx

使用介绍：

将文件夹下方的所有doc文件转换为docx文件（doc文件转换完毕后会被删除）。

`run(path)`

`path`:存放需要转换的doc文件

## image_max

使用介绍：

将图片旋转（还未开发，敬请期待）

## read_docx_paragraph

使用介绍：

自动打标签脚本（读取文件夹下方的docx文件，并对docx文件中的每一段落打上对应标签，并且复制粘贴进对应标签的txt文件中，以空行隔开）

如何使用请自行阅读对应`py`文件

## split_file_in_dir

使用介绍：

对文件夹下面的文件按比例进行切割

可运行文件为：`train_and_test.py`

`util.util(src,dest)`

`src`:待分割文件夹

`dest`：分割后的结果

全局变量`part`是按`1:part-1`比例分割。

## image_to_tf

使用介绍：

将图片转换为tfrecord格式，方便后续处理

`run(path, mode)`

`path`:总路径

`mode`:总路径下需要全部被转换为tfrecord格式的数据集文件夹