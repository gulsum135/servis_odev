import argparse

import rclpy
from alan_interfaces.srv import RectangleArea
from rclpy.utilities import remove_ros_args


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('width', type=float)
    parser.add_argument('height', type=float)
    args = parser.parse_args(remove_ros_args()[1:])

    rclpy.init()
    node = rclpy.create_node('area_client')
    try:
        client = node.create_client(RectangleArea, 'rectangle_area')
        if not client.wait_for_service(timeout_sec=5.0):
            node.get_logger().error('Servis bulunamadi. Sunucuyu baslat.')
            return 1

        request = RectangleArea.Request()
        request.width = args.width
        request.height = args.height
        future = client.call_async(request)
        rclpy.spin_until_future_complete(node, future, timeout_sec=5.0)
        if not future.done():
            node.get_logger().error('Servis zamaninda yanit vermedi.')
            return 1

        print(f'Alan: {future.result().area}')
        return 0
    except KeyboardInterrupt:
        return 130
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
