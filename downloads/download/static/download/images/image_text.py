import os
import os.path

from PIL import Image, ImageDraw

introductory_text = ("Welcome to the image creator script with a new\
 filename for the new image file.").upper()
print(introductory_text, "\n")

mid_text = ("Those are the files with an '.jpg' or '.png' extension\
 you have in this directory:").capitalize()
print(mid_text, "\n")

# 0.Detecting the ".JPG" files in the actual directory and the option to
# chose one from those showed:
list_filenames = []
for filename in os.listdir("."):
    _, extension = os.path.splitext(filename)
    if extension.lower() == '.jpg' or extension.lower() == '.png':
        print(f'{filename}',)
        list_filenames.append(filename)
print()

filename_wanted = input("Introduce the filename\
 you want from those showed (If you type wrong you can try again!): ").lower()
print()
while filename_wanted not in list_filenames:
    print("Give it another try!: ", end="")
    filename_wanted = input().lower()
    if filename_wanted in list_filenames:
        print()
        break
print("Successfully created an image with a new filename!", "\n")

# 1.Opening image file and Data collection:
trust = Image.open(filename_wanted)
WIDTH, HEIGHT = trust.size
draw = ImageDraw.Draw(trust, "RGBA")
text = f"{WIDTH} x {HEIGHT}"

# 2.Position of text in the image:
text_len = len(text)

multiplier = 10                           # This one could be modified
if text_len == 9:
    text_len_final = text_len * multiplier
elif text_len == 10:
    text_len += 1
    text_len_final = text_len * multiplier
x = WIDTH / 2           #- text_len_final # type: ignore

variation_height = 20                     # This one could be modified
y = HEIGHT - variation_height
draw.text((x, y), text, fill="white")

text2 = "By Raul"
x2 = WIDTH /2
y2 = HEIGHT / 14
draw.text((x2, y2), text2, fill="white")

# 3.New image filename:
image_name = os.path.splitext(filename_wanted)
enter = "-stamped"
arg_list = list(image_name)
final_list = arg_list[0] + enter + arg_list[1]
new_image_list = final_list.split()
new_image_str = "".join(new_image_list)

# 4. Save the new image with the new image filename:
if arg_list[1] == ".jpg":
    trust.save(new_image_str, "jpeg")
if arg_list[1] == ".png":
    trust.save(new_image_str, "png")
