txt = ['Personaje_master\Img\spritesZ\ZCD1.png', 'Personaje_master\Img\spritesZ\ZCD2.png',
       'Personaje_master\Img\spritesZ\ZCD3.png', 'Personaje_master\Img\spritesZ\ZCD4.png',
       'Personaje_master\Img\spritesZ\ZCD5.png', 'Personaje_master\Img\spritesZ\ZCD6.png']

for i in range(0, len(txt)):
    if i == 0:
        txt[i] = txt[i].replace('1.png', '*.png')
    else:
        txt.pop(1)

print(txt)
