import imageio.v3 as iio
import numpy as np

#function that calculates the average of the frames
def avgArray(arr1, arr2, amount=2.0):
    sum = arr1 + arr2
    return np.divide(sum, amount)

#main body
for i in range(1,6954):
    #get the 2 frames to average
    
    if i == 1: #case where it is the first frame and there is not frame before
        frame1 = iio.imread(f'Bad Apple Frames\\frame00001.png').astype(int)
        frame2 = iio.imread(f'Bad Apple Frames\\frame00002.png').astype(int)
    
    elif i == 6953: #case where it is the last frame and there is no frame after
        frame1 = iio.imread(f'Bad Apple Frames\\frame06952.png').astype(int)
        frame2 = iio.imread(f'Bad Apple Frames\\frame06953.png').astype(int)
    
    else: #default case grabbing the frame before and after
        frame1 = iio.imread(f'Bad Apple Frames\\frame{i+1:05d}.png').astype(int)
        frame2 = iio.imread(f'Bad Apple Frames\\frame{i-1:05d}.png').astype(int)

    #calculate the average of the 2 frames grabbed from the file
    newFrame = avgArray(frame1, frame2)

    #output the averaged frame to the New Frames folder
    iio.imwrite(f'New Frames\\frame{i}.png', newFrame.astype(np.uint8))