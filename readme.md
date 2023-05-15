### Feelin Light Q1 open-source project for atmosphere lighting

Document version management

| Serial Number | content                       | version | update time | Update personnel |
| ------------- | ----------------------------- | ------- | ----------- | ---------------- |
| 002           | Add device discovery function | 1.1     | 2023.5.12   | kittle.liang     |
| 001           | Initial version               | v1.0    | 2023.5.10   | kittle.liang     |



#### Python version and related dependency packages

1. Python version requires 3.7 and above

2. support Windows  

3. Import related dependency commands

   ```python
   pip install requirements.txt
   ```


#### Example

Description: Control two Feelin Light Q1 intelligent light robots to turn on the entire circle of blue light

```python
# --*--coding=utf-8--*--
from FeelinLight import feelinlight

robot = feelinlight('robot')
robot.ip_list = ['192.168.0.68', '192.168.0.234'] # Need to change to the correct LAN IP address of the device
robot.whole_lamp_color(0, 0, 255)
```

##### Library usage instructions:

1. Import the FeelinLight library and create a 'robot' object

   ```python
   # --*--coding=utf-8--*--
   from FeelinLight import feelinlight
   
   robot = feelinlight('robot')
   ```

2. Discovery of device name and IP address

   1. Default parameter: 5 seconds, modifiable, representing the delay in discovering devices


   ```python
   robot.find_devices(10) # Discovery of device service startup time of 10 seconds
   ```

   2. output

   ```python
   Device Name： FeelinLight:937e Device IP address： 192.168.0.68
   Device Name： FeelinLight:d4c2 Device IP address： 192.168.0.236
   ```

   

3. Loading Smart Lamp Robot

   1. Supports single and multiple devices
   2. Add the IP address of the device to the device list

   ```python
   robot.ip_list = ['192.168.0.79']
   ```

4. Illuminate a single light

   1. Parameter 1: Which RGB light bead to light up, value range: 0-95
   2. Parameter 2: Red, value range: 0-255
   3. Parameter 3: Green, value range: 0-255
   4. Parameter 4: Blue, value range: 0-255

   ```python
   robot.single_lamp(0, 0, 0, 255) 
   ```

5. Illuminate a set of lights

   1. Parameter 1: Which set of RGB light groups to light up, value range: 0-15
   2. Parameter 2: Red, value range: 0-255
   3. Parameter 3: Green, value range: 0-255
   4. Parameter 4: Blue, value range: 0-255

   ```python
   robot.single_set(0, 0, 0, 255)
   ```

6. Illuminate the entire circle light

   1. Parameter 1: Red, value range: 0-255
   2. Parameter 2: Green, value range: 0-255
   3. Parameter 3: Blue, value range: 0-255

   ```python
   robot.whole_lamp_color(0, 0, 255)
   ```

   

