from PIL import Image, ImageDraw, ImageFont
import cups


def print_labels(text, amount, cups_name):
    image = Image.new('RGB', (1682, 1201), color='white')
    font = ImageFont.truetype('/Users/szabelin/PycharmProjects/datamax_label_printer/label_printer/arial.ttf', 200)
    image_edit = ImageDraw.Draw(image)
    image_edit.text((0, 0), text, (0, 0, 0), font=font)
    image_edit.line([(0, 0), (0, 1)], fill='black', width=0)
    image.save('img.png')
    connection = cups.Connection()
    for i in range(amount):
        connection.printFile(cups_name, 'img.png', 'title', {})



