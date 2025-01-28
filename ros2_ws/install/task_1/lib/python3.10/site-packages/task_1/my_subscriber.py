import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('my_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'my_first_topic',  # Topic name must match the publisher
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % (msg.data*2))


def main(args=None):
    rclpy.init(args=args)

    my_subscriber = MinimalSubscriber()

    rclpy.spin(my_subscriber)

    # Destroy the node explicitly
    my_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
