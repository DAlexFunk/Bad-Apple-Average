import imageio.v2 as iio

#create list of file names to be used
fileNames = []
for i in range(1,6954):
    fileNames.append(f'frame{i}')

#function that stitches the frames together
def make_mp4(moviename, fnames, fps):
    with iio.get_writer(moviename, fps=fps) as writer:
        for fname in fnames:
            writer.append_data(iio.imread(f'New Frames\\{fname}.png'))
    return 'done'

make_mp4('finalVideo.mp4', fileNames, 30)