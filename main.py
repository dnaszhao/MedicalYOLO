if __name__ == "__main__":
    from ultralytics import YOLO

    # # 从配置文件创建新的模型
    # model = YOLO("yolov8n.yaml")
    #
    # # 训练模型
    # model.train(data="coco8.yaml", epochs=3)

    # 第二步推理
    model = YOLO("best.pt")
    results = model.predict(show=True)