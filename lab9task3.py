from PIL import Image, ImageFilter
images= ["1.jfif","2.jfif", "3.jfif", "4.jfif", "5.jfif"]
for i in images:
    img = Image.open(i)
    filtered= img.filter(ImageFilter.CONTOUR)
    filtered.save("n"+i)
