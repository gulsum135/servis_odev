import rclpy
from alan_interfaces.srv import RectangleArea
from rclpy.node import Node


class AreaServer(Node):
    def __init__(self):
        super().__init__('area_server')
        self.service = self.create_service(
            RectangleArea, 'rectangle_area', self.calculate_area
        )
        self.get_logger().info('Dikdortgen alani servisi hazir.')

    def calculate_area(self, request, response):
        response.area = request.width * request.height
        return response


def main():
    rclpy.init()
    node = AreaServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
