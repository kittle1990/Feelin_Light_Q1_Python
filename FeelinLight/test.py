from FeelinLight import feelinlight

robot = feelinlight('robot')
robot.ip_list = ['192.168.0.68']  # 需要更改为设备正确的局域网IP地址
robot.whole_lamp_color(0, 255, 255)
