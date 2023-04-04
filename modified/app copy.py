from PIL import Image, ImageDraw, ImageFont, ImageOps
import sys

safe_guide = 270
margin = 140

volunteer = 150
date = volunteer + 70

name_pos = 700
name2_pos = name_pos + margin
job_pos = name2_pos + margin
location_pos = job_pos + margin

logo_w = int(814 * 2/3)
logo_h = int(178 * 2/3)

location = "Northern Ireland"

gen_list = [
     {
        "Name": "Ms. Vasuki Gnana Jothi",
        "Name 1": "Ms. Vasuki",
        "Name 2": "Gnana Jothi",
        "Title": "Ophthalmic Surgeon"
    },
]

def IDCardGen(image, name, name2, job, location):
    card = Image.open("backgrounds/" + image)
    d = ImageDraw.Draw(card)

    font_semib = ImageFont.truetype("assets/fonts/JosefinSans-SemiBold.ttf", 125)
    font = ImageFont.truetype("assets/fonts/JosefinSans-Light.ttf", 110)
    font1 = ImageFont.truetype("assets/fonts/JosefinSans-Regular.ttf", 60)

    logo = Image.open("assets/logo.png")
    logo = logo.resize((logo_w, logo_h))
    
    d.text((safe_guide, volunteer), "VOLUNTEER", font=font1, fill=("#fff"))
    d.text((safe_guide, date), "6 - 11 FEB '23", font=font1, fill=("#fff"))

    d.text((safe_guide, name_pos), name.upper(), font=font_semib, fill=("#1A3E74"))
    d.text((safe_guide, name2_pos), name2.upper(), font=font_semib, fill=("#1A3E74"))
    d.text((safe_guide, job_pos), job.upper(), font=font, fill=("#f6f6f6"), strokeWidth=100)
    d.text((safe_guide, location_pos), location.upper(), font=font1, fill=("#1A3E74"))

    card.paste(logo, (safe_guide, 1700), logo)

    card.save("exports/" + name + ".jpg")
    # card.show()

for i in gen_list:
    IDCardGen((i["Name"]+".jpg"), i["Name 1"], i["Name 2"], i["Title"], location)

# IDCardGen("Prof. Colin Willoughby.jpg", "Prof. Colin", "Willoughby", "Title", location)