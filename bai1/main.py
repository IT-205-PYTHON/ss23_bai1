from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta
from utils.file_helper import create_log_dir
from datetime import datetime

# Dữ liệu các chuyến xe
shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285, "from_lon": 105.8542,
        "to_lat": 10.8231,  "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285, "from_lon": 105.8542,
        "to_lat": 16.0544,  "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00"
    },
]

print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")

# Khởi tạo thư mục log (an toàn, không sập nếu đã tồn tại)
create_log_dir("logs")
print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
print("-" * 75)

for s in shipments:
    distance = calculate_distance(s["from_lat"], s["from_lon"],
                                  s["to_lat"],   s["to_lon"])

    eta = predict_eta(s["depart"], distance)
    deadline = datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")

    if eta <= deadline:
        status = "🟢 AN TOÀN (Kịp tiến độ trước deadline)"
    else:
        status = f"🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline.strftime('%H:%M:%S')})"

    print(f"\n[CHUYẾN XE {s['id']}]")
    print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
    print(f" + Thời gian khởi hành: {s['depart']}")
    print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f" + Trạng thái: {status}")

print("\n" + "=" * 56)
