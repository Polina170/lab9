from PIL import Image, ImageDraw, ImageFont
image = Image.open("_1.png")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf",16)
draw.text((16,16), "водяной знак", font=font)
image.show()
print(f"размер: {image.size}")
image.save("watermark.png")