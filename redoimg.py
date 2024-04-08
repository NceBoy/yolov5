import os
import cv2

def process_files(source_dir, target_dir):
    # 确保目标目录存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 遍历源目录中的文件
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        
        # 读取图像文件
        img = cv2.imread(source_path)

        # 如果图像读取成功
        if img is not None:
            # 构造目标文件路径
            target_path = os.path.join(target_dir, filename)
            
            # 保存图像到目标路径
            cv2.imwrite(target_path, img)
            print(f"Processed {source_path} -> {target_path}")
        else:
            print(f"Failed to read {source_path}")

if __name__ == "__main__":
    # 源目录 A 和目标目录 A1
    source_dir_A = "../dataset/images/train"
    target_dir_A1 = "../dataset/images/trains"
    process_files(source_dir_A, target_dir_A1)

    # 源目录 B 和目标目录 B1
    source_dir_B = "../dataset/images/valid"
    target_dir_B1 = "../dataset/images/valids"
    process_files(source_dir_B, target_dir_B1)