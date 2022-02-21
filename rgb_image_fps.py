#!/usr/bin/env python3

import cv2
import depthai as dai
import time

# Create pipeline
pipeline = dai.Pipeline()

# Define source and output
camRgb = pipeline.create(dai.node.ColorCamera)
xoutVideo = pipeline.create(dai.node.XLinkOut)

xoutVideo.setStreamName("video")

# Properties
camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setVideoSize(650, 600)

xoutVideo.input.setBlocking(False)
xoutVideo.input.setQueueSize(1)

# Linking
camRgb.video.link(xoutVideo.input)


counter=0
# Connect to device and start pipeline
initial_time = 0
end_time = 0
with dai.Device(pipeline) as device:

    video = device.getOutputQueue(name="video", maxSize=1, blocking=False)

    while True:
        videoIn = video.get()
        end_time = time.time()
        Frame=videoIn.getCvFrame()
        fps = str(int(4/(end_time-initial_time)))
        font = cv2.FONT_HERSHEY_SIMPLEX
        initial_time=end_time
        cv2.putText(Frame, fps+' '+str(Frame.shape), (7, 70), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow("video", Frame)
        if cv2.waitKey(1)==ord('c'):
            counter+=1
            cv2.imwrite('fps_image'+str(counter)+'.jpg',Frame)
        if cv2.waitKey(1) == ord('q'):
            break
