# yolov3.pytorch For VOC2007

---

1. 从 [YOLO website](http://pjreddie.com/darknet/yolo/)下载权重。
2. 使用convert.py将darknet的权重转化为keras权重
3. 进行预测

```
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
python yolo_video.py [OPTIONS...] --image, for image detection mode, OR
python yolo_video.py [video_path] [output_path (optional)]
```

 `--model model_file` 和 `--anchors anchor_file` 分别用来制定模型路径与anchor尺寸

4. 使用多个GPU: use `--gpu_num N` 

## Training

1. 创建类文件和标注文件
    运行  `python voc_annotation.py`  
    得到的例子: 
    
    ```
    path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
    path/to/img2.jpg 120,300,250,600,2
    ...
    ```
    
2. 运行 `python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5`  来获取预训练文件model_data/yolo_weights.h5 

    ![1562117769379](1562117769379.png)

3. 修改train.py
    `python train.py`  
    
    

如果想用YOLOv3的基础网络作为与训练模型，执行以下步骤：
    1. `wget https://pjreddie.com/media/files/darknet53.conv.74`   获取模型
    2. 重命名为 darknet53.weights  
    3. `python convert.py -w darknet53.cfg darknet53.weights model_data/darknet53_weights.h5`  将模型转化为h5文件
    4. 修改 train.py 指定使用model_data/darknet53_weights.h5作为预训练模型。

---

## 其他

1. 主要环境要求
    - Python 3.6+
    - Keras 2.1.5
    - tensorflow 1.6.0
2. 目前使用的是默认原版darknet中提供的anchor尺寸，具体可以在model/yolo_anchors.txt中进行修改
3. 在加载与训练权重的过程中会存在一些层无法加载进去的问题。
4. 可以根据需要对训练过程中的超参进行修改。
5. The training strategy is for reference only. Adjust it according to your dataset and your goal. And add further strategy if needed.
6. train_bottleneck.py 冻结了其他层，只训练最后一层，所以训练速度很快。
