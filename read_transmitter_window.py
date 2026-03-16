import hid
import time


# 变送器 的 HID 身份信息（请根据你之前查到的实际 VID/PID 修改）




def get_realtime_data(device,key):
    device.set_nonblocking(1)
    while device.read(64):
        pass
    try:

        # 发送指令访问,指令详询Mettler Toledo工程师
        device.write(key)
        time.sleep(0.3)
        # 读取原始字节并转为 ASCII
        raw = device.read(64)
        res_str = "".join(chr(b) for b in raw if 32 <= b <= 126)

        return res_str

    except Exception as e:
        return [f"连接异常: {e}"]


def start_get_data(VID,PID,key):
    device = hid.device()
    # VID VENDOR ID
    # PID PRODUCT ID
    device.open(VID, PID)

    i=0
    while i<100000:
        data = get_realtime_data(device,key)
        print(data)

        i =i+1
    device.close()

if __name__ == '__main__':
    VID = 0x0000
    PID = 0x0000
    key = [0x00,0x00,0x00,0x00]+[0x00]*56
    start_get_data(VID,PID,key)