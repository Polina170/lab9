from PIL import Image
image=Image.open("_1.png")
image.show()
res_image= image.reduce(3)
res_image.save("_11.png")
rotated1= image.transpose(Image.FLIP_LEFT_RIGHT)
rotated1.save("_12.png")
rotated = image.transpose(Image.ROTATE_90)
rotated.save("_13.png")