from PIL import Image
import ddddocr
import numpy
import cv2
import io

def ocr(code_gif_bin):
    gif=Image.open(io.BytesIO(code_gif_bin))
    frames=[]
    for i in range(4):
        gif.seek(i)
        frames.append(numpy.asarray(gif))

    frames=[frame if len(frame.shape)==2 else frame[:,:,0] for frame in frames]#只用灰度图(RGB帧只拿一个通道)
    frames=[255.0-frame for frame in frames]#转换黑白(有字的地方将变成大值)
    add=(255-sum(frames))#将所有帧叠加，并再次转换黑白
    add=numpy.where(add<0,0,add).astype("uint8")#叠加部分可能超过255，因此负值置零
    add=numpy.where(add<70,0,255)#二值化

    #过滤图像中的细边
    flt=numpy.array([[1,1,1],[1,0,1],[1,1,1]])  # 过滤图像中的细边
    for h in range(1,add.shape[0]-1):
        for w in range(1,add.shape[1]-1):
            if add[h][w]==255:
                continue
            x=add[h-1:h+2,w-1:w+2]*flt
            if x.sum()>5*255:
                add[h][w]=255

    #预测
    success,img_byte=cv2.imencode(".png",add)
    dddd=ddddocr.DdddOcr(show_ad=False)
    res=dddd.classification(bytes(img_byte))

    #增强
    res=res.replace("o","0")
    res=res.replace("O","0")
    res=res.replace("i","1")
    res=res.replace("l","1")
    res=res.replace("g","9")
    return res