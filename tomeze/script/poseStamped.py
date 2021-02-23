#!/usr/bin/env python
import math
import rospy
from geometry_msgs.msg import PoseStamped

def talker():
         pub = rospy.Publisher('chatter', PoseStamped ,queue_size=10)
         rospy.init_node('talker', anonymous=True)
         rate = rospy.Rate(15) # 15
         message = PoseStamped()
	 print(msg)
	 msg.header.frame_id="map"
	 t = - math.pi
	 while not rospy.is_Shutdown():
		 #rayon = 0.5
		 while t <= math.pi :
			 msg.pose.position.x = t
			 msg.pose.position.y = np.sin(msg.pose.position.x)
			 t = t + 0.1
			 #hello_str = "hello world %s" % rospy.get_time()
			 #rospy.loginfo(hello_str)
			 pub.publish(msg)
			 rate.sleep()

		 while t >= -math.pi :
			msg.pose.position.x = t
			msg.pose.position.y = np.sin(- msg.pose.position.x)
			t = t - 0.1
			#hello_str = "hello world %s" % rospy.get_time()
			#rospy.loginfo(hello_str)
			pub.publish(msg)
			rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


