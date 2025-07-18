import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import torch

# Load the model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='E:/DH/DOAN/DoAnNDDT1/yolov5/runs/train/exp3/weights/best.pt')

#dictionary to label all traffic signs class.
classes = {
        0: 'Bến xe buýt',
        1: 'Bến xe điện',
        2: 'Bệnh viện',
        3: 'Biển báo các xe chỉ được rẻ trái -trừ xe được quyền ưu tiên theo quy định-',
        4: 'Biển hiệu lệnh rẻ phải',
        5: 'Biển hiệu lệnh rẻ trái',
        6: 'Bùng binh',
        7: 'Cấm đi ngược chiều',
        8: 'Cấm đỗ xe',
        9: 'Cấm đõ xe áp dụng ngày chẵn',
        10: 'Cấm dừng xe và đõ xe',
        11: 'Cấm người đi bộ',
        12: 'Cấm quay đầu xe',
        13: 'Cấm rẻ phải',
        14: 'Cấm rẻ trái',
        15: 'Cấm rẻ trái - rẻ phải',
        16: 'Cấm rẻ và quay đầu xe',
        17: 'Cấm sử dụng còi',
        18: 'Cấm vượt',
        19: 'Cấm xe 3 bánh có động cơ',
        20: 'Cấm xe 3 bánh không động cơ',
        21: 'Cấm xe đạp',
        22: 'Cấm xe khách',
        23: 'Cấm xe khách và xe tải',
        24: 'Cấm xe máy',
        25: 'Cấm xe ô tô',
        26: 'Cấm xe ô tô quay đầu',
        27: 'Cấm xe ô tô rẻ phải',
        28: 'Cấm xe ô tô rẻ trái',
        29: 'Cấm xe ô tô và xe máy',
        30: 'Cấm xe súc vật kéo',
        31: 'Cấm xe tải',
        32: 'Cấm xe tải có khối lượng',
        33: 'Chỉ hướng đường',
        34: 'Chỗ quay xe',
        35: 'Đi chậm',
        36: 'Đường cấm',
        37: 'Đường một chiều',
        38: 'Hạn chế chiều cao xe',
        39: 'Hạn chế tải trọng toàn bộ xe',
        40: 'Hạn chế tải trọng trục xe',
        41: 'Hết tất cả các lệnh cấm',
        42: 'Hướng phải đi vòng chướng ngại vạt',
        43: 'Hướng trái đi vòng chướng ngại vật',
        44: 'Nơi người đi bộ sang ngang',
        45: 'Cấm xe re trái',
        46: 'Cấm xe re phải',
        47: 'Được quay xe',
        48: 'R.425',
        49: 'Bến xe tải',
        50: 'Chiều cao an toàn',
        51: 'Dừng lại',
        52: 'Tên cầu',
        53: 'Tốc độ tối đa cho phép',
        54: 'Chỗ ngoặt nguy hiêm bên trái',
        55: 'Chỗ ngoặt nguy hiêm bên phải',
        56: 'Nhiều chỗ ngoặt nguy hiểm bên trái',
        57: 'Nhiều chõ ngoặt nguy hiểm bên phải',
        58: 'Đường bị thu hẹp bên trái',
        59: 'Đường bị thu hẹp bên phai',
        60: 'Đường giao nhau',
        61: 'Ngã 3 giao nhau bên phải',
        62: 'Ngã 3 giao nhau bên trái',
        63: 'Giao nhau chạy theo vòng xuyến',
        64: 'Giao nhau với đường không ưu tiên',
        65: 'Giao nhau với đường không ưu tiên',
        66: 'Giao nhau với đường không ưu tiên',
        67: 'Giao nhau với đường ưu tien',
        68: 'Giao nhau có đèn tín hiệu',
        69: 'Giao nhau với đường sắt có rào chắn',
        70: 'Xuống dốc nguy hiểm',
        71: 'Giao nhau với đường sắt không có rào chắn',
        72: 'Giao nhau với đường tàu điện',
        73: 'Đừong người đị bộ cắt ngang',
        74: 'Đọan đường có trẻ em đi qua',
        75: 'Công trường đang thi công',
        76: 'Nguy hiểm khác',
        77: 'Đườg đôi',
        78: 'Đi chậm'
        }

#initialise GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Nhận dạng biển báo giao thông ')
top.configure(background='#ffffff')

label = Label(top, background='#ffffff', font=('arial', 15, 'bold'))
sign_image = Label(top)


def classify(file_path):
    global label
    image = Image.open(file_path)
    # Dự đoán các lớp
    results = model(image)
    print(results)
    # Lấy chỉ số lơp
    class_indices = results.pred[0][:, -1].int().tolist()
    # Chuyển đổi chỉ số lớp thành tên lớp bằng cách sử dụng một tập hợp để loại bỏ trùng lắp
    predicted_classes = set(classes[i] for i in class_indices)
    # Chuyển đổi tập hợp các lớp thành một chuỗi
    label_text = ', '.join(predicted_classes)
    results.xyxy[0]
    results.pandas().xyxy[0]
    label.configure(foreground='#011638', text=label_text, font=('arial', 20, 'bold'))

 

def show_classify_button(file_path):
    classify_b = Button(top, text="Nhận dạng", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#c71b20', foreground='white', font=('arial', 12, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image = im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload = Button(top,text = "Upload an image",command = upload_image,padx = 10,pady = 5)
upload.configure(background='#c71b20', foreground='white', font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Nhận dạng biển báo giao thông", pady=10, font=('arial', 20, 'bold'))
heading.configure(background='#ffffff', foreground='#364156')

heading.pack()
top.mainloop()
