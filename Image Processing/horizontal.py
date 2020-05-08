from cImage import *


def verticalFlip(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW, oldH)

    maxP = oldH - 1
    for row in range(oldH):
        for col in range(oldW):
            oldPixel = oldImage.getPixel(col,maxP - row)

            newIm.setPixel(col, row, oldPixel)

    return newIm


def makeFlip(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin("Vertical Flip", width * 2, height)
    oldImage.draw(myWin)

    newImage = verticalFlip(oldImage)
    newImage.setPosition(width + 1, 0)
    newImage.draw(myWin)

    myWin.exitOnClick()


if __name__ == '__main__':
    oldImage = makeFlip('castle.gif')
    print(oldImage.getWidth(), oldImage.getHeight())
    oldImage.draw(win)