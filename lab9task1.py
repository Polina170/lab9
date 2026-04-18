from PIL import Image
image=Image.open("_1.png")
image.show()
print(f"Размер:{img.size}")
print(f"Формат:{img.format}")
print(f"Модель:{img.mode}")
