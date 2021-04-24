for n in range(5):
oldstu="00000:00000:00000:00000:00000"
imglist=oldstu.split(":")
imglist[0]="99999"
newstu=':'.join(imglist)
display.show(Image(newstu))
for i in range(4)
imglist[i]="00000"
imglist[i+1]="99999"
newstu=':'.join(imglist)
display.show(Image(newstu))