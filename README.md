# OpenCV security cam (person detection)

Capture webcam video frame when a person is detected in the region of interest (ROI). Then save the full frame captured in a specific folder such as web directory (wwww).

## ROI

In the OpenCV library you can find "selectROI" which allow to select a bounding box or a rectangular region of interest (ROI) in an frame. With that compenent we can select a specific region of interest where to detect face and not someheree else.

![ROI](/images/roi.gif)

## Person and face detection

To improve the person detection in the region of interest, we use OpenCV "CascadeClassifier" fonction to detecte face and HOG detector function to detect the whole body. We use that to remove false positive.


## Web

When a person is detected in the region of interest we save the full frame in the web directory (www). With the library "nanogallery2" we can see the all the frame.


![Web gallery 1](/images/g1.jpg)
![Web gallery 2](/images/g2.jpg)
