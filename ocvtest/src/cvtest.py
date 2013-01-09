#!/usr/bin/env python
import roslib
roslib.load_manifest('ocvtest')
import sys
import rospy
import cv
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

	def __init__(self):
		self.image_pub = rospy.Publisher("image_topic_2",Image)
		cv.NamedWindow("Image window", 1)
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/gscam/image_raw/compressed",Image,self.callback)

	def callback(self,data):
		#try:
			cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
		#except CvBridgeError, e:
		#	print e
		
			(cols,rows) = cv.GetSize(cv_image)
    		if cols > 60 and rows > 60 :
      			cv.Circle(cv_image, (640,360), 250, (100,200,50), 10)

    	cv.ShowImage("Image window", cv_image)
    	cv.WaitKey(3)

    	try:
      		self.image_pub.publish(self.bridge.cv_to_imgmsg(cv_image, "bgr8"))
    	except CvBridgeError, e:
      		print e

	def threshhold(self, data):
		image=self.bridge.imgmsg_to_cv(data, "rgb8")
#		cv.ShowImage("Red", image)
#		self.image_pub.publish(self.bridge.cv_to_imgmsg(image, "rgb8"))

		


def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"
  cv.DestroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
