#!/usr/bin/env python3

import sys

from custom.srv import Check
from std_msgs.msg import String, Int32
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(Check, 'check')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Check.Request()

    def send_request(self, computer_name, domain_id):
        self.req.computer_name = computer_name
        self.req.domain_id = domain_id
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    arg1, arg2 = String(), Int32()
    arg1.data, arg2.data = str(sys.argv[1]), int(sys.argv[2])
    future = minimal_client.send_request(arg1,arg2)
    rclpy.spin_until_future_complete(minimal_client, future)
    response = future.result()
    minimal_client.get_logger().info(
        'Result : ' + str(response.answer.data))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()