from datetime import datetime, timedelta

def predict_eta(departure_str: str, distance_km: float, speed: float = 60) -> datetime:
    """
    Tính thời gian dự kiến đến nơi (ETA).

    Args:
        departure_str: Thời gian khởi hành dạng chuỗi "YYYY-MM-DD HH:MM:SS"
        distance_km:   Khoảng cách vận chuyển (km)
        speed:         Vận tốc trung bình (km/h), mặc định 60

    Returns:
        Đối tượng datetime của thời điểm dự kiến đến nơi
    """
    departure = datetime.strptime(departure_str, "%Y-%m-%d %H:%M:%S")
    hours_needed = distance_km / speed
    eta = departure + timedelta(hours=hours_needed)
    return eta
