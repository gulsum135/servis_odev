# RectangleArea servisi

Bu ROS 2 servisi, genişlik ve yükseklik değerlerini alıp dikdörtgenin alanını hesaplar. `alan_interfaces` servis tanımını, `alan_py` ise Python sunucusunu ve istemcisini içerir.

## Derleme

ROS 2 ortamını yükledikten sonra aşağıdaki komutları çalıştır.

```bash
mkdir -p ~/ros2_ws/src
git clone https://github.com/gulsum135/servis_odev.git ~/ros2_ws/src/servis_odev
cd ~/ros2_ws
colcon build --packages-up-to alan_py
source install/setup.bash
```

## Test

İlk terminalde sunucuyu başlat.

```bash
ros2 run alan_py server
```

İkinci terminalde ROS 2 ortamını yükle ve istemciyi çalıştır.

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run alan_py client 3 5
ros2 service call /rectangle_area alan_interfaces/srv/RectangleArea "{width: 3.0, height: 5.0}"
```

Beklenen istemci çıktısı `Alan: 15.0`. Servis çağrısının yanıtında `area=15.0` görünür.
