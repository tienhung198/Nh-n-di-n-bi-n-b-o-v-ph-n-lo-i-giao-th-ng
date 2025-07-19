
# 🚦 Nhận Diện Biển Báo Giao Thông với YOLOv5

Dự án này sử dụng mô hình **YOLOv5** để nhận diện các loại biển báo giao thông trong ảnh và video, phục vụ cho các ứng dụng hỗ trợ giao thông thông minh.

## 📂 Mục lục
- [Giới thiệu](#giới-thiệu)
- [Thu thập và xử lý dữ liệu](#thu-thập-và-xử-lý-dữ-liệu)
- [Cấu hình huấn luyện](#cấu-hình-huấn-luyện)
- [Huấn luyện mô hình](#huấn-luyện-mô-hình)
- [Phát hiện và đánh giá](#phát-hiện-và-đánh-giá)
- [Giao diện người dùng (GUI)](#giao-diện-người-dùng-gui)
- [Kết quả](#kết-quả)
- [Hướng dẫn chạy demo](#hướng-dẫn-chạy-demo)

## 📌 Giới thiệu

Mục tiêu của dự án là phát triển một mô hình có thể nhận diện chính xác các biển báo giao thông trong nhiều điều kiện khác nhau (ánh sáng, thời tiết, góc chụp), ứng dụng trong hệ thống giao thông thông minh.

## 📸 Thu thập và xử lý dữ liệu

- **Nguồn dữ liệu**: ảnh biển báo tự chụp, internet (Google, Kanggle...).
- **Tiền xử lý**:
  - Resize ảnh về kích thước chuẩn (640x640).
  - Chuẩn hóa pixel về [0, 1].
  - Gắn nhãn theo định dạng YOLO (bounding box và class).
- **Phân chia dữ liệu**:
  - Train: 80%
  - Validation: 10%
  - Test: 10%

## ⚙️ Cấu hình huấn luyện

- **Mô hình**: `YOLOv5s`
- **Tham số**:
  - Epochs: 50
  - Batch size: 4
  - Learning rate: 0.001
- **Công cụ**: Sử dụng GPU và framework PyTorch

## 🧠 Huấn luyện mô hình

Sử dụng lệnh sau để huấn luyện:

```bash
python train.py --img 640 --batch 4 --epochs 50 \
--data data.yaml --weights yolov5s.pt --device 0
```

## 🔍 Phát hiện và đánh giá

- **Dự đoán ảnh**:

```bash
python detect.py --source data/trafficsign/test/images \
--weights runs/train/exp3/weights/last.pt --data data.yaml --conf 0.7
```

- **Dự đoán video**:

```bash
python detect.py --source traffic-sign-to-test.mp4 \
--weights runs/train/exp3/weights/last.pt --data data.yaml
```

- **Đánh giá hiệu suất**:

```bash
python val.py --weights runs/train/exp3/weights/last.pt \
--data data.yaml --verbose
```

Các chỉ số quan trọng: **Precision**, **Recall**, **mAP50**, **Confusion Matrix**.

## 🖥️ Giao diện người dùng (GUI)

Giao diện đơn giản giúp người dùng chọn ảnh và hiển thị kết quả nhận diện:

- Chạy GUI:

```bash
python GUI.py
```

- Tính năng:
  - Upload ảnh
  - Nhận dạng đối tượng
  - Hiển thị ảnh và kết quả ngay trên giao diện

## 📊 Kết quả

- Mô hình hoạt động tốt với các ảnh rõ nét, biển báo đơn lẻ.
- Hiệu suất giảm với ảnh có nhiều biển báo chồng lấp, nhiễu hoặc ánh sáng yếu.
- Các biểu đồ theo dõi: loss, precision, recall, mAP...

## ▶️ Hướng dẫn chạy demo

1. Cài đặt các thư viện:

```bash
pip install -r requirements.txt
```

2. Cấu trúc thư mục:

```
project/
│
|──yolov5
|  |── data/
│      ├── train/
│      ├── test/
│      └── valid/
│
|  |── runs/
|  |── data.yaml
|  |── GUI.py
└───── README.md
```

3. Huấn luyện mô hình hoặc sử dụng trọng số có sẵn để phát hiện.
4. Chạy GUI.py để thử nghiệm nhận diện ảnh.

---

**📌 Lưu ý**: Đảm bảo bạn có GPU để tăng tốc độ huấn luyện. Mô hình YOLOv5 được clone từ [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5).

---

## 📬 Liên hệ

> Email: hungtvt218@gmail.com
