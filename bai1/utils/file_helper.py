import os

def create_log_dir(dir_name: str) -> bool:
    """
    Tạo thư mục lưu log an toàn. Nếu thư mục đã tồn tại thì bỏ qua,
    không gây ra FileExistsError.
    """
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    return True
