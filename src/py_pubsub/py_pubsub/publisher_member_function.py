import rclpy                    # import the ROS Client Library for Python (RCLPY)
from rclpy.node import Node     # from RCLPY, import the Node Class used to create ROS 2 nodes
from std_msgs.msg import String # from standard messages, import the String message


class MinimalPublisher(Node):   # Create a new class called MinimalPublisher that inherits variables & functions from Node

    def __init__(self):
        super().__init__('minimal_publisher')                               # Initialize the Node with the name 'minimal_publisher'
        self.publisher_ = self.create_publisher(String, 'my_topic', 10)     # Create a publisher for String type messages on the topic 'my_topic'
        timer_period = 0.5                                                  # Define the timer period in seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)   # Create a timer that calls 'timer_callback' every 0.5 seconds
        self.i = 0                                                          # Initialize a counter for message numbering

    def timer_callback(self):
        msg = String()                                          # Create a new String message
        msg.data = 'Hello World: %d' % self.i                   # Assign text to msg.data, including the current value of i
        self.publisher_.publish(msg)                            # Publish the message to the topic
        self.get_logger().info('Publishing: "%s"' % msg.data)   # Log the published message for debugging
        self.i += 1                                             # Increment the counter for the next message


def main(args=None):
    rclpy.init(args=args)                   # Initialize the ROS 2 Python client library

    minimal_publisher = MinimalPublisher()  # Create an instance of the MinimalPublisher class

    try:
        rclpy.spin(minimal_publisher)       # Keep the node active and processing callbacks until interrupted

    except KeyboardInterrupt:   # Handle a keyboard interrupt (Ctrl+C)
        print("\n")             # Print a newline for better format
        print("Stopping...")    # Print a stopping message
 
    finally:
        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        minimal_publisher.destroy_node()
        if rclpy.ok():                      # Check if the rclpy library is still running
            rclpy.shutdown()                # Shut down the ROS 2 client library, cleanly terminating the node



if __name__ == '__main__':
    main()                  # Call the main function to execute the code when the script is run