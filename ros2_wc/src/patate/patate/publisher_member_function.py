#!/usr/bin/env python3
# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int32
from custom.msg import Custom


class Publisher(Node):
    def __init__(self, computer_name, domain_id):
        super().__init__('computer_name_publisher')
        self.publisher = self.create_publisher(Custom, 'some_informations', 10)
        self.correct_domain_id, self.correct_computer_name = domain_id, computer_name
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Custom()
        value_t, count_t, message_t = Int32(), Int32(), String()
        value_t.data = self.correct_domain_id
        count_t.data = self.i 
        message_t.data = self.correct_computer_name
        msg.computer_name = message_t
        msg.domain_id = value_t
        msg.counter = count_t
        self.publisher.publish(msg)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    publisher = Publisher("student", 5)
    
    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
