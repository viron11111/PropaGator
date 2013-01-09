#!/usr/bin/env python
import roslib
roslib.load_manifest('ocvtest')
import sys
import rospy
import cv
from std_msgs.msg import String 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class opencvtest:
	def __init__(self):
		self.image_pub=rospy.Publisher("image_topic_2",Image)
		cv.NamedWindow("Test", 1)
		self.bridge=CvBridge()
		self.image_sub=rospy.Subscriber("/gscam/image_raw/compressed",Image,self.test)
	def callback(self,data):
		try:
			image=self.bridge.imgmsg_to_cv(data, "bgr8")
		except CvBridgeError, e:
			print e
		(cols, rows)=cv.GetSize(image)
		if cols>60 and rows>60:
			cv.Circle(image,(640,300),250,(100,200,0),10)
		cv.ShowImage("Test",image)
		cv.WaitKey(3)
		try:
			self.image_pub.publish(self.bridge.imgmsg_to_cv(image,"bgr8"))
		except CvBridgeError, e:
			print e
	def test(self, data):
		image=self.bridge.imgmsg_to_cv(data,"bgr8")
		HSVimage= cv.CreateImage(cv.GetSize(image), 8, 3)
		cv.CvtColor(image, HSVimage, cv.CV_BGR2HSV)
		red_thresh=cv.CreateImage(cv.GetSize(image), 8, 1)
		cv.InRangeS(HSVimage, (175, 100, 100), (180, 255, 255), red_thresh)
		cv.ShowImage("Test",red_thresh)
		cv.WaitKey(3)
		self.image_pub.publish(self.bridge.imgmsg_to_cv(image,"bgr8"))
def main(args):
	test_cv=opencvtest()
	rospy.init_node('opencvtest', anonymous =True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print "Shut down"
	cv.DestroyAllWindows()
if __name__=='__main__':
	main(sys.argv)

