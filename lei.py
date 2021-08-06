import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img


# image binary threshold process
def imgBinaryThreshold(img, threshold=128):
    """
    image binary threshold
    im: source image
    threshold:Threshold from 0 to 255
    Return gray image.
    """
    imgarray = np.array(im, dtype=np.uint8)
    rows = im.shape[0]
    cols = im.shape[1]
    for i in range(rows):
        for j in range(cols):
            gray = (imgarray[i, j, 0] * 0.299 + imgarray[i, j, 1] * 0.587 + imgarray[i, j, 2] * 0.114)
            if (gray < threshold):
                imgarray[i, j, :] = 0
            else:
                imgarray[i, j, :] = 255
    return imgarray.astype(np.uint8)


im = img.imread(r"C:\Users\smile\Pictures\Saved Pictures\20150212181243_zTvhk.jpg")  # 图像读取
im = imgBinaryThreshold(im)
plt.imshow(im)  # 图像显示
img.imsave('save.jpg', im)