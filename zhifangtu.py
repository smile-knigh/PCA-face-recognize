from scipy import misc
from PIL import Image
from pylab import *
from numpy import *
def histeq(im,nbr_bins = 256):
    """对一幅灰度图像进行直方图均衡化"""
    #计算图像的直方图
    #在numpy中，也提供了一个计算直方图的函数histogram(),第一个返回的是直方图的统计量，第二个为每个bins的中间值
    imhist,bins = histogram(im.flatten(),nbr_bins,normed= True)
    cdf = imhist.cumsum()   #
    cdf = 255.0 * cdf / cdf[-1]
    #使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape),cdf


pil_im = Image.open(r'C:\Users\smile\Documents\Tencent Files\503490246\FileCloud\lay.png')   #打开原图
pil_im_gray = pil_im.convert('L')     #转化为灰度图像
pil_im_gray.show()         #显示灰度图像

im = array(Image.open(r'C:\Users\smile\Documents\Tencent Files\503490246\FileCloud\lay.png').convert('L'))
figure()
hist(im.flatten(),600)

im2,cdf = histeq(im)
figure()
hist(im2.flatten(),256)
show()

im2 = Image.fromarray(uint8(im2))
im2.show()
print(cdf)
plot(cdf)