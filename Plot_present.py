from numpy import linspace,pi,sin,cos
import matplotlib.pyplot as plt
from pylab import *
from scipy.misc import face

x = linspace(0, 2*pi, 50)
a = sin(x)
b = cos(x)

img = imread('LJ Logo.jpg',True)
#img = face(True)

subplot(2,2,1)
title('sin(x) cos(x)')
plot(x,a,'b-^',  x,b,'r-o')


subplot(2,2,2)
plot(x,b)
grid()
xlabel('Radians')
ylabel('Amplitude')
title('Sin(x)')


subplot(2,2,3)
imshow(img, cm.bone)
plt.axis('tight')
plt.tight_layout()

plt.show()
plt.draw()
plt.savefig('plot_img.jpg',dpi=100)