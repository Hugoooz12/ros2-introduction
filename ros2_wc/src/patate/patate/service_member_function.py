#!/usr/bin/env python3

from example_interfaces.srv import AddTwoInts
from std_msgs.msg import String, Int32, Bool
from custom.srv import Check

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self, computer_name = "student", domain_id = 5):
        super().__init__('minimal_service')
        self.declare_parameter('correct_computer_name', 'default_name')
        self.declare_parameter('correct_domain_id', 0)
        self.computer_name, self.domain_id = String(), Int32()
        self.computer_name.data, self.domain_id.data = self.get_parameter('correct_computer_name').value, self.get_parameter('correct_domain_id').value
        self.srv = self.create_service(Check, 'check', self.check_callback)
 
    def check_callback(self, request, response):
        response.answer = Bool()
        response.answer.data = (request.computer_name.data == self.computer_name.data and request.domain_id.data == self.domain_id.data)
        self.get_logger().info('Incoming request\ncomputer_name: %s domain_id: %d' % (request.computer_name.data, request.domain_id.data))
        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()