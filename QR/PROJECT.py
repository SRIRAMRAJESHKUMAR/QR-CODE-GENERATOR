import qrcode

features = qrcode.QRCode(version=1,box_size=30,border=4)
features.add_data('https:// www.youtube.com/c/GeekforGeeksVideos')
features.make(fit=True)

generate_image = features.make_image(fill_color='black',back_color="white")
generate_image.save('image4.png')