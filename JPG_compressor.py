from PIL import Image
from os import getcwd, listdir

pics = listdir(getcwd())
print('Higher quality will result in a sharper image while higher compression will result in a smaller file')
print('80% recommended for web images as a good balance of file size and quality')
qual = input('Compression quality(0-100%): ')

if qual.endswith('%'):
    qual = int(qual[:-1])
else: qual = int(qual)

for pic in pics:
    if pic.endswith('.jpg'):
        png = Image.open(pic)
        png.save(f'compressed_{pic}', 'JPEG', quality=qual)

